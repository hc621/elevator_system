# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| uniform · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 34.4 | 20.1 | -41.6% | [-14.9, -13.7] | 20/20 | 59% | 10.3 |
| uniform · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks | 47.1 | 27.3 | -41.9% | [-20.2, -19.2] | 20/20 | 54% | 10.4 |
| uniform · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 40.6 | 22.2 | -45.3% | [-19.3, -17.5] | 20/20 | 68% | 13.6 |
| uniform · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks | 56.5 | 27.6 | -51.1% | [-29.3, -28.4] | 20/20 | 67% | 13.6 |
| mixed · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 38.5 | 23.1 | -40.1% | [-15.8, -15.0] | 20/20 | 63% | 14.0 |
| mixed · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks | 47.3 | 29.2 | -38.3% | [-19.0, -17.3] | 20/20 | 54% | 14.0 |
| mixed · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 48.4 | 26.7 | -44.9% | [-22.6, -20.9] | 20/20 | 72% | 18.4 |
| mixed · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks | 58.8 | 31.3 | -46.8% | [-28.1, -26.9] | 20/20 | 68% | 18.6 |
| morning_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 39.3 | 27.0 | -31.2% | [-13.0, -11.4] | 20/20 | 49% | 14.3 |
| morning_rush · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks | 51.3 | 35.6 | -30.6% | [-16.4, -14.9] | 20/20 | 42% | 14.4 |
| morning_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 49.6 | 34.7 | -30.1% | [-15.8, -14.1] | 20/20 | 49% | 19.0 |
| morning_rush · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks | 59.4 | 40.0 | -32.7% | [-20.3, -18.6] | 20/20 | 48% | 19.1 |
| evening_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 39.4 | 26.7 | -32.3% | [-13.3, -12.2] | 20/20 | 51% | 14.3 |
| evening_rush · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks | 51.9 | 31.3 | -39.7% | [-22.1, -19.2] | 20/20 | 55% | 14.4 |
| evening_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 49.1 | 31.8 | -35.2% | [-18.0, -16.5] | 20/20 | 57% | 19.0 |
| evening_rush · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks | 60.4 | 34.2 | -43.3% | [-27.2, -25.2] | 20/20 | 63% | 19.1 |

## Sensitivity: which conclusions survive

Varying: rate. Cells: Δ mean total time vs the baseline; ✓ better, ✗ worse, ? inconclusive (claim rule above).

### `cost` vs `round_robin` (LOOK)

| scenario | building | 0.25/tick | 0.55/tick |
|---|---|---:|---:|
| uniform | 30 x 4 | -42% ✓ | -42% ✓ |
| uniform | 40 x 6 | -45% ✓ | -51% ✓ |
| mixed | 30 x 4 | -40% ✓ | -38% ✓ |
| mixed | 40 x 6 | -45% ✓ | -47% ✓ |
| morning_rush | 30 x 4 | -31% ✓ | -31% ✓ |
| morning_rush | 40 x 6 | -30% ✓ | -33% ✓ |
| evening_rush | 30 x 4 | -32% ✓ | -40% ✓ |
| evening_rush | 40 x 6 | -35% ✓ | -43% ✓ |

### `cost:0.05` vs `round_robin` (LOOK)

| scenario | building | 0.25/tick | 0.55/tick |
|---|---|---:|---:|
| uniform | 30 x 4 | -41% ✓ | -42% ✓ |
| uniform | 40 x 6 | -45% ✓ | -52% ✓ |
| mixed | 30 x 4 | -40% ✓ | -38% ✓ |
| mixed | 40 x 6 | -46% ✓ | -47% ✓ |
| morning_rush | 30 x 4 | -31% ✓ | -30% ✓ |
| morning_rush | 40 x 6 | -30% ✓ | -32% ✓ |
| evening_rush | 30 x 4 | -33% ✓ | -41% ✓ |
| evening_rush | 40 x 6 | -35% ✓ | -43% ✓ |

### `cost:0.2` vs `round_robin` (LOOK)

| scenario | building | 0.25/tick | 0.55/tick |
|---|---|---:|---:|
| uniform | 30 x 4 | -42% ✓ | -43% ✓ |
| uniform | 40 x 6 | -45% ✓ | -52% ✓ |
| mixed | 30 x 4 | -41% ✓ | -39% ✓ |
| mixed | 40 x 6 | -46% ✓ | -48% ✓ |
| morning_rush | 30 x 4 | -31% ✓ | -29% ✓ |
| morning_rush | 40 x 6 | -30% ✓ | -33% ✓ |
| evening_rush | 30 x 4 | -33% ✓ | -40% ✓ |
| evening_rush | 40 x 6 | -35% ✓ | -44% ✓ |

### `cost:1` vs `round_robin` (LOOK)

| scenario | building | 0.25/tick | 0.55/tick |
|---|---|---:|---:|
| uniform | 30 x 4 | -42% ✓ | -43% ✓ |
| uniform | 40 x 6 | -45% ✓ | -53% ✓ |
| mixed | 30 x 4 | -40% ✓ | -40% ✓ |
| mixed | 40 x 6 | -46% ✓ | -49% ✓ |
| morning_rush | 30 x 4 | -32% ✓ | -29% ✓ |
| morning_rush | 40 x 6 | -30% ✓ | -32% ✓ |
| evening_rush | 30 x 4 | -33% ✓ | -40% ✓ |
| evening_rush | 40 x 6 | -35% ✓ | -44% ✓ |

### Ranking by mean total time (LOOK, best first)

