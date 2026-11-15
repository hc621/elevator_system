"""Value types shared by every component.

Everything here is immutable: a policy that receives one of these cannot change the simulation
by accident.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from enum import Enum
from typing import Any

Floor = int
CarId = int
PassengerId = str
Tick = int


class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0

    @property
    def opposite(self) -> Direction:
        return Direction(-self.value)

    @staticmethod
    def of(source: Floor, dest: Floor) -> Direction:
        if dest > source:
            return Direction.UP
        if dest < source:
            return Direction.DOWN
        return Direction.IDLE


class Doors(Enum):
    CLOSED = "closed"
    OPEN = "open"


@dataclass(frozen=True)
class Request:
    """One input row: at ``time``, passenger ``id`` asks to go from ``source`` to ``dest``."""

    time: Tick
    id: PassengerId
    source: Floor
    dest: Floor

    @property
    def direction(self) -> Direction:
        return Direction.of(self.source, self.dest)

    @property
    def direct(self) -> int:
        """Ride time with no waiting and no intermediate stops: the lower bound on total time."""
        return abs(self.dest - self.source)


@dataclass(frozen=True)
class CarSpec:
    capacity: int
    start_floor: Floor = 1
    served_floors: frozenset[Floor] | None = None  # None = every floor

    def serves(self, floor: Floor) -> bool:
        return self.served_floors is None or floor in self.served_floors

    def can_serve(self, request: Request) -> bool:
        return self.serves(request.source) and self.serves(request.dest)


PLACEMENTS = ("lobby", "spread")


def start_floors(floors: int, n_cars: int, placement: str | Sequence[Floor]) -> tuple[Floor, ...]:
    """Starting floor of each car.

    ``lobby``: every car at floor 1. ``spread``: evenly spaced, e.g. 4 cars over 40 floors start at
    1, 11, 21, 31. A sequence gives one floor per car explicitly.
    """
    if isinstance(placement, str):
        if placement == "lobby":
            return (1,) * n_cars
        if placement == "spread":
            return tuple(1 + i * floors // n_cars for i in range(n_cars))
        raise ValueError(f"unknown placement {placement!r}; expected one of {PLACEMENTS}")
    starts = tuple(placement)
    if len(starts) != n_cars:
        raise ValueError(f"placement lists {len(starts)} floors for {n_cars} cars")
    return starts


@dataclass(frozen=True)
class BuildingConfig:
    """Every knob of a run in one place."""

    floors: int
    cars: tuple[CarSpec, ...]
    door_time: int = 1  # extra ticks a car stays at a stop with its doors open

    def __post_init__(self) -> None:
        if self.floors < 2:
            raise ValueError("a building needs at least 2 floors")
        if not self.cars:
            raise ValueError("a building needs at least 1 car")
        if self.door_time < 0:
            raise ValueError("door_time cannot be negative")
        for i, car in enumerate(self.cars):
            if car.capacity < 1:
                raise ValueError(f"car {i}: capacity must be at least 1")
            if not 1 <= car.start_floor <= self.floors:
                raise ValueError(
                    f"car {i}: start floor {car.start_floor} is outside 1..{self.floors}"
                )
            if car.served_floors is not None and not all(
                1 <= f <= self.floors for f in car.served_floors
            ):
                raise ValueError(f"car {i}: served_floors must lie within 1..{self.floors}")

    @classmethod
    def uniform(
        cls,
        floors: int,
        n_cars: int,
        capacity: int,
        placement: str | Sequence[Floor] = "lobby",
        door_time: int = 1,
    ) -> BuildingConfig:
        if n_cars < 1:
            raise ValueError("a building needs at least 1 car")
        starts = start_floors(floors, n_cars, placement)
        return cls(floors, tuple(CarSpec(capacity, start) for start in starts), door_time)

    def to_dict(self) -> dict[str, Any]:
        return {
            "floors": self.floors,
            "door_time": self.door_time,
            "cars": [
                {
                    "capacity": c.capacity,
                    "start_floor": c.start_floor,
                    "served_floors": None if c.served_floors is None else sorted(c.served_floors),
                }
                for c in self.cars
            ],
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> BuildingConfig:
        cars = tuple(
            CarSpec(
                capacity=c["capacity"],
                start_floor=c["start_floor"],
                served_floors=None if c["served_floors"] is None else frozenset(c["served_floors"]),
            )
            for c in data["cars"]
        )
        return cls(floors=data["floors"], cars=cars, door_time=data["door_time"])


@dataclass(frozen=True)
class PlannedStop:
    """One stop on a car's projected route."""

    floor: Floor
    eta: Tick
    alight: tuple[PassengerId, ...]
    board: tuple[PassengerId, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "floor": self.floor,
            "eta": self.eta,
            "alight": list(self.alight),
            "board": list(self.board),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> PlannedStop:
        return cls(data["floor"], data["eta"], tuple(data["alight"]), tuple(data["board"]))
