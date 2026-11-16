"""Seeded random runs over every policy combination; the invariants must hold for all of them.

(Phase 5 adds hypothesis-generated buildings and loads; this is the fixed-seed version.)
"""

import pytest
from helpers import building, check_invariants, run

from elevator_sim.dispatch import DISPATCH_POLICIES
from elevator_sim.motion import MOTION_POLICIES
from elevator_sim.scenarios import SCENARIOS, generate, random_requests


@pytest.mark.parametrize("dispatch", sorted(DISPATCH_POLICIES))
@pytest.mark.parametrize("motion", sorted(MOTION_POLICIES))
@pytest.mark.parametrize("door_time", [0, 1, 2])
def test_invariants_hold_for_every_policy(dispatch: str, motion: str, door_time: int) -> None:
    for seed, scenario in enumerate(sorted(SCENARIOS)):
        requests = generate(scenario, floors=15, duration=60, seed=seed)
        config = building(floors=15, cars=3, capacity=3, door_time=door_time, placement="spread")
        journal, report = run(requests, config, dispatch=dispatch, motion=motion)
        check_invariants(journal, requests)
        assert not report.unserved


@pytest.mark.parametrize("motion", sorted(MOTION_POLICIES))
def test_heavy_load_on_a_single_small_car_still_serves_everyone(motion: str) -> None:
    requests = random_requests(floors=12, count=120, duration=30, seed=99)
    journal, report = run(requests, building(floors=12, cars=1, capacity=2), motion=motion)
    check_invariants(journal, requests)
    assert len(report.passengers) == 120
