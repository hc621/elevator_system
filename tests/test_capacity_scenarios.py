"""Capacity along the route, end to end, and what round-robin does (and doesn't) look at.

All runs use door_time 0 unless stated, so a car moving up from floor 1 at t=0 is at floor 1 + t.
"""

from helpers import building, check_invariants, floors_by_car, records, reqs, run

from elevator_sim.dispatch import make_dispatch
from elevator_sim.events import Assigned
from elevator_sim.journal import Journal
from elevator_sim.model import BuildingConfig, CarSpec, Request
from elevator_sim.report import aggregate
from elevator_sim.simulator import Simulator

# A full car (capacity 4): two get off at 6, two at 10.
FULL_CAR = [(0, "a", 1, 6), (0, "b", 1, 6), (0, "c", 1, 10), (0, "d", 1, 10)]


def test_room_freed_at_floor_6_is_used_at_floor_8_on_the_same_sweep() -> None:
    requests = reqs(*FULL_CAR, (2, "e", 8, 12), (2, "f", 8, 12))
    journal, report = run(requests, building(floors=20, capacity=4))
    r = records(report)
    # t5: floor 6, a and b get off (load 4 -> 2). t7: floor 8, e and f get on (load 4 again).
    assert (r["a"].alighted, r["e"].boarded, r["f"].boarded) == (5, 7, 7)
    assert (r["c"].alighted, r["e"].alighted) == (9, 11)
    assert floors_by_car(journal)[0] == list(range(1, 13))  # straight up, never back
    assert report.diagnostics.full_passby_share == 0
    check_invariants(journal, requests)


def test_three_waiting_with_room_for_two_the_first_two_board_and_the_car_comes_back() -> None:
    requests = reqs(*FULL_CAR, (2, "e", 8, 12), (2, "f", 8, 12), (2, "g", 8, 12))
    journal, report = run(requests, building(floors=20, capacity=4))
    r = records(report)
    assert (r["e"].boarded, r["f"].boarded) == (7, 7)  # earliest assigned first
    # g is left at 8; the car drops e and f at 12 (t11), nothing lies above, so it reverses,
    # reaches 8 at t15, turns up for g and drops g at 12 at t19.
    assert (r["g"].boarded, r["g"].alighted, r["g"].wait) == (15, 19, 13)
    assert floors_by_car(journal)[0] == [*range(1, 13), 11, 10, 9, *range(8, 13)]
    assert report.diagnostics.full_passby_share == 1 / 7  # g saw the car pass full at t7
    check_invariants(journal, requests)


def test_projection_predicts_the_freed_room_and_the_late_pickup() -> None:
    journal = Journal()
    sim = Simulator(building(floors=20, capacity=4), make_dispatch("cost"), sink=journal)
    for request in reqs(*FULL_CAR, (2, "e", 8, 12), (2, "f", 8, 12)):
        sim.submit(request)
    for _ in range(3):  # ticks 0, 1, 2: e and f are assigned at t2
        sim.step()
    car = sim.snapshot()[0]
    now = car.project()
    assert (now.pickup_eta["e"], now.pickup_eta["f"]) == (7, 7)  # room freed at 6, used at 8
    with_g = car.project(Request(3, "g", 8, 12))
    assert (with_g.pickup_eta["g"], with_g.dropoff_eta["g"]) == (15, 19)  # full at 8: comes back
    # ...and that is exactly what happens.
    sim.submit(Request(3, "g", 8, 12))
    while not sim.idle():
        sim.step()
    g = {p.id: p for p in aggregate(journal).passengers}["g"]
    assert (g.boarded, g.alighted) == (15, 19)


def cost_choice_config() -> BuildingConfig:
    # Car 1 can't serve the lobby, so the four lobby passengers must all go to car 0.
    return BuildingConfig(20, (CarSpec(4, 1), CarSpec(4, 4, frozenset(range(2, 21)))), door_time=0)


def test_cost_picks_the_full_car_when_it_frees_room_before_the_pickup() -> None:
    requests = reqs(*FULL_CAR, (4, "e", 8, 12))
    journal, report = run(requests, cost_choice_config())
    # Car 0 (full, at floor 5) frees two places at 6 and reaches 8 at t7: e's total 3 + 4 = 7.
    # Idle car 1 at floor 4 would reach 8 at t8: total 4 + 4 = 8.
    assert {e.passenger: e.car for e in journal.events(Assigned)}["e"] == 0
    assert records(report)["e"].wait == 3


def test_cost_picks_another_car_when_the_full_car_frees_no_room_in_time() -> None:
    full_to_10 = [(0, p, 1, 10) for p in "abcd"]
    requests = reqs(*full_to_10, (4, "e", 8, 12))
    journal, report = run(requests, cost_choice_config())
    # Car 0 passes 8 full, empties at 10 (t9) and comes back to 8 at t11: e's total 7 + 4 = 11.
    # Car 1: total 8. The projection applies the capacity rule, so cost sees this.
    assert {e.passenger: e.car for e in journal.events(Assigned)}["e"] == 1
    assert records(report)["e"].wait == 4


def test_round_robin_ignores_car_state() -> None:
    requests = reqs((0, "r1", 1, 20), (1, "r2", 1, 3), (4, "r3", 2, 5))
    config = building(floors=20, cars=2)
    journal, report = run(requests, config, dispatch="round_robin")
    cars = {e.passenger: e.car for e in journal.events(Assigned)}
    # r3's turn falls to car 0, which is at floor 5 heading for 20, although car 1 sits idle at 3.
    assert cars == {"r1": 0, "r2": 1, "r3": 0}
    # Car 0 reaches 20 at t19, comes back down to 2 at t37: r3 waits 33 ticks.
    assert records(report)["r3"].wait == 33
    assert report.diagnostics.assignment["moving_away"].count == 1

    # Same input, cost dispatch: car 1 is idle one floor away.
    journal, report = run(requests, config, dispatch="cost")
    assert {e.passenger: e.car for e in journal.events(Assigned)}["r3"] == 1
    assert records(report)["r3"].wait == 1


def test_round_robin_does_not_know_about_capacity_but_the_car_enforces_it() -> None:
    requests = reqs(*((0, f"p{i}", 1, 5) for i in range(6)))
    journal, report = run(requests, building(floors=10, cars=2, capacity=1), dispatch="round_robin")
    assert [e.car for e in journal.events(Assigned)] == [0, 1, 0, 1, 0, 1]
    assert all(c.peak_load == 1 for c in report.per_car.values())
    assert report.diagnostics.full_passby_share > 0  # people at the lobby watched a full car leave
    check_invariants(journal, requests)  # includes "load never exceeds capacity" and "all served"


def test_capacity_along_the_route_with_door_time_1() -> None:
    # Same freed-room scenario with real stops: each stop holds the car one extra tick.
    requests = reqs(*FULL_CAR, (2, "e", 8, 12), (2, "f", 8, 12))
    journal, report = run(requests, building(floors=20, capacity=4, door_time=1))
    r = records(report)
    # t0-1 board at 1; up one floor per tick from t2: floor 6 at t6 (stop to t7), 8 at t9.
    assert (r["a"].alighted, r["e"].boarded) == (6, 9)
    assert report.diagnostics.full_passby_share == 0
    check_invariants(journal, requests)
