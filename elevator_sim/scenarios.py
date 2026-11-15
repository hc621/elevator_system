"""Seeded request generators for demos, tests and benchmarks."""

from __future__ import annotations

import random

from elevator_sim.model import Floor, Request

# Trip mix per scenario: share of (lobby -> upper, upper -> lobby);
# the rest of the trips are between upper floors.
SCENARIOS: dict[str, tuple[float, float]] = {
    "uniform": (0.0, 0.0),  # any floor to any floor
    "morning_rush": (0.8, 0.1),
    "evening_rush": (0.1, 0.8),
    "mixed": (0.4, 0.4),
}


def generate(scenario: str, floors: int, count: int, duration: int, seed: int) -> list[Request]:
    """``count`` requests with arrival times uniform over ``[0, duration)``, sorted by time.

    Ids are ``p1``, ``p2``, ... in time order. The same arguments always give the same list.
    """
    if scenario not in SCENARIOS:
        raise ValueError(f"unknown scenario {scenario!r}; expected one of {sorted(SCENARIOS)}")
    if floors < 2 or count < 0 or duration < 1:
        raise ValueError("need floors >= 2, count >= 0 and duration >= 1")
    rng = random.Random(seed)
    up_share, down_share = SCENARIOS[scenario]
    times = sorted(rng.randrange(duration) for _ in range(count))
    requests = []
    for i, t in enumerate(times, start=1):
        source, dest = _trip(rng, floors, scenario, up_share, down_share)
        requests.append(Request(t, f"p{i}", source, dest))
    return requests


def _trip(
    rng: random.Random, floors: int, scenario: str, up_share: float, down_share: float
) -> tuple[Floor, Floor]:
    if scenario == "uniform" or floors == 2:
        source, dest = rng.sample(range(1, floors + 1), 2)
        return source, dest
    roll = rng.random()
    if roll < up_share:
        return 1, rng.randint(2, floors)
    if roll < up_share + down_share:
        return rng.randint(2, floors), 1
    source, dest = rng.sample(range(2, floors + 1), 2)
    return source, dest