| scenario | building | 0.25/tick | 0.55/tick |
|---|---|---:|---:|
| uniform | 30 x 4 | cost:1 > cost:0.2 > cost > cost:0.05 > round_robin | cost:0.2 > cost:1 > cost:0.05 > cost > round_robin |
| uniform | 40 x 6 | cost > cost:0.2 > cost:1 > cost:0.05 > round_robin | cost:1 > cost:0.05 > cost:0.2 > cost > round_robin |
| mixed | 30 x 4 | cost:0.2 > cost:1 > cost:0.05 > cost > round_robin | cost:1 > cost:0.2 > cost:0.05 > cost > round_robin |
| mixed | 40 x 6 | cost:0.2 > cost:0.05 > cost:1 > cost > round_robin | cost:1 > cost:0.2 > cost:0.05 > cost > round_robin |
| morning_rush | 30 x 4 | cost:1 > cost:0.2 > cost > cost:0.05 > round_robin | cost > cost:0.05 > cost:1 > cost:0.2 > round_robin |
| morning_rush | 40 x 6 | cost > cost:0.2 > cost:1 > cost:0.05 > round_robin | cost > cost:0.2 > cost:1 > cost:0.05 > round_robin |
| evening_rush | 30 x 4 | cost:0.05 > cost:1 > cost:0.2 > cost > round_robin | cost:0.05 > cost:0.2 > cost:1 > cost > round_robin |
| evening_rush | 40 x 6 | cost:0.2 > cost:0.05 > cost:1 > cost > round_robin | cost:0.2 > cost:1 > cost > cost:0.05 > round_robin |

## uniform · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.4; B0 floor = 10.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.1 ± 0.7 | -41.6% | [-14.94, -13.74] | 20/20 | 59% | better ✓ |
| cost:0.05 | 20.2 ± 0.8 | -41.4% | [-14.95, -13.61] | 20/20 | 59% | better ✓ |
| cost:0.2 | 20.1 ± 0.8 | -41.7% | [-15.01, -13.73] | 20/20 | 60% | better ✓ |
| cost:1 | 20.0 ± 0.9 | -42.0% | [-15.09, -13.83] | 20/20 | 60% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20.1 | 8.0 | 21.4 | 33.5 |  |  |  |
| 0.05 | 20.2 | 8.0 | 20.8 | 31.7 | +0.1 ? | -0.5 ? | -1.8 ? |
| 0.2 | 20.1 | 7.9 | 20.5 | 31.1 | -0.0 ? | -0.9 ? | -2.5 ? |
| 1 | 20.0 | 7.8 | 20.1 | 31.6 | -0.1 ? | -1.2 ? | -1.9 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 34.4 | 22.4 | 49.4 | 61.5 | 24.1 | 0.69 |
| cost | look | 20.1 | 8.0 | 21.4 | 33.5 | 9.8 | 0.58 |
| cost:0.05 | look | 20.2 | 8.0 | 20.8 | 31.7 | 9.8 | 0.59 |
| cost:0.2 | look | 20.1 | 7.9 | 20.5 | 31.1 | 9.7 | 0.59 |
| cost:1 | look | 20.0 | 7.8 | 20.1 | 31.6 | 9.6 | 0.59 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 22.4 | 1.7 | 44% / 32 | 12% | 9.4 / 3.6 | 93% | 13.7 | 1.05 | 0.00 | 0.0% |
| cost | look | 8.0 | 1.7 | 16% / 13 | 33% | 5.6 / 3.4 | 78% | 10.9 | 1.08 | 0.08 | 0.0% |
| cost:0.05 | look | 8.0 | 1.8 | 16% / 13 | 33% | 5.6 / 3.3 | 78% | 10.9 | 1.08 | 0.09 | 0.0% |
| cost:0.2 | look | 7.9 | 1.8 | 16% / 13 | 34% | 5.6 / 3.3 | 77% | 10.8 | 1.08 | 0.09 | 0.0% |
| cost:1 | look | 7.8 | 1.8 | 15% / 12 | 34% | 5.5 / 3.3 | 77% | 10.7 | 1.08 | 0.08 | 0.0% |

## uniform · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 47.1; B0 floor = 10.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 27.3 ± 1.3 | -41.9% | [-20.22, -19.21] | 20/20 | 54% | better ✓ |
| cost:0.05 | 27.2 ± 1.2 | -42.3% | [-20.51, -19.35] | 20/20 | 54% | better ✓ |
| cost:0.2 | 26.9 ± 1.4 | -42.8% | [-20.75, -19.47] | 20/20 | 55% | better ✓ |
| cost:1 | 26.9 ± 1.8 | -42.7% | [-20.83, -19.22] | 20/20 | 55% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 27.3 | 13.8 | 33.8 | 66.5 |  |  |  |
| 0.05 | 27.2 | 13.4 | 31.9 | 55.1 | -0.2 ? | -1.9 ? | -11.4 ✓ |
| 0.2 | 26.9 | 13.1 | 30.9 | 52.5 | -0.4 ? | -2.9 ? | -13.9 ✓ |
| 1 | 26.9 | 13.1 | 31.0 | 53.6 | -0.4 ? | -2.9 ? | -12.8 ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 47.1 | 33.3 | 66.0 | 78.0 | 36.7 | 0.73 |
| cost | look | 27.3 | 13.8 | 33.8 | 66.5 | 16.9 | 0.61 |
| cost:0.05 | look | 27.2 | 13.4 | 31.9 | 55.1 | 16.8 | 0.64 |
| cost:0.2 | look | 26.9 | 13.1 | 30.9 | 52.5 | 16.5 | 0.64 |
| cost:1 | look | 26.9 | 13.1 | 31.0 | 53.6 | 16.6 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 33.3 | 3.4 | 47% / 46 | 1% | 9.7 / 3.8 | 98% | 6.0 | 1.18 | 0.00 | 0.0% |
| cost | look | 13.8 | 3.2 | 25% / 22 | 2% | 6.7 / 3.6 | 98% | 5.8 | 1.26 | 0.07 | 0.0% |
| cost:0.05 | look | 13.4 | 3.3 | 25% / 20 | 3% | 6.6 / 3.5 | 97% | 5.8 | 1.25 | 0.07 | 0.0% |
| cost:0.2 | look | 13.1 | 3.5 | 25% / 20 | 3% | 6.6 / 3.5 | 97% | 5.7 | 1.25 | 0.07 | 0.0% |
| cost:1 | look | 13.1 | 3.5 | 25% / 20 | 3% | 6.6 / 3.4 | 97% | 5.7 | 1.24 | 0.07 | 0.0% |

