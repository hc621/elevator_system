"""Motion rules: unit tests on snapshots, then LOOK vs SCAN on whole runs."""

from dataclasses import replace

import pytest
from helpers import building, check_invariants, floors_by_car, records, reqs, run

from elevator_sim.model import Direction, Request
from elevator_sim.motion import (
    CarSnapshot,
    Idle,
    LookMotion,
    Move,
    OpenDoors,
    ScanMotion,
    make_motion,
)
from elevator_sim.scenarios import random_requests

UP, DOWN, IDLE = Direction.UP, Direction.DOWN, Direction.IDLE


def snap(
    floor: int,
    direction: Direction = IDLE,
    onboard: tuple[Request, ...] = (),
    waiting: tuple[Request, ...] = (),
    capacity: int = 8,
    top: int = 20,
) -> CarSnapshot:
    return CarSnapshot(floor, direction, len(onboard), capacity, top, onboard, waiting)


def r(pid: str, source: int, dest: int) -> Request:
    return Request(0, pid, source, dest)


@pytest.mark.parametrize("policy", [LookMotion(), ScanMotion()])
def test_no_work_means_idle(policy: LookMotion) -> None:
    assert policy.next_action(snap(5)) == Idle()
    assert policy.next_action(snap(5, UP)) == Idle()


@pytest.mark.parametrize("policy", [LookMotion(), ScanMotion()])
def test_idle_car_serves_its_own_floor_first(policy: LookMotion) -> None:
    s = snap(5, waiting=(r("far", 6, 9), r("here", 5, 1)))
    assert policy.next_action(s) == OpenDoors(DOWN)


@pytest.mark.parametrize("policy", [LookMotion(), ScanMotion()])
def test_idle_car_heads_for_nearest_work_ties_go_up(policy: LookMotion) -> None:
    assert policy.next_action(snap(10, waiting=(r("a", 7, 1), r("b", 12, 1)))) == Move(UP)
    assert policy.next_action(snap(10, waiting=(r("a", 9, 1), r("b", 13, 1)))) == Move(DOWN)


def test_look_keeps_direction_while_work_lies_ahead() -> None:
    s = snap(5, UP, onboard=(r("a", 1, 9),), waiting=(r("b", 3, 1),))
    assert LookMotion().next_action(s) == Move(UP)


def test_look_reverses_when_nothing_lies_ahead() -> None:
    s = snap(5, UP, waiting=(r("b", 3, 1),))
    assert LookMotion().next_action(s) == Move(DOWN)


def test_look_reverses_at_a_floor_to_pick_up_someone_going_the_other_way() -> None:
    s = snap(9, UP, onboard=(r("a", 1, 9),), waiting=(r("b", 9, 2),))
    assert LookMotion().next_action(s) == OpenDoors(DOWN)


def test_scan_runs_to_the_end_of_the_shaft_before_reversing() -> None:
    s = snap(5, UP, waiting=(r("b", 3, 1),), top=20)
    assert ScanMotion().next_action(s) == Move(UP)
    assert ScanMotion().next_action(snap(20, UP, waiting=(r("b", 3, 1),))) == Move(DOWN)
    assert ScanMotion().next_action(snap(1, DOWN, waiting=(r("b", 3, 9),))) == Move(UP)


def test_boarding_respects_direction_and_room() -> None:
    waiting = (r("up1", 5, 9), r("down", 5, 1), r("up2", 5, 8), r("up3", 5, 7))
    onboard = (r("x", 1, 12),)
    s = snap(5, UP, onboard=onboard, waiting=waiting, capacity=3)
    assert LookMotion().who_boards(s) == ("up1", "up2")  # 2 free places, down-going excluded


def test_full_car_does_not_stop_for_a_pickup() -> None:
    s = snap(5, UP, onboard=(r("x", 1, 12),), waiting=(r("b", 5, 9),), capacity=1)
    assert LookMotion().next_action(s) == Move(UP)


def test_room_freed_by_alighting_counts_for_boarding() -> None:
    s = snap(5, UP, onboard=(r("x", 1, 5),), waiting=(r("b", 5, 9),), capacity=1)
    assert LookMotion().next_action(s) == OpenDoors(UP)


def test_make_motion() -> None:
    assert make_motion("look").name == "look"
    assert make_motion("scan").name == "scan"
    with pytest.raises(ValueError, match="unknown motion"):
        make_motion("elevator-music")


# --- whole runs -------------------------------------------------------------------------------


def test_scan_reaches_the_top_floor_and_look_does_not() -> None:
    requests = reqs((0, "a", 1, 10), (0, "b", 1, 5))
    config = building(floors=20)
    look_journal, _ = run(requests, config, motion="look")
    scan_journal, _ = run(requests, config, motion="scan")
    assert max(floors_by_car(look_journal)[0]) == 10
    assert max(floors_by_car(scan_journal)[0]) == 10  # no work left: SCAN idles, it doesn't sweep

    requests = reqs((0, "a", 1, 10), (2, "b", 5, 1))
    look_journal, _ = run(requests, config, motion="look")
    scan_journal, _ = run(requests, config, motion="scan")
    assert max(floors_by_car(look_journal)[0]) == 10
    assert max(floors_by_car(scan_journal)[0]) == 20  # work below: SCAN still goes to the top


def distance(report: object) -> int:
    return sum(c.distance for c in report.per_car.values())  # type: ignore[attr-defined]


@pytest.mark.parametrize("seed", range(3))
def test_look_and_scan_serve_the_same_passengers(seed: int) -> None:
    requests = random_requests(floors=20, count=40, duration=100, seed=seed)
    config = building(floors=20, cars=2, capacity=4, door_time=1)
    look_journal, look = run(requests, config, dispatch="round_robin", motion="look")
    scan_journal, scan = run(requests, config, dispatch="round_robin", motion="scan")
    check_invariants(look_journal, requests)
    check_invariants(scan_journal, requests)
    assert set(records(look)) == set(records(scan)) == {r.id for r in requests}


@pytest.mark.parametrize("seed", range(5))
def test_look_never_travels_further_than_scan_when_all_requests_are_known(seed: int) -> None:
    requests = [replace(r, time=0) for r in random_requests(20, 40, 100, seed)]
    config = building(floors=20, cars=2, capacity=40, door_time=1)
    _, look = run(requests, config, dispatch="round_robin", motion="look")
    _, scan = run(requests, config, dispatch="round_robin", motion="scan")
    assert distance(look) <= distance(scan)


def test_look_can_travel_further_than_scan_when_requests_arrive_over_time() -> None:
    # LOOK turns back early; a later request beyond its turning point sends it back again,
    # where SCAN would already have been. Seed 2 is one such case (about 1 seed in 4).
    requests = random_requests(floors=20, count=40, duration=100, seed=2)
    config = building(floors=20, cars=2, capacity=4, door_time=1)
    _, look = run(requests, config, dispatch="round_robin", motion="look")
    _, scan = run(requests, config, dispatch="round_robin", motion="scan")
    assert distance(look) > distance(scan)
