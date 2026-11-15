"""Phase 0 smoke tests: the package imports and the CLI entry point runs."""

import subprocess
import sys

import pytest

import elevator_sim
from elevator_sim.__main__ import main


def test_version_is_exposed() -> None:
    assert elevator_sim.__version__ == "0.1.0"


def test_cli_without_a_command_shows_usage(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc:
        main([])
    assert exc.value.code == 2
    assert "usage: elevator_sim" in capsys.readouterr().err


def test_cli_version_flag(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert "0.1.0" in capsys.readouterr().out


def test_module_runs_as_script() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "elevator_sim", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "0.1.0" in result.stdout
