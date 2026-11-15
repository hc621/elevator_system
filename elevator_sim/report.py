"""Aggregation: a pure function from a journal to a report. It never reads car state.

Timestamps per passenger::

    requested --wait--> boarded --travel--> alighted
    |<-------------------- total -------------->|
    direct = |dest - source|, excess = total - direct

A car *trip* starts when the car begins to move and ends when it reverses or goes idle; stops
along the way (doors opening while it keeps the same direction) do not end it.
"""

from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from itertools import pairwise

from elevator_sim.events import Alighted, Assigned, Boarded, CarState, DoorsOpened, Requested
from elevator_sim.journal import Journal
from elevator_sim.model import BuildingConfig, CarId, Direction, Doors, Floor, PassengerId, Tick


def percentile(sorted_values: Sequence[float], q: float) -> float:
    """Linear-interpolation percentile (numpy's default) of already-sorted values, q in [0, 100]."""
    if not sorted_values:
        return 0.0
    pos = (len(sorted_values) - 1) * q / 100
    lo, hi = math.floor(pos), math.ceil(pos)
    return sorted_values[lo] + (sorted_values[hi] - sorted_values[lo]) * (pos - lo)


@dataclass(frozen=True)
class Stats:
    count: int
    mean: float
    std: float  # population standard deviation
    min: float
    p50: float
    p90: float
    p95: float
    max: float

    @classmethod
    def of(cls, values: Sequence[float]) -> Stats:
        if not values:
            return cls(0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        ordered = sorted(values)
        n = len(ordered)
        mean = sum(ordered) / n
        std = math.sqrt(sum((v - mean) ** 2 for v in ordered) / n)
        return cls(
            count=n,
            mean=mean,
            std=std,
            min=ordered[0],
            p50=percentile(ordered, 50),
            p90=percentile(ordered, 90),
            p95=percentile(ordered, 95),
            max=ordered[-1],
        )


@dataclass(frozen=True)
class PassengerRecord:
    id: PassengerId
    car: CarId
    source: Floor
    dest: Floor
    requested: Tick
    boarded: Tick
    alighted: Tick

    @property
    def wait(self) -> int:
        return self.boarded - self.requested

    @property
    def travel(self) -> int:
        return self.alighted - self.boarded

    @property
    def total(self) -> int:
        return self.alighted - self.requested

    @property
    def direct(self) -> int:
        return abs(self.dest - self.source)

    @property
    def excess(self) -> int:
        return self.total - self.direct


@dataclass(frozen=True)
class CarStats:
    car: CarId
    passengers: int  # delivered
    trips: int  # moves from start until reversing or going idle (see module docstring)
    distance: int  # floors travelled
    stops: int  # times the doors opened
    door_open_ticks: int  # ticks that ended with the doors open
    peak_load: int
    capacity: int


@dataclass(frozen=True)
class RunReport:
    config: BuildingConfig
    dispatch: str
    motion: str
    passengers: tuple[PassengerRecord, ...]
    unserved: tuple[PassengerId, ...]
    wait: Stats
    travel: Stats
    total: Stats
    excess: Stats
    per_car: Mapping[CarId, CarStats]
    ticks: int  # rows in the positions log (t = 0 .. ticks - 1)
    makespan: Tick  # tick of the last drop-off
    observations: tuple[str, ...]


def aggregate(journal: Journal, config: BuildingConfig | None = None) -> RunReport:
    run = journal.run_info
    if config is None:
        if run is None:
            raise ValueError("journal has no RunStarted event; pass the config explicitly")
        config = run.config

    requested = {e.passenger: e for e in journal.events(Requested)}
    car_of = {e.passenger: e.car for e in journal.events(Assigned)}
    boarded = {e.passenger: e.tick for e in journal.events(Boarded)}
    alighted = {e.passenger: e.tick for e in journal.events(Alighted)}

    records: list[PassengerRecord] = []
    unserved: list[PassengerId] = []
    for pid, req in requested.items():
        if pid in boarded and pid in alighted:
            records.append(
                PassengerRecord(
                    pid, car_of[pid], req.source, req.dest, req.tick, boarded[pid], alighted[pid]
                )
            )
        else:
            unserved.append(pid)

    per_car = _car_stats(journal, config, records)
    wait = Stats.of([r.wait for r in records])
    travel = Stats.of([r.travel for r in records])
    total = Stats.of([r.total for r in records])
    excess = Stats.of([r.excess for r in records])
    ticks = len({e.tick for e in journal.events(CarState)})
    makespan = max(alighted.values(), default=0)

    return RunReport(
        config=config,
        dispatch=run.dispatch if run else "?",
        motion=run.motion if run else "?",
        passengers=tuple(records),
        unserved=tuple(unserved),
        wait=wait,
        travel=travel,
        total=total,
        excess=excess,
        per_car=per_car,
        ticks=ticks,
        makespan=makespan,
        observations=_observe(records, wait, excess, per_car),
    )


def _car_stats(
    journal: Journal, config: BuildingConfig, records: Sequence[PassengerRecord]
) -> dict[CarId, CarStats]:
    states: dict[CarId, list[CarState]] = defaultdict(list)
    for e in journal.events(CarState):
        states[e.car].append(e)
    stops: dict[CarId, int] = defaultdict(int)
    for e in journal.events(DoorsOpened):
        stops[e.car] += 1
    delivered: dict[CarId, int] = defaultdict(int)
    for r in records:
        delivered[r.car] += 1

    result: dict[CarId, CarStats] = {}
    for car_id, spec in enumerate(config.cars):
        rows = sorted(states[car_id], key=lambda s: s.tick)
        distance = sum(abs(b.floor - a.floor) for a, b in pairwise(rows))
        result[car_id] = CarStats(
            car=car_id,
            passengers=delivered[car_id],
            trips=count_trips(rows),
            distance=distance,
            stops=stops[car_id],
            door_open_ticks=sum(1 for s in rows if s.doors is Doors.OPEN),
            peak_load=max((s.load for s in rows), default=0),
            capacity=spec.capacity,
        )
    return result


def count_trips(rows: Sequence[CarState]) -> int:
    """Trips in one car's tick-ordered states.

    A trip starts on the first move after the car was idle or moving the other way. Ticks spent at
    a floor with the doors open keep the trip going as long as the car stays committed to the same
    direction; a state with direction IDLE ends it.
    """
    trips = 0
    heading = 0  # +1 / -1 while on a trip, 0 between trips
    for prev, cur in pairwise(rows):
        step = cur.floor - prev.floor
        if step:
            direction = 1 if step > 0 else -1
            if direction != heading:  # starting from idle, or reversing
                trips += 1
                heading = direction
        if cur.direction is Direction.IDLE:
            heading = 0
    return trips


def _observe(
    records: Sequence[PassengerRecord],
    wait: Stats,
    excess: Stats,
    per_car: Mapping[CarId, CarStats],
) -> tuple[str, ...]:
    """Short, number-driven notes on the distributions and system behaviour."""
    if not records:
        return ("No passengers were served.",)
    notes: list[str] = []

    zero = sum(1 for r in records if r.wait == 0) / len(records)
    tail = f"{wait.p95 / wait.mean:.1f}x the mean" if wait.mean else "also 0"
    notes.append(
        f"{zero:.0%} of passengers were picked up without waiting. "
        f"Wait p95 is {wait.p95:.1f} ticks ({tail}); the longest wait is {wait.max:.0f} ticks."
    )

    worst = max(records, key=lambda r: (r.wait, r.id))
    notes.append(
        f"Longest wait: {worst.id} ({worst.source}->{worst.dest}, "
        f"requested at t={worst.requested}, car {worst.car}) waited {worst.wait} ticks."
    )

    stretch = sum(r.total / r.direct for r in records) / len(records)
    notes.append(
        f"The system adds {excess.mean:.1f} ticks per passenger on average beyond the direct "
        f"ride time; a journey takes {stretch:.2f}x its direct time on average."
    )

    ups = [r.wait for r in records if r.dest > r.source]
    downs = [r.wait for r in records if r.dest < r.source]
    if ups and downs:
        notes.append(
            f"Mean wait going up is {sum(ups) / len(ups):.1f} ticks ({_people(len(ups))}); "
            f"going down {sum(downs) / len(downs):.1f} ticks ({_people(len(downs))})."
        )

    if len(per_car) > 1:
        busiest = max(per_car.values(), key=lambda c: (c.passengers, -c.car))
        idle = [c.car for c in per_car.values() if c.passengers == 0]
        note = f"Car {busiest.car} carried {busiest.passengers / len(records):.0%} of passengers."
        if idle:
            note += f" Cars {idle} carried nobody."
        notes.append(note)

    full = [c.car for c in per_car.values() if c.peak_load >= c.capacity]
    if full:
        notes.append(
            f"Cars {full} reached capacity at some point; capacity was a binding constraint."
        )
    else:
        peak = max(c.peak_load for c in per_car.values())
        notes.append(f"No car reached capacity (highest load {peak}).")
    return tuple(notes)


def _people(n: int) -> str:
    return f"{n} passenger" if n == 1 else f"{n} passengers"
