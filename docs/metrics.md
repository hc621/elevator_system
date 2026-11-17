[← README](../README.md) · [all studies](../README.md#detailed-studies)

# Metrics: what we measure and why

All times are in ticks (1 tick = 1 floor of travel). Per passenger:

```
requested --wait--> boarded --travel--> alighted
|<--------------- total = wait + travel ------>|
direct = |dest - source|      excess = total - direct      detour = travel - direct
```

## Per run (`report.json`, `passengers.json`, the printed summary)

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

## Diagnostics: why the times are what they are (`report.json` → `diagnostics`)

These were added after the first benchmark to make the root cause of each result visible in every
report (see [Why `cost` wins](results.md#why-cost-wins-root-cause-look-motion-from-the-diagnostics-columns-in-summarymd)).

| Metric | Definition | Why we measure it |
|---|---|---|
| `detour` | travel − direct | Separates "waited long" from "rode long": shows that dispatch quality appears as wait, not ride time |
| `assigned_car_state` share / mean wait (bench columns `away_share`, `away_wait`, `idle_pick_share`) | state of the chosen car when the passenger was assigned: idle; on the way (ahead, same direction); ahead but heading the other way; moving away | The main root cause: a passenger given a car moving away waits for it to finish its sweep and come back |
| `chosen_car_distance` vs `nearest_car_distance` | floors from the chosen car / the closest car to the pickup, at assignment | Whether the policy looks at where cars are; together with the state above, shows that direction matters more than distance |
| `busy_share` | share of car time not idle with doors closed | How close the building runs to saturation: near 100% means every new request queues behind existing work |
| `distance_per_passenger` | floors travelled by all cars / passengers served | Wasted (mostly empty) travel |
| `riders_per_stop` | (boardings + alightings) per door opening | Whether a policy groups passengers into shared stops |
| `full_passby_share` | passengers whose own car stood at their floor, heading their way, full | Whether capacity actually bound in this run; "a car reached capacity" alone doesn't show that |

## Benchmark only (`elevator-sim bench`: `raw.jsonl`, `summary.json`, `summary.md`)

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
| `runs`, `passengers_total`, `unserved_total`, `wait_max_worst` | per policy: runs, passengers and unserved summed over seeds; the longest single wait in any run | Evidence for the brief's first objective (everyone served, and how long the worst case waited), from the committed summaries alone |
| Δ, Δ% | mean(policy − baseline), paired by seed | Size of the effect |
| wins / losses | seeds where the policy is strictly better / worse | Consistency: an average can hide a policy that wins big once and loses often |
| 95% CI of Δ | paired percentile bootstrap, 2,000 resamples | Uncertainty: is the effect distinguishable from 0? |
| gap closed | (excess_baseline − excess_policy) / excess_baseline | Share of the removable time a policy removes: 0% = no better than the baseline, 100% = reaches B0 |
| verdict | better / worse / inconclusive | A claim needs the CI to exclude 0 *and* ≥ 80% of seeds to agree; only claimed results go in this README |
| parking vs stay | for each parking policy: Δ mean total, mean wait, max wait and floors travelled per passenger vs `stay`, paired by seed | What parking buys (shorter waits) and what it costs (extra travel) |
| fairness frontier | for each `cost:<α>`: mean total, mean / p95 / max wait, and Δ total, Δ p95, Δ max vs plain `cost` with verdicts | Shows what the fairness weight buys (shorter tails) and what it costs (mean total time) |
