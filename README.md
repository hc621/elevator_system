# Elevator System Simulation

A discrete-time simulation of a destination-dispatch elevator system: passengers give their origin and destination
when they make a request, the controller assigns them to one car straight away, and the simulation moves time forward
one tick (one floor of travel) at a time.

It reads requests in the brief's format (`time,id,source,dest`), never looks ahead of the current
tick, and writes the brief's two outputs: a **positions log** (every car's floor at every tick from
t = 0) and **passenger statistics** (min / max / average wait and total time, plus observations).
On top of that it compares four dispatch policies and two motion rules on realistic office-building
traffic, explains *why* one policy beats another, and renders the results as an HTML report.

**Contents:** [Quick start](#quick-start) · [Findings at a glance](#findings-at-a-glance) ·
[How it works](#how-it-works-who-decides-what) · [Code layout](#code-layout) ·
[Metrics](#metrics-what-we-measure-and-why) ·
[Traffic scenarios](#traffic-scenarios-a-business-building) ·
[How results are measured](#how-results-are-measured) ·
[Sensitivity](#sensitivity-stop-time-and-start-position) ·
[Building sweep](#building-sweep-floors-cars-and-capacity) ·
[Parking](#parking-idle-cars) · [Fairness](#fairness-vs-efficiency) · [Visual report](#visual-report) ·
[Reproduce every result](#reproduce-every-result) · [Testing](#testing) ·
[Assumptions and trade-offs](#assumptions-and-trade-offs) ·
[What I'd improve](#what-id-improve-with-more-time) · [How I used AI](#how-i-used-ai) ·
[Time spent](#time-spent) · [Development](#development) ·
Presentation outline: [`docs/presentation.md`](docs/presentation.md)

## Quick start

```bash
./scripts/install.sh        # installs uv if missing, then `uv sync` (creates .venv from uv.lock)
uv run elevator-sim examples/brief.csv --elevators 3 --floors 60 --capacity 8

uv run elevator-sim generate morning_rush --floors 30 --duration 800 -o rush.csv
uv run elevator-sim rush.csv -f 30 -e 4 --algorithm cost --journal out/run.jsonl
uv run elevator-sim summarize out/run.jsonl   # rebuilds the report without re-simulating
uv run elevator-sim rush.csv -f 30 -e 4 --html  # also writes out/report.html (open it)
uv run elevator-sim report results/standard -o out/bench.html   # benchmark report
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

`report.json` holds the passenger time distributions, completed travels, per-car stats, root-cause
diagnostics and plain-language observations. Every field, and why it is measured, is listed under
[Metrics](#metrics-what-we-measure-and-why). The same numbers are printed as a text summary at the end of each run.

## Findings at a glance

All numbers are means over 20 paired seeds; "better" means the 95% CI of the difference excludes 0
and at least 80% of seeds agree. Details and tables are in the sections linked.

- **`cost` dispatch is the best policy**: 31-47% lower mean total time per passenger than
  round-robin in all 8 standard experiments (better in 20 of 20 seeds every time), closing 52-73%
  of the gap to the theoretical floor. It stays best in all 48 door-time / start-position
  settings. [Results](#results-cost-vs-round_robin-look-motion-mean-total-time-per-passenger-in-ticks)
- **Why round-robin loses**: it ignores where cars are going, so in busy periods 46-50% of its
  passengers get a car that is moving away from them; the empty travel keeps its cars 95-98% busy,
  at saturation. All of the difference is waiting time, not ride time.
  [Root cause](#why-cost-wins-root-cause-look-motion-from-the-diagnostics-columns-in-summarymd)
- **`nearest` backfires in the rushes**: it piles passengers onto the car near the lobby, so 6-12%
  of them watch their own car pass full; it is significantly worse than round-robin in the morning
  rush and gets worse as stops get longer. [Sensitivity](#sensitivity-stop-time-and-start-position)
- **`zone` is a strong simple policy for rush hours** (19-20% better than round-robin), and in an
  overloaded morning rush (45-60 floors on 4 cars) it even beats `cost`: banding cars by destination
  shortens their round trips. [Building sweep](#building-sweep-floors-cars-and-capacity)
- **LOOK beats SCAN** almost everywhere (up to 29% with `cost` in the evening rush).
- **The building matters more than the algorithm at the extremes**: 4 cars can't serve a 45- or
  60-floor office at rush hour, more cars help with diminishing returns past 6, and capacity only
  matters when it is tight (at capacity 4, `cost`'s capacity-aware projection cuts full-car
  pass-bys to 7-21% vs 20-39% for round-robin).
- **Parking idle cars helps when it matches the traffic**: back to the lobby before the morning
  rush (up to 17% better), spread out when it's quiet (5.5%); a demand-following policy is never
  worse and needs no knowledge of the scenario, at the price of extra travel.
  [Parking](#parking-idle-cars)
- **Fairness costs nothing measurable**: a fairness weight on `cost` trims the worst rush-hour waits
  by 7-10 ticks under heavy load with no significant change in mean total time; there is no
  per-passenger guarantee. [Fairness](#fairness-vs-efficiency)

## How it works: who decides what

Two separate decisions, made by different parts of the code at different times:

| | Dispatch policy: *which car?* | Motion policy: *how does a car move?* |
|---|---|---|
| Asked by | the `Dispatcher` | each `Car`, about itself |
| When | once per passenger, on the tick they ask | every tick, for every car |
| Sees | every car (read-only views) | its own car: floor, direction, load, its own passengers |
| Options | `round_robin`, `nearest`, `zone`, `cost` (default) | `look` (default), `scan` |
| Answer | a car id; the assignment is final | move up / down, open doors, or idle; and who boards |

Each tick: new requests are assigned (dispatch), then every car acts (motion), then positions are
logged and moving cars advance one floor. The `Car` enforces the rules (capacity, door timing)
whatever a policy says, and the `Dispatcher` is the only code that changes a car.

- **`round_robin`**: cars in turn; looks at nothing. **`nearest`**: the car closest to the
  passenger's floor, whatever it is doing. **`zone`**: each car owns a band of floors; a trip goes
  to the owner of its upper floor.
- **`cost`**: for each car, simulate its future with and without the new passenger (`project()`
  runs the car's own motion rules, capacity check and door timing on a copy) and pick the car where
  the total time of everyone assigned to it grows least: the newcomer's wait and ride plus any
  delay to passengers already assigned. Ties go to the lowest id. An optional fairness weight
  (`--fairness`, `cost:<α>` in the benchmark) adds α × the increase in the sum of squared waits;
  see [Fairness vs efficiency](#fairness-vs-efficiency).
- **LOOK**: keep going while any of this car's passengers need a floor ahead; reverse when nothing
  lies ahead; idle when there is no work. **SCAN**: the same, but always run to the end of the
  shaft before reversing.

## Code layout

```
elevator_sim/
  model.py        value types: Request, CarSpec, BuildingConfig (floors, cars, door_time)
  feed.py         request feed (lazy, validated, never ahead of the clock) and the Clock
  motion.py       motion policies: LOOK, SCAN (where a car goes, when it stops, who boards)
  car.py          the Car state machine (doors, capacity) and project(), the only look-ahead
  dispatch.py     dispatch policies: cost (+ fairness), nearest, zone, round_robin
  parking.py      parking policies: stay, lobby, spread, demand (where idle cars wait)
  dispatcher.py   per tick: assign new requests, step every car; the only code that changes cars
  simulator.py    Simulator (one tick at a time) and simulate() (a whole run)
  events.py       the event types; journal.py: the append-only journal (save / load as JSONL)
  report.py       aggregate(): journal -> RunReport (stats, per car, by trip type, diagnostics)
  adapters.py     files at the edge: CSV in; positions / passengers / report JSON out; summary
  scenarios.py    business-building traffic: three Poisson streams, generated once per seed
  bench.py        the evaluation harness: paired runs, baselines, bootstrap CIs, suites
  html_report.py  the self-contained HTML report
  __main__.py     the CLI: run, summarize, generate, bench, report
scripts/          install.sh (uv setup); readme_tables.py (the README's tables from results/)
tests/            246 tests (unit, scenario, golden, invariant, benchmark, report, CLI)
results/          committed benchmark summaries (standard, sensitivity, fairness, buildings, parking)
```

Information flows one way: feed → clock → dispatcher → cars → journal → report. Policies get
read-only views and return an answer; they can't move a car or see the future. Every output is
computed from the journal, so a saved run can be re-analysed without simulating again.

## Metrics: what we measure and why

All times are in ticks (1 tick = 1 floor of travel). Per passenger:

```
requested --wait--> boarded --travel--> alighted
|<--------------- total = wait + travel ------>|
direct = |dest - source|      excess = total - direct      detour = travel - direct
```

### Per run (`report.json`, `passengers.json`, the printed summary)

| Metric | Definition | Why we measure it |
|---|---|---|
| `wait` min / mean / p50 / p90 / p95 / max / std | boarded − requested, over passengers | The brief asks for min / max / average; the percentiles show the tail (how bad it gets for the unlucky), which a mean hides |
| `total` (same statistics) | alighted − requested | The brief's objective: minimise total time per passenger |
| `travel` | alighted − boarded | Ride time; with `wait` it shows where the total goes |
| `excess` | total − direct | Time the system adds beyond an instant, direct ride; the part a better algorithm can remove |
| `travels.completed` / `unserved` | passenger journeys delivered / not delivered | The brief's first objective is to serve everyone; `unserved` must be 0 |
| `ticks`, `last_dropoff` | rows in the positions log; tick of the last drop-off | When the run ended; the positions log has one row per tick from t = 0 |
| `by_trip` (inbound / outbound / inter_floor): `count`, `wait`, `total` | the same statistics per trip type: from the lobby, to the lobby, between upper floors | The three traffic categories of the scenario model: shows who pays in each scenario (e.g. inbound passengers in the morning rush) |
| per car: `trips` (all cars: `car_trips`) | moves from starting to move until reversing or going idle | How often each car sets off: many short trips vs a few long sweeps |
| per car: `passengers`, `distance`, `stops`, `peak_load` | delivered; floors travelled; door openings; most on board at once | Load balance between cars, wasted travel, and whether a car ever filled up |
| `observations` | short notes generated from the numbers | The brief asks for notable observations about the distributions and system behaviour |

### Diagnostics: why the times are what they are (`report.json` → `diagnostics`)

These were added after the first benchmark to make the root cause of each result visible in every
report (see [Why `cost` wins](#why-cost-wins-root-cause-look-motion-from-the-diagnostics-columns-in-summarymd)).

| Metric | Definition | Why we measure it |
|---|---|---|
| `detour` | travel − direct | Separates "waited long" from "rode long": shows that dispatch quality appears as wait, not ride time |
| `assigned_car_state` share / mean wait (bench columns `away_share`, `away_wait`, `idle_pick_share`) | state of the chosen car when the passenger was assigned: idle; on the way (ahead, same direction); ahead but heading the other way; moving away | The main root cause: a passenger given a car moving away waits for it to finish its sweep and come back |
| `chosen_car_distance` vs `nearest_car_distance` | floors from the chosen car / the closest car to the pickup, at assignment | Whether the policy looks at where cars are; together with the state above, shows that direction matters more than distance |
| `busy_share` | share of car time not idle with doors closed | How close the building runs to saturation: near 100% means every new request queues behind existing work |
| `distance_per_passenger` | floors travelled by all cars / passengers served | Wasted (mostly empty) travel |
| `riders_per_stop` | (boardings + alightings) per door opening | Whether a policy groups passengers into shared stops |
| `full_passby_share` | passengers whose own car stood at their floor, heading their way, full | Whether capacity actually bound in this run; "a car reached capacity" alone doesn't show that |

### Benchmark only (`elevator-sim bench`: `raw.jsonl`, `summary.json`, `summary.md`)

Each row of `raw.jsonl` is one run. It records the experiment (`scenario`, `floors`, `cars`,
`capacity`, `door_time`, `placement`, `duration`, `load`, `rate`, `skip_first`, `seed`,
`dispatch`, `motion`), the per-passenger metrics above flattened into columns (`wait_mean`,
`wait_p50`, `wait_p90`, `wait_p95`, `wait_max`, `total_mean`, `total_p95`, `total_max`,
`excess_mean`), the diagnostics (`detour_mean`, `away_share`, `away_wait`, `idle_pick_share`,
`chosen_distance`, `nearest_distance`, `busy_share`, `distance_per_passenger`, `riders_per_stop`,
`full_passby_share`), per trip type (`inbound_count`, `inbound_wait_mean`, `inbound_wait_p95`,
`inbound_wait_max`, `inbound_total_mean`; likewise `outbound_count`, `outbound_wait_mean`,
`outbound_wait_p95`, `outbound_wait_max`, `outbound_total_mean`, `inter_floor_count`,
`inter_floor_wait_mean`, `inter_floor_wait_p95`, `inter_floor_wait_max`, `inter_floor_total_mean`),
per-run totals (`passengers`, `unserved`, `distance`, `trips`), plus:

| Metric | Definition | Why we measure it |
|---|---|---|
| `direct_mean` → **B0** | mean direct ride time | The theoretical floor (picked up at once, ride direct): no policy can beat it, so it shows the headroom left |
| `stretch_mean` | mean of total / direct | Scale-free (1.0 is perfect), so short and long trips count alike |
| `zero_wait_share` | share of passengers who boarded on the tick they asked | How often service feels instant |
| `jain_wait` | Jain's index (Σw)² / (n·Σw²) on waits | How *equal* waits are. Reported, but not used to judge fairness: it rewards uniformly long waits (round-robin scores best on it with the worst tails), so fairness is judged on p95 and max wait |
| `load_cv` | coefficient of variation of passengers per car | Load balance: detects policies that pile passengers onto a few cars |
| `makespan` | tick of the last drop-off | Throughput for a fixed set of requests |
| `requests`, `start_floors` | fingerprint of the request list; where cars started | Proof that every policy in a (scenario, seed) ran on identical inputs |

Comparisons in `summary.json` / `summary.md`, per experiment:

| Metric | Definition | Why |
|---|---|---|
| mean ± std | over seeds | Typical result and spread |
| Δ, Δ% | mean(policy − baseline), paired by seed | Size of the effect |
| wins / losses | seeds where the policy is strictly better / worse | Consistency: an average can hide a policy that wins big once and loses often |
| 95% CI of Δ | paired percentile bootstrap, 2,000 resamples | Uncertainty: is the effect distinguishable from 0? |
| gap closed | (excess_baseline − excess_policy) / excess_baseline | Share of the removable time a policy removes: 0% = no better than the baseline, 100% = reaches B0 |
| verdict | better / worse / inconclusive | A claim needs the CI to exclude 0 *and* ≥ 80% of seeds to agree; only claimed results go in this README |
| parking vs stay | for each parking policy: Δ mean total, mean wait, max wait and floors travelled per passenger vs `stay`, paired by seed | What parking buys (shorter waits) and what it costs (extra travel) |
| fairness frontier | for each `cost:<α>`: mean total, mean / p95 / max wait, and Δ total, Δ p95, Δ max vs plain `cost` with verdicts | Shows what the fairness weight buys (shorter tails) and what it costs (mean total time) |

## Traffic scenarios: a business building

The simulation models an **office building**: people arrive in the morning, leave in the evening,
go out and come back at lunch, and move between floors all day. Requests come from three
independent streams, each a **Poisson process** (the number of new requests in a tick is
Poisson-distributed, so arrivals are random and bursty, not evenly spaced):

1. **inbound**: lobby (floor 1) → a random upper floor
2. **outbound**: a random upper floor → lobby
3. **inter-floor**: a random upper floor → a different upper floor, up or down

Inter-floor traffic runs at the same steady rate in every scenario; the scenarios differ in the
inbound and outbound rates (requests per tick):

| scenario | inbound | outbound | inter-floor | total | what it is |
|---|---:|---:|---:|---:|---|
| `quiet` | 0.03 | 0.03 | 0.06 | 0.12 | mid-morning / mid-afternoon: mostly people moving between floors |
| `morning_rush` | **0.30** | 0.03 | 0.06 | 0.39 | arrivals: heavy inbound (up-peak) |
| `lunch` | 0.15 | 0.15 | 0.06 | 0.36 | going out and coming back (two-way) |
| `evening_rush` | 0.03 | **0.30** | 0.06 | 0.39 | departures: heavy outbound (down-peak) |

- **Generated once, shared by every scenario.** For a seed, each stream is drawn once at a cap
  rate and every candidate request gets a random number u; a scenario keeps a candidate when
  u < its rate / cap. Thinning a Poisson process this way gives a Poisson process at the lower
  rate, so for one seed the inter-floor passengers are *identical* in every scenario and the
  morning rush's inbound passengers include the quiet scenario's: the only difference between
  scenarios is the rush stream. Ids name the stream (`in17`, `out3`, `fl8`), so the same
  passenger has the same id across scenarios.
- **Load.** `--load` / `--loads` multiplies every rate (the fairness study uses 1.5).
- The rates were calibrated so the rushes are heavy but stable: at load 1 `cost`, `zone` and
  round-robin finish within 120 ticks of the arrival window closing (`nearest`, which piles up in
  the rushes, within 260), and the rushes are busy enough that a full car passing someone happens
  (under `nearest`, 6-12% of passengers).
- **Other buildings differ.** A residential building reverses the rushes (outbound in the
  morning, inbound in the evening) and a hotel has its own peaks; only the business pattern is
  modelled. With the streams separated, another building type is a different rate table.

```bash
uv run elevator-sim generate morning_rush --floors 30 --duration 800 --seed 1 -o rush.csv
uv run elevator-sim generate lunch --floors 30 --load 1.5 -o lunch_heavy.csv
```

## How results are measured

```bash
uv run elevator-sim bench --suite standard --seeds 20 -o results/standard   # ~40 s on 10 cores
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
- **Standard suite.** The 4 business-building scenarios × 2 buildings (30 floors × 4 cars,
  40 floors × 6 cars), capacity 8, door_time 1, an 800-tick arrival window at load 1 (75-120
  requests per run in the quiet scenario, 250-350 in the busy ones), 20 seeds, 4 dispatch × 2
  motion policies: 1,280 runs.
- Sweeps for the later studies: `--door-times 0,1,2`, `--placements lobby,spread`,
  `--loads 1,1.5` (multiples of the scenario rates), `--skip-first N` (drop start-up
  passengers).

### Results: `cost` vs `round_robin` (LOOK motion, mean total time per passenger in ticks)

| scenario | building | requests / tick | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| quiet | 30 × 4 | 0.12 | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| quiet | 40 × 6 | 0.12 | 35.7 | 23.2 | -34.8% | [-13.3, -11.5] | 20/20 | 65% | 16.6 |
| morning_rush | 30 × 4 | 0.39 | 43.6 | 28.3 | -35.1% | [-15.8, -14.7] | 20/20 | 52% | 14.1 |
| morning_rush | 40 × 6 | 0.39 | 55.9 | 36.8 | -34.2% | [-20.0, -18.1] | 20/20 | 52% | 18.9 |
| lunch | 30 × 4 | 0.36 | 42.4 | 25.3 | -40.4% | [-17.7, -16.6] | 20/20 | 60% | 14.1 |
| lunch | 40 × 6 | 0.36 | 53.6 | 28.2 | -47.4% | [-26.0, -24.8] | 20/20 | 73% | 18.7 |
| evening_rush | 30 × 4 | 0.39 | 44.7 | 28.5 | -36.2% | [-16.8, -15.6] | 20/20 | 53% | 14.3 |
| evening_rush | 40 × 6 | 0.39 | 55.3 | 32.5 | -41.2% | [-23.5, -22.0] | 20/20 | 63% | 18.9 |

The other policies against round-robin, and the motion axis (✓ better, ✗ worse, ? inconclusive;
ranking letters C `cost`, N `nearest`, Z `zone`, R `round_robin`, best first):

| scenario | building | `nearest` vs RR | `zone` vs RR | LOOK vs SCAN (`cost`) | LOOK vs SCAN (RR) | ranking |
|---|---|---:|---:|---:|---:|---|
| quiet | 30 × 4 | -11% ✓ | -0% ? | -13% ✓ | -28% ✓ | CNZR |
| quiet | 40 × 6 | -14% ✓ | +2% ? | -13% ✓ | -27% ✓ | CNRZ |
| morning_rush | 30 × 4 | +9% ✗ | -20% ✓ | -4% ✓ | -10% ✓ | CZRN |
| morning_rush | 40 × 6 | +15% ✗ | -20% ✓ | -2% ? | -10% ✓ | CZRN |
| lunch | 30 × 4 | -10% ✓ | -19% ✓ | -11% ✓ | -11% ✓ | CZNR |
| lunch | 40 × 6 | -14% ✓ | -20% ✓ | -8% ✓ | -14% ✓ | CZNR |
| evening_rush | 30 × 4 | +10% ? | -20% ✓ | -22% ✓ | -9% ✓ | CZRN |
| evening_rush | 40 × 6 | +7% ? | -20% ✓ | -29% ✓ | -13% ✓ | CZRN |

Read from `results/standard/summary.md`:
- `cost` beats round-robin in every scenario and every seed (20/20), by 31-47%, closing 52-73%
  of the gap to the theoretical floor. The gain is largest at lunch (40-47%: two-way traffic,
  where a car that has just come down can take someone up) and smallest in the quiet scenario and
  the morning rush (31-35%): when it's quiet there is little queueing to remove, and in the
  morning rush waiting is bounded by how long a car takes to go up and come back.
- `nearest` helps when it's quiet or two-way (10-14% better than round-robin) but **hurts in the
  rushes**: significantly worse in the morning rush (+9%, +15%) and worse-leaning in the evening
  rush (+7%, +10%, inconclusive). It keeps picking whichever car is near the lobby, so that car
  fills up while others idle (see the capacity table below).
- `zone` is 19-20% better than round-robin in both rushes and at lunch, and no better in the
  quiet scenario, where half the traffic is inter-floor and banding by the trip's upper floor
  loads the cars unevenly (load CV 0.25-0.36).
- LOOK beats SCAN under round-robin everywhere (9-28%) and under `cost` everywhere except the
  40-floor morning rush (-2%, inconclusive); the gain is largest in the evening rush (22-29%),
  where pickups are spread over every floor and reversing early pays.

**By trip type** (passengers per run under `cost`, and mean wait round-robin → `cost`):

| scenario | building | inbound: n, wait RR → cost | outbound: n, wait RR → cost | inter-floor: n, wait RR → cost |
|---|---|---:|---:|---:|
| quiet | 30 × 4 | 23, 14.0 → 4.4 | 24, 15.2 → 6.4 | 46, 15.3 → 6.4 |
| quiet | 40 × 6 | 25, 17.2 → 3.6 | 22, 17.8 → 6.1 | 48, 18.4 → 6.0 |
| morning_rush | 30 × 4 | 234, 26.7 → 11.8 | 24, 27.1 → 8.7 | 46, 28.0 → 9.5 |
| morning_rush | 40 × 6 | 249, 34.0 → 15.8 | 22, 37.0 → 8.7 | 48, 36.1 → 9.9 |
| lunch | 30 × 4 | 114, 25.3 → 7.9 | 120, 26.7 → 9.9 | 46, 27.7 → 10.2 |
| lunch | 40 × 6 | 124, 32.6 → 6.6 | 116, 33.3 → 8.1 | 48, 33.3 → 8.5 |
| evening_rush | 30 × 4 | 23, 25.2 → 6.0 | 242, 27.8 → 12.1 | 46, 28.6 → 13.2 |
| evening_rush | 40 × 6 | 25, 31.9 → 2.8 | 236, 33.8 → 12.2 | 48, 36.4 → 12.3 |

Under round-robin every trip type waits about the same (e.g. 26.7 / 27.1 / 28.0 ticks in the
30-floor morning rush), because the assignment ignores the trip. Under `cost` the waits split by
direction of the traffic: in the morning rush the heavy inbound stream waits longest (11.8-15.8)
while outbound and inter-floor passengers wait 8.7-9.9; in the evening rush inbound passengers
wait only 2.8-6.0 ticks (cars come down full and go back up empty, so a lobby pickup is cheap),
while outbound and inter-floor passengers, competing for the same downward sweeps, wait 12-13.

### Why `cost` wins: root cause (LOOK motion; from the diagnostics columns in `summary.md`)

| scenario | building | wait RR → cost | detour RR → cost | assigned a car moving away RR → cost | chosen car distance RR → cost (nearest) | cars busy RR → cost |
|---|---|---:|---:|---:|---:|---:|
| quiet | 30 × 4 | 15.0 → 6.0 | 1.1 → 1.3 | 21% (wait 27) → 6% (wait 11) | 10.6 → 5.2 (3.9) | 66% → 47% |
| quiet | 40 × 6 | 18.0 → 5.4 | 1.1 → 1.3 | 16% (wait 34) → 5% (wait 11) | 14.2 → 4.9 (3.6) | 60% → 39% |
| morning_rush | 30 × 4 | 26.9 → 11.2 | 2.6 → 3.0 | 50% (wait 40) → 8% (wait 19) | 11.8 → 9.8 (4.6) | 98% → 79% |
| morning_rush | 40 × 6 | 34.5 → 14.5 | 2.4 → 3.4 | 49% (wait 52) → 6% (wait 23) | 15.8 → 13.4 (4.1) | 96% → 65% |
| lunch | 30 × 4 | 26.3 → 9.2 | 2.0 → 2.0 | 48% (wait 38) → 16% (wait 16) | 10.6 → 6.6 (4.0) | 97% → 90% |
| lunch | 40 × 6 | 33.1 → 7.5 | 1.9 → 2.0 | 46% (wait 49) → 10% (wait 14) | 14.3 → 6.0 (3.9) | 95% → 82% |
| evening_rush | 30 × 4 | 27.7 → 11.8 | 2.7 → 2.4 | 48% (wait 38) → 23% (wait 19) | 9.8 → 7.3 (3.9) | 97% → 92% |
| evening_rush | 40 × 6 | 34.1 → 11.4 | 2.4 → 2.2 | 47% (wait 47) → 15% (wait 17) | 13.2 → 8.5 (3.7) | 95% → 83% |

- **All of the gap is waiting.** Detour, the ride time beyond the direct trip, is 1-3.4 ticks for
  every policy; `cost` even accepts a little more of it in the morning rush (3.0-3.4 vs 2.4-2.6),
  grouping lobby passengers (1.67 riders per stop vs 1.50-1.56).
- **Round-robin ignores where cars are and where they're going**, so in the busy scenarios
  46-50% of its passengers are handed to a car moving away from them (16-21% when it's quiet);
  those wait 38-52 ticks while the car finishes its sweep and comes back. `cost` does that for
  5-23%. Round-robin's chosen car is 10-16 floors away when the nearest is about 4. Distance alone
  is not the cause, though: in the morning rush `cost` also picks a car 10-13 floors away, one
  already coming down to the lobby. What matters is which way the car is going.
- **That empty travel keeps round-robin's cars 95-98% busy in the busy scenarios**, at
  saturation, so everyone queues; `cost` does the same work with cars busy 65-92%.

**Capacity and the tail** (LOOK; "passed by a full car" = the passenger's own car stood at their
floor, heading their way, full):

| scenario | building | passed by a full car: RR / nearest / cost | max wait: RR / nearest / cost | load CV: RR / nearest / zone / cost |
|---|---|---:|---:|---:|
| quiet | 30 × 4 | 0.0% / 0.0% / 0.0% | 48 / 57 / 26 | 0.02 / 0.28 / 0.25 / 0.17 |
| quiet | 40 × 6 | 0.0% / 0.0% / 0.0% | 62 / 75 / 30 | 0.03 / 0.37 / 0.36 / 0.26 |
| morning_rush | 30 × 4 | 0.0% / 9.7% / 0.0% | 64 / 127 / 38 | 0.01 / 0.23 / 0.08 / 0.11 |
| morning_rush | 40 × 6 | 0.0% / 12.3% / 0.0% | 82 / 218 / 43 | 0.01 / 0.37 / 0.16 / 0.18 |
| lunch | 30 × 4 | 0.0% / 0.4% / 0.0% | 63 / 81 / 37 | 0.01 / 0.14 / 0.09 / 0.09 |
| lunch | 40 × 6 | 0.0% / 0.1% / 0.0% | 82 / 92 / 38 | 0.01 / 0.17 / 0.16 / 0.13 |
| evening_rush | 30 × 4 | 0.2% / 8.3% / 0.1% | 75 / 270 / 50 | 0.00 / 0.25 / 0.10 / 0.07 |
| evening_rush | 40 × 6 | 0.0% / 6.2% / 0.0% | 81 / 332 / 51 | 0.01 / 0.39 / 0.15 / 0.12 |

- **In the rushes capacity binds**: under `nearest` 6-12% of passengers watch their own car pass
  full, and its worst waits reach 127-332 ticks. Round-robin spreads passengers evenly (load CV
  about 0) and `cost` predicts the full car (the projection applies the capacity rule), so both
  stay at 0-0.2%. The capacity-along-route rule is also pinned down by
  `tests/test_capacity_scenarios.py`.
- **Round-robin has the best Jain fairness index (0.63-0.73 vs 0.44-0.65 for `cost`) yet worse
  tails** (p95 wait 36-71 vs 18-33): Jain rewards *equal* waits, not *short* ones, so the fairness
  study uses p95 and max wait instead.

## Sensitivity: stop time and start position

```bash
uv run elevator-sim bench --suite standard --seeds 20 --door-times 0,1,2 --placements lobby,spread \
    -o results/sensitivity                       # 48 experiments, 7,680 runs, ~4 min on 10 cores
```

The brief doesn't model doors, so `door_time` (extra ticks a stop holds the car) is our assumption,
and so is starting every car at the lobby. This study checks whether either one drives the
conclusions: the standard suite again at door_time 0, 1 and 2, with cars starting at the lobby or
spread evenly up the building. Full pivot tables are in `results/sensitivity/summary.md`; the
summary across the 6 settings per row:

| scenario | building | `cost` vs RR | `nearest` vs RR | `zone` vs RR | LOOK vs SCAN (`cost`) | ranking at door 0 / 1 / 2 (lobby) |
|---|---|---|---|---|---|---|
| quiet | 30 × 4 | -33% to -31% (6✓) | -14% to -8% (6✓) | -2% to +2% (6?) | -15% to -11% (6✓) | CNZR / CNZR / CNRZ |
| quiet | 40 × 6 | -37% to -33% (6✓) | -19% to -11% (6✓) | -1% to +4% (5? / 1✗) | -13% to -9% (6✓) | CNRZ / CNRZ / CNRZ |
| morning_rush | 30 × 4 | -36% to -34% (6✓) | -1% to +27% (2? / 4✗) | -21% to -19% (6✓) | -18% to +0% (2✓ / 4?) | CZNR / CZRN / CZRN |
| morning_rush | 40 × 6 | -36% to -34% (6✓) | +6% to +29% (2? / 4✗) | -22% to -20% (6✓) | -5% to -0% (1✓ / 5?) | CZRN / CZRN / CZRN |
| lunch | 30 × 4 | -43% to -37% (6✓) | -12% to -7% (6✓) | -20% to -18% (6✓) | -22% to -6% (6✓) | CZNR / CZNR / CZNR |
| lunch | 40 × 6 | -49% to -46% (6✓) | -15% to -13% (6✓) | -22% to -20% (6✓) | -12% to -4% (6✓) | CZNR / CZNR / CZNR |
| evening_rush | 30 × 4 | -38% to -34% (6✓) | -2% to +16% (5? / 1✗) | -20% to -18% (6✓) | -26% to -17% (6✓) | CZRN / CZRN / CZRN |
| evening_rush | 40 × 6 | -42% to -40% (6✓) | -4% to +11% (5? / 1✗) | -22% to -19% (6✓) | -33% to -23% (6✓) | CZRN / CZRN / CZRN |

✓ better, ? inconclusive, ✗ worse (counts out of 6 settings). Ranking letters: C `cost`,
N `nearest`, Z `zone`, R `round_robin`, best first.

**Conclusions that hold in every setting**
- `cost` is the best policy in all 48 experiments, 31-49% better than round-robin; its advantage
  moves by at most 6 points across stop times and start positions.
- `zone` is 18-22% better than round-robin in both rushes and at lunch at every stop time, and
  no better in the quiet scenario (once significantly worse, +4%).
- LOOK beats SCAN under `cost` at lunch, in the evening rush and in the quiet scenario in every
  setting; in the morning rush the difference is small and mostly inconclusive.

**Conclusions that depend on the stop time**
- **`nearest` gets worse as stops get longer.** It stays better than round-robin when it's quiet
  or at lunch, but in the rushes it is significantly worse in 10 of the 24 settings (up to +29%)
  and comes last in all 16 rush settings with door_time ≥ 1. It piles passengers onto a few cars,
  and every extra stop now costs more: from door_time 0 to 2 in the 30-floor rushes, its full-car
  pass-bys rise from 5% to 16% (morning) and its worst wait from 188 to 354 ticks (evening).
- **Longer stops hurt round-robin more than `cost`** in every pair: from door_time 0 to 2,
  round-robin's mean total grows by 3.4-13.5 ticks, `cost`'s by 3.0-10.5. `cost` also spreads
  passengers more evenly as stops get dearer (its load CV falls from door_time 0 to 2 in all 8
  pairs, e.g. 0.15 → 0.08 in the 30-floor morning rush), consistent with its projection pricing
  every stop.
- Headroom shrinks: at door_time 2, `cost`'s cars are busy up to 96% (30-floor evening rush).

**Start position barely matters.** Lobby vs spread changes `cost`'s and `zone`'s result by at
most 2 points (`nearest`: up to 11). Over an 800-tick run the cars leave their starting floors
within the first few dozen ticks, so the start only affects the earliest passengers. Where idle
cars wait *during* a run is a different question (parking, not built).

**Caveats**
- "Gap closed" falls as door_time grows (e.g. 60% → 52%, quiet 30 × 4) partly because the B0
  floor is the direct ride with no stops: with longer stops, more of the excess time is
  unavoidable. Compare gap closed within one door_time, not across them.
- Verdicts on `nearest` depend on the stop time, so claims about it name the door_time (the
  standard suite uses 1).

## Building sweep: floors, cars and capacity

```bash
uv run elevator-sim bench --suite buildings --seeds 20 -o results/buildings   # 3,520 runs, ~6 min
```

The brief makes floors, elevators and capacity configurable, and the standard suite's two
buildings differ in floors *and* cars at once. This sweep varies one setting at a time around
30 floors × 4 cars × capacity 8 (LOOK motion, all four dispatch policies, 20 seeds): floors
15 / 30 / 45 / 60, cars 2 / 3 / 4 / 6 / 8, capacity 4 / 6 / 8 / 12. **Demand scales with floors**
(same people per floor: rates × (floors − 1) / 29), so a 60-floor office has about twice the
requests of a 30-floor one; the car and capacity sweeps keep the 30-floor demand. All Δ below are
significant (✓) unless marked; the HTML report (`report results/buildings`) draws each row as a
trend line.

**Varying floors** (cars 4, capacity 8, demand scales with floors): mean total, round_robin → cost (Δ), ranking

| scenario | floors 15 | floors 30 | floors 45 | floors 60 |
|---|---:|---:|---:|---:|
| quiet | 13 → 10 (-23%) CNZR | 28 → 20 (-31%) CNZR | 57 → 32 (-43%) CNZR | 84 → 49 (-42%) CZNR |
| morning_rush | 16 → 14 (-15%) CZRN | 44 → 28 (-35%) CZRN | 169 → 142 (-16%) ZCRN | 483 → 443 (-8%) ZCRN |
| lunch | 15 → 11 (-25%) CNZR | 42 → 25 (-40%) CZNR | 74 → 46 (-38%) CZRN | 192 → 120 (-38%) CZRN |
| evening_rush | 16 → 13 (-16%) CRZN | 45 → 29 (-36%) CZRN | 155 → 63 (-60%) CZRN | 396 → 230 (-42%) CZRN |

**Varying cars** (floors 30, capacity 8): mean total, round_robin → cost (Δ), ranking

| scenario | cars 2 | cars 3 | cars 4 | cars 6 | cars 8 |
|---|---:|---:|---:|---:|---:|
| quiet | 38 → 28 (-26%) CZNR | 32 → 22 (-31%) CNZR | 28 → 20 (-31%) CNZR | 25 → 18 (-30%) CNRZ | 25 → 17 (-31%) CNRZ |
| morning_rush | 113 → 99 (-13%) ZCRN | 48 → 34 (-29%) CZRN | 44 → 28 (-35%) CZRN | 39 → 26 (-34%) CZRN | 36 → 26 (-29%) CZRN |
| lunch | 51 → 41 (-19%) CZRN | 46 → 31 (-33%) CZNR | 42 → 25 (-40%) CZNR | 38 → 21 (-45%) CZNR | 34 → 19 (-44%) CNZR |
| evening_rush | 116 → 59 (-49%) CZRN | 50 → 34 (-32%) CZRN | 45 → 29 (-36%) CZRN | 40 → 25 (-38%) CZRN | 36 → 24 (-33%) CZRN |

**Varying capacity** (floors 30, cars 4): mean total, round_robin → cost (Δ), ranking

| scenario | capacity 4 | capacity 6 | capacity 8 | capacity 12 |
|---|---:|---:|---:|---:|
| quiet | 28 → 20 (-31%) CNRZ | 28 → 20 (-31%) CNZR | 28 → 20 (-31%) CNZR | 28 → 20 (-31%) CNZR |
| morning_rush | 72 → 50 (-30%) CZRN | 45 → 31 (-31%) CZRN | 44 → 28 (-35%) CZRN | 44 → 28 (-37%) CZNR |
| lunch | 43 → 26 (-41%) CZNR | 42 → 25 (-40%) CZNR | 42 → 25 (-40%) CZNR | 42 → 25 (-40%) CZNR |
| evening_rush | 75 → 33 (-56%) CZRN | 46 → 29 (-37%) CZRN | 45 → 29 (-36%) CZRN | 45 → 28 (-36%) CZNR |

**What it shows**
- **Four cars can't serve a 45- or 60-floor office at rush hour.** Mean total times run to
  hundreds of ticks and up to 70% of passengers see a full car pass; a taller building needs more
  cars, and the sweep shows where the bank runs out.
- **In an overloaded morning rush, `zone` beats `cost`** (45 floors: 126 vs 142 ticks, `zone`
  better in 18 of 20 seeds; 60 floors: 327 vs 443, 20 of 20). Banding cars by destination is how
  real buildings handle up-peak: each car serves a short band, so its round trip is shorter, and
  fewer passengers are passed by a full car (32% vs 55% at 45 floors). `cost` is greedy and can't
  see that. In the overloaded evening rush `cost` still wins clearly (230 vs 299 ticks, 20 of 20).
  A known improvement: switch to destination sectoring when the up-peak saturates.
- **More cars help, with diminishing returns.** Going from 2 to 3 cars rescues the rushes (round-
  robin 113 → 48 ticks in the morning); beyond 6 cars `cost`'s mean total barely moves. `cost`
  stays 29-45% better than round-robin from 3 to 8 cars.
- **Capacity only matters when it binds**: in the quiet scenario and at lunch every capacity from 4
  to 12 gives the same result to within a tick. At capacity 4 in the rushes it binds hard, and
  `cost`'s capacity-aware projection pays off most: passengers passed by a full car 7-21% under
  `cost` vs 20-39% under round-robin and 35-54% under `nearest`, and p95 wait 40-71 ticks vs
  122-232 (round-robin). Above capacity 6 the rushes barely change.

## Parking idle cars

When a car has no passengers and no assignments, where should it wait? A **parking policy**
answers once, when the car goes idle; the car then drives there (a real move: it shows in the
positions log, floors travelled and car trips) and drops the target the moment it is assigned a
passenger. The decision is made at the end of the tick the car goes idle, so it leaves on the
next tick. A policy sees read-only car views, the floors other idle cars hold, and requests
already made, never future ones (a spy test checks this).

| Policy | Rule |
|---|---|
| `stay` (default) | wait where the last trip ended |
| `lobby` | go back to floor 1 |
| `spread` | car i waits at its own home floor, spaced evenly up the building |
| `demand` | wait at the floor where the most requests started in the last 100 ticks, skipping floors another idle car already holds |

```bash
uv run elevator-sim bench --suite standard --seeds 20 --parking stay,lobby,spread,demand \
    --dispatch cost,round_robin --motion look -o results/parking    # 1,280 runs, ~1 min
uv run elevator-sim rush.csv -f 30 -e 4 --parking lobby             # a single run
```

Each policy against `stay` on the same seeds and passengers (`cost` dispatch, LOOK; Δ mean total
time with verdict, and the change in floors travelled per passenger, the price of parking moves):

| scenario | building | `cost`, stay | `lobby`: Δ total, extra floors | `spread`: Δ total, extra floors | `demand`: Δ total, extra floors |
|---|---|---:|---:|---:|---:|
| quiet | 30 × 4 | 19.6 | +5.4% ✗, +30% | -5.5% ✓, +40% | -3.6% ✓, +25% |
| quiet | 40 × 6 | 23.2 | +9.8% ✗, +35% | -5.5% ✓, +54% | -3.4% ✓, +29% |
| morning_rush | 30 × 4 | 28.3 | -6.4% ✓, +24% | -5.0% ✓, +19% | -5.7% ✓, +19% |
| morning_rush | 40 × 6 | 36.8 | -17.1% ✓, +51% | -15.0% ✓, +33% | -13.5% ✓, +30% |
| lunch | 30 × 4 | 25.3 | -0.4% ?, +6% | -1.8% ?, +7% | -0.1% ?, +6% |
| lunch | 40 × 6 | 28.2 | +1.0% ?, +15% | +0.1% ?, +15% | -0.5% ?, +13% |
| evening_rush | 30 × 4 | 28.5 | +0.5% ?, +1% | -2.2% ?, +5% | -0.3% ?, +4% |
| evening_rush | 40 × 6 | 32.5 | -0.4% ?, +0% | -3.9% ✓, +13% | -3.0% ✓, +8% |

**What it shows**
- **`lobby` does its job**: it is the best policy in the morning rush (-6%, -17%), and it backfires
  when it's quiet (+5%, +10%), where the next passenger is rarely at the lobby.
- **`spread` is best when it's quiet** (-5.5% in both buildings, max wait 4.5-7 ticks shorter) and
  also helps the morning rush, at the highest travel cost (up to +54% floors per passenger).
- **`demand` is never significantly worse** and helps in 5 of the 8 experiments, with less extra
  travel than `spread`. In the morning rush most recent requests start at the lobby, so it parks
  there by itself; when it's quiet it scatters the cars much like `spread`.
- **At lunch and in the 30-floor evening rush nothing helps**: the cars are rarely idle.
- **Round-robin gains nothing from any parking policy** (all inconclusive, within ±2.5%): it
  never looks at where the cars are, so where they wait doesn't matter to it. Parking only pays
  for a dispatcher that uses car positions.
- **Parking costs travel**: up to +54% floors per passenger under `cost` (0-15% at lunch and in
  the evening rush, where cars are rarely idle).

**Decisions** (made before the results, revisited with them)
1. **Keep `demand`.** A recent request at a floor could mean that passenger has already gone, or
   that colleagues on the same floor of an office will leave around the same time; rather than
   assume, let the simulation decide. It did: `demand` is never worse, and in the morning rush the
   "colleagues follow" reading wins.
2. **`lobby` stays a simple rule** (every idle car goes to floor 1, no cap): it exists to handle the
   morning rush, and the results confirm it is best there and only there.
3. **`stay` remains the default.** A trip to a parking floor is itself a cost to the building
   (energy, wear), and the table shows that cost is real; the headline results use no parking.
   `demand` is the best all-round choice when that travel is acceptable; `lobby` before a known
   morning rush.

## Fairness vs efficiency

The brief's third bonus: the trade-off between serving everyone quickly (fairness) and optimising
for the majority (efficiency). The `cost` policy takes a fairness weight α:

```
cost(car) = increase in Σ total time  +  α · increase in Σ wait²     (over that car's passengers)
```

Squaring the projected waits makes one passenger waiting 40 ticks cost as much as sixteen waiting
10, and makes delaying someone who already waits long expensive (pushing a 30-tick wait to 33 adds
189 to Σ wait²; pushing a 3-tick wait to 6 adds 27), so the policy stops trading one long wait for
a few short ones. α = 0 is the plain policy. Fairness is judged on p95 and max wait, not the Jain
index (see [Metrics](#metrics-what-we-measure-and-why)).

```bash
uv run elevator-sim bench --suite standard --seeds 20 --loads 1,1.5 --dispatch round_robin \
    --fairness 0,0.05,0.2,1 --motion look -o results/fairness   # 1,600 runs, ~4 min
uv run elevator-sim rush.csv -f 30 -e 4 --fairness 0.2          # a single run with α = 0.2
```

The sweep covers α = 0, 0.05, 0.2 and 1 at the standard load and at 1.5 × (the heavy rushes reach
0.585 requests per tick). Per-α frontier tables are in `results/fairness/summary.md`; α = 0.2
against plain `cost`, paired by seed:

| scenario | building | load | `cost`: total / p95 wait / max wait | α = 0.2: Δ total | Δ wait p95 | Δ wait max |
|---|---|---|---|---:|---:|---:|
| quiet | 30 × 4 | 1 (0.12/tick) | 19.6 / 18 / 26 | -0.4% ? | -0.6 ? | -0.7 ? |
| quiet | 40 × 6 | 1 (0.12/tick) | 23.2 / 18 / 30 | -0.1% ? | -0.5 ? | -0.5 ? |
| morning_rush | 30 × 4 | 1 (0.39/tick) | 28.3 / 26 / 38 | +0.0% ? | -1.0 ? | -5.2 ? |
| morning_rush | 40 × 6 | 1 (0.39/tick) | 36.8 / 33 / 43 | +0.4% ? | -0.5 ? | -3.6 ? |
| lunch | 30 × 4 | 1 (0.36/tick) | 25.3 / 24 / 37 | -1.9% ? | -2.0 ? | -3.5 ? |
| lunch | 40 × 6 | 1 (0.36/tick) | 28.2 / 21 / 38 | -0.5% ? | -0.3 ? | -1.6 ? |
| evening_rush | 30 × 4 | 1 (0.39/tick) | 28.5 / 31 / 50 | -0.8% ? | -1.9 ? | -4.9 ✓ |
| evening_rush | 40 × 6 | 1 (0.39/tick) | 32.5 / 33 / 51 | -0.6% ? | -1.5 ✓ | -5.0 ? |
| quiet | 30 × 4 | 1.5 (0.18/tick) | 20.5 / 19 / 27 | -0.4% ? | -0.3 ? | -0.7 ? |
| quiet | 40 × 6 | 1.5 (0.18/tick) | 24.1 / 19 / 33 | -0.2% ? | -0.6 ? | -1.4 ? |
| morning_rush | 30 × 4 | 1.5 (0.585/tick) | 36.5 / 40 / 62 | +1.7% ? | -1.8 ? | -10.3 ✓ |
| morning_rush | 40 × 6 | 1.5 (0.585/tick) | 40.7 / 36 / 52 | +0.9% ? | -1.2 ? | -7.0 ✓ |
| lunch | 30 × 4 | 1.5 (0.54/tick) | 28.9 / 30 / 51 | -1.6% ? | -0.7 ? | -2.5 ? |
| lunch | 40 × 6 | 1.5 (0.54/tick) | 30.9 / 26 / 44 | -2.9% ? | -3.3 ✓ | -5.6 ? |
| evening_rush | 30 × 4 | 1.5 (0.585/tick) | 31.7 / 36 / 64 | -0.9% ? | -2.1 ? | -8.2 ✓ |
| evening_rush | 40 × 6 | 1.5 (0.585/tick) | 34.2 / 34 / 60 | -0.9% ? | -1.8 ? | -7.4 ? |

✓ better, ? inconclusive, ✗ worse (claim rule as above; the max is noisy, so few results clear
the 80%-of-seeds bar).

**What we found**
- **When it's quiet there is nothing to trade.** Plain `cost`'s worst wait is already short
  (26-33 ticks); the fairness term changes it by under 1.5 ticks.
- **In the rushes it trims the worst waits**, and more so under heavy load: at load 1.5, max wait
  falls by 7-10 ticks in both rushes (significant in the morning rush in both buildings and the
  30-floor evening rush); at load 1, by 3.6-5.2 ticks.
- **We found no efficiency price.** Mean total time is never significantly worse at any α tested
  (changes between -2.9% and +1.7%, all inconclusive). The only hint of a cost is the heavy
  morning rush (+0.9%, +1.7%).
  A likely reason: plain `cost` is greedy, so leaving one passenger waiting long is not even good
  for the total; the penalty corrects some of those greedy choices.
- **No guarantee per input.** On a small starvation-prone case (20 floors, 3 cars, 120 requests in
  200 ticks), α = 1 lowers the max wait in 20 of 30 seeds but raises it in 7
  (`tests/test_fairness.py`).
- So, within `cost`, fairness and efficiency did not conflict in our settings. The visible
  trade-off is between policies: round-robin gives the most *equal* waits (highest Jain index)
  but the longest ones. The default stays α = 0 so the headline results are the plain policy;
  α = 0.2 is a reasonable setting for heavy rushes.

## Visual report

`elevator-sim report` turns a run journal or a benchmark folder into **one self-contained HTML
file** (inline SVG and a little JavaScript, no dependencies, works offline: open it by
double-click). `run --html` writes one next to the run's other outputs.

```bash
uv run elevator-sim rush.csv -f 30 -e 4 --html -o out/rush          # out/rush/report.html
uv run elevator-sim report out/run.jsonl -o out/run.html            # from a saved journal
uv run elevator-sim report results/standard -o out/bench.html       # from a benchmark folder
uv run elevator-sim report results/fairness -o out/fairness.html    # includes the frontier
uv run elevator-sim report results/buildings -o out/buildings.html  # trend per floors / cars / capacity
```

| Report | Views |
|---|---|
| Run | headline tiles (passengers, mean / p95 / max wait, mean total, last drop-off); the **time-space diagram** (every car's floor at every tick, with a crosshair that reads each car's floor and load); the wait distribution; wait by trip type (inbound / outbound / inter-floor); the state of the assigned car (idle / on the way / ahead but heading the other way / moving away); passengers per car; observations; the passenger table |
| Benchmark | `cost` vs `round_robin` across all experiments with 95% CIs; for a building sweep, a trend line per setting (floors, cars, capacity) and scenario; then, for the experiment picked in the selector: mean total by policy and motion against the B0 floor, the wait tail (mean, p95, max), wait by trip type, the root-cause diagnostics (assigned to a car moving away, how busy the cars were), and the fairness frontier when the run swept α |

Every chart has a table view, hover and keyboard focus show exact values, colours come from a
palette validated for colour-vision deficiency in light and dark mode, and all text from the data
is escaped.

![Benchmark report: cost vs round-robin across experiments, then mean total time and wait tail per policy](docs/images/bench_report.png)

![Run report: headline tiles, the time-space diagram of a morning rush, and the wait distribution](docs/images/run_report.png)

## Reproduce every result

```bash
./scripts/install.sh                                     # once: uv + the locked environment
uv run elevator-sim bench --suite standard --seeds 20 -o results/standard
uv run elevator-sim bench --suite standard --seeds 20 --door-times 0,1,2 --placements lobby,spread \
    -o results/sensitivity
uv run elevator-sim bench --suite standard --seeds 20 --loads 1,1.5 --dispatch round_robin \
    --fairness 0,0.05,0.2,1 --motion look -o results/fairness
uv run elevator-sim bench --suite buildings --seeds 20 -o results/buildings
uv run elevator-sim bench --suite standard --seeds 20 --parking stay,lobby,spread,demand \
    --dispatch cost,round_robin --motion look -o results/parking
uv run python scripts/readme_tables.py                  # prints every results table in this README
for r in standard sensitivity fairness buildings parking; do
    uv run elevator-sim report results/$r -o out/$r.html
done
```

About 16 minutes on 10 cores in total. Runs are deterministic: the same command gives
byte-identical `raw.jsonl` files (a test checks this, in-process and across worker processes).
`summary.json` and `summary.md` are committed for all five studies; `raw.jsonl` only for the
standard suite (the others are large and regenerated by the commands above).

## Testing

246 tests (`uv run pytest --cov`, about 11 s; coverage 99%, gate 95%; CI on Python 3.10-3.13).
Expected values in the hand-worked tests were computed by hand first, tick by tick, and the tests
written to match; the comments show the working.

| Kind | What it pins down | Tests to look at |
|---|---|---|
| **Golden** | The brief's three-row example, exact boarding and drop-off ticks, with door_time 0 and 1, and with 3 cars | `test_simulate.py::test_brief_example_one_car_door_time_0` (and `_1`, `_three_cars`) |
| **Rules** | One floor per tick; a stop holds the car `door_time + 1` ticks; a request made while the doors are open still boards; assignment happens before cars move, so asking where your car stands means wait 0; no request is visible before its tick | `test_car.py::test_stop_timeline_with_door_time_1`, `test_car.py::test_request_made_mid_dwell_still_boards`, `test_dispatch.py::test_policies_never_see_a_request_before_its_time` |
| **Capacity along the route** | A full car frees room at floor 6 and uses it at floor 8 on the same sweep; three waiting with room for two (the third is picked up at t15); `project()` predicts both before they happen; `cost` picks the full car only when it frees room in time | `test_capacity_scenarios.py` (8 tests) |
| **Policies** | Round-robin cycles and ignores car state (wait 33 vs 1 under `cost` on the same input); `nearest`, `zone` and `cost` choose as specified; ties go to the lowest id; a policy can't choose a car that can't serve the trip | `test_capacity_scenarios.py::test_round_robin_ignores_car_state`, `test_dispatch.py` |
| **Motion** | LOOK keeps going while work lies ahead and reverses when none does; SCAN runs to the end; and a counterexample: LOOK *can* travel further than SCAN when requests arrive over time | `test_motion.py::test_look_can_travel_further_than_scan_when_requests_arrive_over_time` |
| **Invariants** | Over every dispatch × motion × door_time combination (24 runs, all four scenarios): one positions row per car per tick from t = 0, never over capacity, never more than one floor per tick, never moving with doors open, every passenger seen on their tick, assigned once, carried by that car from their floor to their destination | `test_invariants.py` with `helpers.check_invariants` |
| **Projection** | `project()` predicts the real stops exactly when no new requests arrive, for LOOK and SCAN at door_time 0, 1 and 2 | `test_route.py::test_route_predicts_the_real_stops_when_no_new_requests_arrive` |
| **Determinism and replay** | Same inputs, identical journal; a saved journal rebuilds an identical report; benchmark output byte-identical in-process and across worker processes | `test_simulate.py::test_same_inputs_give_an_identical_journal`, `test_bench.py::test_same_seed_gives_byte_identical_raw_output_in_and_across_processes` |
| **Liveness guards** | A policy that never serves anyone is caught; a long idle gap is not mistaken for a stall | `test_simulate.py::test_a_car_that_stops_serving_after_assignment_trips_the_stall_guard` |
| **Scenarios** | Each Poisson stream has the right rate and variance ≈ mean; the inter-floor passengers are identical in every scenario; the quiet inbound stream is contained in the rush's | `test_scenarios.py::test_arrivals_are_poisson_with_the_scenario_rates`, `::test_streams_are_generated_once_and_shared_by_every_scenario` |
| **Measurement** | Every policy in a seed sees identical requests (fingerprints); B0 equals the mean direct ride; gap closed is 0 at the baseline and 1 at the floor; the verdict needs both significance and consistency | `test_bench.py` |
| **Parking** | An idle car returns to the lobby and a waiting passenger then boards at once (wait 0 vs 5); a parking car turns around as soon as it is assigned; `spread` homes; `demand` picks the busiest recent floor, skips claimed floors and never sees a future request; every invariant holds under every parking policy | `test_parking.py` |
| **Diagnostics, fairness, report** | Assignment-state classification; full-car pass-bys; α = 0 is exactly plain `cost`; fairness shortens the longest wait on a starvation-prone input but not on every input; the HTML report is self-contained and escapes data | `test_diagnostics.py`, `test_fairness.py`, `test_html_report.py` |

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
  (`--placement` changes that) and an idle car stays where it is (`--parking` changes that; see
  [Parking](#parking-idle-cars)).
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

**Capacity: the car decides on arrival, the dispatcher looks ahead**
- Capacity is a hard limit: the car refuses to board anyone over it, whatever the policy says.
  When people are left behind, the first assigned board first.
- **A car decides whether to pick someone up when it arrives at their floor, from its actual
  load**, counting the people getting off at that floor first. It never relies on a prediction.
  So a car that is full when a passenger is assigned still picks them up if enough people get off
  before their floor (full at floor 1, two get off at 6, two board at 8); a car that arrives full
  drives past and comes back.
- *Why:* that is how a real car with a load sensor behaves. If the car is fuller than expected
  (say someone stayed on past their floor), it passes rather than overfilling, and it never opens
  its doors when nobody can get on or off. In the simulation passengers always get off at their
  floor, so this is a design choice for robustness rather than something the model exercises.
- **Looking ahead is the dispatcher's job.** When it assigns a passenger, `cost` runs each car's
  own rules forward (`project()`, with the same capacity check), so a car that would arrive full
  shows up as a late pickup and costs more; `cost` rarely gives someone a car that will pass them.
  `round_robin`, `nearest` and `zone` don't check.
- *Limits:* the projection assumes no new requests. If later assignments fill the car before it
  reaches you, it passes you full and, because assignments are fixed, you wait for it to return.
  The passed passenger pays for this (13 ticks instead of 5 in the test below);
  re-assigning waiting passengers would fix it.
- *Alternative not taken:* a hard filter that rejects any car whose projected load ever exceeds
  capacity is simpler, but turns a car down even when it frees up in time.
- Tests: `tests/test_capacity_scenarios.py` (room freed at 6 used at 8; three waiting with room
  for two; the projection predicting both before they happen; `cost` choosing the full car only
  when it frees room in time).

**Motion**
- LOOK by default: keep going while there is work ahead, reverse when there is none. SCAN (run to
  the end of the shaft before reversing) is available for comparison.

**Input**
- Requests must be in time order, on floors 1..n, with source ≠ dest and unique ids; anything else
  is reported as an error rather than guessed at.

**Metrics**
- Definitions are in [Metrics](#metrics-what-we-measure-and-why). Choices made there: travel
  includes stops on the way; percentiles use linear interpolation (numpy's default); a *travel* is
  one passenger's journey; a car *trip* runs from when the car starts to move until it reverses
  or goes idle, and an empty move to fetch someone counts.

**Known gap: starvation.** Nothing proves that every passenger is eventually served. LOOK keeps
sweeping back in practice, but under sustained heavy load a full car could keep passing someone.
The simulator stops with an error if nobody boards or alights for a long stretch while passengers
are waiting, so this can't hang silently. The fairness weight (above) shortens the worst waits
under heavy load but gives no per-passenger bound; a hard bound would need re-assigning a
passenger whose wait passes a limit, or a car that must serve the oldest request next.

## What I'd improve with more time

- **Re-assign waiting passengers.** Assignments are fixed, so when `cost`'s projection goes stale
  (later passengers fill a car before it reaches you) the passenger pays. Re-assigning while
  someone is still waiting would fix that and also bound the worst waits.
- **A hard bound on waiting.** The fairness weight shortens the tail but guarantees nothing per
  passenger; a maximum-wait rule (re-assign, or serve the oldest request first) would close the
  starvation gap.
- **Sectoring when the up-peak saturates.** In an overloaded morning rush `zone` beats `cost`;
  switching to destination sectoring above a load threshold, or a cost that accounts for round-trip
  time, should get the best of both.
- **Express banks / sky lobbies** (cars that skip floors, with transfers): designed in the plan,
  not built. And a parking policy that switches with the time of day (lobby before the morning
  rush, `demand` otherwise).
- **A full-day timeline** with rates that change through the day, calibrated against real
  building data rather than illustrative rates, and other building types (residential reverses
  the rushes).
- **Property-based tests** (hypothesis is already a dev dependency) over random buildings and
  loads, and **performance**: cache each car's projection until its state changes, for 10,000+
  requests.
- **Boarding time that depends on how many people get on or off**, instead of a fixed stop time.

## How I used AI

I built this with Claude Code (Anthropic's coding agent) as a pair programmer, and drafted the
implementation plan with an AI assistant beforehand. The split:

- **My decisions**: scope and the phase-by-phase order (I reviewed each phase before the next);
  fixed assignments; door_time 1 as the default; JSON outputs and the metrics I wanted reported
  (wait percentiles, travels, car trips); the reasoning for deciding pickups on arrival from the
  car's actual load; the business-building traffic model (three Poisson streams, inter-floor at a
  steady rate, rushes as heavy inbound or outbound, generated once per seed); demand scaling with
  floors in the building sweep; keeping α = 0 as the default; and for parking, keeping `demand`
  to let the results decide, `lobby` as a simple morning-rush rule, and `stay` as the default
  because parking moves cost the building.
- **Delegated**: most of the code and tests, running the benchmarks, drafting the analysis and
  the README text, which I then questioned and edited.
- **How I checked it**: every README table is generated from `results/` by
  `scripts/readme_tables.py`, and every claim in the text was checked against the data; behaviour
  is pinned by hand-worked tests; reports were rendered and looked at, in light and dark mode.

Where the AI was wrong, and what caught it:
- The plan claimed LOOK never travels further than SCAN. A test found counterexamples when
  requests arrive over time; it only holds when everything is known at t = 0. Both cases are now
  tests.
- The first verdict rule could only say "better", never "significantly worse". Found when
  `nearest` was clearly worse than round-robin in one experiment; fixed to follow the confidence
  interval's direction.
- The first draft of the findings got `zone` backwards and overstated a LOOK/SCAN exception;
  later drafts overstated ranges more than once (e.g. finish times, floors saved per passenger).
  Each was caught by checking the number against `summary.json` before it went in.
- The first HTML report had label collisions and text too small to read in half-width charts;
  caught by rendering it and looking, not by tests.

## Time spent

About **5.5 hours** in total:

| When | Time | What |
|---|---|---|
| Sat 14 Nov | 1 h | reading the brief and writing the implementation plan |
| Sat 14 Nov | 30 min | Phase 0: repo, tooling and CI |
| Sun 15 Nov | 4 h (about 3.5 h at the keyboard, plus thinking time away from it) | the simulation core, outputs and metrics, the benchmark, root-cause diagnostics, sensitivity, fairness, the HTML report, Poisson scenarios, the building sweep, this README |

## Development

```bash
./scripts/install.sh                          # or, with uv already installed: uv sync
uv run pytest --cov                           # 246 tests, coverage gate 95% (currently 99%)
uv run ruff check . && uv run ruff format --check .
```

Python 3.10 is pinned in `.python-version` (the lowest supported version; CI tests 3.10-3.13) and uv downloads it if
needed. Dependencies are locked in `uv.lock`. Without uv: `pip install -e . && pip install --group dev` (pip >= 25.1).
