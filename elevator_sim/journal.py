"""Append-only record of a run: the only source for every output."""

from __future__ import annotations

import json
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import TypeVar

from elevator_sim.events import Event, RunStarted, event_from_dict, event_to_dict

E = TypeVar("E")


class Journal:
    def __init__(self, events: Iterable[Event] = ()) -> None:
        self._events: list[Event] = list(events)

    def emit(self, event: Event) -> None:
        self._events.append(event)

    def events(self, kind: type[E] | None = None) -> list[E]:
        if kind is None:
            return list(self._events)  # type: ignore[arg-type]
        return [e for e in self._events if isinstance(e, kind)]

    @property
    def run_info(self) -> RunStarted | None:
        starts = self.events(RunStarted)
        return starts[0] if starts else None

    def __len__(self) -> int:
        return len(self._events)

    def __iter__(self) -> Iterator[Event]:
        return iter(self._events)

    def to_jsonl(self, path: str | Path) -> None:
        with open(path, "w", encoding="utf-8") as f:
            for event in self._events:
                f.write(json.dumps(event_to_dict(event), separators=(",", ":")))
                f.write("\n")

    @staticmethod
    def from_jsonl(path: str | Path) -> Journal:
        with open(path, encoding="utf-8") as f:
            return Journal(event_from_dict(json.loads(line)) for line in f if line.strip())
