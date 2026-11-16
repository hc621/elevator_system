"""CLI and file adapters, end to end."""

import json
from pathlib import Path

import pytest

from elevator_sim.__main__ import main
from elevator_sim.adapters import read_positions, read_requests
from elevator_sim.feed import InvalidRequest

BRIEF = "time,id,source,dest\n0,passenger1,1,51\n0,passenger2,1,37\n10,passenger3,20,1\n"


@pytest.fixture
def brief_csv(tmp_path: Path) -> Path:
    path = tmp_path / "brief.csv"
    path.write_text(BRIEF)
    return path


def test_run_writes_json_outputs_and_prints_the_summary(
    brief_csv: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    out = tmp_path / "out"
    assert (
        main(["run", str(brief_csv), "-e", "1", "-f", "60", "--door-time", "0", "-o", str(out)])
        == 0
    )
    printed = capsys.readouterr().out
    assert "Elevator simulation summary" in printed and "Observations" in printed

    lines = (out / "positions.jsonl").read_text().splitlines()
    assert json.loads(lines[0]) == {"t": 0, "floors": [1]}
    assert json.loads(lines[-1]) == {"t": 100, "floors": [1]}
    assert len(lines) == 101  # one row per tick, t = 0..100
    assert read_positions(out / "positions.jsonl")[50] == [51]  # 50 floors up from t=0

    passengers = {p["id"]: p for p in json.loads((out / "passengers.json").read_text())}
    assert passengers["passenger3"]["wait"] == 71

    report = json.loads((out / "report.json").read_text())
    assert report["travels"] == {"completed": 3, "unserved": 0}
    assert report["wait"]["max"] == 71 and report["wait"]["mean"] == pytest.approx(71 / 3, abs=1e-3)
    assert set(report["wait"]) >= {"mean", "max", "p90", "p95"}
    # Up to 51 (stopping at 37 on the way), then one sweep down through 20 to the lobby.
    assert report["cars"][0]["trips"] == 2 and report["car_trips"] == 2


def test_run_is_the_default_command(brief_csv: Path, tmp_path: Path) -> None:
    assert main([str(brief_csv), "-o", str(tmp_path / "o"), "-q", "--placement", "spread"]) == 0
    assert (tmp_path / "o" / "positions.jsonl").exists()


def test_saved_journal_reproduces_the_outputs_without_re_simulating(
    brief_csv: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    out, journal = tmp_path / "out", tmp_path / "run.jsonl"
    main([str(brief_csv), "-e", "2", "-o", str(out), "--journal", str(journal)])
    printed = capsys.readouterr().out
    assert main(["summarize", str(journal)]) == 0
    assert printed.startswith(capsys.readouterr().out)
    again = tmp_path / "again"
    assert main(["summarize", str(journal), "-o", str(again)]) == 0
    for name in ("positions.jsonl", "passengers.json", "report.json"):
        assert (again / name).read_text() == (out / name).read_text()


def test_generate_then_run(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    requests = tmp_path / "rush.csv"
    assert main(["generate", "morning_rush", "-f", "20", "-d", "100", "-o", str(requests)]) == 0
    printed = capsys.readouterr().out
    assert "Wrote" in printed and "inbound" in printed and "inter-floor" in printed
    args = [str(requests), "-f", "20", "-e", "3", "--algorithm", "zone", "--motion", "scan"]
    assert main([*args, "--placement", "1,5,10", "-o", str(tmp_path / "out"), "-q"]) == 0


def test_bad_input_is_reported_with_exit_code_2(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    bad = tmp_path / "bad.csv"
    bad.write_text("time,id,source,dest\n0,a,1,99\n")
    assert main([str(bad), "-f", "10", "-o", str(tmp_path / "out")]) == 2
    assert "dest floor 99" in capsys.readouterr().err


def test_bad_placement_is_a_usage_error(brief_csv: Path) -> None:
    with pytest.raises(SystemExit):
        main([str(brief_csv), "--placement", "middle"])


def test_read_requests_skips_blank_lines_and_reports_bad_rows(tmp_path: Path) -> None:
    good = tmp_path / "good.csv"
    good.write_text("0, a ,1,5\n\n3,b,5,1\n")  # no header, spaces, blank line
    assert [(r.time, r.id) for r in read_requests(good)] == [(0, "a"), (3, "b")]

    for content, message in [("0,a,1\n", "4 fields"), ("x,a,1,2\n", "integers")]:
        bad = tmp_path / "bad.csv"
        bad.write_text(content)
        with pytest.raises(InvalidRequest, match=message):
            list(read_requests(bad))
