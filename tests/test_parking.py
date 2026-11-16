"""Phase 3b: parking policies (where idle cars wait)."""

import json
from pathlib import Path

import pytest
from helpers import building, check_invariants, floors_by_car, records, reqs

from elevator_sim.__main__ import main
from elevator_sim.bench import Benchmark, Experiment, write_outputs
from elevator_sim.dispatch import make_dispatch
from elevator_sim.events import RunStarted
from elevator_sim.feed import IteratorFeed
from elevator_sim.journal import Journal
from elevator_sim.model import BuildingConfig
from elevator_sim.motion import make_motion
from elevator_sim.parking import DemandParking, make_parking
from elevator_sim.report import aggregate
from elevator_sim.scenarios import generate
from elevator_sim.simulator import simulate


def run(requests, config, parking="stay", dispatch="cost", parking_policy=None):  # type: ignore[no-untyped-def]
    policy = parking_policy or make_parking(parking)
    journal = simulate(
        config, IteratorFeed(requests), make_dispatch(dispatch), make_motion("look"),
        parking=policy,
    )  # fmt: skip
    return journal, aggregate(journal)


def test_stay_is_exactly_the_default() -> None:
    requests = generate("lunch", floors=20, duration=150, seed=2)
    config = building(floors=20, cars=3, door_time=1)
    default = simulate(config, IteratorFeed(requests), make_dispatch("cost"), make_motion("look"))
    stay, _ = run(requests, config, "stay")
    assert [e for e in default.events() if not isinstance(e, RunStarted)] == [
        e for e in stay.events() if not isinstance(e, RunStarted)
    ]


def test_lobby_sends_an_idle_car_back_down_and_counts_the_moves() -> None:
    # One car takes a from 1 to 6, then sits idle until b asks at t=20.
    requests = reqs((0, "a", 1, 6), (20, "b", 1, 3))
    journal, report = run(requests, building(floors=10), "lobby")
    floors = floors_by_car(journal)[0]
    # Up to 6 (t5). The parking decision is made at the end of the tick the car goes idle, so it
    # leaves on the next tick: back at the lobby by t11, waits there; b boards at once at t20.
    assert floors[:12] == [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]
    assert records(report)["b"].wait == 0
    _, stay = run(requests, building(floors=10), "stay")
    assert records(stay)["b"].wait == 5  # without parking the car comes down from 6
    assert report.per_car[0].distance == stay.per_car[0].distance  # same floors, earlier
    assert report.per_car[0].trips == 3  # up, parking down, up again


def test_a_parking_car_turns_around_as_soon_as_it_is_assigned() -> None:
    # a rides 1 -> 10 (drop-off t9); the car starts back down to the lobby at t10 and is at
    # floor 9 at t11, when b asks at floor 10, behind it: it turns around at once.
    requests = reqs((0, "a", 1, 10), (11, "b", 10, 2))
    journal, report = run(requests, building(floors=10), "lobby")
    floors = floors_by_car(journal)[0]
    assert floors[9:13] == [10, 10, 9, 10]
    assert records(report)["b"].boarded == 12
    check_invariants(journal, requests)


def test_spread_parks_each_car_at_its_own_home_floor() -> None:
    # Three idle cars at the lobby; one late request keeps the run going until t=50.
    journal, _ = run(reqs((50, "late", 1, 2)), building(floors=30, cars=3), "spread")
    at_t40 = {car: floors[40] for car, floors in floors_by_car(journal).items()}
    assert at_t40 == {0: 1, 1: 11, 2: 21}  # homes 1 + i * 30 // 3, reached within 20 ticks


class _Spy(DemandParking):
    def __init__(self) -> None:
        super().__init__(window=100)
        self.latest: list[tuple[int, int]] = []

    def target(self, car, cars, claimed, history, now):  # type: ignore[no-untyped-def]
        self.latest.append((max((r.time for r in history), default=-1), now))
        return super().target(car, cars, claimed, history, now)


def test_demand_never_sees_a_request_before_its_time() -> None:
    spy = _Spy()
    requests = generate("lunch", floors=20, duration=200, seed=4)
    run(requests, building(floors=20, cars=3), parking_policy=spy)
    assert spy.latest and all(seen <= now for seen, now in spy.latest)


