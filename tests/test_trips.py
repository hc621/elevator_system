"""Car trips: from starting to move until the car reverses or goes idle."""

from helpers import building, reqs, run

from elevator_sim.events import CarState
from elevator_sim.model import Direction, Doors
from elevator_sim.report import count_trips

U, D, IDLE = Direction.UP, Direction.DOWN, Direction.IDLE


def states(*rows: tuple[int, Direction]) -> list[CarState]:
    """Tick-ordered states of car 0 from (floor, direction) pairs."""
    return [CarState(t, 0, f, d, Doors.CLOSED, 0) for t, (f, d) in enumerate(rows)]


def test_a_car_that_never_moves_makes_no_trips() -> None:
    assert count_trips(states((1, IDLE), (1, IDLE), (1, U), (1, IDLE))) == 0


def test_stops_along_the_way_do_not_end_a_trip() -> None:
    # 1 -> 3, doors at 3 (still heading up), 3 -> 5, then idle.
    rows = states((1, U), (2, U), (3, U), (3, U), (4, U), (5, U), (5, IDLE))
    assert count_trips(rows) == 1


def test_reversing_starts_a_new_trip() -> None:
    rows = states((1, U), (2, U), (3, D), (2, D), (1, IDLE))
    assert count_trips(rows) == 2


def test_going_idle_ends_a_trip_even_if_the_next_one_is_the_same_way() -> None:
    rows = states((1, U), (2, U), (3, IDLE), (3, IDLE), (3, U), (4, U), (5, IDLE))
    assert count_trips(rows) == 2


def test_trips_in_a_whole_run() -> None:
    # Car 0 takes a up 1 -> 10, keeps going to 15 for b, then carries b down to 2: two trips.
    # Car 1 is never needed.
    _, report = run(reqs((0, "a", 1, 10), (3, "b", 15, 2)), building(floors=20, cars=2))
    assert [c.trips for c in report.per_car.values()] == [2, 0]
