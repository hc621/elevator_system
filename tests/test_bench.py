"""The evaluation harness: paired inputs, baselines, statistics, determinism, outputs."""

import json
from pathlib import Path

import pytest

from elevator_sim.__main__ import main
from elevator_sim.bench import (
    Benchmark,
    Comparison,
    Experiment,
    SuiteOptions,
    Task,
    bootstrap_ci,
    build_suite,
    coefficient_of_variation,
    compare,
    gap_closed,
    jain,
    read_raw,
    run_task,
    summarise,
    write_outputs,
)
from elevator_sim.model import BuildingConfig


def small(n_seeds: int = 3, **kw: object) -> Experiment:
    defaults: dict = {
        "scenario": "lunch",
        "config": BuildingConfig.uniform(12, 2, 4),
        "duration": 100,
        "seeds": tuple(range(n_seeds)),
    }
    return Experiment(**{**defaults, **kw})


@pytest.fixture(scope="module")
def result():  # type: ignore[no-untyped-def]
    return Benchmark(workers=1).run([small()])


def test_one_row_per_seed_and_policy_pair(result) -> None:  # type: ignore[no-untyped-def]
    assert len(result.rows) == 3 * 4 * 2  # seeds x dispatch x motion
    for r in result.rows:  # trip-type counts add up to the passengers counted
        assert r["inbound_count"] + r["outbound_count"] + r["inter_floor_count"] == r["passengers"]
    assert {(r["dispatch"], r["motion"]) for r in result.rows} == {
        (d, m) for d in ("cost", "nearest", "round_robin", "zone") for m in ("look", "scan")
    }


def test_every_policy_in_a_seed_sees_identical_requests_and_start_state(result) -> None:  # type: ignore[no-untyped-def]
    for seed in range(3):
        rows = [r for r in result.rows if r["seed"] == seed]
        assert len({r["requests"] for r in rows}) == 1
        assert len({tuple(r["start_floors"]) for r in rows}) == 1
    assert len({r["requests"] for r in result.rows}) == 3  # ...and seeds differ from each other


def test_b0_is_the_mean_direct_ride_time(result) -> None:  # type: ignore[no-untyped-def]
    exp = result.experiments[0]
    requests = exp.requests(0)
    row = next(r for r in result.rows if r["seed"] == 0)
    assert row["direct_mean"] == pytest.approx(
        sum(abs(r.dest - r.source) for r in requests) / len(requests), abs=1e-4
    )
    summary = summarise(result, resamples=200)
    b0 = summary["experiments"][0]["b0"]
    expected = sum(r["direct_mean"] for r in result.rows) / len(result.rows)
    assert b0["total_mean"] == pytest.approx(expected, abs=1e-4)
    assert all(r["total_mean"] >= r["direct_mean"] for r in result.rows)  # nothing beats B0


def test_gap_closed_is_0_for_the_baseline_and_1_at_the_floor() -> None:
    assert gap_closed(12.0, 12.0) == 0
    assert gap_closed(12.0, 0.0) == 1
    assert gap_closed(12.0, 6.0) == 0.5
    assert gap_closed(0.0, 0.0) is None


def test_comparing_the_baseline_with_itself_is_a_null_result(result) -> None:  # type: ignore[no-untyped-def]
    look = [r for r in result.rows if r["motion"] == "look"]
    c = compare(look, "dispatch", "round_robin", "round_robin", resamples=200)
    assert (c.delta, c.ci95, c.wins, c.losses, c.gap_closed) == (0, (0, 0), 0, 0, 0)
    assert c.verdict == "inconclusive" and not c.claim


def test_comparison_is_paired_by_seed() -> None:
    rows = [
        {"seed": s, "dispatch": d, "total_mean": v, "excess_mean": v - 10}
        for s, (a, b) in enumerate([(30, 20), (50, 41), (40, 29)])
        for d, v in (("base", a), ("new", b))
    ]
    c = compare(rows, "dispatch", "new", "base", resamples=500)
    # Seeds vary a lot (30-50), but the paired difference is always about -10: a clear claim.
    assert c.delta == pytest.approx(-10)
    assert c.ci95[1] < 0 and c.wins == 3 and c.verdict == "better"
    assert c.gap_closed == pytest.approx(10 / 30, abs=1e-4)


