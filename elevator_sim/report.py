"""Aggregation: a pure function from a journal to a report. It never reads car state.

Timestamps per passenger::

    requested --wait--> boarded --travel--> alighted
    |<-------------------- total -------------->|
    direct = |dest - source|, excess = total - direct

detour = travel - direct (time spent on stops for other passengers on the way)

Diagnostics explain *why* a policy is fast or slow: the chosen car's state when each passenger was
assigned (idle / on the way / ahead but heading the other way / moving away), how far it was
compared with the nearest car, how busy the cars were, how many floors they travelled per
passenger, how many riders each stop served, and how often a full car passed someone.

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

    @property
    def detour(self) -> int:
        return self.travel - self.direct

    @property
    def direction(self) -> Direction:
        return Direction.UP if self.dest > self.source else Direction.DOWN


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


# Trip types, the categories of the business-building traffic model (scenarios.py).
TRIP_KINDS = ("inbound", "outbound", "inter_floor")


def trip_kind(source: Floor, dest: Floor) -> str:
    """inbound = from the lobby (floor 1), outbound = to the lobby, else inter_floor."""
    if source == 1:
        return "inbound"
    if dest == 1:
        return "outbound"
    return "inter_floor"


@dataclass(frozen=True)
class TripStats:
    """The passengers of one trip type."""

    count: int
    wait: Stats
    total: Stats


# State of the chosen car when a passenger was assigned, relative to the passenger's floor.
ASSIGNMENT_STATES = ("idle", "on_the_way", "ahead_opposite", "moving_away")


@dataclass(frozen=True)
class AssignmentState:
    count: int
    share: float  # of served passengers
    mean_wait: float


@dataclass(frozen=True)
class Diagnostics:
    """Root-cause metrics: where the time goes and why."""

    detour: Stats  # travel - direct, per passenger
    assignment: Mapping[str, AssignmentState]  # keyed by ASSIGNMENT_STATES
    chosen_distance: float  # mean floors from the chosen car to the pickup, at assignment
    nearest_distance: float  # mean floors from the closest car to the pickup, at assignment
    busy_share: float  # car-ticks not idle with doors closed
    distance_per_passenger: float  # floors travelled by all cars / passengers served
    riders_per_stop: float  # (boardings + alightings) per door opening
    full_passby_share: float  # passengers whose own car stood at their floor, their way, full


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
    diagnostics: Diagnostics
    by_trip: Mapping[str, TripStats]  # keyed by TRIP_KINDS
    observations: tuple[str, ...]
    parking: str = "stay"


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
    diagnostics = diagnose(journal, config, records, per_car)

    return RunReport(
        config=config,
        dispatch=run.dispatch if run else "?",
        motion=run.motion if run else "?",
        parking=run.parking if run else "?",
        passengers=tuple(records),
        unserved=tuple(unserved),
        wait=wait,
        travel=travel,
        total=total,
        excess=excess,
        per_car=per_car,
        ticks=ticks,
        makespan=makespan,
        diagnostics=diagnostics,
        by_trip=trip_breakdown(records),
        observations=_observe(records, wait, excess, per_car, diagnostics),
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


def trip_breakdown(records: Sequence[PassengerRecord]) -> dict[str, TripStats]:
    groups: dict[str, list[PassengerRecord]] = {kind: [] for kind in TRIP_KINDS}
    for r in records:
        groups[trip_kind(r.source, r.dest)].append(r)
    return {
        kind: TripStats(
            count=len(rs),
            wait=Stats.of([r.wait for r in rs]),
            total=Stats.of([r.total for r in rs]),
        )
        for kind, rs in groups.items()
    }


def classify_assignment(
    car_floor: Floor, car_direction: Direction, source: Floor, wants: Direction
) -> str:
    """Where the chosen car was, relative to the pickup, when the passenger was assigned.

    ``car_direction`` is the car's direction just before the assignment (IDLE if it had no work).
    """
    if car_direction is Direction.IDLE:
        return "idle"
    if (source - car_floor) * car_direction.value >= 0:  # the pickup is here or ahead
        return "on_the_way" if wants is car_direction else "ahead_opposite"
    return "moving_away"


def diagnose(
    journal: Journal,
    config: BuildingConfig,
    records: Sequence[PassengerRecord],
    per_car: Mapping[CarId, CarStats],
) -> Diagnostics:
    states: dict[CarId, dict[Tick, CarState]] = defaultdict(dict)
    for e in journal.events(CarState):
        states[e.car][e.tick] = e
    by_state: dict[str, list[int]] = {name: [] for name in ASSIGNMENT_STATES}
    chosen: list[int] = []
    nearest: list[int] = []
    full_passbys = 0
    for r in records:
        t = r.requested
        before = states[r.car].get(t - 1)
        floor = states[r.car][t].floor  # where the car is during the assignment tick
        direction = before.direction if before else Direction.IDLE
        by_state[classify_assignment(floor, direction, r.source, r.direction)].append(r.wait)
        chosen.append(abs(floor - r.source))
        nearest.append(min(abs(rows[t].floor - r.source) for rows in states.values()))
        capacity = config.cars[r.car].capacity
        for tick in range(t, r.boarded):
            s = states[r.car].get(tick)
            if s and s.floor == r.source and s.direction is r.direction and s.load >= capacity:
                full_passbys += 1
                break

    n = len(records)
    car_ticks = sum(len(rows) for rows in states.values())
    idle = sum(
        1
        for rows in states.values()
        for s in rows.values()
        if s.direction is Direction.IDLE and s.doors is Doors.CLOSED
    )
    stops = sum(c.stops for c in per_car.values())
    return Diagnostics(
        detour=Stats.of([r.detour for r in records]),
        assignment={
            name: AssignmentState(
                count=len(waits),
                share=len(waits) / n if n else 0.0,
                mean_wait=sum(waits) / len(waits) if waits else 0.0,
            )
            for name, waits in by_state.items()
        },
        chosen_distance=sum(chosen) / n if n else 0.0,
        nearest_distance=sum(nearest) / n if n else 0.0,
        busy_share=1 - idle / car_ticks if car_ticks else 0.0,
        distance_per_passenger=sum(c.distance for c in per_car.values()) / n if n else 0.0,
        riders_per_stop=2 * n / stops if stops else 0.0,
        full_passby_share=full_passbys / n if n else 0.0,
    )


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
    diagnostics: Diagnostics,
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

    d = diagnostics
    away = d.assignment["moving_away"]
    if away.count:
        notes.append(
            f"{away.share:.0%} of passengers were assigned to a car moving away from them; "
            f"they waited {away.mean_wait:.1f} ticks on average. The chosen car was "
            f"{d.chosen_distance:.1f} floors away on average; the nearest car "
            f"{d.nearest_distance:.1f}."
        )
    notes.append(
        f"Cars were busy {d.busy_share:.0%} of the time and travelled "
        f"{d.distance_per_passenger:.1f} floors per passenger; ride time beyond the direct trip "
        f"(detour) averaged {d.detour.mean:.1f} ticks against {wait.mean:.1f} of waiting."
    )

    full = [c.car for c in per_car.values() if c.peak_load >= c.capacity]
    if full and d.full_passby_share:
        notes.append(
            f"Cars {full} reached capacity; {d.full_passby_share:.0%} of passengers saw their own "
            "car pass their floor full, so capacity was a binding constraint."
        )
    elif full:
        notes.append(f"Cars {full} reached capacity, but no passenger was passed by a full car.")
    else:
        peak = max(c.peak_load for c in per_car.values())
        notes.append(f"No car reached capacity (highest load {peak}).")
    return tuple(notes)


def _people(n: int) -> str:
    return f"{n} passenger" if n == 1 else f"{n} passengers"
