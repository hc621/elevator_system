# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.18 requests/tick) · 800 ticks | 33.1 | 20.5 | -37.9% | [-13.2, -11.9] | 20/20 | 61% | 12.5 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 35.7 | 23.2 | -34.8% | [-13.3, -11.5] | 20/20 | 65% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.18 requests/tick) · 800 ticks | 40.7 | 24.1 | -40.9% | [-17.8, -15.4] | 20/20 | 69% | 16.5 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 43.6 | 28.3 | -35.1% | [-15.8, -14.7] | 20/20 | 52% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks | 53.0 | 36.5 | -31.2% | [-17.8, -15.2] | 20/20 | 43% | 14.2 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.9 | 36.8 | -34.2% | [-20.0, -18.1] | 20/20 | 52% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks | 60.9 | 40.7 | -33.2% | [-21.4, -19.0] | 20/20 | 48% | 19.0 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 42.4 | 25.3 | -40.4% | [-17.7, -16.6] | 20/20 | 60% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.54 requests/tick) · 800 ticks | 46.6 | 28.9 | -37.9% | [-18.4, -16.9] | 20/20 | 54% | 14.1 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 53.6 | 28.2 | -47.4% | [-26.0, -24.8] | 20/20 | 73% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.54 requests/tick) · 800 ticks | 58.7 | 30.9 | -47.3% | [-28.3, -27.3] | 20/20 | 70% | 18.8 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 44.7 | 28.5 | -36.2% | [-16.8, -15.6] | 20/20 | 53% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks | 55.5 | 31.7 | -42.9% | [-25.7, -22.0] | 20/20 | 58% | 14.2 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.3 | 32.5 | -41.2% | [-23.5, -22.0] | 20/20 | 63% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks | 61.6 | 34.2 | -44.5% | [-28.1, -26.7] | 20/20 | 64% | 18.9 |

## Sensitivity: which conclusions survive

Varying: load. Cells: Δ mean total time vs the baseline; ✓ better, ✗ worse, ? inconclusive (claim rule above).

### `cost` vs `round_robin` (LOOK)

| scenario | building | load 1 | load 1.5 |
|---|---|---:|---:|
| quiet | 30 x 4 | -31% ✓ | -38% ✓ |
| quiet | 40 x 6 | -35% ✓ | -41% ✓ |
| morning_rush | 30 x 4 | -35% ✓ | -31% ✓ |
| morning_rush | 40 x 6 | -34% ✓ | -33% ✓ |
| lunch | 30 x 4 | -40% ✓ | -38% ✓ |
| lunch | 40 x 6 | -47% ✓ | -47% ✓ |
| evening_rush | 30 x 4 | -36% ✓ | -43% ✓ |
| evening_rush | 40 x 6 | -41% ✓ | -45% ✓ |

### `cost:0.05` vs `round_robin` (LOOK)

| scenario | building | load 1 | load 1.5 |
|---|---|---:|---:|
| quiet | 30 x 4 | -32% ✓ | -38% ✓ |
| quiet | 40 x 6 | -35% ✓ | -41% ✓ |
| morning_rush | 30 x 4 | -35% ✓ | -30% ✓ |
| morning_rush | 40 x 6 | -33% ✓ | -33% ✓ |
| lunch | 30 x 4 | -41% ✓ | -39% ✓ |
| lunch | 40 x 6 | -48% ✓ | -48% ✓ |
| evening_rush | 30 x 4 | -37% ✓ | -44% ✓ |
| evening_rush | 40 x 6 | -42% ✓ | -45% ✓ |

### `cost:0.2` vs `round_robin` (LOOK)

| scenario | building | load 1 | load 1.5 |
|---|---|---:|---:|
| quiet | 30 x 4 | -31% ✓ | -38% ✓ |
| quiet | 40 x 6 | -35% ✓ | -41% ✓ |
| morning_rush | 30 x 4 | -35% ✓ | -30% ✓ |
| morning_rush | 40 x 6 | -34% ✓ | -33% ✓ |
| lunch | 30 x 4 | -42% ✓ | -39% ✓ |
| lunch | 40 x 6 | -48% ✓ | -49% ✓ |
| evening_rush | 30 x 4 | -37% ✓ | -43% ✓ |
| evening_rush | 40 x 6 | -42% ✓ | -45% ✓ |

### `cost:1` vs `round_robin` (LOOK)

| scenario | building | load 1 | load 1.5 |
|---|---|---:|---:|
| quiet | 30 x 4 | -31% ✓ | -38% ✓ |
| quiet | 40 x 6 | -35% ✓ | -41% ✓ |
| morning_rush | 30 x 4 | -35% ✓ | -30% ✓ |
| morning_rush | 40 x 6 | -34% ✓ | -33% ✓ |
| lunch | 30 x 4 | -42% ✓ | -40% ✓ |
| lunch | 40 x 6 | -48% ✓ | -49% ✓ |
| evening_rush | 30 x 4 | -37% ✓ | -44% ✓ |
| evening_rush | 40 x 6 | -41% ✓ | -45% ✓ |

### Ranking by mean total time (LOOK, best first)

