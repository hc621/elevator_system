"""The car state machine: initial state, stop timing (dwell), capacity and guard rails."""

import pytest
from helpers import building, check_invariants, floors_by_car, records, reqs, run

from elevator_sim.car import CapacityExceeded, Car
from elevator_sim.events import Boarded, CarState
from elevator_sim.model import CarSpec, Direction, Doors, Request
from elevator_sim.motion import CarSnapshot, LookMotion, Move, OpenDoors


def make_car(motion: object = None, capacity: int = 8, start: int = 1, door_time: int = 0) -> Car:
    return Car(
        0,
        CarSpec(capacity, start),
        top_floor=10,
        door_time=door_time,
        motion=motion or LookMotion(),  # type: ignore[arg-type]
    )


def test_initial_state() -> None:
    car = make_car(start=4)
    assert (car.floor, car.direction, car.doors, car.load) == (4, Direction.IDLE, Doors.CLOSED, 0)
    assert not car.has_passengers
    assert car.route() == ()


def test_step_and_advance_must_alternate_in_tick_order() -> None:
    car = make_car()
    with pytest.raises(RuntimeError, match="advance"):
        car.advance()
    with pytest.raises(RuntimeError, match="out of order"):
        car.step(1)
    car.step(0)
    with pytest.raises(RuntimeError, match="out of order"):
        car.step(0)
    car.advance()
    car.step(1)


def test_assigning_the_same_passenger_twice_fails() -> None:
    car = make_car()
    car.assign(Request(0, "a", 1, 5))
    with pytest.raises(ValueError, match="already assigned"):
        car.assign(Request(0, "a", 1, 5))


def test_stop_timeline_with_door_time_1() -> None:
    journal, report = run(reqs((0, "a", 1, 4)), building(floors=10, door_time=1))
    # t0-1 at floor 1 (doors open, then close and leave), t2-4 floors 2-4. The run ends on the
    # tick of the last drop-off, so the final stop's dwell is not logged.
    assert floors_by_car(journal)[0] == [1, 1, 2, 3, 4]
    doors = [s.doors for s in journal.events(CarState)]
    assert doors == [Doors.OPEN, Doors.CLOSED, Doors.CLOSED, Doors.CLOSED, Doors.OPEN]
    a = records(report)["a"]
    assert (a.boarded, a.alighted, a.wait, a.travel) == (0, 4, 0, 4)


def test_floor_repeats_door_time_plus_one_rows_per_stop() -> None:
    journal, _ = run(reqs((0, "a", 3, 6)), building(floors=10, door_time=2))
    floors = floors_by_car(journal)[0]
    assert floors == [1, 2, 3, 3, 3, 4, 5, 6]


def test_door_time_0_stop_costs_nothing() -> None:
    journal, report = run(reqs((0, "a", 1, 4), (0, "b", 1, 2)), building(floors=10, door_time=0))
    assert floors_by_car(journal)[0] == [1, 2, 3, 4]
    assert records(report)["a"].total == 3


def test_request_made_mid_dwell_still_boards() -> None:
    journal, report = run(reqs((0, "a", 1, 5), (1, "b", 1, 6)), building(floors=10, door_time=2))
    b = records(report)["b"]
    assert (b.boarded, b.wait) == (1, 0)
    check_invariants(journal, reqs((0, "a", 1, 5), (1, "b", 1, 6)))


def test_car_that_went_idle_with_doors_open_takes_a_mid_dwell_request() -> None:
    requests = reqs((0, "a", 1, 5), (7, "b", 5, 3))
    _, report = run(requests, building(floors=10, door_time=2))
    a, b = records(report)["a"], records(report)["b"]
    assert a.alighted == 6  # doors open at t6 at floor 5 and the car goes idle
    assert (b.boarded, b.wait) == (7, 0)


def test_travel_is_at_least_direct_and_longer_with_intermediate_stops() -> None:
    _, report = run(reqs((0, "a", 1, 10), (0, "b", 1, 5)), building(floors=10, door_time=1))
    for rec in report.passengers:
        assert rec.travel >= rec.direct
    # 9 floors + the dwell tick at floor 1 after boarding + the stop at floor 5
    assert records(report)["a"].travel == 9 + 2


class _GreedyBoarding(LookMotion):
    def who_boards(self, s: CarSnapshot) -> tuple[str, ...]:
        return tuple(w.id for w in s.waiting if w.source == s.floor)


def test_car_enforces_capacity_whatever_the_policy_says() -> None:
    car = make_car(_GreedyBoarding(), capacity=1)
    car.assign(Request(0, "a", 1, 5))
    car.assign(Request(0, "b", 1, 6))
    with pytest.raises(CapacityExceeded):
        car.step(0)


class _ThroughTheRoof(LookMotion):
    def next_action(self, s: CarSnapshot) -> Move:
        return Move(Direction.UP)


def test_car_refuses_to_leave_the_shaft() -> None:
    car = make_car(_ThroughTheRoof(), start=10)
    with pytest.raises(RuntimeError, match="invalid move"):
        car.step(0)


class _AlwaysOpen(LookMotion):
    def next_action(self, s: CarSnapshot) -> OpenDoors:
        return OpenDoors(Direction.UP)


def test_car_stops_a_policy_that_reopens_forever() -> None:
    car = make_car(_AlwaysOpen(), door_time=0)
    with pytest.raises(RuntimeError, match="reopened"):
        car.step(0)


def test_capacity_one_car_never_carries_two() -> None:
    requests = reqs((0, "a", 1, 9), (0, "b", 1, 8), (0, "c", 1, 7))
    journal, report = run(requests, building(floors=10, capacity=1))
    check_invariants(journal, requests)
    assert max(s.load for s in journal.events(CarState)) == 1
    assert [e.passenger for e in journal.events(Boarded)] == ["a", "b", "c"]
    assert report.per_car[0].peak_load == 1
