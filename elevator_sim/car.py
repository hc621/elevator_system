"""A car: mutable state owned by the dispatcher, plus a read-only view for policies.

Each tick the dispatcher calls, in order: ``step(now)`` (decide; open, board, alight, close),
``state(now)`` (snapshot for the positions log) and ``advance()`` (apply the move).

A stop takes ``door_time + 1`` ticks at the floor: doors open on the arrival tick, stay open for
``door_time`` extra ticks, and the car leaves on the last of them. With ``door_time = 0`` a stop
costs nothing: open, alight, board, close and depart all happen on the arrival tick.
"""

from __future__ import annotations

import copy
from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from elevator_sim.events import Alighted, Boarded, CarState, DoorsClosed, DoorsOpened, Event
from elevator_sim.feed import SimulationStalled
from elevator_sim.model import (
    CarId,
    CarSpec,
    Direction,
    Doors,
    Floor,
    PassengerId,
    PlannedStop,
    Request,
    Tick,
)
from elevator_sim.motion import CarSnapshot, MotionPolicy, Move, OpenDoors

# One tick can hold at most a stop, a reversal at that floor and a second stop; more means a bug.
_MAX_DECISIONS_PER_TICK = 4


class CapacityExceeded(RuntimeError):
    """A motion policy tried to board more passengers than the car holds."""


@dataclass(frozen=True)
class Projection:
    """A car's future if no further requests arrive."""

    route: tuple[PlannedStop, ...]
    pickup_eta: Mapping[PassengerId, Tick]  # passengers not yet aboard
    dropoff_eta: Mapping[PassengerId, Tick]
    total_time: int  # sum over the car's passengers of (dropoff_eta - request time)
    waits: Mapping[PassengerId, int]  # pickup_eta - request time, for passengers not yet aboard


class Car:
    def __init__(
        self,
        car_id: CarId,
        spec: CarSpec,
        *,
        top_floor: Floor,
        door_time: int,
        motion: MotionPolicy,
    ) -> None:
        self.id = car_id
        self.spec = spec
        self.top_floor = top_floor
        self.door_time = door_time
        self.motion = motion

        self.floor: Floor = spec.start_floor
        self.direction = Direction.IDLE
        self.doors = Doors.CLOSED
        self.door_timer = 0
        self.waiting: dict[PassengerId, Request] = {}  # assigned, not yet aboard
        self.onboard: dict[PassengerId, Request] = {}

        self.park_floor: Floor | None = None  # where to wait while idle (parking policy)
        self.park_decided = False  # the parking policy has been asked since the car went idle

        self.next_tick: Tick = 0
        self._stepped = False
        self._pending_move: Direction | None = None

    # --- read-only properties ----------------------------------------------------------------

    @property
    def capacity(self) -> int:
        return self.spec.capacity

    @property
    def load(self) -> int:
        return len(self.onboard)

    @property
    def has_passengers(self) -> bool:
        return bool(self.waiting or self.onboard)

    def snapshot(self) -> CarSnapshot:
        return CarSnapshot(
            floor=self.floor,
            direction=self.direction,
            load=self.load,
            capacity=self.capacity,
            top_floor=self.top_floor,
            onboard=tuple(self.onboard.values()),
            waiting=tuple(self.waiting.values()),
        )

    def state(self, now: Tick, route: tuple[PlannedStop, ...] | None = None) -> CarState:
        return CarState(now, self.id, self.floor, self.direction, self.doors, self.load, route)

    # --- mutation (dispatcher only) ----------------------------------------------------------

    def assign(self, request: Request) -> None:
        if request.id in self.waiting or request.id in self.onboard:
            raise ValueError(f"passenger {request.id!r} is already assigned to car {self.id}")
        if not self.has_passengers and self.doors is Doors.CLOSED:
            self.direction = Direction.IDLE  # a parking car drops its target and chooses afresh
        self.park_floor = None
        self.park_decided = False
        self.waiting[request.id] = request

    def step(self, now: Tick) -> list[Event]:
        """One tick of behaviour. Returns the events it caused; ``advance`` applies the move."""
        if now != self.next_tick or self._stepped:
            raise RuntimeError(
                f"car {self.id}: step({now}) out of order (expected {self.next_tick})"
            )
        self._stepped = True
        self._pending_move = None
        events: list[Event] = []

        if self.doors is Doors.OPEN:
            if self.direction is Direction.IDLE:
                # An idle car with open doors can still take someone who arrived mid-dwell.
                action = self.motion.next_action(self.snapshot())
                if isinstance(action, OpenDoors):
                    self.direction = action.direction
            self._board(now, events)
            if self.door_timer > 0:
                self.door_timer -= 1
            if self.door_timer > 0:
                return events  # keep the doors open
            self._close(now, events)

        self._decide(now, events)
        return events

    def advance(self) -> None:
        if not self._stepped:
            raise RuntimeError(f"car {self.id}: advance() before step()")
        if self._pending_move is not None:
            self.floor += self._pending_move.value
        self._pending_move = None
        self._stepped = False
        self.next_tick += 1

    # --- look-ahead --------------------------------------------------------------------------

    def project(self, extra: Request | None = None) -> Projection:
        """Run this car's own rules on a private copy until it has no passengers left.

        This is the only look-ahead in the system. It uses the real motion policy, door timing and
        capacity rule, so it stays exact for LOOK, SCAN and any stop time.
        """
        clone = self._clone()
        if extra is not None:
            clone.assign(extra)
        if clone._stepped:  # called between step() and advance(): finish this tick first
            clone.advance()
        passengers = {**clone.onboard, **clone.waiting}
        start = clone.next_tick
        horizon = (len(passengers) + 1) * 2 * (self.top_floor + 1) * (self.door_time + 2)
        events: list[Event] = []
        while clone.has_passengers:
            if clone.next_tick - start > horizon:
                raise SimulationStalled(
                    f"car {self.id}: projection did not finish within {horizon} ticks"
                )
            events.extend(clone.step(clone.next_tick))
            clone.advance()
        return _build_projection(events, passengers)

    def route(self) -> tuple[PlannedStop, ...]:
        return self.project().route

    # --- internals ---------------------------------------------------------------------------

    def _clone(self) -> Car:
        clone = copy.copy(self)
        clone.waiting = dict(self.waiting)
        clone.onboard = dict(self.onboard)
        return clone

    def _decide(self, now: Tick, events: list[Event]) -> None:
        for _ in range(_MAX_DECISIONS_PER_TICK):
            action = self.motion.next_action(self.snapshot())
            if isinstance(action, OpenDoors):
                self.direction = action.direction
                self._open(now, events)
                if self.door_timer > 0:
                    return
                self._close(now, events)  # door_time == 0: the stop costs no time
                continue
            if isinstance(action, Move):
                target = self.floor + action.direction.value
                if action.direction is Direction.IDLE or not 1 <= target <= self.top_floor:
                    raise RuntimeError(
                        f"car {self.id}: invalid move {action} from floor {self.floor}"
                    )
                self.direction = action.direction
                self._pending_move = action.direction
                return
            if self.park_floor is not None and self.park_floor != self.floor:
                # No work: drive towards the parking floor (no stop, no door time).
                self.direction = Direction.UP if self.park_floor > self.floor else Direction.DOWN
                self._pending_move = self.direction
                return
            self.direction = Direction.IDLE
            return
        raise RuntimeError(
            f"car {self.id}: motion policy reopened the doors repeatedly at tick {now}"
        )

    def _open(self, now: Tick, events: list[Event]) -> None:
        self.doors = Doors.OPEN
        events.append(DoorsOpened(now, self.id, self.floor))
        for pid in [pid for pid, p in self.onboard.items() if p.dest == self.floor]:
            del self.onboard[pid]
            events.append(Alighted(now, pid, self.id, self.floor))
        self._board(now, events)
        self.door_timer = self.door_time

    def _board(self, now: Tick, events: list[Event]) -> None:
        ids = self.motion.who_boards(self.snapshot())
        if len(ids) > self.capacity - self.load:
            raise CapacityExceeded(
                f"car {self.id}: {len(ids)} boarding with {self.capacity - self.load} free places"
            )
        for pid in ids:
            request = self.waiting.pop(pid)
            if request.source != self.floor:
                raise RuntimeError(f"car {self.id}: {pid} boarding at {self.floor}, not its source")
            self.onboard[pid] = request
            events.append(Boarded(now, pid, self.id, self.floor))

    def _close(self, now: Tick, events: list[Event]) -> None:
        self.doors = Doors.CLOSED
        events.append(DoorsClosed(now, self.id, self.floor))


