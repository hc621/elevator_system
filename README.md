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

`report.json` holds the passenger time distributions, completed travels, per-car stats, root-cause
diagnostics and plain-language observations. Every field, and why it is measured, is listed under
[Metrics](#metrics-what-we-measure-and-why). The same numbers are printed as a text summary at the end of each run.

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
  delay to passengers already assigned. Ties go to the lowest id.
- **LOOK**: keep going while any of this car's passengers need a floor ahead; reverse when nothing
  lies ahead; idle when there is no work. **SCAN**: the same, but always run to the end of the
  shaft before reversing.

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
`capacity`, `door_time`, `placement`, `count`, `duration`, `rate`, `skip_first`, `seed`,
`dispatch`, `motion`), the per-passenger metrics above flattened into columns (`wait_mean`,
`wait_p50`, `wait_p90`, `wait_p95`, `wait_max`, `total_mean`, `total_p95`, `total_max`,
`excess_mean`), the diagnostics (`detour_mean`, `away_share`, `away_wait`, `idle_pick_share`,
`chosen_distance`, `nearest_distance`, `busy_share`, `distance_per_passenger`, `riders_per_stop`,
`full_passby_share`), per-run totals (`passengers`, `unserved`, `distance`, `trips`), plus:

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

### Why `cost` wins: root cause (LOOK motion; from the diagnostics columns in `summary.md`)

| experiment | wait RR → cost | detour RR → cost | to a car moving away RR → cost | chosen car distance RR → cost (nearest) | cars busy RR → cost |
|---|---:|---:|---:|---:|---:|
| uniform 30×4 | 22.4 → 8.0 | 1.7 → 1.7 | 44% (wait 32) → 16% (wait 13) | 9.4 → 5.6 (3.6) | 93% → 78% |
| uniform 40×6 | 25.5 → 7.0 | 1.5 → 1.6 | 39% (wait 38) → 10% (wait 11) | 12.4 → 5.5 (3.8) | 89% → 66% |
| mixed 30×4 | 22.9 → 7.4 | 1.6 → 1.7 | 43% (wait 35) → 12% (wait 13) | 10.4 → 5.8 (3.9) | 94% → 79% |
| mixed 40×6 | 28.5 → 6.7 | 1.5 → 1.6 | 42% (wait 44) → 7% (wait 13) | 13.7 → 5.6 (3.6) | 90% → 70% |
| morning_rush 30×4 | 23.1 → 10.2 | 1.8 → 2.5 | 47% (wait 36) → 5% (wait 16) | 11.1 → 9.4 (4.1) | 94% → 63% |
| morning_rush 40×6 | 29.0 → 12.8 | 1.6 → 2.9 | 45% (wait 46) → 4% (wait 20) | 14.4 → 12.1 (3.6) | 92% → 49% |
| evening_rush 30×4 | 23.1 → 10.5 | 1.9 → 1.9 | 44% (wait 33) → 17% (wait 17) | 10.1 → 7.6 (4.0) | 92% → 81% |
| evening_rush 40×6 | 28.4 → 11.0 | 1.7 → 1.8 | 43% (wait 41) → 9% (wait 14) | 13.6 → 8.9 (4.0) | 89% → 68% |

- **All of the gap is waiting.** Detour, the ride time beyond the direct trip, is about 2 ticks
  for every policy; `cost` even accepts a little more of it in the morning rush, grouping lobby
  passengers (1.6 riders per stop vs 1.3).
- **Round-robin ignores where cars are and where they're going**, so 39-47% of its passengers are
  handed to a car moving away from them; those wait 32-46 ticks while the car finishes its sweep
  and comes back. Its chosen car is 9-14 floors away when the nearest is about 4. Distance alone
  is not the cause, though: in the morning rush `cost` also picks a car 9-12 floors away, one
  already coming down to the lobby. What matters is which way the car is going.
- **That empty cross-building travel keeps round-robin's cars 89-94% busy**, close to saturation,
  so everyone queues. `cost` does the same work with cars busy 49-81% and travels 15-50% fewer
  floors per passenger.
- **Capacity never binds in this suite** (no passenger is passed by a full car under `cost` or
  round-robin; 2.5-4.6% under `nearest` in the rushes). The capacity-along-route rule is unit-tested
  but needs a capacity-stress experiment to show its effect.
- **Round-robin has the best Jain fairness index (0.67-0.70) yet the worst tails** (p95 wait
  49-64 vs 20-33 for `cost`): Jain rewards *equal* waits, not *short* ones, so the fairness study
  uses p95 and max wait instead.

## Sensitivity: stop time and start position

```bash
uv run elevator-sim bench --suite standard --seeds 20 --door-times 0,1,2 --placements lobby,spread \
    -o results/sensitivity                       # 48 experiments, 7,680 runs, ~3 min on 10 cores
```

The brief doesn't model doors, so `door_time` (extra ticks a stop holds the car) is our assumption,
and so is starting every car at the lobby. This study checks whether either one drives the
conclusions: the standard suite again at door_time 0, 1 and 2, with cars starting at the lobby or
spread evenly up the building. Full pivot tables (every policy, every setting) are in
`results/sensitivity/summary.md`; the summary across the 6 settings per row:

