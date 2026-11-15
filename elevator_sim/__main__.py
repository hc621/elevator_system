"""Command-line entry point.

python -m elevator_sim run requests.csv --elevators 3 --floors 60 --capacity 8
python -m elevator_sim requests.csv ...            # "run" is the default command
python -m elevator_sim summarize out/journal.jsonl # rebuild the summary from a saved journal
python -m elevator_sim generate morning_rush --floors 30 --count 200 -o rush.csv
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from elevator_sim import __version__
from elevator_sim.adapters import (
    format_summary,
    read_requests,
    write_passengers,
    write_positions,
    write_requests,
)
from elevator_sim.dispatch import DISPATCH_POLICIES, make_dispatch
from elevator_sim.dispatcher import NoEligibleCar
from elevator_sim.feed import InvalidRequest, IteratorFeed, SimulationStalled
from elevator_sim.journal import Journal
from elevator_sim.model import PLACEMENTS, BuildingConfig, Floor
from elevator_sim.motion import MOTION_POLICIES, make_motion
from elevator_sim.report import aggregate
from elevator_sim.scenarios import SCENARIOS, generate
from elevator_sim.simulator import simulate

COMMANDS = ("run", "summarize", "generate")


def _placement(text: str) -> str | tuple[Floor, ...]:
    if text in PLACEMENTS:
        return text
    try:
        return tuple(int(part) for part in text.split(","))
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"expected {' or '.join(PLACEMENTS)} or a comma-separated list of floors"
        ) from None


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="elevator_sim", description="Elevator system simulation.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="simulate a request file")
    run.add_argument("input", type=Path, help="CSV with columns time,id,source,dest")
    run.add_argument("-e", "--elevators", type=int, default=3, help="number of cars (default 3)")
    run.add_argument("-f", "--floors", type=int, default=60, help="number of floors (default 60)")
    run.add_argument("-c", "--capacity", type=int, default=8, help="passengers per car (default 8)")
    run.add_argument(
        "--door-time", type=int, default=1, help="extra ticks per stop with doors open (default 1)"
    )
    run.add_argument(
        "--placement",
        type=_placement,
        default="lobby",
        help="start floors: lobby, spread, or e.g. 1,20,40 (default lobby)",
    )
    run.add_argument("--algorithm", choices=sorted(DISPATCH_POLICIES), default="cost")
    run.add_argument("--motion", choices=sorted(MOTION_POLICIES), default="look")
    run.add_argument("-o", "--out", type=Path, default=Path("out"), help="output directory")
    run.add_argument("--journal", type=Path, help="also save the event journal (JSONL) here")
    run.add_argument(
        "--journal-routes", action="store_true", help="record every car's route each tick"
    )
    run.add_argument("--max-ticks", type=int, help="fail if the run goes beyond this tick")
    run.add_argument("-q", "--quiet", action="store_true", help="don't print the summary")

    summarize = sub.add_parser("summarize", help="rebuild the summary from a saved journal")
    summarize.add_argument("journal", type=Path)
    summarize.add_argument("-o", "--out", type=Path, help="also write summary.txt etc. here")

    gen = sub.add_parser("generate", help="write a seeded random request file")
    gen.add_argument("scenario", choices=sorted(SCENARIOS))
    gen.add_argument("-f", "--floors", type=int, default=30)
    gen.add_argument("-n", "--count", type=int, default=100)
    gen.add_argument("-d", "--duration", type=int, default=300, help="arrival window in ticks")
    gen.add_argument("-s", "--seed", type=int, default=0)
    gen.add_argument("-o", "--output", type=Path, required=True)
    return parser


def _write_outputs(journal: Journal, out: Path) -> str:
    report = aggregate(journal)
    out.mkdir(parents=True, exist_ok=True)
    write_positions(journal, out / "positions.csv")
    write_passengers(report, out / "passengers.csv")
    summary = format_summary(report)
    (out / "summary.txt").write_text(summary, encoding="utf-8")
    return summary


def _run(args: argparse.Namespace) -> int:
    config = BuildingConfig.uniform(
        args.floors, args.elevators, args.capacity, args.placement, args.door_time
    )
    journal = simulate(
        config,
        IteratorFeed(read_requests(args.input)),
        make_dispatch(args.algorithm),
        make_motion(args.motion),
        journal_routes=args.journal_routes,
        max_ticks=args.max_ticks,
    )
    summary = _write_outputs(journal, args.out)
    if args.journal:
        args.journal.parent.mkdir(parents=True, exist_ok=True)
        journal.to_jsonl(args.journal)
    if not args.quiet:
        print(summary, end="")
        print(f"\nWrote {args.out}/positions.csv, passengers.csv, summary.txt")
    return 0


def _summarize(args: argparse.Namespace) -> int:
    journal = Journal.from_jsonl(args.journal)
    if args.out:
        print(_write_outputs(journal, args.out), end="")
    else:
        print(format_summary(aggregate(journal)), end="")
    return 0


def _generate(args: argparse.Namespace) -> int:
    requests = generate(args.scenario, args.floors, args.count, args.duration, args.seed)
    write_requests(requests, args.output)
    print(f"Wrote {len(requests)} requests to {args.output}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args_list = list(sys.argv[1:] if argv is None else argv)
    if args_list and args_list[0] not in COMMANDS and not args_list[0].startswith("-"):
        args_list.insert(0, "run")
    args = _parser().parse_args(args_list)
    handlers = {"run": _run, "summarize": _summarize, "generate": _generate}
    try:
        return handlers[args.command](args)
    except (InvalidRequest, NoEligibleCar, SimulationStalled, ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
