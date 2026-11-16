"""Evaluation harness: run policies on identical inputs across seeds and compare them to baselines.

The unit of comparison is an :class:`Experiment`: one scenario on one building at one load, run
for several seeds. For each seed the requests are generated once, from the seed alone, so every
(dispatch, motion) combination sees exactly the same passengers and start state; differences
between policies come from the policy, not from the random draw (a *paired* design).

Baselines (README "How results are measured"):

- **B0**, the theoretical floor: every passenger is picked up at once and rides directly, so
  total = direct and excess = 0. Unbeatable; shows how much headroom is left.
- **round_robin** dispatch: the naive reference every dispatch policy must beat.
- **SCAN** motion: the reference on the motion axis.

A claim needs the paired 95% bootstrap CI of the difference to exclude 0 *and* the result to go the
same way in at least 80% of seeds: "better" (CI below 0, wins >= 80%), "worse" (CI above 0,
losses >= 80%), otherwise "inconclusive".
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import random
from collections.abc import Iterable, Mapping, Sequence
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from elevator_sim.dispatch import DISPATCH_POLICIES, is_dispatch_policy, make_dispatch
from elevator_sim.feed import IteratorFeed
from elevator_sim.model import BuildingConfig, Request
from elevator_sim.motion import MOTION_POLICIES, make_motion
from elevator_sim.report import PassengerRecord, RunReport, Stats, aggregate
from elevator_sim.scenarios import SCENARIOS, generate
from elevator_sim.simulator import simulate

Row = dict[str, Any]  # one run: experiment key, policy, seed and metrics

PRIMARY = "total_mean"  # the brief's objective: total time per passenger
CLAIM_WIN_SHARE = 0.8
RESAMPLES = 2000


# ---------------------------------------------------------------- experiments


@dataclass(frozen=True)
class Experiment:
    """One cell of conditions; every (dispatch, motion) pair runs on it for every seed."""

    scenario: str
    config: BuildingConfig
    count: int  # requests per run
    duration: int  # arrival window in ticks
    seeds: tuple[int, ...]
    dispatch_policies: tuple[str, ...] = tuple(sorted(DISPATCH_POLICIES))
    motion_policies: tuple[str, ...] = ("look", "scan")
    placement: str = "lobby"  # label only; the start floors live in ``config``
    skip_first: int = 0  # ignore passengers requested before this tick (start-up trimming)
    baseline: str = "round_robin"
    baseline_motion: str = "scan"

    def __post_init__(self) -> None:
        if self.scenario not in SCENARIOS:
            raise ValueError(f"unknown scenario {self.scenario!r}")
        for name in self.dispatch_policies:
            if not is_dispatch_policy(name):
                raise ValueError(f"unknown dispatch policy {name!r}")
        for name in self.motion_policies:
            if name not in MOTION_POLICIES:
                raise ValueError(f"unknown motion policy {name!r}")
        if not self.seeds:
            raise ValueError("an experiment needs at least one seed")

    @property
    def key(self) -> dict[str, object]:
        """What identifies this experiment in the outputs."""
        cfg = self.config
        return {
            "scenario": self.scenario,
            "floors": cfg.floors,
            "cars": len(cfg.cars),
            "capacity": cfg.cars[0].capacity,
            "door_time": cfg.door_time,
            "placement": self.placement,
            "count": self.count,
            "duration": self.duration,
            "rate": round(self.count / self.duration, 4),
            "skip_first": self.skip_first,
        }

    @property
    def title(self) -> str:
        k = self.key
        return (
            f"{k['scenario']} · {k['floors']} floors x {k['cars']} cars"
            f" · door_time {k['door_time']} · {k['placement']}"
            f" · {k['count']} requests / {k['duration']} ticks"
        )

    def requests(self, seed: int) -> list[Request]:
        return generate(self.scenario, self.config.floors, self.count, self.duration, seed)


@dataclass(frozen=True)
class Task:
    experiment: Experiment
    seed: int
    dispatch: str
    motion: str


def tasks(experiments: Iterable[Experiment]) -> list[Task]:
    return [
        Task(exp, seed, dispatch, motion)
        for exp in experiments
        for seed in exp.seeds
        for dispatch in exp.dispatch_policies
        for motion in exp.motion_policies
    ]


# ---------------------------------------------------------------- one run


def digest(requests: Sequence[Request]) -> str:
    """Short fingerprint of a request list: equal digests mean identical inputs."""
    text = ";".join(f"{r.time},{r.id},{r.source},{r.dest}" for r in requests)
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def jain(values: Sequence[float]) -> float:
    """Jain's fairness index (sum x)^2 / (n * sum x^2): 1 when all equal, 1/n when one has all."""
    square_sum = sum(v * v for v in values)
    if not values or square_sum == 0:
        return 1.0
    return sum(values) ** 2 / (len(values) * square_sum)