## uniform · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 40.6; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 22.2 ± 0.9 | -45.3% | [-19.30, -17.50] | 20/20 | 68% | better ✓ |
| cost:0.05 | 22.2 ± 0.8 | -45.2% | [-19.33, -17.39] | 20/20 | 68% | better ✓ |
| cost:0.2 | 22.2 ± 0.8 | -45.3% | [-19.34, -17.44] | 20/20 | 68% | better ✓ |
| cost:1 | 22.2 ± 0.9 | -45.2% | [-19.32, -17.42] | 20/20 | 68% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 22.2 | 7.0 | 20.0 | 37.1 |  |  |  |
| 0.05 | 22.2 | 7.0 | 20.2 | 34.5 | +0.0 ? | +0.2 ? | -2.5 ? |
| 0.2 | 22.2 | 6.9 | 19.8 | 34.6 | +0.0 ? | -0.2 ? | -2.5 ? |
| 1 | 22.2 | 6.9 | 19.7 | 34.3 | +0.0 ? | -0.3 ? | -2.8 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 40.6 | 25.5 | 57.4 | 75.2 | 27.0 | 0.68 |
| cost | look | 22.2 | 7.0 | 20.0 | 37.1 | 8.6 | 0.53 |
| cost:0.05 | look | 22.2 | 7.0 | 20.2 | 34.5 | 8.6 | 0.53 |
| cost:0.2 | look | 22.2 | 6.9 | 19.8 | 34.6 | 8.6 | 0.53 |
| cost:1 | look | 22.2 | 6.9 | 19.7 | 34.3 | 8.6 | 0.54 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 25.5 | 1.5 | 39% / 38 | 20% | 12.4 / 3.8 | 89% | 20.8 | 1.03 | 0.01 | 0.0% |
| cost | look | 7.0 | 1.6 | 10% / 11 | 47% | 5.5 / 3.2 | 66% | 14.4 | 1.06 | 0.15 | 0.0% |
| cost:0.05 | look | 7.0 | 1.7 | 9% / 11 | 48% | 5.6 / 3.2 | 66% | 14.4 | 1.05 | 0.14 | 0.0% |
| cost:0.2 | look | 6.9 | 1.7 | 10% / 11 | 47% | 5.5 / 3.2 | 65% | 14.3 | 1.05 | 0.14 | 0.0% |
| cost:1 | look | 6.9 | 1.7 | 9% / 11 | 48% | 5.5 / 3.2 | 65% | 14.2 | 1.05 | 0.14 | 0.0% |

## uniform · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 56.5; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 27.6 ± 1.3 | -51.1% | [-29.33, -28.37] | 20/20 | 67% | better ✓ |
| cost:0.05 | 27.0 ± 1.2 | -52.2% | [-30.02, -28.97] | 20/20 | 69% | better ✓ |
| cost:0.2 | 27.0 ± 0.7 | -52.1% | [-30.03, -28.86] | 20/20 | 69% | better ✓ |
| cost:1 | 26.7 ± 1.0 | -52.7% | [-30.41, -29.11] | 20/20 | 69% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 27.6 | 11.2 | 28.4 | 56.2 |  |  |  |
| 0.05 | 27.0 | 10.4 | 26.1 | 42.6 | -0.6 ✓ | -2.4 ✓ | -13.6 ✓ |
| 0.2 | 27.0 | 10.3 | 25.8 | 42.6 | -0.6 ? | -2.7 ? | -13.6 ✓ |
| 1 | 26.7 | 10.0 | 24.6 | 40.8 | -0.9 ? | -3.8 ✓ | -15.4 ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 56.5 | 40.0 | 79.4 | 92.1 | 42.8 | 0.73 |
| cost | look | 27.6 | 11.2 | 28.4 | 56.2 | 14.0 | 0.59 |
| cost:0.05 | look | 27.0 | 10.4 | 26.1 | 42.6 | 13.4 | 0.61 |
| cost:0.2 | look | 27.0 | 10.3 | 25.8 | 42.6 | 13.4 | 0.62 |
| cost:1 | look | 26.7 | 10.0 | 24.6 | 40.8 | 13.1 | 0.62 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 40.0 | 2.9 | 48% / 55 | 1% | 12.7 / 3.8 | 97% | 9.8 | 1.10 | 0.01 | 0.0% |
| cost | look | 11.2 | 2.8 | 18% / 17 | 8% | 6.8 / 3.3 | 94% | 9.0 | 1.16 | 0.07 | 0.0% |
| cost:0.05 | look | 10.4 | 3.0 | 19% / 15 | 9% | 6.4 / 3.2 | 93% | 8.9 | 1.15 | 0.08 | 0.0% |
| cost:0.2 | look | 10.3 | 3.1 | 18% / 15 | 9% | 6.5 / 3.2 | 93% | 8.8 | 1.15 | 0.09 | 0.0% |
| cost:1 | look | 10.0 | 3.1 | 17% / 15 | 10% | 6.4 / 3.2 | 93% | 8.8 | 1.15 | 0.09 | 0.0% |

