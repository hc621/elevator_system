"""Adapters at the edge: requests come in as CSV (the brief's format); results go out as JSON.

The core never touches files.

Outputs of a run:
- ``positions.jsonl``: one JSON object per tick from t = 0, ``{"t": 0, "floors": [1, 1, 1]}``,
  where ``floors[i]`` is car i's floor (the brief's "one row per timestamp").
- ``passengers.json``: one object per delivered passenger with its timestamps and times.
- ``report.json``: the run's metrics (see ``report_to_dict``).
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from collections.abc import Iterable, Iterator
from pathlib import Path

from elevator_sim.events import CarState
from elevator_sim.feed import InvalidRequest
from elevator_sim.journal import Journal
from elevator_sim.model import Request
from elevator_sim.report import CarStats, RunReport, Stats

HEADER = ("time", "id", "source", "dest")
PASSENGER_COLUMNS = (
    "id", "car", "source", "dest", "requested", "boarded", "alighted",
    "wait", "travel", "total", "direct", "excess",
)  # fmt: skip


def read_requests(path: str | Path) -> Iterator[Request]:
    """Yield requests from a ``time,id,source,dest`` CSV, one row at a time (header optional)."""
    with open(path, newline="", encoding="utf-8") as f:
        for lineno, row in enumerate(csv.reader(f), start=1):
            cells = [c.strip() for c in row]
            if not any(cells):
                continue
            if lineno == 1 and cells[0].lower() == "time":
                continue
            if len(cells) != 4:
                raise InvalidRequest(f"{path}:{lineno}: expected 4 fields time,id,source,dest")
            try:
                yield Request(int(cells[0]), cells[1], int(cells[2]), int(cells[3]))
            except ValueError:
                raise InvalidRequest(
                    f"{path}:{lineno}: time, source and dest must be integers"
                ) from None


def write_requests(requests: Iterable[Request], path: str | Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        for r in requests:
            writer.writerow((r.time, r.id, r.source, r.dest))


def write_positions(journal: Journal, path: str | Path) -> None:
    """JSON Lines, one object per tick from t = 0: ``{"t": tick, "floors": [car 0, car 1]}``."""
    by_tick: dict[int, dict[int, int]] = defaultdict(dict)
    for e in journal.events(CarState):
        by_tick[e.tick][e.car] = e.floor
    cars = sorted({car for row in by_tick.values() for car in row})
    with open(path, "w", encoding="utf-8") as f:
        for tick in sorted(by_tick):
            row = {"t": tick, "floors": [by_tick[tick][c] for c in cars]}
            f.write(json.dumps(row, separators=(",", ":")) + "\n")


def read_positions(path: str | Path) -> list[list[int]]:
    """The floors per tick from a ``positions.jsonl`` file (index = tick)."""
    with open(path, encoding="utf-8") as f:
        return [json.loads(line)["floors"] for line in f if line.strip()]


def write_passengers(report: RunReport, path: str | Path) -> None:
    rows = [{column: getattr(r, column) for column in PASSENGER_COLUMNS} for r in report.passengers]
    _write_json(rows, path)


def _stats_dict(s: Stats) -> dict[str, float]:
    return {
        "min": s.min,
        "mean": round(s.mean, 3),
        "p50": s.p50,
        "p90": round(s.p90, 3),
        "p95": round(s.p95, 3),
        "max": s.max,
        "std": round(s.std, 3),
    }


def _car_dict(c: CarStats) -> dict[str, int]:
    return {
        "car": c.car,
        "trips": c.trips,
        "passengers": c.passengers,
        "distance": c.distance,
        "stops": c.stops,
        "peak_load": c.peak_load,
        "capacity": c.capacity,
    }


def report_to_dict(report: RunReport) -> dict[str, object]:
    """The run's metrics as plain JSON-ready data. All times are in ticks.

    - ``wait`` / ``travel`` / ``total``: per-passenger distributions (mean, max, p90, p95, ...)
    - ``travels``: passenger journeys completed (one passenger from source to destination)
    - ``cars[i].trips``: moves of car i from starting to move until it reverses or goes idle
    """
    cfg = report.config
    return {
        "building": {
            "floors": cfg.floors,
            "cars": len(cfg.cars),
            "capacities": [c.capacity for c in cfg.cars],
            "door_time": cfg.door_time,
        },
        "policies": {"dispatch": report.dispatch, "motion": report.motion},
        "ticks": report.ticks,
        "last_dropoff": report.makespan,
        "travels": {"completed": len(report.passengers), "unserved": len(report.unserved)},
        "wait": _stats_dict(report.wait),
        "travel": _stats_dict(report.travel),
        "total": _stats_dict(report.total),
        "excess": _stats_dict(report.excess),
        "car_trips": sum(c.trips for c in report.per_car.values()),
        "cars": [_car_dict(c) for c in report.per_car.values()],
        "observations": list(report.observations),
    }


def write_report(report: RunReport, path: str | Path) -> None:
    _write_json(report_to_dict(report), path)


def _write_json(data: object, path: str | Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def _row(name: str, s: Stats) -> str:
    cells = (
        f"{s.min:>8.0f}{s.mean:>8.1f}{s.p50:>8.1f}{s.p90:>8.1f}{s.p95:>8.1f}{s.max:>8.0f}"
        f"{s.std:>8.1f}"
    )
    return f"  {name:<8}{cells}"


def format_summary(report: RunReport) -> str:
    cfg = report.config
    capacities = sorted({c.capacity for c in cfg.cars})
    capacity = str(capacities[0]) if len(capacities) == 1 else "/".join(map(str, capacities))
    lines = [
        "Elevator simulation summary",
        f"  building : {cfg.floors} floors, {len(cfg.cars)} cars, capacity {capacity}, "
        f"door_time {cfg.door_time}",
        f"  policies : dispatch={report.dispatch}, motion={report.motion}",
        f"  travels  : {len(report.passengers)} passengers delivered"
        + (f", UNSERVED {len(report.unserved)}" if report.unserved else ""),
        f"  time     : {report.ticks} ticks logged (t=0..{report.ticks - 1}), "
        f"last drop-off at t={report.makespan}",
        "",
        "  ticks        min    mean     p50     p90     p95     max     std",
        _row("wait", report.wait),
        _row("travel", report.travel),
        _row("total", report.total),
        _row("excess", report.excess),
        "",
        "  car  trips  passengers  distance  stops  peak load",
    ]
    for c in report.per_car.values():
        lines.append(
            f"  {c.car:>3}{c.trips:>7}{c.passengers:>12}{c.distance:>10}{c.stops:>7}"
            f"{c.peak_load:>7}/{c.capacity}"
        )
    lines.append(f"  all{sum(c.trips for c in report.per_car.values()):>7}")
    lines += ["", "Observations"]
    lines += [f"  - {note}" for note in report.observations]
    return "\n".join(lines) + "\n"
