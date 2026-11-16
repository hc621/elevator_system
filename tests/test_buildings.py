"""The one-at-a-time building sweep: suite, demand scaling, summary tables, report charts."""

from pathlib import Path

from elevator_sim.bench import (
    BASE_BUILDING,
    SUITES,
    Benchmark,
    Experiment,
    build_suite,
    building_families,
    one_at_a_time,
    write_outputs,
)
from elevator_sim.html_report import render_bench
from elevator_sim.model import BuildingConfig


def test_one_at_a_time_lists_each_building_once() -> None:
    buildings = one_at_a_time((30, 4, 8), (15, 30), (2, 4), (4, 8))
    assert buildings == ((30, 4, 8), (15, 4, 8), (30, 2, 8), (30, 4, 4))


def test_buildings_suite_scales_demand_with_floors() -> None:
    experiments = build_suite("buildings")
    suite = SUITES["buildings"]
    assert len(experiments) == len(suite.scenarios) * len(suite.buildings) == 4 * 11
    loads = {(e.config.floors, len(e.config.cars), e.config.cars[0].capacity): e.load
             for e in experiments}  # fmt: skip
    assert loads[BASE_BUILDING] == 1.0
    assert loads[(60, 4, 8)] == round(59 / 29, 4)  # same people per floor
    assert loads[(30, 8, 8)] == loads[(30, 4, 12)] == 1.0  # more or bigger cars: same demand
    assert all(e.motion_policies == ("look",) for e in experiments)


def small_sweep() -> list[Experiment]:
    experiments = []
    for floors, cars, capacity in one_at_a_time((10, 2, 4), (6, 10), (2, 3), (4, 6)):
        config = BuildingConfig.uniform(floors, cars, capacity, "lobby", 1)
        experiments.append(
            Experiment(
                "lunch",
                config,
                60,
                (0, 1),
                dispatch_policies=("round_robin", "cost"),
                motion_policies=("look",),
            )
        )
    return experiments


def test_summary_and_report_show_one_table_and_chart_per_factor(tmp_path: Path) -> None:
    summary = write_outputs(Benchmark(workers=1).run(small_sweep()), tmp_path, resamples=50)
    families = building_families(summary["experiments"])
    assert set(families) == {"floors", "cars", "capacity"}
    assert all(len(members) == 2 for members in families.values())
    md = (tmp_path / "summary.md").read_text()
    assert "## Building sweep: one setting at a time" in md
    for factor in ("floors", "cars", "capacity"):
        assert f"### Varying {factor}" in md
    assert "## Sensitivity" not in md  # load differs per building, not within one
    page = render_bench(summary)
    assert page.count("<h2>Varying ") == 3


def test_no_building_tables_for_a_single_building() -> None:
    assert building_families([{"key": {"floors": 30, "cars": 4, "capacity": 8}}] * 3) == {}
