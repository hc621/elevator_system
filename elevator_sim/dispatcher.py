"""The dispatcher: owns the cars and is the only code that changes them.

One tick, in order:
  1. each arriving request: Requested -> policy chooses a car -> assign -> Assigned (+ RouteChanged)
  2. each car, in id order, steps: open/keep/close doors, alight, board, decide its move
  3. a CarState for every car (the positions log)
  4. cars that chose to move advance one floor
  5. each car that has just gone idle asks the parking policy where to wait

Assigning before stepping means a request made on tick t can board on tick t if its car is already
at that floor.
"""

from __future__ import annotations

from collections.abc import Sequence

from elevator_sim.car import Car, CarView
from elevator_sim.dispatch import DispatchPolicy
from elevator_sim.events import Assigned, EventSink, NullSink, Requested, RouteChanged
from elevator_sim.model import BuildingConfig, Doors, Request, Tick
from elevator_sim.motion import LookMotion, MotionPolicy
from elevator_sim.parking import ParkingPolicy, StayParking


class NoEligibleCar(ValueError):
    """No car serves both the source and the destination floor."""


class Dispatcher:
    def __init__(
        self,
        config: BuildingConfig,
        dispatch: DispatchPolicy,
        motion: MotionPolicy | None = None,
        sink: EventSink | None = None,
        *,
        journal_routes: bool = False,
        parking: ParkingPolicy | None = None,
    ) -> None:
        self.config = config
        self.dispatch = dispatch
        self.motion = motion if motion is not None else LookMotion()
        self.parking = parking if parking is not None else StayParking()
        self._history: list[Request] = []  # every request released so far (parking sees these)
        self._sink = sink if sink is not None else NullSink()
        self._journal_routes = journal_routes
        self._cars = [
            Car(i, spec, top_floor=config.floors, door_time=config.door_time, motion=self.motion)
            for i, spec in enumerate(config.cars)
        ]
        self._views = tuple(CarView(c) for c in self._cars)

    @property
    def views(self) -> tuple[CarView, ...]:
        return self._views

    def idle(self) -> bool:
        return not any(car.has_passengers for car in self._cars)

    def tick(self, now: Tick, arrivals: Sequence[Request]) -> None:
        for request in arrivals:
            self._history.append(request)
            self._assign(now, request)
        for car in self._cars:
            for event in car.step(now):
                self._sink.emit(event)
        for car in self._cars:
            self._sink.emit(car.state(now, car.route() if self._journal_routes else None))
        for car in self._cars:
            car.advance()
        self._park(now)

    def _park(self, now: Tick) -> None:
        """Give every car that has just gone idle a floor to wait at (or none)."""
        for car in self._cars:
            if car.has_passengers or car.park_decided or car.doors is not Doors.CLOSED:
                continue
            claimed = frozenset(
                other.park_floor if other.park_floor is not None else other.floor
                for other in self._cars
                if other is not car and other.park_decided and not other.has_passengers
            )
            floor = self.parking.target(self._views[car.id], self._views, claimed,
                                        self._history, now)  # fmt: skip
            if floor is not None and not 1 <= floor <= self.config.floors:
                raise ValueError(f"{self.parking.name} chose floor {floor} for car {car.id}")
            car.park_floor = floor
            car.park_decided = True

    def _assign(self, now: Tick, request: Request) -> None:
        self._sink.emit(Requested(now, request.id, request.source, request.dest))
        eligible = [v for v in self._views if v.spec.can_serve(request)]
        if not eligible:
            raise NoEligibleCar(f"no car serves floors {request.source} and {request.dest}")
        car_id = self.dispatch.choose(request, eligible, now)
        if car_id not in {v.id for v in eligible}:
            raise ValueError(
                f"{self.dispatch.name} chose car {car_id}, which cannot serve {request.id}"
            )
        car = self._cars[car_id]
        old = car.route()
        car.assign(request)
        new = car.route()
        self._sink.emit(
            Assigned(now, request.id, car_id, self.dispatch.name, self.dispatch.last_cost)
        )
        if new != old:
            self._sink.emit(RouteChanged(now, car_id, old, new))