def _build_projection(
    events: Sequence[Event], passengers: Mapping[PassengerId, Request]
) -> Projection:
    stops: list[PlannedStop] = []
    floor = eta = 0
    alight: list[PassengerId] = []
    board: list[PassengerId] = []
    pickup: dict[PassengerId, Tick] = {}
    dropoff: dict[PassengerId, Tick] = {}

    def flush() -> None:
        stops.append(PlannedStop(floor, eta, tuple(alight), tuple(board)))

    open_stop = False
    for e in events:
        if isinstance(e, DoorsOpened):
            if open_stop:
                flush()
            floor, eta, alight, board, open_stop = e.floor, e.tick, [], [], True
        elif isinstance(e, Alighted):
            alight.append(e.passenger)
            dropoff[e.passenger] = e.tick
        elif isinstance(e, Boarded):
            board.append(e.passenger)
            pickup[e.passenger] = e.tick
    if open_stop:
        flush()
    total = sum(dropoff[pid] - r.time for pid, r in passengers.items())
    waits = {pid: tick - passengers[pid].time for pid, tick in pickup.items()}
    return Projection(tuple(stops), pickup, dropoff, total, waits)


class CarView:
    """Read-only view of a car: what dispatch policies may see. It can ask, not act."""

    __slots__ = ("_car",)

    def __init__(self, car: Car) -> None:
        self._car = car

    @property
    def id(self) -> CarId:
        return self._car.id

    @property
    def spec(self) -> CarSpec:
        return self._car.spec

    @property
    def floor(self) -> Floor:
        return self._car.floor

    @property
    def direction(self) -> Direction:
        return self._car.direction

    @property
    def doors(self) -> Doors:
        return self._car.doors

    @property
    def load(self) -> int:
        return self._car.load

    @property
    def capacity(self) -> int:
        return self._car.capacity

    @property
    def top_floor(self) -> Floor:
        return self._car.top_floor

    @property
    def assigned(self) -> int:
        """Passengers assigned to this car and not yet delivered."""
        return len(self._car.waiting) + len(self._car.onboard)

    def route(self) -> tuple[PlannedStop, ...]:
        return self._car.route()

    def project(self, extra: Request | None = None) -> Projection:
        return self._car.project(extra)