def coefficient_of_variation(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    mean = sum(values) / len(values)
    if mean == 0:
        return 0.0
    return math.sqrt(sum((v - mean) ** 2 for v in values) / len(values)) / mean


def run_task(task: Task) -> Row:
    """Simulate one (experiment, seed, dispatch, motion) and return one flat row of metrics.

    Top-level so worker processes can import it. Deterministic: same task, same row.
    """
    exp = task.experiment
    requests = exp.requests(task.seed)
    journal = simulate(
        exp.config, IteratorFeed(requests), make_dispatch(task.dispatch), make_motion(task.motion)
    )
    report = aggregate(journal)
    counted = [r for r in report.passengers if r.requested >= exp.skip_first]
    cars = list(report.per_car.values())
    return {
        **exp.key,
        "seed": task.seed,
        "dispatch": task.dispatch,
        "motion": task.motion,
        "requests": digest(requests),
        "start_floors": [c.start_floor for c in exp.config.cars],
        **passenger_metrics(counted),
        "unserved": len(report.unserved),
        "makespan": report.makespan,
        "distance": sum(c.distance for c in cars),
        "trips": sum(c.trips for c in cars),
        "load_cv": round(coefficient_of_variation([c.passengers for c in cars]), 4),
        **diagnostic_metrics(report),
    }


def diagnostic_metrics(report: RunReport) -> dict[str, float]:
    """Root-cause columns (over all served passengers, regardless of ``skip_first``)."""
    d = report.diagnostics
    away, idle = d.assignment["moving_away"], d.assignment["idle"]
    return {
        "detour_mean": round(d.detour.mean, 4),
        "away_share": round(away.share, 4),
        "away_wait": round(away.mean_wait, 4),
        "idle_pick_share": round(idle.share, 4),
        "chosen_distance": round(d.chosen_distance, 4),
        "nearest_distance": round(d.nearest_distance, 4),
        "busy_share": round(d.busy_share, 4),
        "distance_per_passenger": round(d.distance_per_passenger, 4),
        "riders_per_stop": round(d.riders_per_stop, 4),
        "full_passby_share": round(d.full_passby_share, 4),
    }


def passenger_metrics(records: Sequence[PassengerRecord]) -> dict[str, float]:
    wait = Stats.of([r.wait for r in records])
    total = Stats.of([r.total for r in records])
    n = len(records)
    return {
        "passengers": n,
        "wait_mean": round(wait.mean, 4),
        "wait_p50": round(wait.p50, 4),
        "wait_p90": round(wait.p90, 4),
        "wait_p95": round(wait.p95, 4),
        "wait_max": wait.max,
        "total_mean": round(total.mean, 4),
        "total_p95": round(total.p95, 4),
        "total_max": total.max,
        "direct_mean": round(sum(r.direct for r in records) / n, 4) if n else 0.0,
        "excess_mean": round(sum(r.excess for r in records) / n, 4) if n else 0.0,
        "stretch_mean": round(sum(r.total / r.direct for r in records) / n, 4) if n else 0.0,
        "zero_wait_share": round(sum(r.wait == 0 for r in records) / n, 4) if n else 0.0,
        "jain_wait": round(jain([r.wait for r in records]), 4),
    }


# ---------------------------------------------------------------- the benchmark


@dataclass
class BenchResult:
    experiments: list[Experiment]
    rows: list[Row] = field(default_factory=list)

    def rows_for(self, exp: Experiment) -> list[Row]:
        key = exp.key
        return [r for r in self.rows if all(r[k] == v for k, v in key.items())]


class Benchmark:
    def __init__(self, workers: int | None = None) -> None:
        self.workers = workers if workers is not None else (os.cpu_count() or 1)

    def run(self, experiments: Sequence[Experiment]) -> BenchResult:
        todo = tasks(experiments)
        if self.workers <= 1 or len(todo) < 2:
            rows = [run_task(t) for t in todo]
        else:
            with ProcessPoolExecutor(max_workers=self.workers) as pool:
                rows = list(
                    pool.map(run_task, todo, chunksize=max(1, len(todo) // (8 * self.workers)))
                )
        return BenchResult(list(experiments), rows)


# ---------------------------------------------------------------- comparison


@dataclass(frozen=True)
class Comparison:
    """A policy against the baseline on one experiment, paired by seed. Lower is better."""

    policy: str
    baseline: str
    metric: str
    n: int
    mean: float
    std: float
    baseline_mean: float
    delta: float  # mean(policy - baseline)
    delta_pct: float  # delta / baseline_mean
    wins: int  # seeds where the policy is strictly better
    losses: int  # seeds where it is strictly worse
    ci95: tuple[float, float]  # paired bootstrap on the mean difference
    gap_closed: float | None  # share of the baseline's excess time removed

    @property
    def verdict(self) -> str:
        """``better`` / ``worse`` if significant (CI excludes 0) and consistent (>= 80% of seeds
        go that way); ``inconclusive`` otherwise."""
        lo, hi = self.ci95
        if hi < 0 and self.wins >= CLAIM_WIN_SHARE * self.n:
            return "better"
        if lo > 0 and self.losses >= CLAIM_WIN_SHARE * self.n:
            return "worse"
        return "inconclusive"

    @property
    def claim(self) -> bool:
        return self.verdict != "inconclusive"

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["ci95"] = list(self.ci95)
        data["wins"] = f"{self.wins}/{self.n}"
        data["losses"] = f"{self.losses}/{self.n}"
        data["verdict"] = self.verdict
        return data


def bootstrap_ci(
    diffs: Sequence[float], resamples: int = RESAMPLES, seed: int = 0
) -> tuple[float, float]:
    """95% percentile-bootstrap interval for the mean of paired differences (stdlib only)."""
    if not diffs:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(diffs)
    means = sorted(sum(rng.choices(diffs, k=n)) / n for _ in range(resamples))
    return (means[int(0.025 * resamples)], means[min(resamples - 1, int(0.975 * resamples))])


def gap_closed(baseline_excess: float, policy_excess: float) -> float | None:
    """0 = no better than the baseline, 1 = reaches the theoretical floor (excess 0)."""
    if baseline_excess == 0:
        return None
    return (baseline_excess - policy_excess) / baseline_excess


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _std(values: Sequence[float]) -> float:
    m = _mean(values)
    return math.sqrt(_mean([(v - m) ** 2 for v in values])) if values else 0.0


def compare(
    rows: Sequence[Row],
    field_name: str,
    policy: str,
    baseline: str,
    metric: str = PRIMARY,
    resamples: int = RESAMPLES,
) -> Comparison:
    """Compare ``policy`` with ``baseline`` on ``field_name`` (``dispatch`` or ``motion``).

    ``rows`` must hold exactly one row per seed for each of the two values (the other axis fixed).
    """
    by_seed = {r["seed"]: r for r in rows if r[field_name] == policy}
    base_by_seed = {r["seed"]: r for r in rows if r[field_name] == baseline}
    if by_seed.keys() != base_by_seed.keys():
        raise ValueError(f"{policy} and {baseline} were not run on the same seeds")
    seeds = sorted(by_seed)
    values = [float(by_seed[s][metric]) for s in seeds]
    base = [float(base_by_seed[s][metric]) for s in seeds]
    diffs = [v - b for v, b in zip(values, base, strict=True)]
    delta, base_mean = _mean(diffs), _mean(base)
    lo, hi = bootstrap_ci(diffs, resamples)
    excess = _mean([float(by_seed[s]["excess_mean"]) for s in seeds])
    base_excess = _mean([float(base_by_seed[s]["excess_mean"]) for s in seeds])
    gap = gap_closed(base_excess, excess)
    return Comparison(
        policy=policy,
        baseline=baseline,
        metric=metric,
        n=len(seeds),
        mean=round(_mean(values), 4),
        std=round(_std(values), 4),
        baseline_mean=round(base_mean, 4),
        delta=round(delta, 4),
        delta_pct=round(delta / base_mean, 4) if base_mean else 0.0,
        wins=sum(d < 0 for d in diffs),
        losses=sum(d > 0 for d in diffs),
        ci95=(round(lo, 4), round(hi, 4)),
        gap_closed=round(gap, 4) if gap is not None else None,
    )


MEAN_COLUMNS = (
    "total_mean", "wait_mean", "wait_p95", "wait_max", "excess_mean", "jain_wait",
    "detour_mean", "away_share", "away_wait", "idle_pick_share", "chosen_distance",
    "nearest_distance", "busy_share", "distance_per_passenger", "riders_per_stop",
    "full_passby_share", "load_cv",
)  # fmt: skip


def summarise(result: BenchResult, resamples: int = RESAMPLES) -> dict[str, Any]:
    """Everything the README needs, per experiment: means, B0, dispatch axis, motion axis."""
    experiments = []
    for exp in result.experiments:
        rows = result.rows_for(exp)
        combos = []
        for dispatch in exp.dispatch_policies:
            for motion in exp.motion_policies:
                sel = [r for r in rows if r["dispatch"] == dispatch and r["motion"] == motion]
                means = {c: round(_mean([float(r[c]) for r in sel]), 4) for c in MEAN_COLUMNS}
                combos.append({"dispatch": dispatch, "motion": motion, **means})

        entry: dict[str, Any] = {
            "key": exp.key,
            "title": exp.title,
            "seeds": len(exp.seeds),
            "b0": {
                "total_mean": round(_mean([float(r["direct_mean"]) for r in rows]), 4),
                "wait_mean": 0.0,
                "excess_mean": 0.0,
            },
            "combos": combos,
            "dispatch_axis": [],
            "motion_axis": [],
        }
        if "look" in exp.motion_policies and exp.baseline in exp.dispatch_policies:
            look = [r for r in rows if r["motion"] == "look"]
            entry["dispatch_axis"] = [
                compare(look, "dispatch", d, exp.baseline, resamples=resamples).to_dict()
                for d in exp.dispatch_policies
                if d != exp.baseline
            ]
        if exp.baseline_motion in exp.motion_policies:
            axis = []
            for dispatch in exp.dispatch_policies:
                sel = [r for r in rows if r["dispatch"] == dispatch]
                for motion in exp.motion_policies:
                    if motion != exp.baseline_motion:
                        c = compare(sel, "motion", motion, exp.baseline_motion, resamples=resamples)
                        axis.append({"dispatch": dispatch, **c.to_dict()})
            entry["motion_axis"] = axis
        entry["fairness"] = fairness_frontier(rows, exp.dispatch_policies, resamples)
        experiments.append(entry)
    return {
        "metric": PRIMARY,
        "claim_rule": (
            f"95% CI of the difference excludes 0 and >= {CLAIM_WIN_SHARE:.0%} of seeds "
            "go the same way"
        ),
        "resamples": resamples,
        "experiments": experiments,
    }


def fairness_name(alpha: float) -> str:
    """The dispatch-policy name of the cost policy with fairness weight alpha."""
    return f"cost:{alpha:g}" if alpha else "cost"


FRONTIER_COLUMNS = ("total_mean", "wait_mean", "wait_p95", "wait_max")


def fairness_frontier(
    rows: Sequence[Row], policies: Sequence[str], resamples: int = RESAMPLES
) -> list[dict[str, Any]]:
    """Each cost:<alpha> variant against plain cost (LOOK), on efficiency and on the wait tail."""
    look = [r for r in rows if r["motion"] == "look"]
    variants = [p for p in policies if p.startswith("cost:")]
    if "cost" not in policies or not variants or not look:
        return []
    frontier = []
    for policy in ["cost", *variants]:
        sel = [r for r in look if r["dispatch"] == policy]
        entry: dict[str, Any] = {
            "policy": policy,
            "fairness": float(policy.partition(":")[2] or 0),
            **{c: round(_mean([float(r[c]) for r in sel]), 4) for c in FRONTIER_COLUMNS},
        }
        if policy != "cost":
            for metric in ("total_mean", "wait_p95", "wait_max"):
                c = compare(look, "dispatch", policy, "cost", metric=metric, resamples=resamples)
                entry[f"{metric}_vs_cost"] = {
                    "delta": c.delta,
                    "delta_pct": c.delta_pct,
                    "ci95": list(c.ci95),
                    "verdict": c.verdict,
                }
        frontier.append(entry)
    return frontier


# ---------------------------------------------------------------- suites


@dataclass(frozen=True)
class SuiteOptions:
    seeds: int = 20
    door_times: tuple[int, ...] = (1,)
    placements: tuple[str, ...] = ("lobby",)
    rates: tuple[float, ...] | None = None  # requests per tick; None = the suite's default
    scenarios: tuple[str, ...] | None = None
    dispatch: tuple[str, ...] | None = None
    motion: tuple[str, ...] | None = None
    skip_first: int = 0
    fairness: tuple[
        float, ...
    ] = ()  # fairness weights; adds cost:<alpha> variants (0 = plain cost)


# name -> (scenarios, buildings as (floors, cars, capacity), default rate, duration)
SUITES: dict[str, tuple[tuple[str, ...], tuple[tuple[int, int, int], ...], float, int]] = {
    "standard": (
        ("uniform", "mixed", "morning_rush", "evening_rush"),
        ((30, 4, 8), (40, 6, 8)),
        0.25,
        800,
    ),
    "quick": (("uniform", "morning_rush"), ((30, 4, 8),), 0.25, 400),
}


def build_suite(name: str, options: SuiteOptions = SuiteOptions()) -> list[Experiment]:
    if name not in SUITES:
        raise ValueError(f"unknown suite {name!r}; expected one of {sorted(SUITES)}")
    scenarios, buildings, default_rate, duration = SUITES[name]
    dispatch = options.dispatch or tuple(sorted(DISPATCH_POLICIES))
    if options.fairness:
        variants = tuple(fairness_name(a) for a in options.fairness)
        dispatch = tuple(dict.fromkeys((*dispatch, *variants)))
    experiments = []
    for scenario in options.scenarios or scenarios:
        for floors, cars, capacity in buildings:
            for door_time in options.door_times:
                for placement in options.placements:
                    for rate in options.rates or (default_rate,):
                        config = BuildingConfig.uniform(
                            floors, cars, capacity, placement, door_time
                        )
                        experiments.append(
                            Experiment(
                                scenario=scenario,
                                config=config,
                                count=round(rate * duration),
                                duration=duration,
                                seeds=tuple(range(options.seeds)),
                                dispatch_policies=dispatch,
                                motion_policies=options.motion or ("look", "scan"),
                                placement=placement,
                                skip_first=options.skip_first,
                            )
                        )
    return experiments


# ---------------------------------------------------------------- outputs


def write_raw(result: BenchResult, path: str | Path) -> None:
    """JSON Lines, one row per run, in a fixed order: same inputs give a byte-identical file."""
    with open(path, "w", encoding="utf-8") as f:
        for row in result.rows:
            f.write(json.dumps(row, separators=(",", ":")) + "\n")


def read_raw(path: str | Path) -> list[Row]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _pct(x: float) -> str:
    return f"{x:+.1%}"


def format_markdown(summary: Mapping[str, object]) -> str:
    """Paste-ready tables for the README."""
    experiments: list[dict[str, Any]] = summary["experiments"]
    lines = [
        "# Benchmark results",
        "",
        f"Metric: mean total time per passenger (ticks), lower is better. "
        f"Claim rule: {summary['claim_rule']}. Paired bootstrap, {summary['resamples']} resamples.",
        "",
    ]
    headline = [e for e in experiments if any(c["policy"] == "cost" for c in e["dispatch_axis"])]
    if headline:
        lines += [
            "## Headline: `cost` vs `round_robin` (LOOK motion)",
            "",
            "| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |",
            "|---|---:|---:|---:|---|---:|---:|---:|",
        ]
        for e in headline:
            c = next(c for c in e["dispatch_axis"] if c["policy"] == "cost")
            lines.append(
                f"| {e['title']} | {c['baseline_mean']:.1f} | {c['mean']:.1f} "
                f"| {_pct(c['delta_pct'])} | [{c['ci95'][0]:+.1f}, {c['ci95'][1]:+.1f}] "
                f"| {c['wins']} | {_gap(c['gap_closed'])} | {e['b0']['total_mean']:.1f} |"
            )
        lines.append("")

    lines += _sensitivity_tables(experiments)

    for e in experiments:
        lines += [f"## {e['title']}", "", f"{e['seeds']} seeds.", ""]
        if e["dispatch_axis"]:
            base = e["dispatch_axis"][0]
            lines += [
                f"**Dispatch axis** (LOOK motion; baseline `{base['baseline']}` = "
                f"{base['baseline_mean']:.1f}; B0 floor = {e['b0']['total_mean']:.1f})",
                "",
                "| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |",
                "|---|---:|---:|---|---:|---:|:---:|",
            ]
            for c in e["dispatch_axis"]:
                lines.append(
                    f"| {c['policy']} | {c['mean']:.1f} ± {c['std']:.1f} | {_pct(c['delta_pct'])} "
                    f"| [{c['ci95'][0]:+.2f}, {c['ci95'][1]:+.2f}] | {c['wins']} "
                    f"| {_gap(c['gap_closed'])} | {_verdict(c['verdict'])} |"
                )
            lines.append("")
        if e.get("fairness"):
            lines += [
                "**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)",
                "",
                "| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 "
                "| Δ wait max |",
                "|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
            for f in e["fairness"]:
                deltas = [
                    f"{f[m + '_vs_cost']['delta']:+.1f} {_MARK[f[m + '_vs_cost']['verdict']]}"
                    if m + "_vs_cost" in f
                    else ""
                    for m in ("total_mean", "wait_p95", "wait_max")
                ]
                lines.append(
                    f"| {f['fairness']:g} | {f['total_mean']:.1f} | {f['wait_mean']:.1f} "
                    f"| {f['wait_p95']:.1f} | {f['wait_max']:.1f} | " + " | ".join(deltas) + " |"
                )
            lines.append("")
        if e["motion_axis"]:
            lines += [
                f"**Motion axis** (baseline `{e['motion_axis'][0]['baseline']}`)",
                "",
                "| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |",
                "|---|---|---:|---:|---|---:|:---:|",
            ]
            for c in e["motion_axis"]:
                lines.append(
                    f"| {c['dispatch']} | {c['policy']} | {c['mean']:.1f} | {_pct(c['delta_pct'])} "
                    f"| [{c['ci95'][0]:+.2f}, {c['ci95'][1]:+.2f}] | {c['wins']} "
                    f"| {_verdict(c['verdict'])} |"
                )
            lines.append("")
        lines += [
            "**All combinations** (means over seeds)",
            "",
            "| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
        for c in e["combos"]:
            lines.append(
                f"| {c['dispatch']} | {c['motion']} | {c['total_mean']:.1f} | {c['wait_mean']:.1f} "
                f"| {c['wait_p95']:.1f} | {c['wait_max']:.1f} | {c['excess_mean']:.1f} "
                f"| {c['jain_wait']:.2f} |"
            )
        lines += [
            "",
            "**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from "
            "the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / "
            "nearest car at assignment; busy = share of car time not idle)",
            "",
            "| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / "
            "nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for c in e["combos"]:
            lines.append(
                f"| {c['dispatch']} | {c['motion']} | {c['wait_mean']:.1f} "
                f"| {c['detour_mean']:.1f} | {c['away_share']:.0%} / {c['away_wait']:.0f} "
                f"| {c['idle_pick_share']:.0%} "
                f"| {c['chosen_distance']:.1f} / {c['nearest_distance']:.1f} "
                f"| {c['busy_share']:.0%} | {c['distance_per_passenger']:.1f} "
                f"| {c['riders_per_stop']:.2f} | {c['load_cv']:.2f} "
                f"| {c['full_passby_share']:.1%} |"
            )
        lines.append("")
    return "\n".join(lines)


SENSITIVITY_FIELDS = ("door_time", "placement", "rate")
_MARK = {"better": "✓", "worse": "✗", "inconclusive": "?"}


def _sensitivity_tables(experiments: Sequence[Mapping[str, Any]]) -> list[str]:
    """When experiments differ in door time, placement or load: one pivot per comparison.

    Rows are (scenario, building); columns the settings that vary; cells Δ% vs the baseline with
    ✓ better / ✗ worse / ? inconclusive. Shows at a glance which conclusions survive.
    """
    varying = [f for f in SENSITIVITY_FIELDS if len({e["key"][f] for e in experiments}) > 1]
    if not varying:
        return []

    def setting(e: Mapping[str, Any]) -> tuple:
        return tuple(e["key"][f] for f in varying)

    def label(values: tuple) -> str:
        names = {"door_time": "door {}", "placement": "{}", "rate": "{}/tick"}
        return " · ".join(names[f].format(v) for f, v in zip(varying, values, strict=True))

    columns = sorted({setting(e) for e in experiments})
    rows: dict[tuple, dict[tuple, Mapping[str, Any]]] = {}
    for e in experiments:
        k = e["key"]
        rows.setdefault((k["scenario"], k["floors"], k["cars"]), {})[setting(e)] = e

    def table(title: str, cell: Any) -> list[str]:
        out = [
            f"### {title}",
            "",
            "| scenario | building | " + " | ".join(label(c) for c in columns) + " |",
            "|---|---|" + "---:|" * len(columns),
        ]
        for (scenario, floors, cars), by_setting in rows.items():
            cells = [cell(by_setting[c]) if c in by_setting else "" for c in columns]
            out.append(f"| {scenario} | {floors} x {cars} | " + " | ".join(cells) + " |")
        return [*out, ""]

    def dispatch_cell(policy: str) -> Any:
        def cell(e: Mapping[str, Any]) -> str:
            c = next((c for c in e["dispatch_axis"] if c["policy"] == policy), None)
            return f"{c['delta_pct']:+.0%} {_MARK[c['verdict']]}" if c else ""

        return cell

    def motion_cell(dispatch: str) -> Any:
        def cell(e: Mapping[str, Any]) -> str:
            c = next((c for c in e["motion_axis"] if c["dispatch"] == dispatch), None)
            return f"{c['delta_pct']:+.0%} {_MARK[c['verdict']]}" if c else ""

        return cell

    def ranking(e: Mapping[str, Any]) -> str:
        look = sorted(
            (c for c in e["combos"] if c["motion"] == "look"), key=lambda c: c["total_mean"]
        )
        return " > ".join(c["dispatch"] for c in look)

    lines = [
        "## Sensitivity: which conclusions survive",
        "",
        f"Varying: {', '.join(varying)}. Cells: Δ mean total time vs the baseline; "
        "✓ better, ✗ worse, ? inconclusive (claim rule above).",
        "",
    ]
    policies = sorted({c["policy"] for e in experiments for c in e["dispatch_axis"]})
    for policy in policies:
        lines += table(f"`{policy}` vs `round_robin` (LOOK)", dispatch_cell(policy))
    dispatches = sorted({c["dispatch"] for e in experiments for c in e["motion_axis"]})
    for dispatch in dispatches:
        lines += table(f"LOOK vs SCAN with `{dispatch}`", motion_cell(dispatch))
    lines += table("Ranking by mean total time (LOOK, best first)", ranking)
    return lines


def _verdict(verdict: str) -> str:
    return {"better": "better ✓", "worse": "worse ✗"}.get(verdict, "-")


def _gap(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.0%}"


def write_outputs(result: BenchResult, out: str | Path, resamples: int = RESAMPLES) -> dict:
    """``raw.jsonl``, ``summary.json`` and ``summary.md`` in ``out``."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    write_raw(result, out / "raw.jsonl")
    summary = summarise(result, resamples)
    with open(out / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
        f.write("\n")
    (out / "summary.md").write_text(format_markdown(summary), encoding="utf-8")
    return summary
