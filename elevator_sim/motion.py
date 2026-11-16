"""Motion policies: how one car moves, when it stops, and who boards.

A motion policy is asked only at decision points (the car is closed, or its door timer has run out)
and answers from a read-only snapshot. The car owns the door timer itself.

Shared rules for LOOK and SCAN:
- A car stops at a floor when someone aboard gets off there, or when someone assigned to it is
  waiting there, heading the way the car will go, and there is room.
- Only passengers heading in the car's direction board, earliest assignment first, up to capacity.
- An idle car first serves anyone waiting at its own floor, otherwise heads for the nearest floor
  with work (ties go up).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from elevator_sim.model import Direction, Floor, PassengerId, Request


@dataclass(frozen=True)
class Move:
    direction: Direction


@dataclass(frozen=True)
class OpenDoors:
    direction: Direction  # the direction the car serves from this stop


@dataclass(frozen=True)
class Idle:
    pass


Action = Move | OpenDoors | Idle


@dataclass(frozen=True)
class CarSnapshot:
    """What a motion policy may see of a car."""

    floor: Floor
    direction: Direction
    load: int
    capacity: int
    top_floor: Floor
    onboard: tuple[Request, ...]
    waiting: tuple[Request, ...]  # assigned to this car, not yet boarded, in assignment order


class MotionPolicy(Protocol):
    name: str

    def next_action(self, state: CarSnapshot) -> Action: ...

    def who_boards(self, state: CarSnapshot) -> tuple[PassengerId, ...]: ...


class _SweepMotion:
    """Behaviour shared by LOOK and SCAN; subclasses choose the direction."""

    name = "sweep"
    # A moving car with closed doors keeps moving until the next floor where someone gets off or
    # is waiting, so a projection may jump straight there (Car.project). Policies that decide on
    # anything else must leave this False.
    skip_floors_without_work = True

    def choose_direction(self, s: CarSnapshot) -> Direction:
        raise NotImplementedError

    def next_action(self, s: CarSnapshot) -> Action:
        direction = self.choose_direction(s)
        alighting = sum(1 for p in s.onboard if p.dest == s.floor)
        room = s.capacity - s.load + alighting
        if alighting or _boarders(s, direction, room):
            return OpenDoors(direction)
        if direction is Direction.IDLE:
            return Idle()
        return Move(direction)

    def who_boards(self, s: CarSnapshot) -> tuple[PassengerId, ...]:
        return _boarders(s, s.direction, s.capacity - s.load)


def _boarders(s: CarSnapshot, direction: Direction, room: int) -> tuple[PassengerId, ...]:
    if direction is Direction.IDLE or room <= 0:
        return ()
    ids = [w.id for w in s.waiting if w.source == s.floor and w.direction is direction]
    return tuple(ids[:room])


def _work_ahead(s: CarSnapshot, direction: Direction) -> bool:
    """Is there a drop-off or pick-up strictly ahead, or a pick-up here heading this way?"""
    sign = direction.value
    if any((p.dest - s.floor) * sign > 0 for p in s.onboard):
        return True
    return any(
        (w.source - s.floor) * sign > 0 or (w.source == s.floor and w.direction is direction)
        for w in s.waiting
    )


def _direction_from_idle(s: CarSnapshot) -> Direction:
    for w in s.waiting:
        if w.source == s.floor:
            return w.direction
    targets = [w.source for w in s.waiting] + [p.dest for p in s.onboard]
    targets = [f for f in targets if f != s.floor]
    if not targets:
        return Direction.IDLE
    nearest = min(targets, key=lambda f: (abs(f - s.floor), -f))
    return Direction.UP if nearest > s.floor else Direction.DOWN


class LookMotion(_SweepMotion):
    """Keep going while any work lies ahead; reverse only when none does."""

    name = "look"

    def choose_direction(self, s: CarSnapshot) -> Direction:
        if s.direction is Direction.IDLE:
            return _direction_from_idle(s)
        if _work_ahead(s, s.direction):
            return s.direction
        if _work_ahead(s, s.direction.opposite):
            return s.direction.opposite
        return Direction.IDLE


class ScanMotion(_SweepMotion):
    """While there is any work, travel to the end of the shaft before reversing."""

    name = "scan"

    def choose_direction(self, s: CarSnapshot) -> Direction:
        if not s.onboard and not s.waiting:
            return Direction.IDLE
        if s.direction is Direction.UP:
            return Direction.UP if s.floor < s.top_floor else Direction.DOWN
        if s.direction is Direction.DOWN:
            return Direction.DOWN if s.floor > 1 else Direction.UP
        return _direction_from_idle(s)


MOTION_POLICIES: dict[str, type[_SweepMotion]] = {"look": LookMotion, "scan": ScanMotion}


def make_motion(name: str) -> MotionPolicy:
    try:
        return MOTION_POLICIES[name]()
    except KeyError:
        raise ValueError(
            f"unknown motion policy {name!r}; expected one of {sorted(MOTION_POLICIES)}"
        ) from None
