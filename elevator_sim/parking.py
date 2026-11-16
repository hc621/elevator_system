"""Parking policies: where a car waits once it has no passengers and no assignments.

The dispatcher asks once, when a car goes idle; the car then drives to the floor it was given (a
real move: it appears in the positions log, floors travelled and car trips) and drops the target
the moment it is assigned a passenger. A policy sees read-only car views, the floors other idle
cars already hold, and the requests made so far, never future ones.

- ``stay`` (default): wait where the last trip ended. A parking move is itself a cost to the
  building (energy, wear), so not moving is the baseline every other policy must beat.
- ``lobby``: go back to floor 1. A deliberately simple rule for the morning rush, when the next
  passengers start at the lobby.
- ``spread``: car i waits at its own home floor, spaced evenly up the building, so some car is
  always nearby when traffic is scattered.
- ``demand``: wait at the floor where the most requests started recently (the last ``window``
  ticks), skipping floors another idle car already holds. Two readings are plausible: a recent
  request means that passenger has already left, or colleagues on the same floor will follow
  soon. The simulation results decide.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Sequence
from typing import Protocol

from elevator_sim.car import CarView
from elevator_sim.model import Floor, Request, Tick, start_floors


class ParkingPolicy(Protocol):
    name: str

    def target(
        self,
        car: CarView,
        cars: Sequence[CarView],
        claimed: frozenset[Floor],
        history: Sequence[Request],
        now: Tick,
    ) -> Floor | None:
        """The floor ``car`` should wait at, or None to stay where it is."""
        ...


class StayParking:
    name = "stay"

    def target(self, car, cars, claimed, history, now):  # type: ignore[no-untyped-def]
        return None


class LobbyParking:
    name = "lobby"

    def target(self, car, cars, claimed, history, now):  # type: ignore[no-untyped-def]
        return 1 if car.spec.serves(1) else None


class SpreadParking:
    name = "spread"

    def target(self, car, cars, claimed, history, now):  # type: ignore[no-untyped-def]
        homes = start_floors(car.top_floor, len(cars), "spread")
        home = homes[car.id]
        return home if car.spec.serves(home) else None


class DemandParking:
    name = "demand"

    def __init__(self, window: int = 100) -> None:
        self.window = window

    def target(self, car, cars, claimed, history, now):  # type: ignore[no-untyped-def]
        recent: Counter[Floor] = Counter()
        for request in reversed(history):  # history is in time order; stop at the window
            if request.time <= now - self.window:
                break
            recent[request.source] += 1
        ranked = sorted(recent, key=lambda f: (-recent[f], abs(f - car.floor), f))
        for floor in ranked:
            if floor not in claimed and car.spec.serves(floor):
                return floor
        return None


PARKING_POLICIES: dict[str, Callable[[], ParkingPolicy]] = {
    "stay": StayParking,
    "lobby": LobbyParking,
    "spread": SpreadParking,
    "demand": DemandParking,
}


def make_parking(name: str) -> ParkingPolicy:
    try:
        return PARKING_POLICIES[name]()
    except KeyError:
        raise ValueError(
            f"unknown parking policy {name!r}; expected one of {sorted(PARKING_POLICIES)}"
        ) from None