## mixed · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.5; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.1 ± 0.8 | -40.1% | [-15.85, -15.04] | 20/20 | 63% | better ✓ |
| cost:0.05 | 23.0 ± 0.9 | -40.4% | [-15.99, -15.12] | 20/20 | 63% | better ✓ |
| cost:0.2 | 22.9 ± 0.9 | -40.7% | [-16.08, -15.29] | 20/20 | 64% | better ✓ |
| cost:1 | 23.0 ± 1.0 | -40.4% | [-15.98, -15.18] | 20/20 | 63% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 23.1 | 7.4 | 21.0 | 35.1 |  |  |  |
| 0.05 | 23.0 | 7.3 | 20.6 | 31.9 | -0.1 ? | -0.4 ? | -3.2 ? |
| 0.2 | 22.9 | 7.1 | 20.6 | 31.3 | -0.2 ? | -0.4 ? | -3.8 ? |
| 1 | 23.0 | 7.2 | 20.9 | 31.6 | -0.1 ? | -0.1 ? | -3.5 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 38.5 | 22.9 | 51.6 | 60.5 | 24.5 | 0.68 |
| cost | look | 23.1 | 7.4 | 21.0 | 35.1 | 9.1 | 0.53 |
| cost:0.05 | look | 23.0 | 7.3 | 20.6 | 31.9 | 9.0 | 0.54 |
| cost:0.2 | look | 22.9 | 7.1 | 20.6 | 31.3 | 8.9 | 0.53 |
| cost:1 | look | 23.0 | 7.2 | 20.9 | 31.6 | 9.0 | 0.53 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 22.9 | 1.6 | 43% / 35 | 9% | 10.4 / 3.9 | 94% | 14.4 | 1.33 | 0.00 | 0.0% |
| cost | look | 7.4 | 1.7 | 12% / 13 | 29% | 5.8 / 3.3 | 79% | 11.5 | 1.36 | 0.10 | 0.0% |
| cost:0.05 | look | 7.3 | 1.7 | 12% / 13 | 29% | 5.7 / 3.2 | 78% | 11.4 | 1.36 | 0.10 | 0.0% |
| cost:0.2 | look | 7.1 | 1.7 | 11% / 12 | 30% | 5.6 / 3.2 | 78% | 11.4 | 1.35 | 0.10 | 0.0% |
| cost:1 | look | 7.2 | 1.7 | 11% / 13 | 29% | 5.7 / 3.2 | 78% | 11.4 | 1.35 | 0.09 | 0.0% |

## mixed · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 47.3; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.2 ± 1.8 | -38.3% | [-18.95, -17.31] | 20/20 | 54% | better ✓ |
| cost:0.05 | 29.2 ± 1.8 | -38.4% | [-18.92, -17.34] | 20/20 | 54% | better ✓ |
| cost:0.2 | 28.7 ± 1.1 | -39.5% | [-19.27, -18.08] | 20/20 | 56% | better ✓ |
| cost:1 | 28.4 ± 1.2 | -40.0% | [-19.52, -18.27] | 20/20 | 57% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 29.2 | 12.3 | 31.0 | 59.0 |  |  |  |
| 0.05 | 29.2 | 12.1 | 29.9 | 49.0 | -0.0 ? | -1.1 ? | -10.1 ? |
| 0.2 | 28.7 | 11.5 | 29.4 | 44.7 | -0.5 ? | -1.6 ? | -14.3 ✓ |
| 1 | 28.4 | 11.3 | 27.9 | 47.2 | -0.8 ? | -3.1 ✓ | -11.8 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 47.3 | 30.4 | 60.4 | 77.8 | 33.3 | 0.73 |
| cost | look | 29.2 | 12.3 | 31.0 | 59.0 | 15.2 | 0.60 |
| cost:0.05 | look | 29.2 | 12.1 | 29.9 | 49.0 | 15.2 | 0.61 |
| cost:0.2 | look | 28.7 | 11.5 | 29.4 | 44.7 | 14.6 | 0.61 |
| cost:1 | look | 28.4 | 11.3 | 27.9 | 47.2 | 14.4 | 0.61 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 30.4 | 3.0 | 47% / 44 | 1% | 11.1 / 4.8 | 98% | 6.5 | 1.64 | 0.00 | 0.1% |
| cost | look | 12.3 | 2.9 | 18% / 22 | 3% | 7.7 / 4.1 | 96% | 6.2 | 1.71 | 0.08 | 0.1% |
| cost:0.05 | look | 12.1 | 3.0 | 19% / 21 | 4% | 7.6 / 4.2 | 96% | 6.2 | 1.70 | 0.08 | 0.1% |
| cost:0.2 | look | 11.5 | 3.1 | 19% / 20 | 4% | 7.3 / 3.9 | 96% | 6.1 | 1.69 | 0.07 | 0.0% |
| cost:1 | look | 11.3 | 3.1 | 18% / 19 | 4% | 7.2 / 3.8 | 96% | 6.1 | 1.68 | 0.07 | 0.1% |

## mixed · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 48.4; B0 floor = 18.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.7 ± 1.4 | -44.9% | [-22.55, -20.94] | 20/20 | 72% | better ✓ |
| cost:0.05 | 26.4 ± 1.2 | -45.6% | [-22.95, -21.19] | 20/20 | 73% | better ✓ |
| cost:0.2 | 26.3 ± 1.3 | -45.6% | [-22.95, -21.23] | 20/20 | 74% | better ✓ |
| cost:1 | 26.4 ± 1.3 | -45.5% | [-22.92, -21.19] | 20/20 | 73% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 26.7 | 6.7 | 20.6 | 36.5 |  |  |  |
| 0.05 | 26.4 | 6.4 | 19.7 | 35.0 | -0.3 ✓ | -0.9 ? | -1.6 ? |
| 0.2 | 26.3 | 6.3 | 19.7 | 34.0 | -0.3 ✓ | -0.9 ? | -2.5 ? |
| 1 | 26.4 | 6.3 | 20.0 | 33.8 | -0.3 ✓ | -0.7 ? | -2.8 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 48.4 | 28.5 | 64.6 | 77.0 | 30.0 | 0.67 |
| cost | look | 26.7 | 6.7 | 20.6 | 36.5 | 8.3 | 0.47 |
| cost:0.05 | look | 26.4 | 6.4 | 19.7 | 35.0 | 8.0 | 0.47 |
| cost:0.2 | look | 26.3 | 6.3 | 19.7 | 34.0 | 7.9 | 0.47 |
| cost:1 | look | 26.4 | 6.3 | 20.0 | 33.8 | 8.0 | 0.47 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 28.5 | 1.5 | 42% / 44 | 15% | 13.7 / 3.6 | 90% | 21.8 | 1.26 | 0.01 | 0.0% |
| cost | look | 6.7 | 1.6 | 7% / 13 | 42% | 5.6 / 3.1 | 70% | 16.0 | 1.28 | 0.16 | 0.0% |
| cost:0.05 | look | 6.4 | 1.6 | 7% / 12 | 43% | 5.4 / 3.0 | 69% | 15.7 | 1.28 | 0.16 | 0.0% |
| cost:0.2 | look | 6.3 | 1.6 | 7% / 12 | 43% | 5.3 / 3.0 | 69% | 15.7 | 1.28 | 0.15 | 0.0% |
| cost:1 | look | 6.3 | 1.6 | 7% / 12 | 43% | 5.4 / 3.0 | 69% | 15.7 | 1.28 | 0.16 | 0.0% |

