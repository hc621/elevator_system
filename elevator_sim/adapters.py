"""Adapters at the edge: CSV in, CSV and text out. The core never touches files."""

from __future__ import annotations

import csv
from collections import defaultdict
from collections.abc import Iterable, Iterator
from pathlib import Path

from elevator_sim.events import CarState
from elevator_sim.feed import InvalidRequest
from elevator_sim.journal import Journal
from elevator_sim.model import Request
from elevator_sim.report import RunReport, Stats

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
    """One row per tick from t = 0: the floor of every car."""
    by_tick: dict[int, dict[int, int]] = defaultdict(dict)
    for e in journal.events(CarState):
        by_tick[e.tick][e.car] = e.floor
    cars = sorted({car for row in by_tick.values() for car in row})
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["tick", *(f"car_{c}" for c in cars)])
        for tick in sorted(by_tick):
            writer.writerow([tick, *(by_tick[tick][c] for c in cars)])


def write_passengers(report: RunReport, path: str | Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(PASSENGER_COLUMNS)
        for r in report.passengers:
            writer.writerow(getattr(r, column) for column in PASSENGER_COLUMNS)


def _row(name: str, s: Stats) -> str:
    cells = f"{s.min:>8.0f}{s.mean:>8.1f}{s.p50:>8.1f}{s.p95:>8.1f}{s.max:>8.0f}{s.std:>8.1f}"
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
        f"  served   : {len(report.passengers)} passengers"
        + (f", UNSERVED {len(report.unserved)}" if report.unserved else ""),
        f"  time     : {report.ticks} ticks logged (t=0..{report.ticks - 1}), "
        f"last drop-off at t={report.makespan}",
        "",
        "  ticks        min    mean     p50     p95     max     std",
        _row("wait", report.wait),
        _row("travel", report.travel),
        _row("total", report.total),
        _row("excess", report.excess),
        "",
        "  car  passengers  distance  stops  peak load",
    ]
    for c in report.per_car.values():
        lines.append(
            f"  {c.car:>3}{c.passengers:>12}{c.distance:>10}{c.stops:>7}"
            f"{c.peak_load:>7}/{c.capacity}"
        )
    lines += ["", "Observations"]
    lines += [f"  - {note}" for note in report.observations]
    return "\n".join(lines) + "\n"
