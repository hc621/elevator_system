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

## How results are measured

```bash
uv run elevator-sim bench --suite standard --seeds 20 -o results/standard   # ~30 s on 10 cores
```

This one command regenerates every number below into `results/standard/`: `raw.jsonl` (one row
per run), `summary.json`, and `summary.md` (all tables, per experiment).

- **Paired runs.** For each (scenario, building, seed) the requests are generated once from the
  seed; every dispatch × motion combination runs on exactly that list from the same start state,
  so differences come from the policy, not the random draw. A test checks the request
  fingerprints match.
- **Baselines.** **B0** is the theoretical floor (picked up at once, ride direct: total = direct
  ride time); `round_robin` is the dispatch baseline; SCAN is the motion baseline.
- **Statistics.** Per policy: mean ± std over seeds, Δ vs the baseline, wins out of N seeds, a
  paired 95% bootstrap CI of the difference (2,000 resamples, stdlib only), and *gap closed*:
  the share of the baseline's excess time (total − direct) the policy removes (0% = no better
  than round-robin, 100% = reaches B0).
- **Verdict rule.** "better" needs the CI below 0 *and* wins in ≥ 80% of seeds; "worse" the
  mirror image; anything else is inconclusive and is not claimed.
- **Standard suite.** 4 scenarios (uniform, mixed, morning rush, evening rush) × 2 buildings
  (30 floors × 4 cars, 40 floors × 6 cars), capacity 8, door_time 1, 200 requests over 800
  ticks, 20 seeds, 4 dispatch × 2 motion policies: 1,280 runs.
- Sweeps for the later studies: `--door-times 0,1,2`, `--placements lobby,spread`,
  `--rates 0.1,0.2,0.4` (requests per tick), `--skip-first N` (drop start-up passengers).

### Results: `cost` vs `round_robin` (LOOK motion, mean total time per passenger in ticks)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| uniform · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 34.4 | 20.1 | -41.6% | [-14.9, -13.7] | 20/20 | 59% | 10.3 |
| uniform · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 40.6 | 22.2 | -45.3% | [-19.3, -17.5] | 20/20 | 68% | 13.6 |
| mixed · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 38.5 | 23.1 | -40.1% | [-15.8, -15.0] | 20/20 | 63% | 14.0 |
| mixed · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 48.4 | 26.7 | -44.9% | [-22.6, -20.9] | 20/20 | 72% | 18.4 |
| morning_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 39.3 | 27.0 | -31.2% | [-13.0, -11.4] | 20/20 | 49% | 14.3 |
| morning_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 49.6 | 34.7 | -30.1% | [-15.8, -14.1] | 20/20 | 49% | 19.0 |
| evening_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 39.4 | 26.7 | -32.3% | [-13.3, -12.2] | 20/20 | 51% | 14.3 |
| evening_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 49.1 | 31.8 | -35.2% | [-18.0, -16.5] | 20/20 | 57% | 19.0 |

Read from `results/standard/summary.md` (load balance = coefficient of variation of passengers
per car, from `raw.jsonl`):
- `cost` beats round-robin in every experiment and every seed (20/20), by 30-45%, closing
  49-72% of the gap to the theoretical floor. It gains least in the rushes.
- `nearest` is 11-16% better than round-robin on uniform and mixed traffic but inconclusive in
  both rushes (-1% to +6%). There it piles passengers onto a few cars: load CV 0.33 vs 0.11-0.17
  for `cost` (30-floor building).
- `zone` is the reverse: 14-17% better on mixed traffic and in both rushes, inconclusive on
  uniform traffic, where assigning by the higher floor of each trip overloads the top zone
  (load CV 0.50).
- LOOK beats SCAN for every dispatch policy in every experiment (8-32%), with one exception:
  `cost` in the morning rush (-1% to -2%, inconclusive). A likely reason, not yet tested: nearly
  every trip starts at the lobby, so the two motion rules end up making similar sweeps.

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