## mixed · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 58.8; B0 floor = 18.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.3 ± 1.3 | -46.8% | [-28.06, -26.93] | 20/20 | 68% | better ✓ |
| cost:0.05 | 30.9 ± 1.5 | -47.5% | [-28.49, -27.33] | 20/20 | 69% | better ✓ |
| cost:0.2 | 30.6 ± 1.4 | -48.0% | [-28.86, -27.58] | 20/20 | 70% | better ✓ |
| cost:1 | 30.3 ± 1.1 | -48.5% | [-29.14, -27.95] | 20/20 | 71% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 31.3 | 10.1 | 26.6 | 43.5 |  |  |  |
| 0.05 | 30.9 | 9.5 | 25.5 | 41.7 | -0.4 ? | -1.1 ? | -1.8 ? |
| 0.2 | 30.6 | 9.2 | 24.5 | 42.5 | -0.7 ? | -2.1 ? | -0.9 ? |
| 1 | 30.3 | 8.8 | 23.7 | 37.7 | -1.0 ✓ | -2.9 ? | -5.8 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 58.8 | 37.6 | 75.7 | 87.6 | 40.2 | 0.72 |
| cost | look | 31.3 | 10.1 | 26.6 | 43.5 | 12.7 | 0.58 |
| cost:0.05 | look | 30.9 | 9.5 | 25.5 | 41.7 | 12.3 | 0.57 |
| cost:0.2 | look | 30.6 | 9.2 | 24.5 | 42.5 | 12.0 | 0.57 |
| cost:1 | look | 30.3 | 8.8 | 23.7 | 37.7 | 11.7 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 37.6 | 2.6 | 48% / 54 | 2% | 14.6 / 4.2 | 96% | 10.4 | 1.55 | 0.01 | 0.0% |
| cost | look | 10.1 | 2.6 | 12% / 18 | 8% | 7.3 / 3.6 | 93% | 9.4 | 1.59 | 0.11 | 0.0% |
| cost:0.05 | look | 9.5 | 2.8 | 12% / 17 | 9% | 7.0 / 3.5 | 92% | 9.3 | 1.59 | 0.12 | 0.0% |
| cost:0.2 | look | 9.2 | 2.8 | 12% / 16 | 10% | 6.8 / 3.5 | 91% | 9.2 | 1.57 | 0.12 | 0.0% |
| cost:1 | look | 8.8 | 2.9 | 12% / 15 | 10% | 6.6 / 3.3 | 91% | 9.2 | 1.57 | 0.11 | 0.0% |

## morning_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.3; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 27.0 ± 1.4 | -31.2% | [-12.99, -11.43] | 20/20 | 49% | better ✓ |
| cost:0.05 | 27.1 ± 1.3 | -31.1% | [-12.93, -11.39] | 20/20 | 49% | better ✓ |
| cost:0.2 | 26.9 ± 1.3 | -31.4% | [-13.07, -11.53] | 20/20 | 49% | better ✓ |
| cost:1 | 26.9 ± 1.2 | -31.5% | [-13.12, -11.55] | 20/20 | 50% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 27.0 | 10.2 | 24.5 | 29.6 |  |  |  |
| 0.05 | 27.1 | 10.2 | 24.6 | 29.6 | +0.1 ? | +0.1 ? | +0.0 ? |
| 0.2 | 26.9 | 10.0 | 24.5 | 29.4 | -0.1 ? | -0.0 ? | -0.1 ? |
| 1 | 26.9 | 10.0 | 24.3 | 29.6 | -0.1 ? | -0.2 ? | +0.0 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 39.3 | 23.1 | 50.4 | 59.0 | 25.0 | 0.68 |
| cost | look | 27.0 | 10.2 | 24.5 | 29.6 | 12.7 | 0.62 |
| cost:0.05 | look | 27.1 | 10.2 | 24.6 | 29.6 | 12.8 | 0.62 |
| cost:0.2 | look | 26.9 | 10.0 | 24.5 | 29.4 | 12.6 | 0.62 |
| cost:1 | look | 26.9 | 10.0 | 24.3 | 29.6 | 12.6 | 0.62 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 23.1 | 1.8 | 47% / 36 | 8% | 11.1 / 4.1 | 94% | 14.6 | 1.39 | 0.00 | 0.0% |
| cost | look | 10.2 | 2.5 | 5% / 16 | 23% | 9.4 / 4.9 | 63% | 9.3 | 1.60 | 0.17 | 0.0% |
| cost:0.05 | look | 10.2 | 2.6 | 5% / 16 | 23% | 9.5 / 4.8 | 63% | 9.2 | 1.60 | 0.17 | 0.0% |
| cost:0.2 | look | 10.0 | 2.6 | 5% / 15 | 24% | 9.3 / 4.8 | 63% | 9.2 | 1.60 | 0.17 | 0.0% |
| cost:1 | look | 10.0 | 2.6 | 6% / 15 | 23% | 9.3 / 4.8 | 63% | 9.2 | 1.59 | 0.16 | 0.0% |

