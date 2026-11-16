"""Journal round-trip and the pure aggregation from journal to report."""

from pathlib import Path

import pytest
from helpers import building, reqs, run

from elevator_sim.adapters import format_summary
from elevator_sim.events import (
    Alighted,
    Assigned,
    Boarded,
    CarState,
    DoorsOpened,
    Requested,
    RunStarted,
    event_from_dict,
)
from elevator_sim.journal import Journal
from elevator_sim.model import Direction, Doors
from elevator_sim.report import Stats, aggregate, percentile
from elevator_sim.scenarios import random_requests


def test_jsonl_round_trip_rebuilds_an_identical_report(tmp_path: Path) -> None:
    requests = random_requests(
        floors=20, count=30, duration=60, seed=3, lobby_up=0.4, lobby_down=0.4
    )
    journal, report = run(
        requests, building(floors=20, cars=2, capacity=4, door_time=1), journal_routes=True
    )
    path = tmp_path / "run.jsonl"
    journal.to_jsonl(path)
    loaded = Journal.from_jsonl(path)
    assert loaded.events() == journal.events()
    assert aggregate(loaded) == report
    assert format_summary(aggregate(loaded)) == format_summary(report)


def hand_written_journal() -> Journal:
    config = building(floors=10, cars=1, capacity=2, door_time=0)
    up, idle, closed, open_ = Direction.UP, Direction.IDLE, Doors.CLOSED, Doors.OPEN
    return Journal(
        [
            RunStarted(0, config, "cost", "look"),
            Requested(0, "a", 1, 3),
            Assigned(0, "a", 0, "cost", 2.0),
            Requested(1, "b", 2, 4),
            Assigned(1, "b", 0, "cost", 3.0),
            DoorsOpened(0, 0, 1),
            Boarded(0, "a", 0, 1),
            CarState(0, 0, 1, up, closed, 1),
            CarState(1, 0, 2, up, closed, 1),
            DoorsOpened(2, 0, 2),
            Boarded(2, "b", 0, 2),  # b requested at 1, boards at 2: wait 1
            CarState(2, 0, 2, up, open_, 2),
            CarState(3, 0, 3, up, closed, 2),
            DoorsOpened(3, 0, 3),
            Alighted(3, "a", 0, 3),
            CarState(4, 0, 4, up, closed, 1),
            DoorsOpened(4, 0, 4),
            Alighted(4, "b", 0, 4),
            CarState(5, 0, 4, idle, closed, 0),
        ]
    )


def test_hand_written_journal_gives_the_expected_report() -> None:
    report = aggregate(hand_written_journal())
    a, b = report.passengers
    assert (a.wait, a.travel, a.total, a.excess) == (0, 3, 3, 1)
    assert (b.wait, b.travel, b.total, b.excess) == (1, 2, 3, 1)
    assert report.wait == Stats(2, 0.5, 0.5, 0, 0.5, 0.9, 0.95, 1)
    assert report.total.mean == 3
    assert report.makespan == 4 and report.ticks == 6
    car = report.per_car[0]
    assert (car.passengers, car.distance, car.stops, car.door_open_ticks, car.peak_load) == (
        2,
        3,
        4,
        1,
        2,
    )
    assert car.trips == 1  # straight up 1 -> 4, stopping on the way, then idle
    assert any("reached capacity" in note for note in report.observations)


def test_unserved_passengers_are_reported_not_hidden() -> None:
    journal = Journal(hand_written_journal().events()[:6])  # stops before anyone is delivered
    report = aggregate(journal)
    assert report.passengers == () and set(report.unserved) == {"a", "b"}
    assert report.observations == ("No passengers were served.",)
    assert "UNSERVED 2" in format_summary(report)


def test_aggregate_needs_a_config_if_the_journal_has_none() -> None:
    events = [e for e in hand_written_journal() if not isinstance(e, RunStarted)]
    with pytest.raises(ValueError, match="RunStarted"):
        aggregate(Journal(events))
    report = aggregate(Journal(events), building(floors=10, capacity=2))
    assert report.dispatch == "?" and len(report.passengers) == 2


def test_stats_and_percentiles() -> None:
    assert percentile([], 50) == 0.0
    assert percentile([1, 2, 3, 4], 50) == 2.5
    assert percentile([0, 10], 95) == 9.5
    s = Stats.of([4, 1, 3, 2])
    assert (s.count, s.mean, s.min, s.max, s.p50) == (4, 2.5, 1, 4, 2.5)
    assert s.std == pytest.approx(1.1180, abs=1e-4)
    assert Stats.of([]) == Stats(0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    assert Stats.of(list(range(11))).p90 == 9


def test_unknown_event_kind_is_rejected() -> None:
    with pytest.raises(ValueError, match="unknown event kind"):
        event_from_dict({"kind": "Teleported", "tick": 0})


def test_observations_cover_waits_direction_and_load_balance() -> None:
    requests = reqs((0, "a", 1, 9), (0, "b", 9, 1), (5, "c", 4, 2))
    _, report = run(requests, building(floors=10, cars=3))
    text = " ".join(report.observations)
    for phrase in ("without waiting", "Longest wait", "direct ride time", "going up", "carried"):
        assert phrase in text
    assert "No car reached capacity" in text
