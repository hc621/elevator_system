"""Business-building scenarios from three Poisson streams, and plain random traffic for tests."""

import random
from collections import Counter

import pytest

from elevator_sim.scenarios import (
    MAX_LOAD,
    SCENARIOS,
    draw_stream,
    generate,
    poisson,
    random_requests,
)


def by_stream(requests: list) -> dict[str, list]:
    out: dict[str, list] = {"in": [], "out": [], "fl": []}
    for r in requests:
        out[r.id.rstrip("0123456789")].append(r)
    return out


@pytest.mark.parametrize("scenario", sorted(SCENARIOS))
def test_requests_are_valid_sorted_and_reproducible(scenario: str) -> None:
    requests = generate(scenario, floors=20, duration=300, seed=5)
    assert requests == generate(scenario, floors=20, duration=300, seed=5)
    assert requests != generate(scenario, floors=20, duration=300, seed=6)
    assert [r.time for r in requests] == sorted(r.time for r in requests)
    assert all(0 <= r.time < 300 for r in requests)
    assert all(1 <= r.source <= 20 and 1 <= r.dest <= 20 and r.source != r.dest for r in requests)
    assert len({r.id for r in requests}) == len(requests)


def test_each_stream_makes_its_own_kind_of_trip() -> None:
    streams = by_stream(generate("lunch", floors=30, duration=500, seed=1))
    assert all(r.source == 1 and r.dest >= 2 for r in streams["in"])  # inbound: lobby -> up
    assert all(r.source >= 2 and r.dest == 1 for r in streams["out"])  # outbound: up -> lobby
    assert all(r.source >= 2 and r.dest >= 2 for r in streams["fl"])  # inter-floor
    assert {r.dest > r.source for r in streams["fl"]} == {True, False}  # both up and down


def test_arrivals_are_poisson_with_the_scenario_rates() -> None:
    duration = 20_000
    for scenario, rates in SCENARIOS.items():
        streams = by_stream(generate(scenario, floors=30, duration=duration, seed=3))
        for prefix, rate in (("in", rates.inbound), ("out", rates.outbound),
                             ("fl", rates.inter_floor)):  # fmt: skip
            assert len(streams[prefix]) == pytest.approx(rate * duration, rel=0.06)
    # Poisson signature: the per-tick count has variance equal to its mean.
    counts = Counter(r.time for r in generate("morning_rush", 30, duration, seed=4))
    per_tick = [counts.get(t, 0) for t in range(duration)]
    mean = sum(per_tick) / duration
    variance = sum((c - mean) ** 2 for c in per_tick) / duration
    assert mean == pytest.approx(SCENARIOS["morning_rush"].total, rel=0.05)
    assert variance / mean == pytest.approx(1.0, abs=0.06)


def test_streams_are_generated_once_and_shared_by_every_scenario() -> None:
    runs = {s: by_stream(generate(s, floors=30, duration=800, seed=7)) for s in SCENARIOS}
    # Inter-floor traffic is the same passengers in every scenario.
    inter = [runs[s]["fl"] for s in SCENARIOS]
    assert all(group == inter[0] for group in inter)
    # The rush's inbound passengers include every quiet-scenario inbound passenger.
    assert set(runs["quiet"]["in"]) <= set(runs["morning_rush"]["in"])
    assert set(runs["quiet"]["out"]) <= set(runs["evening_rush"]["out"])
    assert len(runs["morning_rush"]["in"]) > 5 * len(runs["quiet"]["in"])


def test_rush_shapes() -> None:
    morning = by_stream(generate("morning_rush", 30, 800, seed=2))
    evening = by_stream(generate("evening_rush", 30, 800, seed=2))
    lunch = by_stream(generate("lunch", 30, 800, seed=2))
    assert len(morning["in"]) > 5 * len(morning["out"])
    assert len(evening["out"]) > 5 * len(evening["in"])
    assert 0.7 < len(lunch["in"]) / len(lunch["out"]) < 1.4


def test_load_scales_the_rates_and_keeps_the_same_passengers() -> None:
    base = generate("quiet", floors=30, duration=2000, seed=9)
    heavy = generate("quiet", floors=30, duration=2000, seed=9, load=2.0)
    assert set(base) <= set(heavy)
    assert len(heavy) == pytest.approx(2 * len(base), rel=0.12)


def test_two_floor_building() -> None:
    requests = generate("lunch", floors=2, duration=200, seed=0)
    assert requests and all({r.source, r.dest} == {1, 2} for r in requests)


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"scenario": "uniform"}, "unknown scenario"),
        ({"floors": 1}, "floors"),
        ({"duration": 0}, "duration"),
        ({"load": 0}, "load"),
        ({"load": MAX_LOAD + 1}, "load"),
    ],
)
def test_bad_arguments(kwargs: dict, message: str) -> None:
    args = {"scenario": "quiet", "floors": 10, "duration": 50, "seed": 0, **kwargs}
    with pytest.raises(ValueError, match=message):
        generate(**args)


def test_poisson_and_stream_helpers() -> None:
    rng = random.Random(0)
    assert poisson(rng, 0) == 0
    draws = [poisson(rng, 2.0) for _ in range(20_000)]
    assert sum(draws) / len(draws) == pytest.approx(2.0, rel=0.03)
    with pytest.raises(ValueError, match="unknown stream"):
        draw_stream("sideways", 10, 10, 0)


def test_random_requests_for_tests() -> None:
    requests = random_requests(floors=20, count=200, duration=100, seed=5)
    assert requests == random_requests(floors=20, count=200, duration=100, seed=5)
    assert [r.id for r in requests] == [f"p{i}" for i in range(1, 201)]
    assert all(r.source != r.dest for r in requests)
    lobby = random_requests(30, 1000, 100, 1, lobby_up=0.8, lobby_down=0.1)
    assert 0.75 < sum(r.source == 1 for r in lobby) / 1000 < 0.85
    assert all({r.source, r.dest} == {1, 2} for r in random_requests(2, 10, 5, 0, 0.4, 0.4))
    with pytest.raises(ValueError, match="floors"):
        random_requests(1, 5, 5, 0)


def test_stream_ids_match_trip_kinds() -> None:
    from elevator_sim.report import trip_kind

    kind = {"in": "inbound", "out": "outbound", "fl": "inter_floor"}
    for r in generate("lunch", floors=30, duration=400, seed=3):
        assert trip_kind(r.source, r.dest) == kind[r.id.rstrip("0123456789")]
