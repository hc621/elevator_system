"""Events: the facts a run produces.

Events record what happened, never derived numbers: wait time is ``Boarded.tick - Requested.tick``,
computed later by the aggregator, so measuring something new never needs a re-run.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, fields
from enum import Enum
from typing import Any, Protocol

from elevator_sim.model import (
    BuildingConfig,
    CarId,
    Direction,
    Doors,
    Floor,
    PassengerId,
    PlannedStop,
    Tick,
)


@dataclass(frozen=True)
class RunStarted:
    """First event of every journal: what was run, so a saved journal can be re-analysed alone."""

    tick: Tick
    config: BuildingConfig
    dispatch: str
    motion: str


@dataclass(frozen=True)
class Requested:
    tick: Tick
    passenger: PassengerId
    source: Floor
    dest: Floor


@dataclass(frozen=True)
class Assigned:
    tick: Tick
    passenger: PassengerId
    car: CarId
    policy: str
    cost: float | None  # the dispatch policy's cost for the chosen car, if it computes one


@dataclass(frozen=True)
class DoorsOpened:
    tick: Tick
    car: CarId
    floor: Floor


@dataclass(frozen=True)
class DoorsClosed:
    tick: Tick
    car: CarId
    floor: Floor


@dataclass(frozen=True)
class Boarded:
    tick: Tick
    passenger: PassengerId
    car: CarId
    floor: Floor


@dataclass(frozen=True)
class Alighted:
    tick: Tick
    passenger: PassengerId
    car: CarId
    floor: Floor


@dataclass(frozen=True)
class RouteChanged:
    """A new assignment changed a car's projected route."""

    tick: Tick
    car: CarId
    old: tuple[PlannedStop, ...]
    new: tuple[PlannedStop, ...]


@dataclass(frozen=True)
class CarState:
    """One car at the end of a tick's decisions, before it moves: one per car per tick."""

    tick: Tick
    car: CarId
    floor: Floor
    direction: Direction
    doors: Doors
    load: int
    route: tuple[PlannedStop, ...] | None = None  # only with --journal-routes


Event = (
    RunStarted
    | Requested
    | Assigned
    | DoorsOpened
    | DoorsClosed
    | Boarded
    | Alighted
    | RouteChanged
    | CarState
)

EVENT_TYPES: dict[str, type] = {
    cls.__name__: cls
    for cls in (
        RunStarted,
        Requested,
        Assigned,
        DoorsOpened,
        DoorsClosed,
        Boarded,
        Alighted,
        RouteChanged,
        CarState,
    )
}


class EventSink(Protocol):
    def emit(self, event: Event) -> None: ...


class NullSink:
    """Discards events; for runs where only the final state matters."""

    def emit(self, event: Event) -> None:
        pass


# --- JSON codec ----------------------------------------------------------------------------------


def _encode(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.name
    if isinstance(value, (PlannedStop, BuildingConfig)):
        return value.to_dict()
    if isinstance(value, tuple):
        return [_encode(v) for v in value]
    return value


def event_to_dict(event: Event) -> dict[str, Any]:
    data: dict[str, Any] = {"kind": type(event).__name__}
    for f in fields(event):
        data[f.name] = _encode(getattr(event, f.name))
    return data


def _stops(raw: Any) -> tuple[PlannedStop, ...] | None:
    return None if raw is None else tuple(PlannedStop.from_dict(s) for s in raw)


_DECODERS: dict[str, Any] = {
    "config": BuildingConfig.from_dict,
    "direction": lambda raw: Direction[raw],
    "doors": lambda raw: Doors[raw],
    "old": _stops,
    "new": _stops,
    "route": _stops,
}


def event_from_dict(data: Mapping[str, Any]) -> Event:
    payload = dict(data)
    kind = payload.pop("kind")
    try:
        cls = EVENT_TYPES[kind]
    except KeyError:
        raise ValueError(f"unknown event kind {kind!r}") from None
    for name, decode in _DECODERS.items():
        if name in payload:
            payload[name] = decode(payload[name])
    return cls(**payload)