| scenario | building | `cost` vs RR | `nearest` vs RR | `zone` vs RR | LOOK vs SCAN (`cost`) | ranking at door 0 / 1 / 2 (lobby) |
|---|---|---|---|---|---|---|
| uniform | 30 × 4 | -42% to -39% (6✓) | -17% to -8% (6✓) | -6% to +1% (2✓ / 4?) | -18% to -11% (6✓) | CNZR / CNZR / CNRZ |
| uniform | 40 × 6 | -48% to -45% (6✓) | -20% to -6% (5✓ / 1?) | -9% to -0% (2✓ / 4?) | -14% to -10% (6✓) | CNZR / CNZR / CNZR |
| mixed | 30 × 4 | -42% to -39% (6✓) | -15% to -11% (6✓) | -16% to -14% (6✓) | -11% to -7% (6✓) | CNZR / CZNR / CZNR |
| mixed | 40 × 6 | -46% to -45% (6✓) | -19% to -15% (6✓) | -16% to -14% (6✓) | -11% to -5% (6✓) | CNZR / CNZR / CNZR |
| morning_rush | 30 × 4 | -32% to -31% (6✓) | -3% to +10% (5? / 1✗) | -18% to -15% (6✓) | -2% to -1% (1✓ / 5?) | CZNR / CZRN / CZRN |
| morning_rush | 40 × 6 | -31% to -30% (6✓) | -1% to +12% (5? / 1✗) | -18% to -17% (6✓) | -2% to +0% (1✓ / 5?) | CZRN / CZRN / CZRN |
| evening_rush | 30 × 4 | -33% to -32% (6✓) | -4% to +5% (5? / 1✗) | -16% to -13% (6✓) | -24% to -20% (6✓) | CZNR / CZRN / CZRN |
| evening_rush | 40 × 6 | -36% to -35% (6✓) | -2% to +12% (5? / 1✗) | -16% to -13% (6✓) | -31% to -27% (6✓) | CZRN / CZRN / CZRN |

✓ better, ? inconclusive, ✗ worse (counts out of 6 settings). Ranking letters: C `cost`,
N `nearest`, Z `zone`, R `round_robin`, best first.

**Conclusions that hold in every setting**
- `cost` is the best policy in all 48 experiments, 30-48% better than round-robin, and its
  advantage moves by at most 3 points across stop times and start positions.
- LOOK beats SCAN under round-robin everywhere, and under `cost` everywhere except the morning
  rush, where the difference stays within 2% at every stop time.
- `zone` is reliably 13-18% better than round-robin on mixed traffic and in both rushes.

**Conclusions that depend on the stop time**
- **`nearest` gets worse as stops get longer.** On uniform and mixed traffic it stays better
  than round-robin (one exception at door_time 2), but in the rushes it slides from inconclusive
  at door_time 0 to significantly worse in 4 of the 8 rush settings at door_time 2 (+5% to +12%),
  and comes last in 14 of the 16 rush settings with door_time ≥ 1. Mechanism (diagnostics): it
  piles passengers onto a few cars (load CV 0.29-0.40 in the 30-floor rushes) while the others
  sit partly idle (busy 58-69%), and every extra stop now costs more, so the overloaded cars slow
  further: from door_time 0 to 2 its morning-rush wait grows by 7.7 ticks (round-robin: 4.0), its
  maximum wait from 72 to 121, and full-car pass-bys from 2.0% to 5.5%.
- **`zone` helps on uniform traffic only when stops are free** (6-9% better at door_time 0,
  inconclusive at 1 and 2).
- **Longer stops hurt round-robin more than `cost`**: from door_time 0 to 2, round-robin's mean
  total grows by 6-12 ticks, `cost`'s by 4-8. `cost` also spreads passengers more evenly as stops
  get dearer (its load CV falls in all 8 pairs, e.g. 0.22 → 0.14 in the 30-floor morning rush),
  consistent with its projection pricing every stop.
- Headroom shrinks: at door_time 2 `cost`'s cars are busy up to 88% (uniform and evening rush,
  30 × 4), close to where queueing takes off.

**Start position barely matters.** Lobby vs spread changes `cost`'s and `zone`'s result by at
most 2 points (`nearest`: up to 8). With 200 requests over 800 ticks the cars leave their starting
floors within the first few dozen ticks, so the start only affects the earliest passengers. Where
idle cars wait *during* a run is a different question (parking, not built).

**Caveats**
- "Gap closed" falls as door_time grows (e.g. 65% → 53%, uniform 30 × 4) partly because the B0
  floor is the direct ride with no stops: with longer stops, more of the excess time is
  unavoidable. Compare gap closed within one door_time, not across them.
- Verdicts on `nearest` and `zone` depend on the stop time, so claims about them in this README
  name the door_time (the standard suite uses 1).

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
are waiting, so this can't hang silently. A fairness rule that bounds the wait is the planned fix.

## Development

```bash
./scripts/install.sh                          # or, with uv already installed: uv sync
uv run pytest --cov
uv run ruff check . && uv run ruff format --check .
```

Python 3.10 is pinned in `.python-version` (the lowest supported version; CI tests 3.10-3.13) and uv downloads it if
needed. Dependencies are locked in `uv.lock`. Without uv: `pip install -e . && pip install --group dev` (pip >= 25.1).
