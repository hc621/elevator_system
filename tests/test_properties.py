"""Property-based tests (hypothesis): random buildings, loads and policies.

Derandomized so CI is reproducible; each property tries a few dozen generated cases.
"""

from helpers import check_invariants
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from elevator_sim.dispatch import make_dispatch
from elevator_sim.journal import Journal
from elevator_sim.model import BuildingConfig, Request
from elevator_sim.motion import make_motion
from elevator_sim.parking import make_parking
from elevator_sim.report import aggregate
from elevator_sim.scenarios import SCENARIOS, generate
from elevator_sim.simulator import Simulator

SETTINGS = settings(
    max_examples=40, deadline=None, derandomize=True, suppress_health_check=[HealthCheck.too_slow]
)

buildings = st.builds(
    lambda floors, cars, capacity, door_time, placement: BuildingConfig.uniform(
        floors, cars, capacity, placement, door_time
    ),
    floors=st.integers(2, 30),
    cars=st.integers(1, 5),
    capacity=st.integers(1, 10),
    door_time=st.integers(0, 2),
    placement=st.sampled_from(["lobby", "spread"]),
)
policies = st.tuples(
    st.sampled_from(["cost", "cost:0.2", "nearest", "zone", "round_robin"]),
    st.sampled_from(["look", "scan"]),
    st.sampled_from(["stay", "lobby", "spread", "demand"]),
)
traffic = st.tuples(
    st.sampled_from(sorted(SCENARIOS)), st.integers(10, 120), st.integers(0, 10_000),
    st.sampled_from([0.5, 1.0, 2.0]),
)  # fmt: skip


def requests_for(config: BuildingConfig, scenario: str, duration: int, seed: int, load: float):
    return generate(scenario, config.floors, duration, seed, load)


def simulator(config: BuildingConfig, dispatch: str, motion: str, parking: str):  # type: ignore[no-untyped-def]
    journal = Journal()
    sim = Simulator(
        config, make_dispatch(dispatch), make_motion(motion), journal, parking=make_parking(parking)
    )
    return sim, journal


@SETTINGS
@given(config=buildings, policy=policies, load=traffic)
def test_every_run_serves_everyone_and_keeps_every_invariant(
    config: BuildingConfig, policy: tuple[str, str, str], load: tuple
) -> None:
    requests = requests_for(config, *load)
    sim, journal = simulator(config, *policy)
    for r in requests:
        sim.submit(r)
    while not sim.idle():  # SimulationStalled would fail the test: every run must terminate
        sim.step()
    check_invariants(journal, requests)
    report = aggregate(journal)
    assert not report.unserved and len(report.passengers) == len(requests)
    assert all(r.wait >= 0 and r.travel >= r.direct for r in report.passengers)


def _same(a: object, b: object) -> bool:
    return (a.route, dict(a.pickup_eta), dict(a.dropoff_eta), a.total_time, dict(a.waits)) == (  # type: ignore[attr-defined]
        b.route, dict(b.pickup_eta), dict(b.dropoff_eta), b.total_time, dict(b.waits),  # type: ignore[attr-defined]
    )  # fmt: skip


@SETTINGS
@given(config=buildings, policy=policies, load=traffic, probe=st.integers(2, 29))
def test_fast_projection_equals_the_exact_step_by_step_one(
    config: BuildingConfig, policy: tuple[str, str, str], load: tuple, probe: int
) -> None:
    """The cached plan and the floor-skipping give exactly what stepping every tick gives."""
    requests = requests_for(config, *load)
    sim, _ = simulator(config, *policy)
    for r in requests:
        sim.submit(r)
    extra_floor = min(probe, config.floors)
    source, dest = (1, extra_floor) if extra_floor > 1 else (2, 1)
    while not sim.idle():
        sim.step()
        for view in sim.snapshot():
            car = view._car  # the car itself, to compare fast and exact projections
            assert _same(car.project(), car.project(fast=False))
            extra = Request(sim.now, "probe", source, dest)
            if car.spec.can_serve(extra):
                assert _same(car.project(extra), car.project(extra, fast=False))


@SETTINGS
@given(config=buildings, policy=policies, load=traffic, cut=st.integers(0, 60))
def test_projection_predicts_what_really_happens_when_no_more_requests_arrive(
    config: BuildingConfig, policy: tuple[str, str, str], load: tuple, cut: int
) -> None:
    requests = [r for r in requests_for(config, *load) if r.time <= cut]
    sim, journal = simulator(config, *policy)
    for r in requests:
        sim.submit(r)
    while sim.now <= cut:
        sim.step()
    predicted = {view.id: view.project() for view in sim.snapshot()}
    while not sim.idle():
        sim.step()
    report = aggregate(journal)
    for record in report.passengers:
        projection = predicted[record.car]
        if record.id in projection.dropoff_eta:
            assert projection.dropoff_eta[record.id] == record.alighted
        if record.id in projection.pickup_eta:
            assert projection.pickup_eta[record.id] == record.boarded
