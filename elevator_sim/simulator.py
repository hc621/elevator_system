"""Façade: ``Simulator`` advances one tick at a time; ``simulate`` runs a feed to completion."""

from __future__ import annotations

import heapq
from collections.abc import Sequence

from elevator_sim.car import CarView
from elevator_sim.dispatch import DispatchPolicy
from elevator_sim.dispatcher import Dispatcher
from elevator_sim.events import Alighted, Boarded, Event, EventSink, NullSink, RunStarted
from elevator_sim.feed import Clock, RequestFeed, SimulationStalled, ValidatingFeed
from elevator_sim.journal import Journal
from elevator_sim.model import BuildingConfig, Request, Tick
from elevator_sim.motion import LookMotion, MotionPolicy


class _ProgressSink:
    """Forwards events and remembers the last tick anyone boarded or alighted (or the building was
    idle)."""

    def __init__(self, inner: EventSink) -> None:
        self.inner = inner
        self.last_progress: Tick = 0

    def emit(self, event: Event) -> None:
        if isinstance(event, (Boarded, Alighted)):
            self.last_progress = event.tick
        self.inner.emit(event)


class Simulator:
    """The stepwise core. A batch run and a live service would both drive it."""

    def __init__(
        self,
        config: BuildingConfig,
        dispatch: DispatchPolicy,
        motion: MotionPolicy | None = None,
        sink: EventSink | None = None,
        *,
        journal_routes: bool = False,
        max_ticks: int | None = None,
    ) -> None:
        motion = motion if motion is not None else LookMotion()
        self.config = config
        self.clock = Clock(max_ticks)
        self._sink = _ProgressSink(sink if sink is not None else NullSink())
        self._dispatcher = Dispatcher(
            config, dispatch, motion, self._sink, journal_routes=journal_routes
        )
        self._pending: list[tuple[Tick, int, Request]] = []
        self._seq = 0
        # Liveness guard: with passengers in the system, someone must board or alight within this
        # many ticks (a full sweep of the shaft and back, with a stop on every floor, twice over).
        self._stall_after = 4 * (config.floors + 1) * (config.door_time + 2)
        self._sink.emit(RunStarted(0, config, dispatch.name, motion.name))

    @property
    def now(self) -> Tick:
        return self.clock.now

    def submit(self, request: Request) -> None:
        """Queue a request; it is released to the dispatcher when its time arrives."""
        if request.time < self.clock.now:
            raise ValueError(f"request {request.id!r} at t={request.time} is in the past")
        heapq.heappush(self._pending, (request.time, self._seq, request))
        self._seq += 1

    def step(self) -> Tick:
        """Advance exactly one tick. Returns the tick that was simulated."""
        self.clock.check_limit()
        now = self.clock.now
        arrivals = []
        while self._pending and self._pending[0][0] <= now:
            arrivals.append(heapq.heappop(self._pending)[2])
        self._dispatcher.tick(now, arrivals)
        if self._dispatcher.idle():
            self._sink.last_progress = now  # nothing outstanding: restart the stall timer
        elif now - self._sink.last_progress > self._stall_after:
            raise SimulationStalled(
                f"no passenger boarded or alighted for {self._stall_after} ticks (t={now})"
            )
        self.clock.advance()
        return now

    def idle(self) -> bool:
        return not self._pending and self._dispatcher.idle()

    def snapshot(self) -> Sequence[CarView]:
        return self._dispatcher.views


def simulate(
    config: BuildingConfig,
    feed: RequestFeed,
    dispatch: DispatchPolicy,
    motion: MotionPolicy | None = None,
    *,
    journal_routes: bool = False,
    max_ticks: int | None = None,
) -> Journal:
    """Run a feed to completion: every request released, every passenger delivered."""
    feed = ValidatingFeed(feed, config.floors)
    journal = Journal()
    sim = Simulator(
        config, dispatch, motion, journal, journal_routes=journal_routes, max_ticks=max_ticks
    )
    while True:
        for request in feed.release(sim.now):
            sim.submit(request)
        sim.step()
        if sim.clock.finished(feed, sim.idle()):
            return journal
