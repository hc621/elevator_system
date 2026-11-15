# Elevator System Simulation

A discrete-time simulation of a destination-dispatch elevator system: passengers give their origin and destination
when they make a request, the controller assigns them to one car straight away, and the simulation moves time forward
one tick (one floor of travel) at a time.

> Work in progress. Usage, design, assumptions, results and time spent will be written here as the build goes on.

## Quick start

```bash
./scripts/install.sh        # installs uv if missing, then `uv sync` (creates .venv from uv.lock)
uv run elevator-sim examples/brief.csv --elevators 3 --floors 60 --capacity 8

uv run elevator-sim generate morning_rush --floors 30 --count 200 -o rush.csv
uv run elevator-sim rush.csv -f 30 -e 4 --algorithm cost --journal out/run.jsonl
uv run elevator-sim summarize out/run.jsonl   # rebuilds the report without re-simulating
uv run elevator-sim run --help                # all options
```

`elevator-sim` is the console script declared in `pyproject.toml` (`python -m elevator_sim` is
equivalent). Input is a CSV in the brief's format, `time,id,source,dest`.

### Outputs (in `--out`, default `out/`)

| File | Contents |
|---|---|
| `positions.jsonl` | The positions log: one JSON object per tick from t = 0, e.g. `{"t":0,"floors":[1,1,1]}` (`floors[i]` is car i's floor) |
| `passengers.json` | One record per passenger: car, requested / boarded / alighted ticks, wait, travel, total |
| `report.json` | The run's metrics (below) |

`report.json`, all times in ticks:

- `wait`, `total` (and `travel`, `excess`): per-passenger `min`, `mean`, `p50`, `p90`, `p95`, `max`, `std`
- `travels.completed`: passenger journeys completed (one passenger from source to destination)
- `cars[i].trips` and `car_trips`: a car's trip starts when it begins to move and ends when it
  reverses or goes idle; stopping to open its doors on the way does not end it
- per car: passengers carried, floors travelled, stops, peak load; plus plain-language observations

The same numbers are printed as a text summary at the end of each run.

## Assumptions and trade-offs

The brief fixes 1 tick = 1 floor, no peeking ahead, and immediate assignment of each passenger to
one car. Everything else below is a choice made here.

**Time**
- Each tick: requests made this tick are assigned first, then every car acts. A passenger who asks
  where their car is already standing boards on the same tick (wait 0).
- Positions row `t` is each car's floor at the start of tick `t`; rows run from t = 0 with no gaps.
- The run ends on the tick of the last drop-off.

**Building**
- Floors are 1..n with no basement; every car serves every floor; cars start at the lobby
  (`--placement` changes that).
- **Doors: `--door-time 1` by default.** A stop holds the car at the floor for `door_time + 1`
  ticks. The brief doesn't model doors; without a cost for stopping, sharing a car is free and
  every policy looks better than it would in a real building. `--door-time 0` gives the brief's
  pure model; the golden tests cover both.
- Boarding and alighting take no time beyond the stop itself, however many people move.

**Dispatch**
- **Assignments are fixed.** A passenger keeps their car for the whole journey; the controller
  never re-assigns. This matches destination dispatch as the brief describes it (the passenger is
  told their car) and keeps every decision explainable. The cost is that an early choice can't be
  undone when better information arrives; re-assignment is listed under improvements.
- A car stops only for its own passengers, and only people heading its way board.
- The default policy, `cost`, simulates each car's future with and without the new passenger and
  picks the car where the total time of everyone on it grows least (ties to the lowest id). It
  plans only for requests already made and is greedy: each choice is the best at that moment.

**Capacity**
- Capacity is a hard limit: the car refuses to board anyone over it, whatever the policy says.
  When people are left behind, the first assigned board first.
- The cost policy's look-ahead runs the same rule, so a car that would be full when it reaches
  you shows up as a late pickup and costs more. A hard filter ("reject any car whose projected load
  ever exceeds capacity") is simpler but turns a car down even when it frees up in time.

**Motion**
- LOOK by default: keep going while there is work ahead, reverse when there is none. SCAN (run to
  the end of the shaft before reversing) is available for comparison.

**Input**
- Requests must be in time order, on floors 1..n, with source ≠ dest and unique ids; anything else
  is reported as an error rather than guessed at.

**Metrics**
- wait = boarded − requested; travel = alighted − boarded (includes stops on the way);
  total = wait + travel. Percentiles use linear interpolation (numpy's default).
- A *travel* is one passenger's journey. A car *trip* runs from when the car starts to move until
  it reverses or goes idle; an empty move to fetch someone counts.

**Known gap: starvation.** Nothing proves that every passenger is eventually served. LOOK keeps
sweeping back in practice, but under sustained heavy load a full car could keep passing someone.
The simulator stops with an error if nobody boards or alights for a long stretch while passengers
are waiting, so this can't hang silently. A fairness rule that bounds the wait is the planned fix.

## Development

```bash
./scripts/install.sh                          # or, with uv already installed: uv sync
uv run pytest --cov
uv run ruff check . && uv run ruff format --check .
```

Python 3.10 is pinned in `.python-version` (the lowest supported version; CI tests 3.10-3.13) and uv downloads it if
needed. Dependencies are locked in `uv.lock`. Without uv: `pip install -e . && pip install --group dev` (pip >= 25.1).