| scenario | building | load 1 | load 1.5 |
|---|---|---:|---:|
| quiet | 30 x 4 | cost:0.05 > cost:1 > cost:0.2 > cost > round_robin | cost:0.05 > cost:0.2 > cost:1 > cost > round_robin |
| quiet | 40 x 6 | cost:0.05 > cost:0.2 > cost > cost:1 > round_robin | cost:1 > cost:0.2 > cost:0.05 > cost > round_robin |
| morning_rush | 30 x 4 | cost:1 > cost > cost:0.2 > cost:0.05 > round_robin | cost > cost:0.05 > cost:0.2 > cost:1 > round_robin |
| morning_rush | 40 x 6 | cost:1 > cost > cost:0.2 > cost:0.05 > round_robin | cost > cost:0.05 > cost:1 > cost:0.2 > round_robin |
| lunch | 30 x 4 | cost:0.2 > cost:1 > cost:0.05 > cost > round_robin | cost:1 > cost:0.2 > cost:0.05 > cost > round_robin |
| lunch | 40 x 6 | cost:0.2 > cost:1 > cost:0.05 > cost > round_robin | cost:1 > cost:0.2 > cost:0.05 > cost > round_robin |
| evening_rush | 30 x 4 | cost:1 > cost:0.2 > cost:0.05 > cost > round_robin | cost:1 > cost:0.05 > cost:0.2 > cost > round_robin |
| evening_rush | 40 x 6 | cost:0.05 > cost:0.2 > cost:1 > cost > round_robin | cost:1 > cost:0.2 > cost > cost:0.05 > round_robin |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.6 ± 1.4 | -31.1% | [-9.71, -8.04] | 20/20 | 55% | better ✓ |
| cost:0.05 | 19.5 ± 1.4 | -31.5% | [-9.76, -8.23] | 20/20 | 56% | better ✓ |
| cost:0.2 | 19.5 ± 1.4 | -31.4% | [-9.73, -8.17] | 20/20 | 55% | better ✓ |
| cost:1 | 19.5 ± 1.4 | -31.4% | [-9.75, -8.17] | 20/20 | 55% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 19.6 | 6.0 | 18.3 | 26.4 |  |  |  |
| 0.05 | 19.5 | 5.9 | 17.9 | 26.6 | -0.1 ? | -0.4 ? | +0.2 ? |
| 0.2 | 19.5 | 5.9 | 17.6 | 25.7 | -0.1 ? | -0.6 ? | -0.7 ? |
| 1 | 19.5 | 5.9 | 17.6 | 25.7 | -0.1 ? | -0.6 ? | -0.7 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 28.5 | 15.0 | 36.2 | 47.8 | 16.1 | 0.63 |
| cost | look | 19.6 | 6.0 | 18.3 | 26.4 | 7.3 | 0.49 |
| cost:0.05 | look | 19.5 | 5.9 | 17.9 | 26.6 | 7.1 | 0.49 |
| cost:0.2 | look | 19.5 | 5.9 | 17.6 | 25.7 | 7.2 | 0.50 |
| cost:1 | look | 19.5 | 5.9 | 17.6 | 25.7 | 7.2 | 0.50 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 15.0 | 1.1 | 21% / 27 | 60% | 10.6 / 3.9 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |
| cost | look | 6.0 | 1.3 | 6% / 11 | 67% | 5.2 / 3.6 | 47% | 14.7 | 1.08 | 0.17 | 0.0% |
| cost:0.05 | look | 5.9 | 1.3 | 6% / 11 | 68% | 5.1 / 3.6 | 47% | 14.6 | 1.08 | 0.17 | 0.0% |
| cost:0.2 | look | 5.9 | 1.3 | 6% / 11 | 67% | 5.1 / 3.6 | 47% | 14.7 | 1.08 | 0.16 | 0.0% |
| cost:1 | look | 5.9 | 1.3 | 6% / 11 | 67% | 5.1 / 3.6 | 47% | 14.6 | 1.08 | 0.17 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 23, 14.0 / 33 | 24, 15.2 / 34 | 46, 15.3 / 36 |
| cost | look | 23, 4.4 / 16 | 24, 6.4 / 18 | 46, 6.4 / 17 |
| cost:0.05 | look | 23, 4.2 / 15 | 24, 6.4 / 17 | 46, 6.3 / 17 |
| cost:0.2 | look | 23, 4.1 / 14 | 24, 6.4 / 17 | 46, 6.3 / 17 |
| cost:1 | look | 23, 4.1 / 14 | 24, 6.4 / 17 | 46, 6.3 / 17 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.18 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 33.1; B0 floor = 12.5)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.5 ± 1.0 | -37.9% | [-13.18, -11.86] | 20/20 | 61% | better ✓ |
| cost:0.05 | 20.4 ± 1.0 | -38.2% | [-13.27, -11.94] | 20/20 | 61% | better ✓ |
| cost:0.2 | 20.4 ± 1.1 | -38.2% | [-13.24, -11.96] | 20/20 | 61% | better ✓ |
| cost:1 | 20.5 ± 1.1 | -38.1% | [-13.23, -11.90] | 20/20 | 61% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20.5 | 6.6 | 18.9 | 27.1 |  |  |  |
| 0.05 | 20.4 | 6.5 | 18.3 | 26.9 | -0.1 ? | -0.6 ? | -0.2 ? |
| 0.2 | 20.4 | 6.4 | 18.6 | 26.4 | -0.1 ? | -0.3 ? | -0.7 ? |
| 1 | 20.5 | 6.5 | 18.7 | 26.8 | -0.1 ? | -0.2 ? | -0.2 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 33.1 | 19.2 | 44.0 | 55.7 | 20.6 | 0.67 |
| cost | look | 20.5 | 6.6 | 18.9 | 27.1 | 8.0 | 0.53 |
| cost:0.05 | look | 20.4 | 6.5 | 18.3 | 26.9 | 7.9 | 0.53 |
| cost:0.2 | look | 20.4 | 6.4 | 18.6 | 26.4 | 7.9 | 0.53 |
| cost:1 | look | 20.5 | 6.5 | 18.7 | 26.8 | 8.0 | 0.53 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 19.2 | 1.3 | 35% / 30 | 28% | 10.4 / 4.0 | 85% | 18.8 | 1.09 | 0.01 | 0.0% |
| cost | look | 6.6 | 1.5 | 9% / 12 | 50% | 5.3 / 3.3 | 64% | 13.4 | 1.13 | 0.12 | 0.0% |
| cost:0.05 | look | 6.5 | 1.5 | 10% / 11 | 51% | 5.2 / 3.2 | 64% | 13.3 | 1.13 | 0.13 | 0.0% |
| cost:0.2 | look | 6.4 | 1.5 | 9% / 11 | 51% | 5.2 / 3.2 | 64% | 13.3 | 1.13 | 0.12 | 0.0% |
| cost:1 | look | 6.5 | 1.5 | 10% / 11 | 50% | 5.2 / 3.2 | 64% | 13.3 | 1.13 | 0.14 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 36, 18.6 / 42 | 35, 18.8 / 42 | 68, 19.7 / 44 |
| cost | look | 36, 5.5 / 18 | 35, 6.9 / 19 | 68, 6.9 / 18 |
| cost:0.05 | look | 36, 5.2 / 17 | 35, 6.8 / 18 | 68, 6.9 / 17 |
| cost:0.2 | look | 36, 5.3 / 17 | 35, 6.8 / 18 | 68, 6.8 / 18 |
| cost:1 | look | 36, 5.4 / 18 | 35, 6.7 / 18 | 68, 6.9 / 18 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.7; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.2 ± 1.3 | -34.8% | [-13.31, -11.53] | 20/20 | 65% | better ✓ |
| cost:0.05 | 23.2 ± 1.3 | -34.9% | [-13.34, -11.56] | 20/20 | 65% | better ✓ |
| cost:0.2 | 23.2 ± 1.3 | -34.9% | [-13.33, -11.57] | 20/20 | 65% | better ✓ |
| cost:1 | 23.2 ± 1.4 | -34.8% | [-13.27, -11.56] | 20/20 | 65% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 23.2 | 5.4 | 17.7 | 29.9 |  |  |  |
| 0.05 | 23.2 | 5.4 | 17.4 | 29.9 | -0.0 ? | -0.3 ? | +0.0 ? |
| 0.2 | 23.2 | 5.4 | 17.2 | 29.4 | -0.0 ? | -0.5 ? | -0.5 ? |
| 1 | 23.2 | 5.4 | 17.2 | 29.4 | +0.0 ? | -0.5 ? | -0.5 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 35.7 | 18.0 | 43.2 | 62.1 | 19.1 | 0.63 |
| cost | look | 23.2 | 5.4 | 17.7 | 29.9 | 6.7 | 0.44 |
| cost:0.05 | look | 23.2 | 5.4 | 17.4 | 29.9 | 6.7 | 0.44 |
| cost:0.2 | look | 23.2 | 5.4 | 17.2 | 29.4 | 6.7 | 0.44 |
| cost:1 | look | 23.2 | 5.4 | 17.2 | 29.4 | 6.7 | 0.44 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 18.0 | 1.1 | 16% / 34 | 71% | 14.2 / 3.6 | 60% | 30.0 | 1.02 | 0.03 | 0.0% |
| cost | look | 5.4 | 1.3 | 5% / 11 | 71% | 4.9 / 3.3 | 39% | 18.5 | 1.07 | 0.26 | 0.0% |
| cost:0.05 | look | 5.4 | 1.3 | 5% / 12 | 71% | 4.9 / 3.4 | 38% | 18.3 | 1.07 | 0.26 | 0.0% |
| cost:0.2 | look | 5.4 | 1.3 | 5% / 11 | 71% | 4.8 / 3.4 | 38% | 18.3 | 1.07 | 0.27 | 0.0% |
| cost:1 | look | 5.4 | 1.3 | 5% / 11 | 71% | 4.9 / 3.4 | 38% | 18.4 | 1.07 | 0.27 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 25, 17.2 / 42 | 22, 17.8 / 41 | 48, 18.4 / 41 |
| cost | look | 25, 3.6 / 15 | 22, 6.1 / 16 | 48, 6.0 / 17 |
| cost:0.05 | look | 25, 3.7 / 15 | 22, 6.0 / 16 | 48, 6.0 / 17 |
| cost:0.2 | look | 25, 3.7 / 15 | 22, 6.0 / 16 | 48, 5.9 / 17 |
| cost:1 | look | 25, 3.7 / 15 | 22, 6.1 / 16 | 48, 5.9 / 17 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.18 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 40.7; B0 floor = 16.5)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.1 ± 1.3 | -40.9% | [-17.81, -15.39] | 20/20 | 69% | better ✓ |
| cost:0.05 | 24.1 ± 1.3 | -40.9% | [-17.84, -15.36] | 20/20 | 69% | better ✓ |
| cost:0.2 | 24.0 ± 1.3 | -41.0% | [-17.91, -15.38] | 20/20 | 69% | better ✓ |
| cost:1 | 23.9 ± 1.3 | -41.2% | [-17.99, -15.46] | 20/20 | 69% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 24.1 | 6.2 | 19.3 | 33.0 |  |  |  |
| 0.05 | 24.1 | 6.2 | 18.8 | 32.9 | -0.0 ? | -0.5 ? | -0.1 ? |
| 0.2 | 24.0 | 6.1 | 18.7 | 31.6 | -0.1 ? | -0.6 ? | -1.4 ? |
| 1 | 23.9 | 6.0 | 18.3 | 31.2 | -0.1 ? | -1.0 ? | -1.9 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 40.7 | 23.0 | 54.9 | 71.3 | 24.2 | 0.64 |
| cost | look | 24.1 | 6.2 | 19.3 | 33.0 | 7.6 | 0.47 |
| cost:0.05 | look | 24.1 | 6.2 | 18.8 | 32.9 | 7.6 | 0.48 |
| cost:0.2 | look | 24.0 | 6.1 | 18.7 | 31.6 | 7.5 | 0.48 |
| cost:1 | look | 23.9 | 6.0 | 18.3 | 31.2 | 7.4 | 0.48 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 23.0 | 1.2 | 31% / 39 | 41% | 13.8 / 3.7 | 79% | 26.8 | 1.06 | 0.02 | 0.0% |
| cost | look | 6.2 | 1.4 | 8% / 11 | 58% | 5.3 / 3.3 | 55% | 17.4 | 1.10 | 0.15 | 0.0% |
| cost:0.05 | look | 6.2 | 1.4 | 7% / 11 | 58% | 5.3 / 3.3 | 54% | 17.3 | 1.11 | 0.17 | 0.0% |
| cost:0.2 | look | 6.1 | 1.4 | 7% / 11 | 58% | 5.3 / 3.2 | 54% | 17.3 | 1.11 | 0.17 | 0.0% |
| cost:1 | look | 6.0 | 1.4 | 7% / 11 | 59% | 5.2 / 3.2 | 54% | 17.2 | 1.10 | 0.16 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 38, 23.4 / 54 | 32, 23.8 / 53 | 70, 22.5 / 53 |
| cost | look | 38, 5.3 / 20 | 32, 6.3 / 17 | 70, 6.6 / 18 |
| cost:0.05 | look | 38, 5.2 / 19 | 32, 6.4 / 17 | 70, 6.6 / 18 |
| cost:0.2 | look | 38, 5.1 / 19 | 32, 6.3 / 17 | 70, 6.5 / 18 |
| cost:1 | look | 38, 5.0 / 18 | 32, 6.2 / 17 | 70, 6.5 / 18 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.3 ± 1.1 | -35.1% | [-15.84, -14.71] | 20/20 | 52% | better ✓ |
| cost:0.05 | 28.5 ± 1.4 | -34.7% | [-15.75, -14.40] | 20/20 | 51% | better ✓ |
| cost:0.2 | 28.3 ± 1.4 | -35.1% | [-15.96, -14.62] | 20/20 | 52% | better ✓ |
| cost:1 | 28.2 ± 1.3 | -35.4% | [-16.01, -14.80] | 20/20 | 52% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 28.3 | 11.2 | 25.9 | 38.0 |  |  |  |
| 0.05 | 28.5 | 11.2 | 25.6 | 34.8 | +0.2 ? | -0.3 ? | -3.2 ? |
| 0.2 | 28.3 | 11.0 | 24.9 | 32.8 | +0.0 ? | -1.0 ? | -5.2 ? |
| 1 | 28.2 | 10.9 | 24.6 | 33.0 | -0.1 ? | -1.3 ✓ | -5.0 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 43.6 | 26.9 | 55.2 | 64.1 | 29.5 | 0.71 |
| cost | look | 28.3 | 11.2 | 25.9 | 38.0 | 14.2 | 0.64 |
| cost:0.05 | look | 28.5 | 11.2 | 25.6 | 34.8 | 14.4 | 0.66 |
| cost:0.2 | look | 28.3 | 11.0 | 24.9 | 32.8 | 14.2 | 0.66 |
| cost:1 | look | 28.2 | 10.9 | 24.6 | 33.0 | 14.1 | 0.66 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 26.9 | 2.6 | 50% / 40 | 2% | 11.8 / 4.6 | 98% | 9.7 | 1.56 | 0.01 | 0.0% |
| cost | look | 11.2 | 3.0 | 8% / 19 | 14% | 9.8 / 4.4 | 79% | 7.5 | 1.67 | 0.11 | 0.0% |
| cost:0.05 | look | 11.2 | 3.2 | 7% / 18 | 15% | 10.0 / 4.4 | 78% | 7.4 | 1.67 | 0.11 | 0.0% |
| cost:0.2 | look | 11.0 | 3.2 | 7% / 17 | 15% | 9.9 / 4.3 | 77% | 7.3 | 1.67 | 0.12 | 0.0% |
| cost:1 | look | 10.9 | 3.2 | 6% / 16 | 15% | 9.8 / 4.3 | 77% | 7.3 | 1.67 | 0.12 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 234, 26.7 / 55 | 24, 27.1 / 53 | 46, 28.0 / 54 |
| cost | look | 234, 11.8 / 26 | 24, 8.7 / 20 | 46, 9.5 / 25 |
| cost:0.05 | look | 234, 11.9 / 26 | 24, 8.5 / 19 | 46, 9.1 / 23 |
| cost:0.2 | look | 234, 11.7 / 25 | 24, 8.4 / 19 | 46, 8.9 / 22 |
| cost:1 | look | 234, 11.5 / 25 | 24, 8.4 / 19 | 46, 8.9 / 21 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 53.0; B0 floor = 14.2)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.5 ± 4.0 | -31.2% | [-17.77, -15.25] | 20/20 | 43% | better ✓ |
| cost:0.05 | 36.9 ± 4.9 | -30.5% | [-17.38, -14.88] | 20/20 | 42% | better ✓ |
| cost:0.2 | 37.1 ± 4.6 | -30.1% | [-17.25, -14.61] | 20/20 | 41% | better ✓ |
| cost:1 | 37.4 ± 5.4 | -29.5% | [-16.85, -14.43] | 20/20 | 40% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 36.5 | 18.6 | 39.9 | 61.7 |  |  |  |
| 0.05 | 36.9 | 18.9 | 38.6 | 53.8 | +0.4 ? | -1.3 ? | -8.0 ? |
| 0.2 | 37.1 | 19.0 | 38.1 | 51.4 | +0.6 ? | -1.8 ? | -10.3 ✓ |
| 1 | 37.4 | 19.3 | 38.3 | 52.2 | +0.9 ? | -1.6 ? | -9.4 ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 53.0 | 35.2 | 69.0 | 147.4 | 38.8 | 0.73 |
| cost | look | 36.5 | 18.6 | 39.9 | 61.7 | 22.3 | 0.70 |
| cost:0.05 | look | 36.9 | 18.9 | 38.6 | 53.8 | 22.7 | 0.73 |
| cost:0.2 | look | 37.1 | 19.0 | 38.1 | 51.4 | 22.9 | 0.74 |
| cost:1 | look | 37.4 | 19.3 | 38.3 | 52.2 | 23.2 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 35.2 | 3.6 | 51% / 46 | 1% | 12.3 / 5.0 | 97% | 6.4 | 1.73 | 0.00 | 7.5% |
| cost | look | 18.6 | 3.7 | 22% / 31 | 5% | 13.4 / 4.4 | 93% | 5.8 | 1.80 | 0.06 | 0.7% |
| cost:0.05 | look | 18.9 | 3.8 | 23% / 30 | 5% | 13.6 / 4.3 | 93% | 5.8 | 1.79 | 0.05 | 0.6% |
| cost:0.2 | look | 19.0 | 3.8 | 22% / 30 | 5% | 13.9 / 4.2 | 93% | 5.8 | 1.78 | 0.06 | 0.5% |
| cost:1 | look | 19.3 | 3.8 | 22% / 30 | 5% | 13.9 / 4.2 | 93% | 5.8 | 1.78 | 0.05 | 1.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 351, 35.7 / 70 | 35, 31.1 / 60 | 68, 34.8 / 68 |
| cost | look | 351, 20.3 / 40 | 35, 10.8 / 26 | 68, 13.6 / 37 |
| cost:0.05 | look | 351, 20.7 / 39 | 35, 11.8 / 28 | 68, 13.2 / 32 |
| cost:0.2 | look | 351, 20.9 / 39 | 35, 11.7 / 28 | 68, 12.7 / 30 |
| cost:1 | look | 351, 21.3 / 39 | 35, 11.8 / 28 | 68, 12.8 / 30 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.8 ± 1.8 | -34.2% | [-20.03, -18.08] | 20/20 | 52% | better ✓ |
| cost:0.05 | 37.4 ± 1.9 | -33.1% | [-19.42, -17.54] | 20/20 | 50% | better ✓ |
| cost:0.2 | 37.0 ± 1.7 | -33.9% | [-19.78, -17.99] | 20/20 | 51% | better ✓ |
| cost:1 | 36.7 ± 1.7 | -34.3% | [-20.03, -18.21] | 20/20 | 52% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 36.8 | 14.5 | 33.3 | 42.6 |  |  |  |
| 0.05 | 37.4 | 14.9 | 33.1 | 39.6 | +0.6 ✗ | -0.2 ? | -3.0 ? |
| 0.2 | 37.0 | 14.5 | 32.8 | 39.0 | +0.2 ? | -0.5 ? | -3.6 ? |
| 1 | 36.7 | 14.3 | 32.5 | 38.9 | -0.1 ? | -0.8 ? | -3.7 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 55.9 | 34.5 | 70.9 | 81.9 | 36.9 | 0.71 |
| cost | look | 36.8 | 14.5 | 33.3 | 42.6 | 17.9 | 0.65 |
| cost:0.05 | look | 37.4 | 14.9 | 33.1 | 39.6 | 18.4 | 0.67 |
| cost:0.2 | look | 37.0 | 14.5 | 32.8 | 39.0 | 18.0 | 0.66 |
| cost:1 | look | 36.7 | 14.3 | 32.5 | 38.9 | 17.8 | 0.66 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 34.5 | 2.4 | 49% / 52 | 3% | 15.8 / 4.1 | 96% | 14.6 | 1.50 | 0.01 | 0.0% |
| cost | look | 14.5 | 3.4 | 6% / 23 | 16% | 13.4 / 5.0 | 65% | 9.3 | 1.67 | 0.18 | 0.0% |
| cost:0.05 | look | 14.9 | 3.5 | 5% / 22 | 17% | 13.9 / 5.1 | 64% | 9.1 | 1.67 | 0.19 | 0.0% |
| cost:0.2 | look | 14.5 | 3.5 | 5% / 20 | 17% | 13.6 / 5.0 | 64% | 9.1 | 1.67 | 0.21 | 0.0% |
| cost:1 | look | 14.3 | 3.5 | 4% / 20 | 17% | 13.3 / 5.0 | 64% | 9.1 | 1.66 | 0.20 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 249, 34.0 / 71 | 22, 37.0 / 67 | 48, 36.1 / 71 |
| cost | look | 249, 15.8 / 34 | 22, 8.7 / 21 | 48, 9.9 / 27 |
| cost:0.05 | look | 249, 16.4 / 34 | 22, 9.3 / 21 | 48, 9.7 / 26 |
| cost:0.2 | look | 249, 15.9 / 33 | 22, 9.4 / 21 | 48, 9.4 / 25 |
| cost:1 | look | 249, 15.6 / 33 | 22, 9.5 / 21 | 48, 9.3 / 25 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 60.9; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 40.7 ± 2.0 | -33.2% | [-21.41, -19.01] | 20/20 | 48% | better ✓ |
| cost:0.05 | 41.0 ± 2.2 | -32.6% | [-21.16, -18.62] | 20/20 | 47% | better ✓ |
| cost:0.2 | 41.1 ± 2.3 | -32.5% | [-21.13, -18.63] | 20/20 | 47% | better ✓ |
| cost:1 | 41.0 ± 2.1 | -32.6% | [-21.10, -18.65] | 20/20 | 47% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 40.7 | 18.0 | 36.4 | 51.8 |  |  |  |
| 0.05 | 41.0 | 18.2 | 35.6 | 45.0 | +0.3 ? | -0.8 ? | -6.7 ✓ |
| 0.2 | 41.1 | 18.2 | 35.3 | 44.8 | +0.4 ? | -1.2 ? | -7.0 ✓ |
| 1 | 41.0 | 18.1 | 35.1 | 44.4 | +0.4 ? | -1.3 ? | -7.3 ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 60.9 | 38.5 | 76.7 | 105.2 | 41.9 | 0.72 |
| cost | look | 40.7 | 18.0 | 36.4 | 51.8 | 21.7 | 0.72 |
| cost:0.05 | look | 41.0 | 18.2 | 35.6 | 45.0 | 22.1 | 0.74 |
| cost:0.2 | look | 41.1 | 18.2 | 35.3 | 44.8 | 22.1 | 0.74 |
| cost:1 | look | 41.0 | 18.1 | 35.1 | 44.4 | 22.1 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 38.5 | 3.4 | 50% / 56 | 1% | 16.4 / 4.6 | 97% | 9.8 | 1.64 | 0.00 | 0.9% |
| cost | look | 18.0 | 3.7 | 8% / 26 | 10% | 16.4 / 4.3 | 83% | 8.0 | 1.74 | 0.09 | 0.0% |
| cost:0.05 | look | 18.2 | 3.9 | 7% / 24 | 11% | 16.7 / 4.2 | 82% | 7.8 | 1.73 | 0.09 | 0.0% |
| cost:0.2 | look | 18.2 | 3.9 | 6% / 23 | 11% | 16.8 / 4.1 | 81% | 7.7 | 1.73 | 0.09 | 0.0% |
| cost:1 | look | 18.1 | 3.9 | 6% / 24 | 11% | 16.7 / 4.1 | 81% | 7.7 | 1.72 | 0.09 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 368, 38.3 / 77 | 32, 39.0 / 75 | 70, 39.4 / 77 |
| cost | look | 368, 20.0 / 37 | 32, 9.4 / 24 | 70, 11.4 / 33 |
| cost:0.05 | look | 368, 20.4 / 36 | 32, 9.4 / 21 | 70, 10.3 / 27 |
| cost:0.2 | look | 368, 20.4 / 36 | 32, 9.8 / 22 | 70, 10.2 / 28 |
| cost:1 | look | 368, 20.3 / 36 | 32, 9.8 / 22 | 70, 10.5 / 28 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.3 ± 1.3 | -40.4% | [-17.67, -16.55] | 20/20 | 60% | better ✓ |
| cost:0.05 | 25.0 ± 1.1 | -41.0% | [-17.85, -16.90] | 20/20 | 61% | better ✓ |
| cost:0.2 | 24.8 ± 1.0 | -41.5% | [-18.07, -17.15] | 20/20 | 62% | better ✓ |
| cost:1 | 24.8 ± 0.8 | -41.5% | [-18.02, -17.22] | 20/20 | 62% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 25.3 | 9.2 | 24.5 | 37.0 |  |  |  |
| 0.05 | 25.0 | 8.8 | 23.2 | 34.6 | -0.2 ? | -1.3 ? | -2.4 ? |
| 0.2 | 24.8 | 8.6 | 22.4 | 33.5 | -0.5 ? | -2.0 ? | -3.5 ? |
| 1 | 24.8 | 8.6 | 22.6 | 34.4 | -0.5 ? | -1.8 ? | -2.6 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 42.4 | 26.3 | 54.0 | 63.0 | 28.3 | 0.72 |
| cost | look | 25.3 | 9.2 | 24.5 | 37.0 | 11.2 | 0.57 |
| cost:0.05 | look | 25.0 | 8.8 | 23.2 | 34.6 | 11.0 | 0.58 |
| cost:0.2 | look | 24.8 | 8.6 | 22.4 | 33.5 | 10.7 | 0.58 |
| cost:1 | look | 24.8 | 8.6 | 22.6 | 34.4 | 10.7 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 26.3 | 2.0 | 48% / 38 | 3% | 10.6 / 4.0 | 97% | 10.5 | 1.50 | 0.01 | 0.0% |
| cost | look | 9.2 | 2.0 | 16% / 16 | 14% | 6.6 / 3.6 | 90% | 9.4 | 1.51 | 0.09 | 0.0% |
| cost:0.05 | look | 8.8 | 2.1 | 15% / 15 | 15% | 6.4 / 3.5 | 90% | 9.3 | 1.51 | 0.10 | 0.0% |
| cost:0.2 | look | 8.6 | 2.1 | 13% / 15 | 16% | 6.3 / 3.4 | 90% | 9.3 | 1.50 | 0.08 | 0.0% |
| cost:1 | look | 8.6 | 2.2 | 14% / 15 | 16% | 6.3 / 3.4 | 90% | 9.3 | 1.50 | 0.10 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 114, 25.3 / 54 | 120, 26.7 / 53 | 46, 27.7 / 53 |
| cost | look | 114, 7.9 / 23 | 120, 9.9 / 25 | 46, 10.2 / 25 |
| cost:0.05 | look | 114, 7.6 / 22 | 120, 9.6 / 24 | 46, 9.8 / 23 |
| cost:0.2 | look | 114, 7.2 / 21 | 120, 9.5 / 23 | 46, 9.6 / 22 |
| cost:1 | look | 114, 7.2 / 22 | 120, 9.4 / 23 | 46, 9.5 / 22 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.54 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 46.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.9 ± 1.9 | -37.9% | [-18.37, -16.90] | 20/20 | 54% | better ✓ |
| cost:0.05 | 28.6 ± 2.0 | -38.7% | [-18.76, -17.22] | 20/20 | 56% | better ✓ |
| cost:0.2 | 28.5 ± 2.0 | -38.9% | [-18.75, -17.42] | 20/20 | 56% | better ✓ |
| cost:1 | 28.1 ± 1.1 | -39.8% | [-18.97, -18.13] | 20/20 | 57% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 28.9 | 12.1 | 30.1 | 50.6 |  |  |  |
| 0.05 | 28.6 | 11.6 | 29.0 | 47.4 | -0.4 ? | -1.1 ? | -3.3 ? |
| 0.2 | 28.5 | 11.4 | 29.3 | 48.1 | -0.5 ? | -0.7 ? | -2.5 ? |
| 1 | 28.1 | 11.0 | 28.4 | 43.2 | -0.9 ? | -1.7 ? | -7.4 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 46.6 | 29.7 | 59.2 | 68.1 | 32.5 | 0.73 |
| cost | look | 28.9 | 12.1 | 30.1 | 50.6 | 14.8 | 0.61 |
| cost:0.05 | look | 28.6 | 11.6 | 29.0 | 47.4 | 14.4 | 0.61 |
| cost:0.2 | look | 28.5 | 11.4 | 29.3 | 48.1 | 14.4 | 0.60 |
| cost:1 | look | 28.1 | 11.0 | 28.4 | 43.2 | 13.9 | 0.60 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 29.7 | 2.8 | 47% / 43 | 1% | 11.1 / 4.3 | 98% | 6.8 | 1.66 | 0.00 | 0.0% |
| cost | look | 12.1 | 2.7 | 20% / 21 | 4% | 7.5 / 4.1 | 96% | 6.5 | 1.73 | 0.08 | 0.1% |
| cost:0.05 | look | 11.6 | 2.9 | 19% / 20 | 4% | 7.3 / 3.9 | 96% | 6.4 | 1.72 | 0.08 | 0.0% |
| cost:0.2 | look | 11.4 | 3.0 | 19% / 20 | 5% | 7.2 / 3.9 | 96% | 6.4 | 1.71 | 0.08 | 0.1% |
| cost:1 | look | 11.0 | 3.0 | 19% / 19 | 5% | 7.0 / 3.8 | 96% | 6.4 | 1.70 | 0.08 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 176, 28.6 / 58 | 180, 30.6 / 59 | 68, 30.1 / 60 |
| cost | look | 176, 11.0 / 29 | 180, 12.8 / 30 | 68, 13.1 / 32 |
| cost:0.05 | look | 176, 10.6 / 28 | 180, 12.1 / 29 | 68, 12.4 / 29 |
| cost:0.2 | look | 176, 10.2 / 28 | 180, 12.4 / 30 | 68, 11.7 / 28 |
| cost:1 | look | 176, 9.9 / 27 | 180, 11.9 / 29 | 68, 11.4 / 27 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 53.6; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.2 ± 1.0 | -47.4% | [-26.01, -24.84] | 20/20 | 73% | better ✓ |
| cost:0.05 | 28.1 ± 1.0 | -47.5% | [-26.13, -24.85] | 20/20 | 73% | better ✓ |
| cost:0.2 | 28.1 ± 0.9 | -47.7% | [-26.28, -24.88] | 20/20 | 73% | better ✓ |
| cost:1 | 28.1 ± 1.0 | -47.6% | [-26.21, -24.84] | 20/20 | 73% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 28.2 | 7.5 | 21.4 | 37.8 |  |  |  |
| 0.05 | 28.1 | 7.4 | 20.9 | 36.8 | -0.1 ? | -0.5 ? | -1.0 ? |
| 0.2 | 28.1 | 7.3 | 21.0 | 36.2 | -0.1 ? | -0.3 ? | -1.6 ? |
| 1 | 28.1 | 7.3 | 21.3 | 36.0 | -0.1 ? | -0.1 ? | -1.7 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 53.6 | 33.1 | 69.7 | 81.6 | 34.9 | 0.71 |
| cost | look | 28.2 | 7.5 | 21.4 | 37.8 | 9.5 | 0.53 |
| cost:0.05 | look | 28.1 | 7.4 | 20.9 | 36.8 | 9.4 | 0.54 |
| cost:0.2 | look | 28.1 | 7.3 | 21.0 | 36.2 | 9.3 | 0.53 |
| cost:1 | look | 28.1 | 7.3 | 21.3 | 36.0 | 9.4 | 0.52 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 33.1 | 1.9 | 46% / 49 | 4% | 14.3 / 3.9 | 95% | 16.0 | 1.43 | 0.01 | 0.0% |
| cost | look | 7.5 | 2.0 | 10% / 14 | 23% | 6.0 / 3.3 | 82% | 13.0 | 1.45 | 0.13 | 0.0% |
| cost:0.05 | look | 7.4 | 2.0 | 9% / 13 | 24% | 6.0 / 3.2 | 82% | 12.8 | 1.45 | 0.13 | 0.0% |
| cost:0.2 | look | 7.3 | 2.0 | 9% / 14 | 24% | 5.9 / 3.2 | 82% | 12.9 | 1.44 | 0.14 | 0.0% |
| cost:1 | look | 7.3 | 2.1 | 9% / 14 | 25% | 6.0 / 3.2 | 81% | 12.8 | 1.43 | 0.14 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 124, 32.6 / 69 | 116, 33.3 / 69 | 48, 33.3 / 68 |
| cost | look | 124, 6.6 / 20 | 116, 8.1 / 22 | 48, 8.5 / 23 |
| cost:0.05 | look | 124, 6.5 / 20 | 116, 8.0 / 21 | 48, 8.2 / 21 |
| cost:0.2 | look | 124, 6.2 / 20 | 116, 8.0 / 21 | 48, 8.4 / 22 |
| cost:1 | look | 124, 6.3 / 20 | 116, 8.1 / 22 | 48, 8.2 / 22 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.54 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 58.7; B0 floor = 18.8)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 30.9 ± 1.2 | -47.3% | [-28.32, -27.32] | 20/20 | 70% | better ✓ |
| cost:0.05 | 30.6 ± 1.2 | -47.9% | [-28.75, -27.41] | 20/20 | 70% | better ✓ |
| cost:0.2 | 30.0 ± 1.3 | -48.9% | [-29.32, -28.10] | 20/20 | 72% | better ✓ |
| cost:1 | 30.0 ± 1.1 | -48.9% | [-29.36, -28.15] | 20/20 | 72% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 30.9 | 9.6 | 26.2 | 44.5 |  |  |  |
| 0.05 | 30.6 | 9.1 | 24.4 | 39.9 | -0.3 ? | -1.8 ? | -4.5 ? |
| 0.2 | 30.0 | 8.5 | 22.9 | 38.9 | -0.9 ? | -3.3 ✓ | -5.6 ? |
| 1 | 30.0 | 8.4 | 22.7 | 37.5 | -0.9 ✓ | -3.5 ✓ | -7.0 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 58.7 | 37.4 | 75.2 | 87.4 | 40.0 | 0.72 |
| cost | look | 30.9 | 9.6 | 26.2 | 44.5 | 12.2 | 0.56 |
| cost:0.05 | look | 30.6 | 9.1 | 24.4 | 39.9 | 11.8 | 0.57 |
| cost:0.2 | look | 30.0 | 8.5 | 22.9 | 38.9 | 11.3 | 0.56 |
| cost:1 | look | 30.0 | 8.4 | 22.7 | 37.5 | 11.2 | 0.56 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 37.4 | 2.5 | 48% / 54 | 2% | 14.6 / 4.1 | 97% | 10.6 | 1.58 | 0.01 | 0.0% |
| cost | look | 9.6 | 2.6 | 11% / 18 | 9% | 7.2 / 3.6 | 92% | 9.5 | 1.62 | 0.12 | 0.0% |
| cost:0.05 | look | 9.1 | 2.7 | 11% / 16 | 10% | 6.9 / 3.4 | 91% | 9.4 | 1.62 | 0.11 | 0.0% |
| cost:0.2 | look | 8.5 | 2.7 | 10% / 15 | 11% | 6.5 / 3.3 | 91% | 9.3 | 1.60 | 0.11 | 0.0% |
| cost:1 | look | 8.4 | 2.8 | 10% / 14 | 11% | 6.5 / 3.2 | 91% | 9.4 | 1.60 | 0.10 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 189, 36.8 / 75 | 174, 37.7 / 75 | 70, 38.2 / 75 |
| cost | look | 189, 8.7 / 25 | 174, 10.0 / 26 | 70, 10.5 / 26 |
| cost:0.05 | look | 189, 8.2 / 23 | 174, 9.8 / 25 | 70, 9.9 / 25 |
| cost:0.2 | look | 189, 7.6 / 22 | 174, 9.3 / 24 | 70, 9.1 / 23 |
| cost:1 | look | 189, 7.4 / 21 | 174, 9.3 / 24 | 70, 9.0 / 22 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.7; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.5 ± 1.3 | -36.2% | [-16.75, -15.57] | 20/20 | 53% | better ✓ |
| cost:0.05 | 28.3 ± 1.2 | -36.7% | [-16.99, -15.76] | 20/20 | 54% | better ✓ |
| cost:0.2 | 28.3 ± 1.2 | -36.7% | [-16.91, -15.88] | 20/20 | 54% | better ✓ |
| cost:1 | 28.1 ± 1.4 | -37.0% | [-17.10, -15.92] | 20/20 | 54% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 28.5 | 11.8 | 31.2 | 49.9 |  |  |  |
| 0.05 | 28.3 | 11.5 | 29.4 | 48.9 | -0.2 ? | -1.8 ? | -0.9 ? |
| 0.2 | 28.3 | 11.5 | 29.3 | 45.0 | -0.2 ? | -1.9 ? | -4.9 ✓ |
| 1 | 28.1 | 11.3 | 28.7 | 45.2 | -0.4 ? | -2.5 ✓ | -4.7 ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 44.7 | 27.7 | 55.8 | 75.1 | 30.4 | 0.73 |
| cost | look | 28.5 | 11.8 | 31.2 | 49.9 | 14.3 | 0.58 |
| cost:0.05 | look | 28.3 | 11.5 | 29.4 | 48.9 | 14.0 | 0.59 |
| cost:0.2 | look | 28.3 | 11.5 | 29.3 | 45.0 | 14.0 | 0.60 |
| cost:1 | look | 28.1 | 11.3 | 28.7 | 45.2 | 13.9 | 0.60 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 27.7 | 2.7 | 48% / 38 | 3% | 9.8 / 3.9 | 97% | 9.4 | 1.57 | 0.00 | 0.2% |
| cost | look | 11.8 | 2.4 | 23% / 19 | 13% | 7.3 / 3.9 | 92% | 8.7 | 1.57 | 0.07 | 0.1% |
| cost:0.05 | look | 11.5 | 2.5 | 22% / 18 | 14% | 7.2 / 3.9 | 91% | 8.5 | 1.57 | 0.07 | 0.3% |
| cost:0.2 | look | 11.5 | 2.5 | 21% / 18 | 14% | 7.3 / 4.0 | 91% | 8.5 | 1.57 | 0.07 | 0.4% |
| cost:1 | look | 11.3 | 2.5 | 21% / 17 | 14% | 7.3 / 3.9 | 91% | 8.5 | 1.57 | 0.07 | 0.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 23, 25.2 / 51 | 242, 27.8 / 56 | 46, 28.6 / 55 |
| cost | look | 23, 6.0 / 19 | 242, 12.1 / 31 | 46, 13.2 / 32 |
| cost:0.05 | look | 23, 6.1 / 19 | 242, 11.8 / 29 | 46, 12.7 / 31 |
| cost:0.2 | look | 23, 5.7 / 18 | 242, 11.8 / 29 | 46, 13.0 / 31 |
| cost:1 | look | 23, 5.7 / 17 | 242, 11.6 / 29 | 46, 12.6 / 30 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.5; B0 floor = 14.2)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.7 ± 1.2 | -42.9% | [-25.72, -22.03] | 20/20 | 58% | better ✓ |
| cost:0.05 | 31.4 ± 1.3 | -43.5% | [-26.07, -22.43] | 20/20 | 58% | better ✓ |
| cost:0.2 | 31.4 ± 1.2 | -43.4% | [-25.84, -22.48] | 20/20 | 58% | better ✓ |
| cost:1 | 31.3 ± 1.2 | -43.6% | [-25.98, -22.64] | 20/20 | 59% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 31.7 | 14.5 | 36.0 | 63.8 |  |  |  |
| 0.05 | 31.4 | 14.0 | 34.0 | 55.5 | -0.3 ? | -2.0 ? | -8.2 ? |
| 0.2 | 31.4 | 14.0 | 33.9 | 55.5 | -0.3 ? | -2.1 ? | -8.2 ✓ |
| 1 | 31.3 | 13.9 | 33.4 | 54.2 | -0.4 ? | -2.7 ✓ | -9.6 ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 55.5 | 37.7 | 85.7 | 318.5 | 41.3 | 0.56 |
| cost | look | 31.7 | 14.5 | 36.0 | 63.8 | 17.5 | 0.61 |
| cost:0.05 | look | 31.4 | 14.0 | 34.0 | 55.5 | 17.2 | 0.63 |
| cost:0.2 | look | 31.4 | 14.0 | 33.9 | 55.5 | 17.2 | 0.63 |
| cost:1 | look | 31.3 | 13.9 | 33.4 | 54.2 | 17.1 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 37.7 | 3.6 | 49% / 49 | 1% | 10.0 / 3.8 | 97% | 6.2 | 1.76 | 0.00 | 6.8% |
| cost | look | 14.5 | 3.0 | 28% / 22 | 3% | 7.3 / 4.0 | 97% | 5.9 | 1.84 | 0.05 | 1.7% |
| cost:0.05 | look | 14.0 | 3.1 | 28% / 21 | 3% | 7.2 / 3.8 | 97% | 5.9 | 1.81 | 0.05 | 1.5% |
| cost:0.2 | look | 14.0 | 3.2 | 27% / 21 | 4% | 7.4 / 3.8 | 97% | 5.9 | 1.80 | 0.06 | 2.3% |
| cost:1 | look | 13.9 | 3.2 | 28% / 20 | 4% | 7.3 / 3.7 | 96% | 5.9 | 1.79 | 0.06 | 1.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 36, 30.0 / 57 | 360, 39.5 / 99 | 68, 31.6 / 61 |
| cost | look | 36, 9.6 / 27 | 360, 14.8 / 36 | 68, 15.2 / 36 |
| cost:0.05 | look | 36, 9.8 / 28 | 360, 14.2 / 34 | 68, 15.1 / 35 |
| cost:0.2 | look | 36, 9.3 / 27 | 360, 14.3 / 34 | 68, 14.9 / 36 |
| cost:1 | look | 36, 9.2 / 26 | 360, 14.2 / 34 | 68, 14.5 / 34 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.3; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.5 ± 0.8 | -41.2% | [-23.50, -21.99] | 20/20 | 63% | better ✓ |
| cost:0.05 | 32.3 ± 0.8 | -41.6% | [-23.70, -22.27] | 20/20 | 63% | better ✓ |
| cost:0.2 | 32.3 ± 0.8 | -41.5% | [-23.64, -22.24] | 20/20 | 63% | better ✓ |
| cost:1 | 32.4 ± 0.9 | -41.4% | [-23.64, -22.13] | 20/20 | 63% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 32.5 | 11.4 | 32.6 | 50.7 |  |  |  |
| 0.05 | 32.3 | 11.1 | 31.5 | 46.1 | -0.2 ? | -1.1 ? | -4.5 ? |
| 0.2 | 32.3 | 11.1 | 31.1 | 45.7 | -0.2 ? | -1.5 ✓ | -5.0 ? |
| 1 | 32.4 | 11.1 | 31.2 | 46.4 | -0.1 ? | -1.4 ✓ | -4.3 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 55.3 | 34.1 | 70.5 | 81.5 | 36.4 | 0.72 |
| cost | look | 32.5 | 11.4 | 32.6 | 50.7 | 13.7 | 0.54 |
| cost:0.05 | look | 32.3 | 11.1 | 31.5 | 46.1 | 13.4 | 0.55 |
| cost:0.2 | look | 32.3 | 11.1 | 31.1 | 45.7 | 13.5 | 0.55 |
| cost:1 | look | 32.4 | 11.1 | 31.2 | 46.4 | 13.5 | 0.55 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 34.1 | 2.4 | 47% / 47 | 4% | 13.2 / 3.7 | 95% | 14.8 | 1.48 | 0.01 | 0.0% |
| cost | look | 11.4 | 2.2 | 15% / 17 | 25% | 8.5 / 4.0 | 83% | 12.4 | 1.44 | 0.12 | 0.0% |
| cost:0.05 | look | 11.1 | 2.3 | 14% / 16 | 26% | 8.3 / 3.9 | 82% | 12.1 | 1.45 | 0.11 | 0.0% |
| cost:0.2 | look | 11.1 | 2.3 | 14% / 15 | 26% | 8.3 / 3.9 | 82% | 12.1 | 1.45 | 0.12 | 0.0% |
| cost:1 | look | 11.1 | 2.4 | 13% / 16 | 26% | 8.3 / 3.9 | 81% | 12.0 | 1.45 | 0.13 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 25, 31.9 / 67 | 236, 33.8 / 70 | 48, 36.4 / 70 |
| cost | look | 25, 2.8 / 12 | 236, 12.2 / 33 | 48, 12.3 / 32 |
| cost:0.05 | look | 25, 2.5 / 11 | 236, 11.8 / 32 | 48, 12.6 / 32 |
| cost:0.2 | look | 25, 2.5 / 11 | 236, 11.7 / 31 | 48, 12.6 / 32 |
| cost:1 | look | 25, 2.4 / 10 | 236, 11.7 / 31 | 48, 12.7 / 32 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1.5 (0.585 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 61.6; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 34.2 ± 1.2 | -44.5% | [-28.14, -26.73] | 20/20 | 64% | better ✓ |
| cost:0.05 | 34.2 ± 1.4 | -44.5% | [-28.15, -26.71] | 20/20 | 64% | better ✓ |
| cost:0.2 | 33.9 ± 1.3 | -45.0% | [-28.45, -27.02] | 20/20 | 65% | better ✓ |
| cost:1 | 33.8 ± 1.1 | -45.2% | [-28.53, -27.12] | 20/20 | 65% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 34.2 | 12.5 | 34.3 | 60.0 |  |  |  |
| 0.05 | 34.2 | 12.4 | 33.3 | 54.7 | +0.0 ? | -1.0 ? | -5.3 ? |
| 0.2 | 33.9 | 12.1 | 32.5 | 52.6 | -0.3 ? | -1.8 ? | -7.4 ? |
| 1 | 33.8 | 11.9 | 31.9 | 51.5 | -0.4 ? | -2.4 ✓ | -8.6 ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 61.6 | 39.4 | 78.2 | 172.3 | 42.7 | 0.71 |
| cost | look | 34.2 | 12.5 | 34.3 | 60.0 | 15.3 | 0.56 |
| cost:0.05 | look | 34.2 | 12.4 | 33.3 | 54.7 | 15.3 | 0.58 |
| cost:0.2 | look | 33.9 | 12.1 | 32.5 | 52.6 | 15.0 | 0.57 |
| cost:1 | look | 33.8 | 11.9 | 31.9 | 51.5 | 14.9 | 0.58 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 39.4 | 3.3 | 48% / 54 | 1% | 13.1 / 4.0 | 96% | 9.8 | 1.64 | 0.00 | 1.3% |
| cost | look | 12.5 | 2.8 | 20% / 19 | 10% | 8.0 / 3.7 | 93% | 9.0 | 1.64 | 0.09 | 0.6% |
| cost:0.05 | look | 12.4 | 2.9 | 20% / 18 | 11% | 8.0 / 3.7 | 92% | 8.9 | 1.64 | 0.08 | 0.5% |
| cost:0.2 | look | 12.1 | 2.9 | 18% / 17 | 12% | 7.9 / 3.6 | 91% | 8.8 | 1.63 | 0.09 | 0.6% |
| cost:1 | look | 11.9 | 3.0 | 17% / 17 | 12% | 7.9 / 3.6 | 91% | 8.8 | 1.64 | 0.10 | 0.5% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| round_robin | look | 38, 36.2 / 75 | 356, 39.9 / 79 | 70, 38.8 / 76 |
| cost | look | 38, 5.9 / 19 | 356, 13.0 / 35 | 70, 13.6 / 34 |
| cost:0.05 | look | 38, 5.4 / 19 | 356, 12.9 / 34 | 70, 13.7 / 34 |
| cost:0.2 | look | 38, 4.9 / 17 | 356, 12.6 / 33 | 70, 13.3 / 32 |
| cost:1 | look | 38, 4.7 / 16 | 356, 12.5 / 33 | 70, 13.1 / 32 |
