"""Root-cause diagnostics: assignment state, distances, busy share, grouping, full pass-bys."""

import pytest
from helpers import building, records, reqs, run
from test_journal_report import hand_written_journal

from elevator_sim.model import Direction
from elevator_sim.report import aggregate, classify_assignment

UP, DOWN, IDLE = Direction.UP, Direction.DOWN, Direction.IDLE


@pytest.mark.parametrize(
    ("car_floor", "car_dir", "source", "wants", "expected"),
    [
        (5, IDLE, 9, UP, "idle"),
        (5, UP, 9, UP, "on_the_way"),
        (5, UP, 5, UP, "on_the_way"),  # already there, same way
        (5, UP, 9, DOWN, "ahead_opposite"),  # must go past, then come back
        (5, UP, 2, UP, "moving_away"),
        (5, DOWN, 9, DOWN, "moving_away"),
        (5, DOWN, 2, DOWN, "on_the_way"),
    ],
)
def test_classify_assignment(
    car_floor: int, car_dir: Direction, source: int, wants: Direction, expected: str
) -> None:
    assert classify_assignment(car_floor, car_dir, source, wants) == expected


def test_hand_written_journal_diagnostics() -> None:
    d = aggregate(hand_written_journal()).diagnostics
    # a gets the idle car at floor 1; b asks at floor 2 just as the car arrives there heading up.
    assert {k: v.count for k, v in d.assignment.items()} == {
        "idle": 1, "on_the_way": 1, "ahead_opposite": 0, "moving_away": 0,
    }  # fmt: skip
    assert d.assignment["on_the_way"].mean_wait == 1
    assert (d.chosen_distance, d.nearest_distance) == (0, 0)
    assert d.busy_share == pytest.approx(5 / 6)  # idle with doors closed only at t=5
    assert d.distance_per_passenger == 1.5  # 3 floors, 2 passengers
    assert d.riders_per_stop == 1.0  # 4 door openings, 2 boardings + 2 alightings
    assert d.detour.mean == 0.5 and d.full_passby_share == 0


def test_a_passenger_behind_a_moving_car_is_counted_as_moving_away() -> None:
    _, report = run(reqs((0, "a", 1, 20), (5, "b", 2, 8)), building(floors=20))
    d = report.diagnostics
    assert d.assignment["moving_away"].count == 1
    assert d.assignment["moving_away"].mean_wait == records(report)["b"].wait
    assert d.chosen_distance == pytest.approx((0 + 4) / 2)  # door_time 0: car at 6 when b asks


def test_a_full_car_passing_its_own_passenger_is_counted() -> None:
    # Capacity 1: the car carries a up past floor 10, where b (assigned to it) waits to go up.
    _, report = run(reqs((0, "a", 1, 20), (3, "b", 10, 15)), building(floors=20, capacity=1))
    assert report.diagnostics.full_passby_share == 0.5
    assert any("pass their floor full" in note for note in report.observations)


def test_reaching_capacity_without_a_pass_by_is_not_called_binding() -> None:
    _, report = run(reqs((0, "a", 1, 5)), building(floors=10, capacity=1))
    assert report.diagnostics.full_passby_share == 0
    assert any("no passenger was passed by a full car" in note for note in report.observations)


def test_cost_dispatch_avoids_cars_moving_away_compared_with_round_robin() -> None:
    from elevator_sim.scenarios import random_requests

    requests = random_requests(floors=20, count=120, duration=400, seed=4)
    config = building(floors=20, cars=4)
    _, rr = run(requests, config, dispatch="round_robin")
    _, cost = run(requests, config, dispatch="cost")
    assert (
        cost.diagnostics.assignment["moving_away"].share
        < rr.diagnostics.assignment["moving_away"].share
    )
    assert cost.diagnostics.chosen_distance < rr.diagnostics.chosen_distance


def test_trip_kinds_and_breakdown() -> None:
    from elevator_sim.report import trip_kind

    assert (trip_kind(1, 9), trip_kind(9, 1), trip_kind(4, 9)) == (
        "inbound", "outbound", "inter_floor",
    )  # fmt: skip
    requests = reqs((0, "a", 1, 9), (0, "b", 1, 5), (2, "c", 8, 1), (3, "d", 4, 7))
    _, report = run(requests, building(floors=10, cars=2))
    t = report.by_trip
    assert (t["inbound"].count, t["outbound"].count, t["inter_floor"].count) == (2, 1, 1)
    assert sum(x.count for x in t.values()) == len(report.passengers)
    assert t["outbound"].wait.max == records(report)["c"].wait
