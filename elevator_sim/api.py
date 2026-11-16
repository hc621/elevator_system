"""The brief's entry point: a function that takes a list of requests and runs the simulation.

    from elevator_sim import run_requests

    result = run_requests(
        [(0, "passenger1", 1, 51), (0, "passenger2", 1, 37), (10, "passenger3", 20, 1)],
        elevators=3, floors=60, capacity=8,
    )
    result.positions[0]          # every car's floor at t = 0: [1, 1, 1]
    result.report.wait.max       # max / min / mean wait and total time, observations, ...

The requests are fed to the simulation one tick at a time (it never looks ahead) and checked like
the CLI's input: in time order, floors in range, source != dest, unique ids.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass

from elevator_sim.dispatch import make_dispatch
from elevator_sim.events import CarState
from elevator_sim.feed import IteratorFeed
from elevator_sim.journal import Journal
from elevator_sim.model import BuildingConfig, Floor, Request
from elevator_sim.motion import make_motion
from elevator_sim.parking import make_parking
from elevator_sim.report import RunReport, aggregate
from elevator_sim.simulator import simulate

RequestLike = Request | Sequence[object]  # a Request, or a (time, id, source, dest) row


@dataclass(frozen=True)
class RunResult:
    report: RunReport  # passenger statistics, per car, by trip type, diagnostics, observations
    positions: list[list[Floor]]  # positions[t][i] = car i's floor at tick t, from t = 0
    journal: Journal  # every event; save with journal.to_jsonl(path)


def _as_request(row: RequestLike) -> Request:
    if isinstance(row, Request):
        return row
    time, rid, source, dest = row
    return Request(int(time), str(rid), int(source), int(dest))  # type: ignore[call-overload]


def run_requests(
    requests: Iterable[RequestLike],
    *,
    elevators: int = 3,
    floors: int = 60,
    capacity: int = 8,
    door_time: int = 1,
    algorithm: str = "cost",
    motion: str = "look",
    parking: str = "stay",
    placement: str = "lobby",
) -> RunResult:
    """Simulate ``requests`` (``Request`` objects or ``(time, id, source, dest)`` rows)."""
    config = BuildingConfig.uniform(floors, elevators, capacity, placement, door_time)
    journal = simulate(
        config,
        IteratorFeed(_as_request(r) for r in requests),
        make_dispatch(algorithm),
        make_motion(motion),
        parking=make_parking(parking),
    )
    by_tick: dict[int, dict[int, Floor]] = {}
    for e in journal.events(CarState):
        by_tick.setdefault(e.tick, {})[e.car] = e.floor
    positions = [[by_tick[t][c] for c in sorted(by_tick[t])] for t in sorted(by_tick)]
    return RunResult(aggregate(journal), positions, journal)
