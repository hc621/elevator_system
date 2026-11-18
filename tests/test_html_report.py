"""Phase 4: the self-contained HTML report."""

import json
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest
from helpers import building, reqs, run

from elevator_sim.__main__ import main
from elevator_sim.bench import Benchmark, SuiteOptions, build_suite, summarise
from elevator_sim.html_report import _bar, nice_ticks, render_bench, render_run, segmented_bar

REPO = Path(__file__).resolve().parents[1]


class _Checker(HTMLParser):
    """Collects tags and fails on any reference to an external resource."""

    def __init__(self) -> None:
        super().__init__()
        self.tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag)
        for name, value in attrs:
            assert name not in ("src", "href"), f"external reference: <{tag} {name}={value}>"


def parse(page: str) -> _Checker:
    checker = _Checker()
    checker.feed(page)
    return checker


def test_run_report_is_self_contained_and_has_every_section() -> None:
    requests = reqs((0, "a", 1, 9), (0, "b", 1, 5), (3, "c", 8, 1), (4, "d", 2, 7))
    journal, report = run(requests, building(floors=10, cars=2, door_time=1))
    page = render_run(journal, report)
    tags = parse(page).tags
    assert page.startswith("<!doctype html>") and "</html>" in page
    assert "http://" not in page and "https://" not in page  # opens offline
    for title in ("Time-space diagram", "Wait time distribution", "Wait by trip type",
                  "Why: the assigned car",
                  "Load per car", "Observations", "Passengers"):  # fmt: skip
        assert title in page
    # One line per car in the time-space diagram plus one for the wait distribution.
    assert page.count("<polyline") == 2 + 1
    assert tags.count("details") >= 5  # every chart has a table view
    assert "prefers-color-scheme: dark" in page and 'data-theme="dark"' in page


def test_text_from_the_data_is_escaped() -> None:
    requests = reqs((0, "<script>alert(1)</script>", 1, 5))
    journal, report = run(requests, building(floors=10))
    page = render_run(journal, report)
    assert "<script>alert(1)</script>" not in page
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in page
    # JSON payloads can't close their own <script> element either.
    for payload in re.findall(r'<script type="application/json"[^>]*>(.*?)</script>', page, re.S):
        assert "</" not in payload


def test_bench_report_has_a_selector_and_one_section_per_experiment() -> None:
    options = SuiteOptions(
        seeds=2, scenarios=("quiet",), dispatch=("round_robin", "cost"), fairness=(0, 1)
    )
    experiments = [type(e)(**{**e.__dict__, "duration": 60}) for e in build_suite("quick", options)]
    summary = summarise(Benchmark(workers=1).run(experiments), resamples=50)
    page = render_bench(summary)
    parse(page)
    assert page.count('<section data-exp="') == len(experiments)
    assert page.count("<option ") == len(experiments)
    for title in ("cost vs round_robin across experiments", "Mean total time per passenger",
                  "B0 floor", "Wait time: average and tail", "Why: assigned to a car moving away",
                  "Wait by trip type (LOOK)", "Fairness frontier"):  # fmt: skip
        assert title in page


def test_committed_reports_match_their_summaries() -> None:
    """results/<study>/report.html must be exactly what its summary.json renders to (no drift)."""
    for folder in ("standard", "sensitivity", "fairness", "buildings", "parking"):
        summary = REPO / "results" / folder / "summary.json"
        committed = REPO / "results" / folder / "report.html"
        assert committed.exists(), f"missing {committed}"
        page = render_bench(json.loads(summary.read_text()))
        assert committed.read_text() == page, f"{committed} is stale: re-run `elevator-sim report`"


def test_rendering_is_deterministic() -> None:
    summary = json.loads((REPO / "results" / "standard" / "summary.json").read_text())
    assert render_bench(summary) == render_bench(summary)


def test_report_renders_the_committed_benchmark_summaries() -> None:
    for folder in ("standard", "sensitivity", "fairness"):
        path = REPO / "results" / folder / "summary.json"
        if path.exists():
            page = render_bench(json.loads(path.read_text()))
            parse(page)
            assert page.count("<section data-exp=") == len(
                json.loads(path.read_text())["experiments"]
            )


def test_chart_helpers() -> None:
    assert nice_ticks(0, 34) == [0, 10, 20, 30, 40]
    assert nice_ticks(0, 1) == [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert nice_ticks(5, 5) == [5, 5.2, 5.4, 5.6, 5.8, 6.0]
    assert _bar(10, 10, 0, 14) == ""  # zero-length bar draws nothing
    assert "A4,4 0 0 1" in _bar(0, 50, 0, 14)  # rounded at the data end (right)
    assert "A4,4 0 0 0" in _bar(50, 0, 0, 14)  # negative bar: rounded at the left
    seg = segmented_bar([("a", 3, "var(--s1)"), ("b", 0, "var(--s2)"), ("c", 1, "var(--s4)")], "x")
    assert seg.count("flex:") == 2  # the zero part draws no block
    assert "75%" in seg and "color:#0b0b0b" in seg  # dark text on yellow


def test_cli_report_and_run_html(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    csv = tmp_path / "r.csv"
    csv.write_text("time,id,source,dest\n0,a,1,9\n2,b,8,1\n")
    out = tmp_path / "out"
    assert main([str(csv), "-f", "10", "-e", "2", "--html", "-q", "-o", str(out),
                 "--journal", str(out / "run.jsonl")]) == 0  # fmt: skip
    assert (out / "report.html").read_text().startswith("<!doctype html>")
    assert main(["report", str(out / "run.jsonl"), "-o", str(tmp_path / "r.html")]) == 0
    assert "Time-space diagram" in (tmp_path / "r.html").read_text()
    standard = REPO / "results" / "standard"
    assert main(["report", str(standard), "-o", str(tmp_path / "b.html")]) == 0
    assert main(["report", str(standard / "summary.json"), "-o", str(tmp_path / "c.html")]) == 0
    assert "Elevator benchmark" in (tmp_path / "b.html").read_text()
    assert "Wrote" in capsys.readouterr().out
