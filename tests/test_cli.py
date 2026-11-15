"""CLI and CSV adapters, end to end."""

import csv
from pathlib import Path

import pytest

from elevator_sim.__main__ import main
from elevator_sim.adapters import read_requests
from elevator_sim.feed import InvalidRequest

BRIEF = "time,id,source,dest\n0,passenger1,1,51\n0,passenger2,1,37\n10,passenger3,20,1\n"


@pytest.fixture
def brief_csv(tmp_path: Path) -> Path:
    path = tmp_path / "brief.csv"
    path.write_text(BRIEF)
    return path


def test_run_writes_positions_passengers_and_summary(
    brief_csv: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    out = tmp_path / "out"
    assert (
        main(["run", str(brief_csv), "-e", "1", "-f", "60", "--door-time", "0", "-o", str(out)])
        == 0
    )
    printed = capsys.readouterr().out
    assert "Elevator simulation summary" in printed and "Observations" in printed

    with open(out / "positions.csv") as f:
        rows = list(csv.reader(f))
    assert rows[0] == ["tick", "car_0"]
    assert rows[1] == ["0", "1"] and rows[-1] == ["100", "1"]
    assert len(rows) == 1 + 101

    with open(out / "passengers.csv") as f:
        passengers = {r["id"]: r for r in csv.DictReader(f)}
    assert passengers["passenger3"]["wait"] == "71"
    assert (out / "summary.txt").read_text() in printed


def test_run_is_the_default_command(brief_csv: Path, tmp_path: Path) -> None:
    assert main([str(brief_csv), "-o", str(tmp_path / "o"), "-q", "--placement", "spread"]) == 0
    assert (tmp_path / "o" / "positions.csv").exists()


def test_saved_journal_reproduces_the_summary_without_re_simulating(
    brief_csv: Path, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    out, journal = tmp_path / "out", tmp_path / "run.jsonl"
    main([str(brief_csv), "-e", "2", "-o", str(out), "--journal", str(journal), "-q"])
    capsys.readouterr()
    assert main(["summarize", str(journal)]) == 0
    assert capsys.readouterr().out == (out / "summary.txt").read_text()
    assert main(["summarize", str(journal), "-o", str(tmp_path / "again")]) == 0
    assert (tmp_path / "again" / "positions.csv").read_text() == (out / "positions.csv").read_text()


def test_generate_then_run(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    requests = tmp_path / "rush.csv"
    assert main(["generate", "morning_rush", "-f", "20", "-n", "50", "-o", str(requests)]) == 0
    assert "Wrote 50 requests" in capsys.readouterr().out
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
