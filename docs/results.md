[← README](../README.md) · [all studies](../README.md#detailed-studies)

# How results are measured

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

## Results: `cost` vs `round_robin` (LOOK motion, mean total time per passenger in ticks)

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

## Why `cost` wins: root cause (LOOK motion; from the diagnostics columns in `summary.md`)

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
