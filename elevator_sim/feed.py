"""Request feed and clock.

The feed's single access method, ``release(now)``, is the only way the simulation sees requests, so
reading the future is impossible by construction rather than merely tested for.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Protocol

from elevator_sim.model import PassengerId, Request, Tick


class InvalidRequest(ValueError):
    """An input request breaks the input contract."""


class SimulationStalled(RuntimeError):
    """The run exceeded its tick limit or stopped making progress."""


class RequestFeed(Protocol):
    def release(self, now: Tick) -> Sequence[Request]: ...  # only requests with time <= now
    def exhausted(self) -> bool: ...


class IteratorFeed:
    """Feed over any iterable of requests in time order, read lazily.

    It holds at most one unreleased request: the next one it has read. A request is handed out only
    once its time has come, so a file is consumed as the clock reaches each row.
    """

    def __init__(self, requests: Iterable[Request]) -> None:
        self._source = iter(requests)
        self._next: Request | None = None
        self._done = False
        self._pull()

    def _pull(self) -> None:
        try:
            self._next = next(self._source)
        except StopIteration:
            self._next = None
            self._done = True

    def release(self, now: Tick) -> list[Request]:
        released: list[Request] = []
        while self._next is not None and self._next.time <= now:
            released.append(self._next)
            self._pull()
        return released

    def exhausted(self) -> bool:
        return self._done


class ValidatingFeed:
    """Wraps a feed and checks every request as it is released (still no look-ahead).

    Rejects floors outside ``1..floors``, ``source == dest``, duplicate ids, negative times and
    times that go backwards.
    """

    def __init__(self, inner: RequestFeed, floors: int) -> None:
        self._inner = inner
        self._floors = floors
        self._seen: set[PassengerId] = set()
        self._last_time: Tick = 0

    def release(self, now: Tick) -> list[Request]:
        released = list(self._inner.release(now))
        for request in released:
            self._check(request, now)
        return released

    def exhausted(self) -> bool:
        return self._inner.exhausted()

    def _check(self, r: Request, now: Tick) -> None:
        where = f"request {r.id!r} (time={r.time})"
        if r.time < 0:
            raise InvalidRequest(f"{where}: time cannot be negative")
        if r.time < self._last_time or r.time < now:
            raise InvalidRequest(f"{where}: request times must be non-decreasing")
        for name, floor in (("source", r.source), ("dest", r.dest)):
            if not 1 <= floor <= self._floors:
                raise InvalidRequest(f"{where}: {name} floor {floor} is outside 1..{self._floors}")
        if r.source == r.dest:
            raise InvalidRequest(f"{where}: source and dest are the same floor ({r.source})")
        if r.id in self._seen:
            raise InvalidRequest(f"{where}: duplicate passenger id")
        self._seen.add(r.id)
        self._last_time = r.time


class Clock:
    """Owns ``now``; advances exactly one tick at a time; decides when the run is over."""

    def __init__(self, max_ticks: int | None = None) -> None:
        self.now: Tick = 0
        self.max_ticks = max_ticks

    def advance(self) -> Tick:
        self.now += 1
        return self.now

    def check_limit(self) -> None:
        if self.max_ticks is not None and self.now > self.max_ticks:
            raise SimulationStalled(f"tick limit reached ({self.max_ticks}) with work outstanding")

    def finished(self, feed: RequestFeed, cars_idle: bool) -> bool:
        return feed.exhausted() and cars_idle