def test_compare_rejects_unpaired_rows() -> None:
    rows = [
        {"seed": 0, "dispatch": "a", "total_mean": 1, "excess_mean": 0},
        {"seed": 1, "dispatch": "b", "total_mean": 1, "excess_mean": 0},
    ]
    with pytest.raises(ValueError, match="same seeds"):
        compare(rows, "dispatch", "a", "b")


def test_a_verdict_needs_both_significance_and_consistency() -> None:
    def verdict(ci: tuple[float, float], wins: int, losses: int) -> str:
        return Comparison("p", "b", "total_mean", 10, 0, 0, 0, 0, 0, wins, losses, ci, None).verdict

    assert verdict((-3, -1), 8, 2) == "better"
    assert verdict((-3, 1), 10, 0) == "inconclusive"  # CI includes 0
    assert verdict((-3, -1), 7, 3) == "inconclusive"  # better in only 70% of seeds
    assert verdict((1, 3), 2, 8) == "worse"  # a consistent, significant loss is reported too
    assert verdict((1, 3), 4, 6) == "inconclusive"


def test_bootstrap_ci_is_deterministic_and_brackets_the_mean() -> None:
    diffs = [-3.0, -1.0, -2.0, -4.0, 0.0]
    lo, hi = bootstrap_ci(diffs)
    assert lo <= -2 <= hi and bootstrap_ci(diffs) == (lo, hi)
    assert bootstrap_ci([-2.0] * 5) == (-2.0, -2.0)
    assert bootstrap_ci([]) == (0.0, 0.0)


def test_fairness_and_balance_helpers() -> None:
    assert jain([5, 5, 5]) == 1 and jain([0, 0, 9]) == pytest.approx(1 / 3) and jain([]) == 1
    assert jain([0, 0]) == 1  # nobody waited: perfectly fair
    assert coefficient_of_variation([4, 4]) == 0 and coefficient_of_variation([]) == 0
    assert coefficient_of_variation([0, 0]) == 0
    assert coefficient_of_variation([2, 6]) == pytest.approx(0.5)


def test_skip_first_ignores_passengers_requested_before_the_cutoff() -> None:
    full = run_task(Task(small(1), 0, "cost", "look"))
    trimmed = run_task(Task(small(1, skip_first=50), 0, "cost", "look"))
    assert trimmed["passengers"] < full["passengers"] == len(small(1).requests(0))
    assert trimmed["makespan"] == full["makespan"]  # the simulation itself is unchanged


def test_same_seed_gives_byte_identical_raw_output_in_and_across_processes(tmp_path: Path) -> None:
    exp = small(2)
    write_outputs(Benchmark(workers=1).run([exp]), tmp_path / "a", resamples=100)
    write_outputs(Benchmark(workers=1).run([exp]), tmp_path / "b", resamples=100)
    write_outputs(Benchmark(workers=2).run([exp]), tmp_path / "c", resamples=100)
    raw = [(tmp_path / d / "raw.jsonl").read_bytes() for d in "abc"]
    assert raw[0] == raw[1] == raw[2]
    assert (tmp_path / "a" / "summary.json").read_bytes() == (
        tmp_path / "c" / "summary.json"
    ).read_bytes()
    assert len(read_raw(tmp_path / "a" / "raw.jsonl")) == 2 * 8


def test_outputs_and_markdown(tmp_path: Path) -> None:
    summary = write_outputs(Benchmark(workers=1).run([small(2)]), tmp_path, resamples=100)
    assert json.loads((tmp_path / "summary.json").read_text()) == json.loads(json.dumps(summary))
    md = (tmp_path / "summary.md").read_text()
    assert "## Headline: `cost` vs `round_robin`" in md
    assert "**Dispatch axis**" in md and "**Motion axis**" in md and "**All combinations**" in md
    assert "**By trip type**" in md
    exp = summary["experiments"][0]
    assert [c["policy"] for c in exp["dispatch_axis"]] == ["cost", "nearest", "zone"]
    assert len(exp["motion_axis"]) == 4 and len(exp["combos"]) == 8


