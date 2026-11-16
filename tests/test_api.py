"""The brief's function entry point and the CSV positions log."""

import csv
from pathlib import Path

import pytest

from elevator_sim import run_requests
from elevator_sim.__main__ import main
from elevator_sim.feed import InvalidRequest
from elevator_sim.model import Request

BRIEF = [(0, "passenger1", 1, 51), (0, "passenger2", 1, 37), (10, "passenger3", 20, 1)]


def test_run_requests_takes_the_brief_rows_and_matches_the_golden_timeline() -> None:
    result = run_requests(BRIEF, elevators=1, floors=60, door_time=0)
    times = {r.id: (r.boarded, r.alighted) for r in result.report.passengers}
    assert times["passenger3"] == (81, 100)  # same as test_brief_example_one_car_door_time_0
    assert result.positions[0] == [1] and len(result.positions) == 101
    assert result.report.wait.max == 71


def test_run_requests_accepts_request_objects_and_options() -> None:
    requests = [Request(*row) for row in BRIEF]
    result = run_requests(requests, elevators=3, algorithm="round_robin", parking="lobby")
    assert {r.car for r in result.report.passengers} == {0, 1, 2}
    assert result.report.dispatch == "round_robin" and result.report.parking == "lobby"
    assert len(result.positions[0]) == 3


def test_run_requests_validates_like_the_cli() -> None:
    with pytest.raises(InvalidRequest, match="dest floor 99"):
        run_requests([(0, "a", 1, 99)], floors=10)


def test_cli_also_writes_positions_csv(tmp_path: Path) -> None:
    rows = "time,id,source,dest\n" + "".join(f"{t},{i},{s},{d}\n" for t, i, s, d in BRIEF)
    (tmp_path / "brief.csv").write_text(rows)
    out = tmp_path / "out"
    assert main([str(tmp_path / "brief.csv"), "-e", "2", "-o", str(out), "-q"]) == 0
    with open(out / "positions.csv") as f:
        table = list(csv.reader(f))
    assert table[0] == ["t", "car_0", "car_1"] and table[1] == ["0", "1", "1"]
    assert len(table) - 1 == len((out / "positions.jsonl").read_text().splitlines())