def test_demand_picks_the_busiest_recent_floor_and_skips_claimed_ones() -> None:
    from elevator_sim.car import Car, CarView
    from elevator_sim.model import CarSpec, Request

    car = CarView(Car(0, CarSpec(8, 5), top_floor=20, door_time=1, motion=make_motion("look")))
    history = [Request(t, f"p{t}", s, 1) for t, s in [(1, 12), (2, 12), (3, 7), (4, 7), (5, 7)]]
    demand = DemandParking(window=100)
    assert demand.target(car, [car], frozenset(), history, now=10) == 7
    assert demand.target(car, [car], frozenset({7}), history, now=10) == 12
    assert demand.target(car, [car], frozenset(), history, now=500) is None  # all too old
    assert DemandParking(window=6).target(car, [car], frozenset(), history, now=10) == 7


@pytest.mark.parametrize("parking", ["stay", "lobby", "spread", "demand"])
@pytest.mark.parametrize("dispatch", ["cost", "round_robin"])
def test_invariants_hold_with_every_parking_policy(parking: str, dispatch: str) -> None:
    for seed, scenario in enumerate(["quiet", "morning_rush", "evening_rush"]):
        requests = generate(scenario, floors=15, duration=80, seed=seed)
        config = building(floors=15, cars=3, capacity=3, door_time=1)
        journal, report = run(requests, config, parking, dispatch)
        check_invariants(journal, requests)
        assert not report.unserved and report.parking == parking


def test_parking_respects_the_floors_a_car_serves() -> None:
    from elevator_sim.car import Car, CarView
    from elevator_sim.model import CarSpec

    express = CarSpec(8, 21, frozenset(range(21, 41)))
    view = CarView(Car(0, express, top_floor=40, door_time=1, motion=make_motion("look")))
    assert make_parking("lobby").target(view, [view], frozenset(), [], 0) is None


def test_names_and_errors() -> None:
    assert {make_parking(n).name for n in ("stay", "lobby", "spread", "demand")} == {
        "stay", "lobby", "spread", "demand",
    }  # fmt: skip
    with pytest.raises(ValueError, match="unknown parking"):
        make_parking("valet")
    with pytest.raises(ValueError, match="parking"):
        Experiment("quiet", building(floors=10), 50, (0,), parking="valet")


def test_journal_records_the_parking_policy(tmp_path: Path) -> None:
    journal, report = run(reqs((0, "a", 1, 5)), building(floors=10), "spread")
    path = tmp_path / "run.jsonl"
    journal.to_jsonl(path)
    loaded = Journal.from_jsonl(path)
    assert loaded.run_info.parking == "spread" and aggregate(loaded) == report


def test_bench_compares_each_policy_with_stay(tmp_path: Path) -> None:
    config = BuildingConfig.uniform(12, 2, 4, "lobby", 1)
    experiments = [
        Experiment(
            "lunch",
            config,
            80,
            (0, 1),
            dispatch_policies=("cost",),
            motion_policies=("look",),
            parking=p,
        )
        for p in ("stay", "lobby", "demand")
    ]
    summary = write_outputs(Benchmark(workers=1).run(experiments), tmp_path, resamples=50)
    comparisons = summary["parking"]
    assert [(c["dispatch"], c["parking"]) for c in comparisons] == [
        ("cost", "lobby"), ("cost", "demand"),
    ]  # fmt: skip
    assert {"total_mean", "wait_mean", "wait_max", "distance_per_passenger"} <= set(comparisons[0])
    assert "## Parking: each policy vs `stay`" in (tmp_path / "summary.md").read_text()
    from elevator_sim.html_report import render_bench

    page = render_bench(summary)
    assert "Parking: lobby vs stay" in page and "Parking: demand vs stay" in page


def test_cli_parking(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    csv = tmp_path / "r.csv"
    csv.write_text("time,id,source,dest\n0,a,1,6\n20,b,1,3\n")
    assert main([str(csv), "-f", "10", "-e", "1", "--parking", "lobby", "-o", str(tmp_path)]) == 0
    assert "parking=lobby" in capsys.readouterr().out
    report = json.loads((tmp_path / "report.json").read_text())
    assert report["policies"]["parking"] == "lobby"
    out = tmp_path / "bench"
    args = ["bench", "--suite", "quick", "--seeds", "2", "--scenarios", "quiet", "--motion", "look"]
    assert main([*args, "--dispatch", "cost", "--parking", "stay,spread", "--workers", "1",
                 "-o", str(out)]) == 0  # fmt: skip
    assert "## Parking" in (out / "summary.md").read_text()
