# Elevator System Simulation

A discrete-time simulation of a destination-dispatch elevator system: passengers give their origin and destination
when they make a request, the controller assigns them to one car straight away, and the simulation moves time forward
one tick (one floor of travel) at a time.

> Work in progress. Usage, design, assumptions, results and time spent will be written here as the build goes on.

## Quick start

```bash
./scripts/install.sh        # installs uv if missing, then `uv sync` (creates .venv from uv.lock)
source .venv/bin/activate   # or prefix each command with `uv run`
python -m elevator_sim examples/brief.csv --elevators 3 --floors 60 --capacity 8
# -> out/positions.csv (one row per tick from t=0), out/passengers.csv, out/summary.txt

python -m elevator_sim generate morning_rush --floors 30 --count 200 -o rush.csv
python -m elevator_sim rush.csv -f 30 -e 4 --algorithm cost --journal out/run.jsonl
python -m elevator_sim summarize out/run.jsonl   # rebuilds the summary without re-simulating
```

## Development

```bash
./scripts/install.sh                          # or, with uv already installed: uv sync
uv run pytest --cov
uv run ruff check . && uv run ruff format --check .
```

Python 3.10 is pinned in `.python-version` (the lowest supported version; CI tests 3.10-3.13) and uv downloads it if
needed. Dependencies are locked in `uv.lock`. Without uv: `pip install -e . && pip install --group dev` (pip >= 25.1).
