"""Whole runs: the brief's example (golden), the positions log, determinism and liveness."""

import pytest
from helpers import building, check_invariants, floors_by_car, records, reqs, run

from elevator_sim.dispatch import make_dispatch
from elevator_sim.events import CarState
from elevator_sim.feed import IteratorFeed, SimulationStalled
from elevator_sim.journal import Journal
from elevator_sim.motion import CarSnapshot, Idle, LookMotion
from elevator_sim.scenarios import generate
from elevator_sim.simulator import Simulator, simulate

BRIEF = reqs((0, "passenger1", 1, 51), (0, "passenger2", 1, 37), (10, "passenger3", 20, 1))


def timeline(report: object) -> dict[str, tuple[int, int, int]]:
    return {pid: (r.boarded, r.alighted, r.total) for pid, r in records(report).items()}  # type: ignore[arg-type]


def test_brief_example_one_car_door_time_0() -> None:
    journal, report = run(BRIEF, building(floors=60, door_time=0))
    assert timeline(report) == {
        "passenger1": (0, 50, 50),
        "passenger2": (0, 36, 36),
        "passenger3": (81, 100, 90),  # waits while the car finishes its trip up to 51
    }
    assert report.ticks == 101 and report.makespan == 100
    check_invariants(journal, BRIEF)


def test_brief_example_one_car_door_time_1() -> None:
    journal, report = run(BRIEF, building(floors=60, door_time=1))
    assert timeline(report) == {
        "passenger1": (0, 52, 52),  # +1 at floor 1 and +1 at the stop at 37
        "passenger2": (0, 37, 37),
        "passenger3": (84, 104, 94),
    }
    check_invariants(journal, BRIEF)


def test_brief_example_three_cars() -> None:
    journal, report = run(BRIEF, building(floors=60, cars=3, door_time=1))
    p3 = records(report)["passenger3"]
    assert p3.car != records(report)["passenger1"].car
    assert (p3.boarded, p3.wait) == (29, 19)
    check_invariants(journal, BRIEF)


def test_positions_log_has_one_row_per_tick_from_zero_including_idle_gaps() -> None:
    requests = reqs((0, "a", 1, 3), (20, "b", 3, 1))
    journal, report = run(requests, building(floors=5, cars=2))
    rows = floors_by_car(journal)
    assert len(rows[0]) == len(rows[1]) == 23  # t = 0..22
    assert rows[0][:3] == [1, 2, 3] and rows[0][3:20] == [3] * 17  # idles at 3 until b
    assert report.makespan == 22


def test_no_requests_still_logs_tick_zero() -> None:
    journal, report = run([], building(floors=5, cars=2))
    assert [(s.tick, s.floor) for s in journal.events(CarState)] == [(0, 1), (0, 1)]
    assert report.passengers == ()


def test_same_inputs_give_an_identical_journal() -> None:
    requests = generate("morning_rush", floors=30, count=80, duration=120, seed=11)
    config = building(floors=30, cars=4, capacity=6, door_time=1)
    first, _ = run(requests, config)
    second, _ = run(requests, config)
    assert first.events() == second.events()


def test_a_request_after_a_long_idle_gap_is_not_a_stall() -> None:
    requests = reqs((0, "a", 1, 2), (5000, "b", 2, 1))
    _, report = run(requests, building(floors=3))
    assert records(report)["b"].wait == 0


class _NeverMoves(LookMotion):
    def next_action(self, s: CarSnapshot) -> Idle:
        return Idle()


def test_a_policy_that_never_serves_anyone_is_caught_by_the_projection() -> None:
    feed = IteratorFeed(reqs((0, "a", 5, 1)))
    with pytest.raises(SimulationStalled, match="projection did not finish"):
        simulate(building(floors=10), feed, make_dispatch("cost"), _NeverMoves())


class _BreaksLater(LookMotion):
    broken = False

    def next_action(self, s: CarSnapshot) -> object:
        return Idle() if self.broken else super().next_action(s)


def test_a_car_that_stops_serving_after_assignment_trips_the_stall_guard() -> None:
    motion = _BreaksLater()
    sim = Simulator(building(floors=10), make_dispatch("cost"), motion)
    sim.submit(reqs((0, "a", 5, 1))[0])
    sim.step()  # assigned and projected while the policy still works
    motion.broken = True
    with pytest.raises(SimulationStalled, match="no passenger boarded"):
        while True:
            sim.step()


def test_max_ticks_limit() -> None:
    feed = IteratorFeed(reqs((0, "a", 1, 50)))
    with pytest.raises(SimulationStalled, match="tick limit"):
        simulate(building(floors=60), feed, make_dispatch("cost"), max_ticks=10)


def test_simulator_rejects_requests_in_the_past_and_accepts_future_ones() -> None:
    journal = Journal()
    sim = Simulator(building(floors=10), make_dispatch("cost"), sink=journal)
    sim.submit(reqs((3, "later", 1, 4))[0])
    for _ in range(5):
        sim.step()
    with pytest.raises(ValueError, match="in the past"):
        sim.submit(reqs((2, "late", 1, 4))[0])
    assert not sim.idle()
    assert sim.snapshot()[0].assigned == 1
