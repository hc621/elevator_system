"""Dispatch policies and the dispatcher's ordering and eligibility rules."""

from collections.abc import Sequence

import pytest
from helpers import building, check_invariants, records, reqs, run

from elevator_sim.car import CarView
from elevator_sim.dispatch import (
    CostDispatch,
    NearestDispatch,
    RoundRobinDispatch,
    ZoneDispatch,
    make_dispatch,
)
from elevator_sim.dispatcher import NoEligibleCar
from elevator_sim.events import Assigned
from elevator_sim.feed import IteratorFeed
from elevator_sim.model import BuildingConfig, CarSpec, Request
from elevator_sim.simulator import simulate


def assigned_cars(journal: object) -> dict[str, int]:
    return {e.passenger: e.car for e in journal.events(Assigned)}  # type: ignore[attr-defined]


def test_round_robin_cycles_through_cars() -> None:
    requests = reqs(*((i, f"p{i}", 1, 5) for i in range(5)))
    journal, _ = run(requests, building(floors=10, cars=3), dispatch="round_robin")
    assert list(assigned_cars(journal).values()) == [0, 1, 2, 0, 1]


def test_nearest_picks_the_closest_car_and_ties_go_to_the_lowest_id() -> None:
    config = building(floors=40, cars=3, placement=(1, 20, 20))
    journal, _ = run(reqs((0, "a", 18, 1), (0, "b", 3, 9)), config, dispatch="nearest")
    assert assigned_cars(journal) == {"a": 1, "b": 0}


def test_zone_assigns_by_the_upper_floor_of_the_trip() -> None:
    requests = reqs((0, "low", 1, 10), (0, "mid", 25, 1), (0, "high", 40, 30))
    journal, _ = run(requests, building(floors=40, cars=3), dispatch="zone")
    assert assigned_cars(journal) == {"low": 0, "mid": 1, "high": 2}


def test_cost_sends_a_new_request_to_the_car_that_serves_it_soonest() -> None:
    requests = reqs((0, "p1", 1, 51), (0, "p2", 1, 37), (10, "p3", 20, 1))
    journal, report = run(requests, building(floors=60, cars=2))
    cars = assigned_cars(journal)
    assert cars["p1"] == cars["p2"] == 0  # same trip, cheaper together
    assert cars["p3"] == 1  # car 0 is heading away; idle car 1 gets there first
    p3 = records(report)["p3"]
    assert (p3.wait, p3.total) == (19, 38)
    costs = {e.passenger: e.cost for e in journal.events(Assigned)}
    assert costs["p3"] == 38.0  # the marginal total time on the idle car


def test_cost_prefers_a_car_already_going_that_way() -> None:
    config = building(floors=30, cars=2, placement=(1, 12))
    journal, _ = run(reqs((0, "a", 1, 20), (3, "b", 10, 15)), config)
    # Car 1 idles at floor 12 (2 floors away) but car 0 passes floor 10 anyway at t9.
    assert assigned_cars(journal) == {"a": 0, "b": 1}
    # ...and it's the marginal cost that decides: b waits 2 ticks on car 1 vs 6 on car 0.


def test_policies_break_ties_by_lowest_id() -> None:
    config = building(floors=10, cars=3)
    for name in ("cost", "nearest"):
        journal, _ = run(reqs((0, "a", 5, 1)), config, dispatch=name)
        assert assigned_cars(journal) == {"a": 0}


def test_make_dispatch_returns_fresh_instances() -> None:
    assert make_dispatch("round_robin") is not make_dispatch("round_robin")
    assert isinstance(make_dispatch("cost"), CostDispatch)
    assert isinstance(make_dispatch("nearest"), NearestDispatch)
    assert isinstance(make_dispatch("zone"), ZoneDispatch)
    with pytest.raises(ValueError, match="unknown dispatch"):
        make_dispatch("paternoster")


def test_assignment_happens_before_the_car_steps_on_the_same_tick() -> None:
    _, report = run(reqs((5, "a", 1, 3)), building(floors=10))
    a = records(report)["a"]
    assert (a.requested, a.boarded, a.wait) == (5, 5, 0)


class _Spy(RoundRobinDispatch):
    def __init__(self) -> None:
        super().__init__()
        self.seen: list[tuple[int, int]] = []

    def choose(self, request: Request, cars: Sequence[CarView], now: int) -> int:
        self.seen.append((request.time, now))
        return super().choose(request, cars, now)


def test_policies_never_see_a_request_before_its_time() -> None:
    requests = reqs((0, "a", 1, 5), (4, "b", 2, 9), (4, "c", 9, 1), (30, "d", 5, 6))
    spy = _Spy()
    simulate(building(floors=10, cars=2), IteratorFeed(requests), spy)
    assert spy.seen == [(0, 0), (4, 4), (4, 4), (30, 30)]


def express_building() -> BuildingConfig:
    express = frozenset({1, *range(21, 41)})
    return BuildingConfig(40, (CarSpec(8), CarSpec(8, 1, express)), door_time=0)


@pytest.mark.parametrize("name", ["cost", "nearest", "round_robin", "zone"])
def test_dispatcher_only_offers_cars_that_serve_both_floors(name: str) -> None:
    requests = reqs((0, "a", 1, 10), (1, "b", 5, 30), (2, "c", 1, 35), (3, "d", 1, 9))
    journal, _ = run(requests, express_building(), dispatch=name)
    cars = assigned_cars(journal)
    assert cars["a"] == cars["b"] == cars["d"] == 0  # floors 5-10 are not served by the express
    check_invariants(journal, requests)


def test_no_eligible_car_is_an_error() -> None:
    config = BuildingConfig(40, (CarSpec(8, 1, frozenset({1, 2, 3})),), door_time=0)
    with pytest.raises(NoEligibleCar):
        run(reqs((0, "a", 1, 30)), config)


class _Rogue(RoundRobinDispatch):
    def choose(self, request: Request, cars: Sequence[CarView], now: int) -> int:
        return 1


def test_a_policy_cannot_choose_an_ineligible_car() -> None:
    config = BuildingConfig(40, (CarSpec(8), CarSpec(8, 1, frozenset({1, 40}))), door_time=0)
    with pytest.raises(ValueError, match="cannot serve"):
        simulate(config, IteratorFeed(reqs((0, "a", 1, 10))), _Rogue())
