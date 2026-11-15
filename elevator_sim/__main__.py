"""Command-line entry point: ``python -m elevator_sim``.

Phase 0 placeholder; the real CLI is wired in Phase 1a (task 1a.10).
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from elevator_sim import __version__


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="elevator_sim", description=__doc__)
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.parse_args(argv)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
