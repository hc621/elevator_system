"""Routes and projections: the derived route must predict what the car really does."""

import pytest
from helpers import building, records, reqs, run

from elevator_sim.dispatch import make_dispatch
from elevator_sim.events import Alighted, Boarded, CarState, DoorsOpened, RouteChanged
from elevator_sim.journal import Journal
from elevator_sim.motion import make_motion
from elevator_sim.scenarios import random_requests
from elevator_sim.simulator import Simulator


@pytest.mark.parametrize("motion", ["look", "scan"])
@pytest.mark.parametrize("door_time", [0, 1, 2])
def test_route_predicts_the_real_stops_when_no_new_requests_arrive(
    motion: str, door_time: int
) -> None:
    requests = random_requests(
        floors=25, count=30, duration=40, seed=7, lobby_up=0.4, lobby_down=0.4
    )
    config = building(floors=25, cars=3, capacity=4, door_time=door_time)
    journal = Journal()
    sim = Simulator(config, make_dispatch("cost"), make_motion(motion), journal)
    for r in requests:
        sim.submit(r)
    while sim.now <= requests[-1].time:  # every request has been assigned
        sim.step()
    predicted = {v.id: v.project() for v in sim.snapshot()}
    start = sim.now
    while not sim.idle():
        sim.step()

    for car_id, projection in predicted.items():
        opened = [(e.floor, e.tick) for e in journal.events(DoorsOpened) if e.car == car_id]
        actual = [stop for stop in opened if stop[1] >= start]
        assert [(s.floor, s.eta) for s in projection.route] == actual
        boards = {e.passenger: e.tick for e in journal.events(Boarded) if e.tick >= start}
        drops = {e.passenger: e.tick for e in journal.events(Alighted) if e.tick >= start}
        assert all(boards[p] == t for p, t in projection.pickup_eta.items())
        assert all(drops[p] == t for p, t in projection.dropoff_eta.items())


def test_request_beyond_the_last_stop_extends_the_route() -> None:
    journal, _ = run(reqs((0, "a", 1, 10), (3, "b", 15, 20)), building(floors=30))
    changes = journal.events(RouteChanged)
    assert [c.tick for c in changes] == [0, 3]
    later = changes[1]
    assert [s.floor for s in later.old] == [10]
    assert [s.floor for s in later.new] == [10, 15, 20]
    assert later.new[1].board == ("b",) and later.new[2].alight == ("b",)


def test_a_car_on_its_way_up_picks_up_a_passenger_along_the_way_without_detour() -> None:
    journal, report = run(reqs((0, "a", 1, 20), (3, "b", 10, 15)), building(floors=30))
    a, b = records(report)["a"], records(report)["b"]
    assert (b.boarded, b.alighted, b.wait) == (9, 14, 6)
    assert a.alighted == 19  # no detour: still the direct time
    floors = [s.floor for s in journal.events(CarState)]
    assert floors == list(range(1, 21))  # straight up, never down


def test_a_full_car_passes_by_and_comes_back_later() -> None:
    _, report = run(reqs((0, "a", 1, 20), (3, "b", 10, 15)), building(floors=30, capacity=1))
    b = records(report)["b"]
    # The car reaches 10 at t9 full, goes on to 20 (t19), comes back down to 10 (t29).
    assert (b.boarded, b.alighted, b.wait) == (29, 34, 26)


def test_routes_in_the_journal_look_ahead_from_the_next_tick() -> None:
    journal, _ = run(reqs((0, "a", 1, 5)), building(floors=10, door_time=1), journal_routes=True)
    states = journal.events(CarState)
    assert states[0].route is not None
    assert [(s.floor, s.eta) for s in states[0].route] == [(5, 5)]
    assert all(stop.eta > s.tick for s in states for stop in (s.route or ()))
