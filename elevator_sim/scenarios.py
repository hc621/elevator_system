"""Seeded request generators: business-building scenarios from Poisson streams, and plain random
traffic for tests.

Business building (offices): people arrive in the morning, leave in the evening, go out and come
back at lunch, and move between floors all day. Requests come from three independent streams, each
a Poisson process (the number of new requests in a tick is Poisson-distributed with the stream's
rate, so arrivals are random and bursty, not evenly spaced):

1. **inbound**: lobby (floor 1) -> a random upper floor
2. **outbound**: a random upper floor -> lobby
3. **inter-floor**: a random upper floor -> a different random upper floor, up or down

Inter-floor traffic runs at the same steady rate in every scenario; the scenarios differ only in
the inbound and outbound rates:

| scenario | inbound | outbound | inter-floor |
|---|---|---|---|
| quiet | light | light | steady |
| morning_rush | **heavy** | light | steady |
| lunch | moderate | moderate | steady |
| evening_rush | light | **heavy** | steady |

**Generated once, shared by every scenario.** For a seed, each stream is drawn once at a cap rate
(``MAX_LOAD`` times the highest rate any scenario uses for it), and every candidate request gets a
uniform random number u. A scenario keeps a candidate when ``u < its rate / cap rate``: thinning a
Poisson process this way gives a Poisson process at the lower rate. So for one seed the inter-floor
passengers are *identical* in every scenario, the morning rush's inbound passengers include the
quiet scenario's, and the only difference between scenarios is the rush stream itself.

A residential building would reverse the rushes (outbound in the morning, inbound in the evening)
and a hotel has different peaks; only the business pattern is modelled here.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass

from elevator_sim.model import Floor, Request

STREAMS = ("inbound", "outbound", "inter_floor")
_PREFIX = {"inbound": "in", "outbound": "out", "inter_floor": "fl"}


@dataclass(frozen=True)
class Rates:
    """Expected new requests per tick for each stream."""

    inbound: float
    outbound: float
    inter_floor: float

    @property
    def total(self) -> float:
        return self.inbound + self.outbound + self.inter_floor

    def scaled(self, load: float) -> Rates:
        return Rates(self.inbound * load, self.outbound * load, self.inter_floor * load)


LIGHT, MODERATE, HEAVY, STEADY = 0.03, 0.15, 0.30, 0.06
SCENARIOS: dict[str, Rates] = {
    "quiet": Rates(inbound=LIGHT, outbound=LIGHT, inter_floor=STEADY),
    "morning_rush": Rates(inbound=HEAVY, outbound=LIGHT, inter_floor=STEADY),
    "lunch": Rates(inbound=MODERATE, outbound=MODERATE, inter_floor=STEADY),
    "evening_rush": Rates(inbound=LIGHT, outbound=HEAVY, inter_floor=STEADY),
}
MAX_LOAD = 4.0  # loads up to this multiple of the scenario rates share one generated stream


def _cap(stream: str) -> float:
    return MAX_LOAD * max(getattr(r, stream) for r in SCENARIOS.values())


def poisson(rng: random.Random, rate: float) -> int:
    """A Poisson(rate) draw (Knuth's method; fine for the small rates used per tick)."""
    if rate <= 0:
        return 0
    limit, k, p = math.exp(-rate), 0, rng.random()
    while p > limit:
        k += 1
        p *= rng.random()
    return k


@dataclass(frozen=True)
class Candidate:
    """One request of a stream drawn at the cap rate, before thinning."""

    time: int
    index: int  # position in its stream; gives a stable id across scenarios
    u: float  # kept by a scenario when u < rate / cap
    source: Floor
    dest: Floor


def draw_stream(stream: str, floors: int, duration: int, seed: int) -> list[Candidate]:
    """Every candidate request of one stream for one seed, at the stream's cap rate."""
    if stream not in STREAMS:
        raise ValueError(f"unknown stream {stream!r}; expected one of {STREAMS}")
    rng = random.Random(f"{seed}:{stream}")  # independent, reproducible substream per stream
    cap = _cap(stream)
    uppers = range(2, floors + 1)
    out: list[Candidate] = []
    for t in range(duration):
        for _ in range(poisson(rng, cap)):
            u = rng.random()
            if stream == "inbound":
                source, dest = 1, rng.choice(uppers)
            elif stream == "outbound":
                source, dest = rng.choice(uppers), 1
            elif floors >= 3:
                source, dest = rng.sample(uppers, 2)
            else:  # two floors: no pair of distinct upper floors exists
                source, dest = rng.sample(range(1, floors + 1), 2)
            out.append(Candidate(t, len(out) + 1, u, source, dest))
    return out


def generate(
    scenario: str, floors: int, duration: int, seed: int, load: float = 1.0
) -> list[Request]:
    """The requests of one business-building scenario, sorted by time.

    ``load`` scales every stream's rate (1.0 = the scenario as defined, up to ``MAX_LOAD``).
    Ids name the stream and the passenger's position in it (``in17``, ``out3``, ``fl8``), so the
    same passenger has the same id in every scenario of a seed.
    """
    if scenario not in SCENARIOS:
        raise ValueError(f"unknown scenario {scenario!r}; expected one of {sorted(SCENARIOS)}")
    if floors < 2 or duration < 1:
        raise ValueError("need floors >= 2 and duration >= 1")
    if not 0 < load <= MAX_LOAD:
        raise ValueError(f"load must be in (0, {MAX_LOAD:g}]")
    rates = SCENARIOS[scenario].scaled(load)
    requests = []
    for order, stream in enumerate(STREAMS):
        keep = getattr(rates, stream) / _cap(stream)
        for c in draw_stream(stream, floors, duration, seed):
            if c.u < keep:
                requests.append(
                    (c.time, order, c.index, Request(c.time, f"{_PREFIX[stream]}{c.index}",
                                                     c.source, c.dest))
                )  # fmt: skip
    requests.sort(key=lambda item: item[:3])
    return [r for *_, r in requests]


def random_requests(
    floors: int,
    count: int,
    duration: int,
    seed: int,
    lobby_up: float = 0.0,
    lobby_down: float = 0.0,
) -> list[Request]:
    """Plain random traffic for tests: ``count`` requests, arrival times uniform over the window.

    With both shares 0 every trip is any floor -> any other floor; otherwise ``lobby_up`` of trips
    start at the lobby, ``lobby_down`` end there and the rest are between upper floors. Ids are
    ``p1``, ``p2``, ... in time order. Kept unchanged so hand-checked test expectations hold.
    """
    if floors < 2 or count < 0 or duration < 1:
        raise ValueError("need floors >= 2, count >= 0 and duration >= 1")
    rng = random.Random(seed)
    times = sorted(rng.randrange(duration) for _ in range(count))
    requests = []
    for i, t in enumerate(times, start=1):
        source, dest = _trip(rng, floors, lobby_up, lobby_down)
        requests.append(Request(t, f"p{i}", source, dest))
    return requests


def _trip(
    rng: random.Random, floors: int, lobby_up: float, lobby_down: float
) -> tuple[Floor, Floor]:
    if (lobby_up == 0 and lobby_down == 0) or floors == 2:
        source, dest = rng.sample(range(1, floors + 1), 2)
        return source, dest
    roll = rng.random()
    if roll < lobby_up:
        return 1, rng.randint(2, floors)
    if roll < lobby_up + lobby_down:
        return rng.randint(2, floors), 1
    source, dest = rng.sample(range(2, floors + 1), 2)
    return source, dest