## morning_rush · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 51.3; B0 floor = 14.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 35.6 ± 2.7 | -30.6% | [-16.40, -14.94] | 20/20 | 42% | better ✓ |
| cost:0.05 | 36.2 ± 3.6 | -29.5% | [-16.19, -14.06] | 20/20 | 41% | better ✓ |
| cost:0.2 | 36.4 ± 3.5 | -29.1% | [-15.87, -14.05] | 20/20 | 40% | better ✓ |
| cost:1 | 36.3 ± 3.4 | -29.3% | [-15.94, -14.21] | 20/20 | 41% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 35.6 | 17.7 | 36.6 | 52.2 |  |  |  |
| 0.05 | 36.2 | 18.1 | 36.7 | 49.4 | +0.5 ? | +0.1 ? | -2.9 ? |
| 0.2 | 36.4 | 18.3 | 37.1 | 48.5 | +0.7 ? | +0.6 ? | -3.8 ? |
| 1 | 36.3 | 18.2 | 36.9 | 48.1 | +0.6 ? | +0.3 ? | -4.0 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 51.3 | 33.5 | 66.6 | 120.7 | 36.9 | 0.73 |
| cost | look | 35.6 | 17.7 | 36.6 | 52.2 | 21.2 | 0.72 |
| cost:0.05 | look | 36.2 | 18.1 | 36.7 | 49.4 | 21.8 | 0.74 |
| cost:0.2 | look | 36.4 | 18.3 | 37.1 | 48.5 | 22.0 | 0.74 |
| cost:1 | look | 36.3 | 18.2 | 36.9 | 48.1 | 21.9 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 33.5 | 3.5 | 51% / 44 | 1% | 12.4 / 4.9 | 98% | 6.6 | 1.77 | 0.00 | 6.2% |
| cost | look | 17.7 | 3.6 | 19% / 30 | 6% | 13.8 / 4.2 | 92% | 5.9 | 1.85 | 0.06 | 0.4% |
| cost:0.05 | look | 18.1 | 3.7 | 20% / 29 | 6% | 14.0 / 4.1 | 91% | 5.9 | 1.84 | 0.05 | 0.3% |
| cost:0.2 | look | 18.3 | 3.7 | 20% / 30 | 7% | 14.1 / 4.1 | 91% | 5.9 | 1.83 | 0.05 | 0.2% |
| cost:1 | look | 18.2 | 3.7 | 19% / 30 | 7% | 14.1 / 4.1 | 91% | 5.9 | 1.83 | 0.06 | 0.2% |

## morning_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.6; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 34.7 ± 2.0 | -30.1% | [-15.79, -14.07] | 20/20 | 49% | better ✓ |
| cost:0.05 | 34.9 ± 2.2 | -29.8% | [-15.66, -13.83] | 20/20 | 48% | better ✓ |
| cost:0.2 | 34.8 ± 2.1 | -29.9% | [-15.73, -13.87] | 20/20 | 48% | better ✓ |
| cost:1 | 34.8 ± 2.0 | -29.9% | [-15.72, -13.86] | 20/20 | 48% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 34.7 | 12.8 | 31.5 | 38.5 |  |  |  |
| 0.05 | 34.9 | 12.9 | 31.0 | 37.6 | +0.2 ? | -0.5 ? | -0.8 ? |
| 0.2 | 34.8 | 12.9 | 31.3 | 37.8 | +0.1 ? | -0.2 ? | -0.7 ? |
| 1 | 34.8 | 12.9 | 31.3 | 37.7 | +0.1 ? | -0.2 ? | -0.8 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 49.6 | 29.0 | 64.3 | 77.3 | 30.6 | 0.67 |
| cost | look | 34.7 | 12.8 | 31.5 | 38.5 | 15.7 | 0.62 |
| cost:0.05 | look | 34.9 | 12.9 | 31.0 | 37.6 | 15.9 | 0.62 |
| cost:0.2 | look | 34.8 | 12.9 | 31.3 | 37.8 | 15.8 | 0.63 |
| cost:1 | look | 34.8 | 12.9 | 31.3 | 37.7 | 15.8 | 0.63 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 29.0 | 1.6 | 45% / 46 | 11% | 14.4 / 3.6 | 92% | 22.3 | 1.33 | 0.01 | 0.0% |
| cost | look | 12.8 | 2.9 | 4% / 20 | 22% | 12.1 / 5.5 | 49% | 11.1 | 1.62 | 0.37 | 0.0% |
| cost:0.05 | look | 12.9 | 3.0 | 4% / 21 | 22% | 12.2 / 5.5 | 48% | 10.9 | 1.62 | 0.37 | 0.0% |
| cost:0.2 | look | 12.9 | 2.9 | 4% / 20 | 22% | 12.1 / 5.6 | 48% | 11.0 | 1.62 | 0.36 | 0.0% |
| cost:1 | look | 12.9 | 2.9 | 4% / 20 | 22% | 12.1 / 5.6 | 49% | 11.0 | 1.62 | 0.36 | 0.0% |

