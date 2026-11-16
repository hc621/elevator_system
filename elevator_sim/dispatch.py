"""Dispatch policies: which car a new request goes to.

A policy sees read-only car views and returns a car id; only the dispatcher acts on the answer.
The dispatcher has already removed cars that cannot serve both floors. Ties go to the lowest car id.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import Protocol

from elevator_sim.car import CarView, Projection
from elevator_sim.model import CarId, Request, Tick


class DispatchPolicy(Protocol):
    name: str
    last_cost: float | None  # cost of the last choice, for the journal; None if not cost-based

    def choose(self, request: Request, cars: Sequence[CarView], now: Tick) -> CarId: ...


class RoundRobinDispatch:
    """Cycle through the cars in id order, ignoring state. The naive baseline."""

    name = "round_robin"

    def __init__(self) -> None:
        self._next: CarId = 0
        self.last_cost: float | None = None

    def choose(self, request: Request, cars: Sequence[CarView], now: Tick) -> CarId:
        ids = sorted(c.id for c in cars)
        chosen = next((i for i in ids if i >= self._next), ids[0])
        self._next = chosen + 1
        return chosen


class NearestDispatch:
    """The car currently closest to the passenger's floor, whatever it is doing."""

    name = "nearest"

    def __init__(self) -> None:
        self.last_cost: float | None = None

    def choose(self, request: Request, cars: Sequence[CarView], now: Tick) -> CarId:
        best = min(cars, key=lambda c: (abs(c.floor - request.source), c.id))
        self.last_cost = float(abs(best.floor - request.source))
        return best.id


class ZoneDispatch:
    """Each car owns a contiguous band of floors 2..n; a trip goes to the owner of its upper floor.

    Keying on the upper floor (not the source) spreads lobby traffic across cars: a trip 1 -> 37 and
    a trip 37 -> 1 both belong to the zone holding floor 37.
    """

    name = "zone"

    def __init__(self) -> None:
        self.last_cost: float | None = None

    def choose(self, request: Request, cars: Sequence[CarView], now: Tick) -> CarId:
        ordered = sorted(cars, key=lambda c: c.id)
        upper = max(request.source, request.dest)  # always >= 2
        span = ordered[0].top_floor - 1  # floors 2..n
        index = min((upper - 2) * len(ordered) // span, len(ordered) - 1)
        return ordered[index].id


class CostDispatch:
    """Destination dispatch by marginal cost, with an optional fairness penalty.

    For each car, project its future with and without the new passenger and take the increase in
    total time summed over everyone on that car: the newcomer's own wait and ride plus any delay
    imposed on passengers already assigned. The projection runs the car's real rules, including the
    capacity check at boarding, so a car that would be full along the way shows up as a late pickup
    and costs more.

    ``fairness`` (alpha >= 0) adds ``alpha * increase in sum(wait ** 2)`` over the car's passengers
    still waiting (projected waits). Squaring makes one passenger waiting 40 ticks cost as much as
    sixteen waiting 10, and makes delaying someone who already waits long expensive, so the policy
    stops trading one long wait for a few short ones. alpha = 0 is the plain cost policy.
    """

    def __init__(self, fairness: float = 0.0) -> None:
        if fairness < 0:
            raise ValueError("fairness must be >= 0")
        self.fairness = fairness
        self.name = f"cost:{fairness:g}" if fairness else "cost"
        self.last_cost: float | None = None

    @staticmethod
    def wait_penalty(projection: Projection) -> int:
        """Sum of squared projected waits of the car's passengers not yet aboard."""
        return sum(w * w for w in projection.waits.values())

    def choose(self, request: Request, cars: Sequence[CarView], now: Tick) -> CarId:
        best: tuple[float, CarId] | None = None
        for car in sorted(cars, key=lambda c: c.id):
            with_new, without = car.project(request), car.project()
            cost: float = with_new.total_time - without.total_time
            if self.fairness:
                increase = self.wait_penalty(with_new) - self.wait_penalty(without)
                cost += self.fairness * increase
            if best is None or cost < best[0]:
                best = (cost, car.id)
        assert best is not None, "dispatcher always passes at least one car"
        self.last_cost = float(best[0])
        return best[1]


DISPATCH_POLICIES: dict[str, Callable[[], DispatchPolicy]] = {
    "cost": CostDispatch,
    "nearest": NearestDispatch,
    "round_robin": RoundRobinDispatch,
    "zone": ZoneDispatch,
}


def make_dispatch(name: str) -> DispatchPolicy:
    """A fresh policy instance (some policies keep state, so never share one across runs).

    ``cost:<alpha>`` is the cost policy with fairness weight alpha, e.g. ``cost:0.5``.
    """
    base, _, arg = name.partition(":")
    if base == "cost" and arg:
        try:
            return CostDispatch(fairness=float(arg))
        except ValueError:
            raise ValueError(f"bad fairness weight in {name!r}; expected e.g. cost:0.5") from None
    try:
        return DISPATCH_POLICIES[name]()
    except KeyError:
        raise ValueError(
            f"unknown dispatch policy {name!r}; expected one of {sorted(DISPATCH_POLICIES)} "
            "or cost:<fairness>"
        ) from None


def is_dispatch_policy(name: str) -> bool:
    try:
        make_dispatch(name)
    except ValueError:
        return False
    return True
