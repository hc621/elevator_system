"""Phase 3a: the fairness weight on the cost policy."""

import json
from pathlib import Path

import pytest
from helpers import building, run

from elevator_sim.__main__ import main
from elevator_sim.bench import Benchmark, SuiteOptions, build_suite, fairness_name, write_outputs
from elevator_sim.car import Projection
from elevator_sim.dispatch import CostDispatch, is_dispatch_policy, make_dispatch
from elevator_sim.feed import IteratorFeed
from elevator_sim.model import BuildingConfig
from elevator_sim.motion import make_motion
from elevator_sim.report import aggregate
from elevator_sim.scenarios import random_requests
from elevator_sim.simulator import simulate

STARVATION_PRONE = BuildingConfig.uniform(20, 3, 8, "lobby", 1)  # 120 requests in 200 ticks


def max_wait(alpha: float, seed: int) -> tuple[int, float]:
    requests = random_requests(20, 120, 200, seed)
    report = aggregate(
        simulate(STARVATION_PRONE, IteratorFeed(requests), CostDispatch(alpha), make_motion("look"))
    )
    return int(report.wait.max), report.total.mean


def test_names_and_parsing() -> None:
    assert make_dispatch("cost:0.5").name == "cost:0.5"
    assert make_dispatch("cost:0.5").fairness == 0.5  # type: ignore[attr-defined]
    assert make_dispatch("cost:0").name == "cost"  # alpha 0 is the plain policy
    assert fairness_name(0) == "cost" and fairness_name(0.2) == "cost:0.2"
    assert is_dispatch_policy("cost:1") and not is_dispatch_policy("cost:x")
    assert not is_dispatch_policy("nearest:1")
    with pytest.raises(ValueError, match="fairness weight"):
        make_dispatch("cost:abc")
    with pytest.raises(ValueError, match=">= 0"):
        CostDispatch(-1)


def test_wait_penalty_is_the_sum_of_squared_projected_waits() -> None:
    projection = Projection((), {}, {}, 0, {"a": 3, "b": 4})
    assert CostDispatch.wait_penalty(projection) == 9 + 16


def test_alpha_zero_is_exactly_the_plain_cost_policy() -> None:
    requests = random_requests(20, 60, 150, 3, lobby_up=0.4, lobby_down=0.4)
    plain, _ = run(requests, building(floors=20, cars=3, door_time=1), dispatch="cost")
    zero, _ = run(requests, building(floors=20, cars=3, door_time=1), dispatch="cost:0")
    assert plain.events() == zero.events()


def test_fairness_shortens_the_longest_wait_on_a_starvation_prone_input() -> None:
    # Seed 5: plain cost leaves one passenger waiting 52 ticks; alpha = 1 halves it, and the mean
    # total time improves too (21.3 -> 18.4), so here fairness costs nothing.
    (plain_max, plain_total), (fair_max, fair_total) = max_wait(0, 5), max_wait(1, 5)
    assert (plain_max, fair_max) == (52, 26)
    assert fair_total < plain_total


def test_fairness_lowers_the_longest_wait_on_average_but_not_on_every_input() -> None:
    plain = [max_wait(0, s)[0] for s in range(10)]
    fair = [max_wait(1, s)[0] for s in range(10)]
    assert sum(fair) < sum(plain)
    assert any(f > p for f, p in zip(fair, plain, strict=True))  # no per-input guarantee


def test_a_long_wait_makes_further_delay_expensive() -> None:
    # Squared penalty: delaying someone who already waits 30 ticks by 3 adds 189;
    # delaying someone who waits 3 by 3 adds only 27. Linear cost sees 3 either way.
    assert (33**2 - 30**2, 6**2 - 3**2) == (189, 27)
    penalty = CostDispatch.wait_penalty
    assert (
        penalty(Projection((), {}, {}, 0, {"x": 33}))
        - penalty(Projection((), {}, {}, 0, {"x": 30}))
        == 189
    )


def test_suite_adds_fairness_variants_and_the_summary_has_a_frontier(tmp_path: Path) -> None:
    options = SuiteOptions(
        seeds=2,
        scenarios=("quiet",),
        dispatch=("round_robin",),
        fairness=(0, 1),
        motion=("look",),
    )
    experiments = build_suite("quick", options)
    assert experiments[0].dispatch_policies == ("round_robin", "cost", "cost:1")
    small = [type(e)(**{**e.__dict__, "duration": 80}) for e in experiments]
    summary = write_outputs(Benchmark(workers=1).run(small), tmp_path, resamples=50)
    frontier = summary["experiments"][0]["fairness"]
    assert [f["policy"] for f in frontier] == ["cost", "cost:1"]
    assert {"total_mean_vs_cost", "wait_p95_vs_cost", "wait_max_vs_cost"} <= set(frontier[1])
    md = (tmp_path / "summary.md").read_text()
    assert "**Fairness frontier**" in md


def test_frontier_is_empty_without_variants() -> None:
    from elevator_sim.bench import fairness_frontier

    assert fairness_frontier([], ("cost",)) == []


def test_cli_fairness(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    brief = tmp_path / "brief.csv"
    brief.write_text("time,id,source,dest\n0,a,1,9\n0,b,1,5\n3,c,8,1\n")
    assert main([str(brief), "-f", "10", "-e", "2", "--fairness", "0.5", "-o", str(tmp_path)]) == 0
    assert "dispatch=cost:0.5" in capsys.readouterr().out
    report = json.loads((tmp_path / "report.json").read_text())
    assert report["policies"]["dispatch"] == "cost:0.5"
    assert main([str(brief), "-f", "10", "--algorithm", "nearest", "--fairness", "1"]) == 2
    assert main([str(brief), "-f", "10", "--fairness", "-1"]) == 2
    out = tmp_path / "bench"
    args = ["bench", "--suite", "quick", "--seeds", "2", "--scenarios", "quiet"]
    assert main([*args, "--dispatch", "round_robin", "--fairness", "0,1", "--motion", "look",
                 "--workers", "1", "-o", str(out)]) == 0  # fmt: skip
    assert "**Fairness frontier**" in (out / "summary.md").read_text()