## morning_rush · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 59.4; B0 floor = 19.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 40.0 ± 1.7 | -32.7% | [-20.27, -18.59] | 20/20 | 48% | better ✓ |
| cost:0.05 | 40.6 ± 1.6 | -31.6% | [-19.59, -18.05] | 20/20 | 47% | better ✓ |
| cost:0.2 | 40.1 ± 1.6 | -32.6% | [-20.04, -18.68] | 20/20 | 48% | better ✓ |
| cost:1 | 40.1 ± 1.7 | -32.5% | [-20.02, -18.62] | 20/20 | 48% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 40.0 | 17.3 | 35.7 | 48.9 |  |  |  |
| 0.05 | 40.6 | 17.8 | 35.4 | 44.5 | +0.6 ? | -0.3 ? | -4.3 ✓ |
| 0.2 | 40.1 | 17.2 | 34.7 | 43.1 | +0.1 ? | -1.1 ? | -5.8 ✓ |
| 1 | 40.1 | 17.2 | 34.6 | 44.7 | +0.1 ? | -1.1 ? | -4.2 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 59.4 | 37.2 | 74.7 | 98.3 | 40.3 | 0.72 |
| cost | look | 40.0 | 17.3 | 35.7 | 48.9 | 20.9 | 0.71 |
| cost:0.05 | look | 40.6 | 17.8 | 35.4 | 44.5 | 21.5 | 0.73 |
| cost:0.2 | look | 40.1 | 17.2 | 34.7 | 43.1 | 21.0 | 0.72 |
| cost:1 | look | 40.1 | 17.2 | 34.6 | 44.7 | 21.0 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 37.2 | 3.1 | 50% / 55 | 2% | 16.2 / 4.4 | 97% | 10.5 | 1.67 | 0.01 | 0.5% |
| cost | look | 17.3 | 3.6 | 7% / 26 | 11% | 15.9 / 4.4 | 80% | 8.1 | 1.79 | 0.11 | 0.0% |
| cost:0.05 | look | 17.8 | 3.7 | 6% / 25 | 12% | 16.5 / 4.3 | 78% | 8.0 | 1.77 | 0.12 | 0.0% |
| cost:0.2 | look | 17.2 | 3.7 | 5% / 24 | 12% | 16.0 / 4.2 | 78% | 7.9 | 1.77 | 0.12 | 0.0% |
| cost:1 | look | 17.2 | 3.8 | 5% / 25 | 12% | 16.0 / 4.2 | 78% | 7.9 | 1.77 | 0.12 | 0.0% |

## evening_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.4; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.7 ± 1.6 | -32.3% | [-13.27, -12.17] | 20/20 | 51% | better ✓ |
| cost:0.05 | 26.5 ± 1.4 | -32.8% | [-13.42, -12.44] | 20/20 | 51% | better ✓ |
| cost:0.2 | 26.5 ± 1.4 | -32.6% | [-13.36, -12.35] | 20/20 | 51% | better ✓ |
| cost:1 | 26.5 ± 1.4 | -32.7% | [-13.38, -12.39] | 20/20 | 51% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 26.7 | 10.5 | 27.8 | 42.4 |  |  |  |
| 0.05 | 26.5 | 10.3 | 27.0 | 39.2 | -0.2 ? | -0.8 ? | -3.1 ? |
| 0.2 | 26.5 | 10.3 | 27.1 | 40.0 | -0.1 ? | -0.7 ? | -2.4 ? |
| 1 | 26.5 | 10.3 | 26.9 | 39.8 | -0.1 ? | -0.8 ? | -2.6 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 39.4 | 23.1 | 49.9 | 60.2 | 25.1 | 0.70 |
| cost | look | 26.7 | 10.5 | 27.8 | 42.4 | 12.4 | 0.57 |
| cost:0.05 | look | 26.5 | 10.3 | 27.0 | 39.2 | 12.2 | 0.58 |
| cost:0.2 | look | 26.5 | 10.3 | 27.1 | 40.0 | 12.2 | 0.58 |
| cost:1 | look | 26.5 | 10.3 | 26.9 | 39.8 | 12.2 | 0.58 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 23.1 | 1.9 | 44% / 33 | 12% | 10.1 / 4.0 | 92% | 14.2 | 1.40 | 0.00 | 0.0% |
| cost | look | 10.5 | 1.9 | 17% / 17 | 29% | 7.6 / 4.2 | 81% | 12.1 | 1.40 | 0.11 | 0.0% |
| cost:0.05 | look | 10.3 | 1.9 | 16% / 16 | 30% | 7.6 / 4.2 | 80% | 11.9 | 1.39 | 0.11 | 0.0% |
| cost:0.2 | look | 10.3 | 1.9 | 16% / 16 | 30% | 7.6 / 4.2 | 80% | 11.9 | 1.40 | 0.11 | 0.0% |
| cost:1 | look | 10.3 | 1.9 | 16% / 15 | 30% | 7.6 / 4.1 | 80% | 11.9 | 1.39 | 0.11 | 0.0% |

## evening_rush · 30 floors x 4 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 51.9; B0 floor = 14.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.3 ± 1.3 | -39.7% | [-22.07, -19.22] | 20/20 | 55% | better ✓ |
| cost:0.05 | 30.8 ± 1.2 | -40.7% | [-22.59, -19.79] | 20/20 | 56% | better ✓ |
| cost:0.2 | 30.9 ± 1.3 | -40.4% | [-22.10, -19.82] | 20/20 | 56% | better ✓ |
| cost:1 | 31.1 ± 1.4 | -40.1% | [-22.40, -19.28] | 20/20 | 55% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 31.3 | 14.0 | 35.2 | 58.5 |  |  |  |
| 0.05 | 30.8 | 13.4 | 33.3 | 53.9 | -0.5 ✓ | -1.9 ? | -4.7 ? |
| 0.2 | 30.9 | 13.5 | 32.8 | 52.5 | -0.4 ? | -2.4 ? | -6.0 ? |
| 1 | 31.1 | 13.7 | 33.0 | 52.0 | -0.2 ? | -2.1 ? | -6.6 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 51.9 | 34.0 | 70.9 | 243.8 | 37.5 | 0.60 |
| cost | look | 31.3 | 14.0 | 35.2 | 58.5 | 16.9 | 0.61 |
| cost:0.05 | look | 30.8 | 13.4 | 33.3 | 53.9 | 16.4 | 0.62 |
| cost:0.2 | look | 30.9 | 13.5 | 32.8 | 52.5 | 16.5 | 0.63 |
| cost:1 | look | 31.1 | 13.7 | 33.0 | 52.0 | 16.7 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 34.0 | 3.4 | 47% / 45 | 1% | 10.0 / 3.7 | 98% | 6.5 | 1.79 | 0.00 | 5.2% |
| cost | look | 14.0 | 2.9 | 28% / 22 | 4% | 7.3 / 4.0 | 97% | 6.3 | 1.86 | 0.07 | 1.8% |
| cost:0.05 | look | 13.4 | 3.0 | 27% / 20 | 4% | 7.3 / 3.9 | 96% | 6.3 | 1.84 | 0.06 | 1.5% |
| cost:0.2 | look | 13.5 | 3.0 | 28% / 21 | 4% | 7.4 / 3.9 | 96% | 6.3 | 1.84 | 0.06 | 1.5% |
| cost:1 | look | 13.7 | 3.0 | 27% / 20 | 4% | 7.4 / 3.9 | 96% | 6.3 | 1.84 | 0.06 | 1.7% |

