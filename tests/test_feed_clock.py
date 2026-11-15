from collections.abc import Iterator

import pytest
from helpers import reqs

from elevator_sim.feed import (
    Clock,
    InvalidRequest,
    IteratorFeed,
    SimulationStalled,
    ValidatingFeed,
)
from elevator_sim.model import Request


def test_feed_releases_requests_exactly_at_their_time() -> None:
    feed = IteratorFeed(reqs((0, "a", 1, 2), (0, "b", 1, 3), (3, "c", 2, 1)))
    assert [r.id for r in feed.release(0)] == ["a", "b"]
    assert feed.release(1) == []
    assert feed.release(2) == []
    assert not feed.exhausted()
    assert [r.id for r in feed.release(3)] == ["c"]
    assert feed.exhausted()


def test_feed_reads_at_most_one_request_ahead() -> None:
    consumed: list[str] = []

    def source() -> Iterator[Request]:
        for r in reqs((0, "a", 1, 2), (5, "b", 1, 3), (9, "c", 2, 1)):
            consumed.append(r.id)
            yield r

    feed = IteratorFeed(source())
    feed.release(0)
    assert consumed == ["a", "b"]  # "b" is buffered but not released
    feed.release(4)
    assert consumed == ["a", "b"]
    feed.release(5)
    assert consumed == ["a", "b", "c"]


def test_empty_feed_is_exhausted() -> None:
    assert IteratorFeed([]).exhausted()


@pytest.mark.parametrize(
    ("rows", "message"),
    [
        ([(-1, "a", 1, 2)], "negative"),
        ([(0, "a", 0, 2)], "source floor 0"),
        ([(0, "a", 1, 11)], "dest floor 11"),
        ([(0, "a", 4, 4)], "same floor"),
        ([(0, "a", 1, 2), (0, "a", 2, 3)], "duplicate"),
        ([(5, "a", 1, 2), (3, "b", 2, 3)], "non-decreasing"),
    ],
)
def test_validating_feed_rejects_bad_requests(rows: list, message: str) -> None:
    feed = ValidatingFeed(IteratorFeed(reqs(*rows)), floors=10)
    with pytest.raises(InvalidRequest, match=message):
        for now in range(10):
            feed.release(now)


def test_validating_feed_passes_good_requests_through() -> None:
    feed = ValidatingFeed(IteratorFeed(reqs((0, "a", 1, 2), (2, "b", 10, 1))), floors=10)
    assert [r.id for r in feed.release(0)] == ["a"]
    assert [r.id for r in feed.release(2)] == ["b"]
    assert feed.exhausted()


def test_clock_advances_one_tick_at_a_time() -> None:
    clock = Clock()
    assert clock.now == 0
    assert [clock.advance() for _ in range(3)] == [1, 2, 3]


def test_clock_finishes_only_when_feed_is_empty_and_cars_idle() -> None:
    clock = Clock()
    pending = IteratorFeed(reqs((5, "a", 1, 2)))
    assert not clock.finished(pending, cars_idle=True)
    done = IteratorFeed([])
    assert not clock.finished(done, cars_idle=False)
    assert clock.finished(done, cars_idle=True)


def test_clock_limit() -> None:
    clock = Clock(max_ticks=2)
    clock.check_limit()
    clock.advance()
    clock.advance()
    clock.check_limit()  # tick 2 may still run
    clock.advance()
    with pytest.raises(SimulationStalled, match="tick limit"):
        clock.check_limit()
