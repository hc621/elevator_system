"""Shared test helpers: building runs and checking the invariants every run must satisfy."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence

from elevator_sim.dispatch import make_dispatch
from elevator_sim.events import Alighted, Assigned, Boarded, CarState, Requested
from elevator_sim.feed import IteratorFeed
from elevator_sim.journal import Journal
from elevator_sim.model import BuildingConfig, Doors, Request
from elevator_sim.motion import make_motion
from elevator_sim.report import PassengerRecord, RunReport, aggregate
from elevator_sim.simulator import simulate


def reqs(*rows: tuple[int, str, int, int]) -> list[Request]:
    return [Request(*row) for row in rows]


def building(
    floors: int = 60,
    cars: int = 1,
    capacity: int = 8,
    door_time: int = 0,
    placement: str | Sequence[int] = "lobby",
) -> BuildingConfig:
    return BuildingConfig.uniform(floors, cars, capacity, placement, door_time)


def run(
    requests: Sequence[Request],
    config: BuildingConfig | None = None,
    dispatch: str = "cost",
    motion: str = "look",
    **kwargs: object,
) -> tuple[Journal, RunReport]:
    config = config or building()
    journal = simulate(
        config, IteratorFeed(requests), make_dispatch(dispatch), make_motion(motion), **kwargs
    )
    return journal, aggregate(journal)


def records(report: RunReport) -> dict[str, PassengerRecord]:
    return {r.id: r for r in report.passengers}


def floors_by_car(journal: Journal) -> dict[int, list[int]]:
    """Each car's floor at t = 0, 1, 2, ..."""
    rows: dict[int, list[int]] = defaultdict(list)
    for e in sorted(journal.events(CarState), key=lambda s: (s.car, s.tick)):
        rows[e.car].append(e.floor)
    return dict(rows)


def check_invariants(journal: Journal, requests: Sequence[Request]) -> None:
    """Assert everything that must hold for any run, whatever the policies."""
    run_info = journal.run_info
    assert run_info is not None
    config = run_info.config
    n_cars = len(config.cars)

    # Positions: one CarState per car per tick, ticks contiguous from 0.
    states: dict[int, dict[int, CarState]] = defaultdict(dict)
    for s in journal.events(CarState):
        assert s.car not in states[s.tick], f"two CarStates for car {s.car} at t={s.tick}"
        states[s.tick][s.car] = s
    ticks = sorted(states)
    assert ticks == list(range(len(ticks))), "positions log must start at 0 with no gaps"
    for t in ticks:
        assert len(states[t]) == n_cars
        for car, s in states[t].items():
            assert 1 <= s.floor <= config.floors
            assert 0 <= s.load <= config.cars[car].capacity, f"car {car} over capacity at t={t}"
            if t > 0:
                prev = states[t - 1][car]
                assert abs(s.floor - prev.floor) <= 1, f"car {car} jumped floors at t={t}"
                if prev.doors is Doors.OPEN:
                    assert s.floor == prev.floor, f"car {car} moved with doors open at t={t}"

    # Passengers: requested on time, assigned once, picked up and dropped off correctly.
    requested = {e.passenger: e for e in journal.events(Requested)}
    assigned: dict[str, Assigned] = {}
    for a in journal.events(Assigned):
        assert a.passenger not in assigned, f"{a.passenger} assigned twice"
        assigned[a.passenger] = a
    boarded = {e.passenger: e for e in journal.events(Boarded)}
    alighted = {e.passenger: e for e in journal.events(Alighted)}
    assert len(journal.events(Boarded)) == len(boarded), "someone boarded twice"
    assert len(journal.events(Alighted)) == len(alighted), "someone alighted twice"

    for r in requests:
        assert requested[r.id].tick == r.time, f"{r.id} seen at the wrong tick (no peeking)"
        assert assigned[r.id].tick == r.time, f"{r.id} not assigned on its request tick"
        b, a = boarded[r.id], alighted[r.id]  # KeyError = not delivered
        car = assigned[r.id].car
        assert b.car == a.car == car, f"{r.id} rode a car it was not assigned to"
        assert r.time <= b.tick < a.tick
        assert b.floor == r.source and a.floor == r.dest
        assert states[b.tick][car].floor == r.source
        assert states[a.tick][car].floor == r.dest
        assert config.cars[car].can_serve(r)
    assert set(requested) == {r.id for r in requests}