## evening_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.1; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.8 ± 1.5 | -35.2% | [-17.98, -16.45] | 20/20 | 57% | better ✓ |
| cost:0.05 | 31.7 ± 1.5 | -35.3% | [-18.01, -16.53] | 20/20 | 58% | better ✓ |
| cost:0.2 | 31.7 ± 1.5 | -35.3% | [-18.03, -16.52] | 20/20 | 58% | better ✓ |
| cost:1 | 31.8 ± 1.5 | -35.3% | [-18.01, -16.50] | 20/20 | 58% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 31.8 | 11.0 | 33.0 | 43.5 |  |  |  |
| 0.05 | 31.7 | 10.8 | 32.4 | 42.5 | -0.1 ? | -0.6 ? | -0.9 ? |
| 0.2 | 31.7 | 10.8 | 32.4 | 42.0 | -0.1 ? | -0.6 ? | -1.4 ? |
| 1 | 31.8 | 10.8 | 32.4 | 42.0 | -0.1 ? | -0.6 ? | -1.4 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 49.1 | 28.4 | 62.9 | 77.8 | 30.1 | 0.69 |
| cost | look | 31.8 | 11.0 | 33.0 | 43.5 | 12.8 | 0.52 |
| cost:0.05 | look | 31.7 | 10.8 | 32.4 | 42.5 | 12.7 | 0.52 |
| cost:0.2 | look | 31.7 | 10.8 | 32.4 | 42.0 | 12.7 | 0.52 |
| cost:1 | look | 31.8 | 10.8 | 32.4 | 42.0 | 12.7 | 0.52 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 28.4 | 1.7 | 43% / 41 | 17% | 13.6 / 4.0 | 89% | 21.5 | 1.33 | 0.01 | 0.0% |
| cost | look | 11.0 | 1.8 | 9% / 14 | 42% | 8.9 / 4.5 | 68% | 15.6 | 1.33 | 0.22 | 0.0% |
| cost:0.05 | look | 10.8 | 1.9 | 8% / 13 | 42% | 8.8 / 4.4 | 66% | 15.2 | 1.34 | 0.24 | 0.0% |
| cost:0.2 | look | 10.8 | 2.0 | 8% / 13 | 41% | 8.7 / 4.5 | 66% | 15.1 | 1.34 | 0.23 | 0.0% |
| cost:1 | look | 10.8 | 2.0 | 8% / 13 | 41% | 8.7 / 4.5 | 66% | 15.1 | 1.35 | 0.24 | 0.1% |

## evening_rush · 40 floors x 6 cars · door_time 1 · lobby · 440 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 60.4; B0 floor = 19.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 34.2 ± 1.6 | -43.3% | [-27.19, -25.15] | 20/20 | 63% | better ✓ |
| cost:0.05 | 34.2 ± 1.3 | -43.3% | [-26.98, -25.40] | 20/20 | 63% | better ✓ |
| cost:0.2 | 33.9 ± 1.3 | -43.8% | [-27.33, -25.63] | 20/20 | 64% | better ✓ |
| cost:1 | 34.1 ± 1.6 | -43.5% | [-27.14, -25.45] | 20/20 | 64% | better ✓ |

**Fairness frontier** (`cost:<alpha>` vs plain `cost`, LOOK; Δ with verdict)

| alpha | total mean | wait mean | wait p95 | wait max | Δ total | Δ wait p95 | Δ wait max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 34.2 | 12.5 | 34.4 | 54.8 |  |  |  |
| 0.05 | 34.2 | 12.4 | 33.2 | 53.9 | +0.0 ? | -1.1 ? | -0.9 ? |
| 0.2 | 33.9 | 12.0 | 32.5 | 50.5 | -0.3 ? | -1.8 ✓ | -4.2 ? |
| 1 | 34.1 | 12.2 | 33.1 | 54.1 | -0.1 ? | -1.2 ? | -0.7 ? |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| round_robin | look | 60.4 | 38.1 | 75.9 | 139.3 | 41.3 | 0.72 |
| cost | look | 34.2 | 12.5 | 34.4 | 54.8 | 15.1 | 0.57 |
| cost:0.05 | look | 34.2 | 12.4 | 33.2 | 53.9 | 15.1 | 0.57 |
| cost:0.2 | look | 33.9 | 12.0 | 32.5 | 50.5 | 14.8 | 0.57 |
| cost:1 | look | 34.1 | 12.2 | 33.1 | 54.1 | 15.0 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| round_robin | look | 38.1 | 3.1 | 48% / 52 | 2% | 13.3 / 3.7 | 96% | 10.4 | 1.68 | 0.01 | 1.2% |
| cost | look | 12.5 | 2.6 | 20% / 18 | 11% | 8.1 / 3.9 | 92% | 9.4 | 1.68 | 0.08 | 0.5% |
| cost:0.05 | look | 12.4 | 2.7 | 18% / 18 | 12% | 8.1 / 3.8 | 91% | 9.3 | 1.67 | 0.10 | 0.5% |
| cost:0.2 | look | 12.0 | 2.8 | 17% / 17 | 13% | 8.0 / 3.7 | 90% | 9.2 | 1.67 | 0.10 | 0.5% |
| cost:1 | look | 12.2 | 2.8 | 18% / 18 | 12% | 8.1 / 3.8 | 91% | 9.3 | 1.67 | 0.09 | 0.7% |