def test_axes_are_skipped_when_their_baseline_is_not_run() -> None:
    exp = small(2, dispatch_policies=("cost", "nearest"), motion_policies=("look",))
    summary = summarise(Benchmark(workers=1).run([exp]), resamples=50)
    entry = summary["experiments"][0]
    assert entry["dispatch_axis"] == [] and entry["motion_axis"] == []
    assert "Headline" not in json.dumps(summary)


def test_suites_expand_over_the_requested_axes() -> None:
    standard = build_suite("standard", SuiteOptions(seeds=2))
    assert len(standard) == 4 * 2  # scenarios x buildings
    assert {e.scenario for e in standard} == {"quiet", "morning_rush", "lunch", "evening_rush"}
    assert {e.load for e in standard} == {1.0}
    swept = build_suite(
        "quick",
        SuiteOptions(seeds=1, door_times=(0, 2), placements=("lobby", "spread"), loads=(1, 1.5)),
    )
    assert len(swept) == 2 * 2 * 2 * 2
    assert {e.config.door_time for e in swept} == {0, 2}
    assert {e.load for e in swept} == {1, 1.5}
    assert {e.key["rate"] for e in swept if e.scenario == "quiet"} == {0.12, 0.18}
    spread = next(e for e in swept if e.placement == "spread")
    assert [c.start_floor for c in spread.config.cars] == [1, 8, 16, 23]
    with pytest.raises(ValueError, match="unknown suite"):
        build_suite("everything")


def test_experiment_validation() -> None:
    for bad, match in [
        ({"scenario": "uniform"}, "scenario"),
        ({"dispatch_policies": ("elevator_operator",)}, "dispatch"),
        ({"motion_policies": ("teleport",)}, "motion"),
        ({"seeds": ()}, "seed"),
    ]:
        with pytest.raises(ValueError, match=match):
            small(**bad)


def test_bench_cli(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    out = tmp_path / "bench"
    args = ["bench", "--suite", "quick", "--seeds", "2", "--scenarios", "quiet"]
    assert main([*args, "--dispatch", "cost,round_robin", "--workers", "1", "-o", str(out)]) == 0
    assert "8 runs over 1 experiments" in capsys.readouterr().out
    assert {p.name for p in out.iterdir()} == {"raw.jsonl", "summary.json", "summary.md"}


def test_bench_cli_rejects_bad_lists() -> None:
    for flag, value in [("--dispatch", "cost,psychic"), ("--door-times", "1,x"), ("--loads", ",")]:
        with pytest.raises(SystemExit):
            main(["bench", flag, value])


def test_sensitivity_tables_appear_only_when_settings_vary(tmp_path: Path) -> None:
    options = SuiteOptions(
        seeds=2, door_times=(0, 1), scenarios=("quiet",), dispatch=("cost", "round_robin")
    )
    experiments = [
        Experiment(**{**e.__dict__, "duration": 80}) for e in build_suite("quick", options)
    ]
    summary = write_outputs(Benchmark(workers=1).run(experiments), tmp_path, resamples=50)
    md = (tmp_path / "summary.md").read_text()
    assert "## Sensitivity: which conclusions survive" in md
    assert "| scenario | building | door 0 | door 1 |" in md
    assert "### `cost` vs `round_robin` (LOOK)" in md and "### LOOK vs SCAN with `cost`" in md
    assert "cost > round_robin" in md or "round_robin > cost" in md  # the ranking table
    assert len(summary["experiments"]) == 2

    write_outputs(Benchmark(workers=1).run([small(2)]), tmp_path / "plain", resamples=50)
    assert "Sensitivity" not in (tmp_path / "plain" / "summary.md").read_text()
