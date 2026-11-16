# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 35.7 | 23.2 | -34.8% | [-13.3, -11.5] | 20/20 | 65% | 16.6 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 43.6 | 28.3 | -35.1% | [-15.8, -14.7] | 20/20 | 52% | 14.1 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.9 | 36.8 | -34.2% | [-20.0, -18.1] | 20/20 | 52% | 18.9 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 42.4 | 25.3 | -40.4% | [-17.7, -16.6] | 20/20 | 60% | 14.1 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 53.6 | 28.2 | -47.4% | [-26.0, -24.8] | 20/20 | 73% | 18.7 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 44.7 | 28.5 | -36.2% | [-16.8, -15.6] | 20/20 | 53% | 14.3 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.3 | 32.5 | -41.2% | [-23.5, -22.0] | 20/20 | 63% | 18.9 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.6 ± 1.4 | -31.1% | [-9.71, -8.04] | 20/20 | 55% | better ✓ |
| nearest | 25.4 ± 1.6 | -10.7% | [-3.92, -2.16] | 20/20 | 19% | better ✓ |
| zone | 28.5 ± 2.5 | -0.1% | [-1.00, +0.81] | 7/20 | 0% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 19.6 | -12.8% | [-3.40, -2.34] | 20/20 | better ✓ |
| nearest | look | 25.4 | -27.7% | [-11.05, -8.53] | 20/20 | better ✓ |
| round_robin | look | 28.5 | -27.5% | [-11.89, -9.84] | 20/20 | better ✓ |
| zone | look | 28.5 | -30.3% | [-13.42, -11.45] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.6 | 6.0 | 18.3 | 26.4 | 7.3 | 0.49 |
| cost | scan | 22.5 | 8.6 | 25.6 | 44.9 | 10.1 | 0.47 |
| nearest | look | 25.4 | 11.7 | 46.0 | 57.3 | 13.1 | 0.38 |
| nearest | scan | 35.2 | 21.3 | 59.0 | 63.0 | 22.8 | 0.48 |
| round_robin | look | 28.5 | 15.0 | 36.2 | 47.8 | 16.1 | 0.63 |
| round_robin | scan | 39.3 | 25.7 | 54.4 | 59.4 | 26.9 | 0.69 |
| zone | look | 28.5 | 14.7 | 43.0 | 55.9 | 16.1 | 0.53 |
| zone | scan | 40.9 | 26.9 | 56.7 | 61.2 | 28.5 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.0 | 1.3 | 6% / 11 | 67% | 5.2 / 3.6 | 47% | 14.7 | 1.08 | 0.17 | 0.0% |
| cost | scan | 8.6 | 1.5 | 7% / 20 | 60% | 5.7 / 3.5 | 47% | 14.7 | 1.09 | 0.21 | 0.0% |
| nearest | look | 11.7 | 1.4 | 23% / 29 | 48% | 3.7 / 3.7 | 46% | 14.5 | 1.09 | 0.28 | 0.0% |
| nearest | scan | 21.3 | 1.5 | 29% / 44 | 36% | 3.8 / 3.8 | 58% | 19.2 | 1.10 | 0.23 | 0.0% |
| round_robin | look | 15.0 | 1.1 | 21% / 27 | 60% | 10.6 / 3.9 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |
| round_robin | scan | 25.7 | 1.3 | 30% / 41 | 40% | 10.8 / 4.1 | 78% | 26.2 | 1.07 | 0.02 | 0.0% |
| zone | look | 14.7 | 1.4 | 25% / 31 | 47% | 8.0 / 3.6 | 49% | 15.6 | 1.09 | 0.25 | 0.0% |
| zone | scan | 26.9 | 1.6 | 33% / 43 | 34% | 9.2 / 3.6 | 62% | 20.7 | 1.14 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.4 / 16 | 24, 6.4 / 18 | 46, 6.4 / 17 |
| cost | scan | 23, 4.1 / 15 | 24, 11.8 / 32 | 46, 9.0 / 24 |
| nearest | look | 23, 7.6 / 34 | 24, 13.1 / 41 | 46, 12.6 / 45 |
| nearest | scan | 23, 14.5 / 54 | 24, 25.7 / 58 | 46, 21.9 / 59 |
| round_robin | look | 23, 14.0 / 33 | 24, 15.2 / 34 | 46, 15.3 / 36 |
| round_robin | scan | 23, 20.9 / 50 | 24, 29.3 / 55 | 46, 25.9 / 52 |
| zone | look | 23, 12.2 / 34 | 24, 12.7 / 37 | 46, 16.8 / 45 |
| zone | scan | 23, 21.8 / 53 | 24, 30.2 / 57 | 46, 27.6 / 56 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.7; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.2 ± 1.3 | -34.8% | [-13.31, -11.53] | 20/20 | 65% | better ✓ |
| nearest | 30.8 ± 2.5 | -13.5% | [-5.81, -3.81] | 20/20 | 25% | better ✓ |
| zone | 36.5 ± 3.6 | +2.4% | [-0.07, +1.76] | 6/20 | -4% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 23.2 | -12.6% | [-3.90, -2.77] | 20/20 | better ✓ |
| nearest | look | 30.8 | -28.8% | [-14.01, -11.11] | 20/20 | better ✓ |
| round_robin | look | 35.7 | -27.0% | [-14.00, -12.31] | 20/20 | better ✓ |
| zone | look | 36.5 | -30.2% | [-16.99, -14.47] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.2 | 5.4 | 17.7 | 29.9 | 6.7 | 0.44 |
| cost | scan | 26.6 | 8.6 | 27.6 | 53.3 | 10.0 | 0.43 |
| nearest | look | 30.8 | 12.9 | 56.2 | 75.0 | 14.3 | 0.33 |
| nearest | scan | 43.3 | 25.3 | 78.4 | 82.7 | 26.8 | 0.43 |
| round_robin | look | 35.7 | 18.0 | 43.2 | 62.1 | 19.1 | 0.63 |
| round_robin | scan | 48.8 | 31.1 | 71.2 | 78.5 | 32.3 | 0.65 |
| zone | look | 36.5 | 18.6 | 55.0 | 70.3 | 20.0 | 0.52 |
| zone | scan | 52.3 | 34.2 | 74.2 | 80.5 | 35.7 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.4 | 1.3 | 5% / 11 | 71% | 4.9 / 3.3 | 39% | 18.5 | 1.07 | 0.26 | 0.0% |
| cost | scan | 8.6 | 1.4 | 5% / 20 | 65% | 6.1 / 3.6 | 39% | 18.9 | 1.09 | 0.24 | 0.0% |
| nearest | look | 12.9 | 1.4 | 20% / 37 | 52% | 3.8 / 3.8 | 39% | 19.0 | 1.07 | 0.37 | 0.0% |
| nearest | scan | 25.3 | 1.5 | 24% / 62 | 43% | 3.8 / 3.8 | 50% | 25.3 | 1.09 | 0.29 | 0.0% |
| round_robin | look | 18.0 | 1.1 | 16% / 34 | 71% | 14.2 / 3.6 | 60% | 30.0 | 1.02 | 0.03 | 0.0% |
| round_robin | scan | 31.1 | 1.2 | 24% / 55 | 53% | 14.2 / 3.6 | 71% | 37.0 | 1.05 | 0.03 | 0.0% |
| zone | look | 18.6 | 1.4 | 25% / 39 | 51% | 10.7 / 3.4 | 42% | 20.8 | 1.08 | 0.36 | 0.0% |
| zone | scan | 34.2 | 1.5 | 29% / 58 | 39% | 11.9 / 3.2 | 56% | 29.0 | 1.11 | 0.36 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 3.6 / 15 | 22, 6.1 / 16 | 48, 6.0 / 17 |
| cost | scan | 25, 4.5 / 16 | 22, 11.3 / 31 | 48, 9.4 / 28 |
| nearest | look | 25, 9.0 / 44 | 22, 13.9 / 46 | 48, 14.2 / 53 |
| nearest | scan | 25, 15.7 / 68 | 22, 31.9 / 77 | 48, 27.3 / 79 |
| round_robin | look | 25, 17.2 / 42 | 22, 17.8 / 41 | 48, 18.4 / 41 |
| round_robin | scan | 25, 24.0 / 63 | 22, 35.3 / 69 | 48, 32.6 / 70 |
| zone | look | 25, 16.6 / 49 | 22, 15.4 / 45 | 48, 21.2 / 55 |
| zone | scan | 25, 24.6 / 68 | 22, 41.6 / 74 | 48, 35.8 / 73 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.3 ± 1.1 | -35.1% | [-15.84, -14.71] | 20/20 | 52% | better ✓ |
| nearest | 47.7 ± 5.5 | +9.4% | [+2.04, +6.81] | 2/20 | -14% | worse ✗ |
| zone | 34.7 ± 1.1 | -20.5% | [-9.39, -8.50] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.3 | -4.2% | [-1.71, -0.75] | 18/20 | better ✓ |
| nearest | look | 47.7 | -17.9% | [-14.79, -5.84] | 18/20 | better ✓ |
| round_robin | look | 43.6 | -10.1% | [-5.50, -4.24] | 20/20 | better ✓ |
| zone | look | 34.7 | -29.7% | [-15.40, -13.95] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.3 | 11.2 | 25.9 | 38.0 | 14.2 | 0.64 |
| cost | scan | 29.5 | 12.2 | 28.5 | 47.0 | 15.4 | 0.63 |
| nearest | look | 47.7 | 30.5 | 74.5 | 126.5 | 33.6 | 0.54 |
| nearest | scan | 58.1 | 40.7 | 98.4 | 174.9 | 44.0 | 0.57 |
| round_robin | look | 43.6 | 26.9 | 55.2 | 64.1 | 29.5 | 0.71 |
| round_robin | scan | 48.5 | 31.5 | 60.5 | 69.8 | 34.4 | 0.74 |
| zone | look | 34.7 | 18.4 | 50.2 | 93.5 | 20.6 | 0.55 |
| zone | scan | 49.3 | 32.6 | 62.9 | 124.3 | 35.2 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.2 | 3.0 | 8% / 19 | 14% | 9.8 / 4.4 | 79% | 7.5 | 1.67 | 0.11 | 0.0% |
| cost | scan | 12.2 | 3.2 | 5% / 26 | 15% | 10.6 / 4.5 | 78% | 7.3 | 1.68 | 0.08 | 0.0% |
| nearest | look | 30.5 | 3.2 | 42% / 50 | 6% | 5.0 / 5.0 | 80% | 7.9 | 1.63 | 0.23 | 9.7% |
| nearest | scan | 40.7 | 3.3 | 45% / 64 | 5% | 4.9 / 4.9 | 82% | 8.5 | 1.66 | 0.25 | 14.4% |
| round_robin | look | 26.9 | 2.6 | 50% / 40 | 2% | 11.8 / 4.6 | 98% | 9.7 | 1.56 | 0.01 | 0.0% |
| round_robin | scan | 31.5 | 2.8 | 51% / 46 | 2% | 13.3 / 8.1 | 97% | 9.9 | 1.61 | 0.01 | 0.1% |
| zone | look | 18.4 | 2.1 | 42% / 31 | 13% | 8.6 / 2.7 | 85% | 8.3 | 1.56 | 0.08 | 0.9% |
| zone | scan | 32.6 | 2.6 | 49% / 47 | 5% | 12.4 / 4.9 | 93% | 9.4 | 1.85 | 0.08 | 3.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 11.8 / 26 | 24, 8.7 / 20 | 46, 9.5 / 25 |
| cost | scan | 234, 12.7 / 28 | 24, 10.4 / 27 | 46, 10.8 / 28 |
| nearest | look | 234, 32.6 / 78 | 24, 22.8 / 58 | 46, 23.5 / 64 |
| nearest | scan | 234, 43.7 / 101 | 24, 31.0 / 63 | 46, 30.8 / 75 |
| round_robin | look | 234, 26.7 / 55 | 24, 27.1 / 53 | 46, 28.0 / 54 |
| round_robin | scan | 234, 31.4 / 60 | 24, 33.6 / 59 | 46, 31.4 / 61 |
| zone | look | 234, 17.2 / 49 | 24, 17.4 / 45 | 46, 24.9 / 61 |
| zone | scan | 234, 32.0 / 63 | 24, 32.3 / 59 | 46, 35.8 / 76 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.8 ± 1.8 | -34.2% | [-20.03, -18.08] | 20/20 | 52% | better ✓ |
| nearest | 64.4 ± 10.0 | +15.2% | [+4.72, +13.14] | 3/20 | -23% | worse ✗ |
| zone | 44.6 ± 1.9 | -20.2% | [-12.14, -10.38] | 20/20 | 31% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 36.8 | -2.2% | [-1.36, -0.26] | 15/20 | - |
| nearest | look | 64.4 | -19.6% | [-23.06, -8.95] | 18/20 | better ✓ |
| round_robin | look | 55.9 | -10.5% | [-7.24, -5.84] | 20/20 | better ✓ |
| zone | look | 44.6 | -28.0% | [-18.49, -16.29] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 36.8 | 14.5 | 33.3 | 42.6 | 17.9 | 0.65 |
| cost | scan | 37.6 | 15.1 | 34.4 | 58.4 | 18.7 | 0.64 |
| nearest | look | 64.4 | 42.2 | 116.6 | 218.0 | 45.4 | 0.50 |
| nearest | scan | 80.0 | 57.7 | 153.2 | 286.4 | 61.1 | 0.54 |
| round_robin | look | 55.9 | 34.5 | 70.9 | 81.9 | 36.9 | 0.71 |
| round_robin | scan | 62.4 | 40.8 | 78.8 | 84.5 | 43.5 | 0.73 |
| zone | look | 44.6 | 23.6 | 64.7 | 114.2 | 25.6 | 0.55 |
| zone | scan | 61.9 | 40.5 | 79.4 | 172.8 | 43.0 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.5 | 3.4 | 6% / 23 | 16% | 13.4 / 5.0 | 65% | 9.3 | 1.67 | 0.18 | 0.0% |
| cost | scan | 15.1 | 3.6 | 2% / 28 | 17% | 13.7 / 5.1 | 63% | 8.9 | 1.68 | 0.19 | 0.0% |
| nearest | look | 42.2 | 3.2 | 42% / 72 | 9% | 5.0 / 5.0 | 70% | 10.7 | 1.61 | 0.37 | 12.3% |
| nearest | scan | 57.7 | 3.4 | 42% / 91 | 7% | 4.9 / 4.9 | 73% | 11.7 | 1.63 | 0.42 | 19.0% |
| round_robin | look | 34.5 | 2.4 | 49% / 52 | 3% | 15.8 / 4.1 | 96% | 14.6 | 1.50 | 0.01 | 0.0% |
| round_robin | scan | 40.8 | 2.7 | 51% / 60 | 2% | 17.4 / 8.4 | 96% | 15.0 | 1.54 | 0.01 | 0.0% |
| zone | look | 23.6 | 2.0 | 42% / 40 | 18% | 11.0 / 2.3 | 79% | 11.8 | 1.51 | 0.16 | 0.5% |
| zone | scan | 40.5 | 2.5 | 47% / 62 | 8% | 16.0 / 4.1 | 88% | 13.7 | 1.78 | 0.16 | 1.7% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 15.8 / 34 | 22, 8.7 / 21 | 48, 9.9 / 27 |
| cost | scan | 249, 16.1 / 34 | 22, 10.4 / 26 | 48, 11.8 / 32 |
| nearest | look | 249, 45.8 / 118 | 22, 27.9 / 75 | 48, 29.5 / 92 |
| nearest | scan | 249, 63.2 / 159 | 22, 37.4 / 84 | 48, 37.3 / 104 |
| round_robin | look | 249, 34.0 / 71 | 22, 37.0 / 67 | 48, 36.1 / 71 |
| round_robin | scan | 249, 40.6 / 79 | 22, 41.9 / 76 | 48, 40.9 / 76 |
| zone | look | 249, 22.4 / 63 | 22, 20.2 / 51 | 48, 31.8 / 75 |
| zone | scan | 249, 39.5 / 79 | 22, 40.7 / 75 | 48, 45.6 / 99 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.3 ± 1.3 | -40.4% | [-17.67, -16.55] | 20/20 | 60% | better ✓ |
| nearest | 38.2 ± 2.2 | -9.8% | [-5.11, -3.19] | 19/20 | 15% | better ✓ |
| zone | 34.2 ± 1.5 | -19.3% | [-8.70, -7.63] | 20/20 | 29% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 25.3 | -10.8% | [-3.82, -2.27] | 19/20 | better ✓ |
| nearest | look | 38.2 | -15.1% | [-8.19, -5.41] | 20/20 | better ✓ |
| round_robin | look | 42.4 | -11.0% | [-5.78, -4.70] | 20/20 | better ✓ |
| zone | look | 34.2 | -27.2% | [-13.40, -12.19] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.3 | 9.2 | 24.5 | 37.0 | 11.2 | 0.57 |
| cost | scan | 28.3 | 11.9 | 33.3 | 49.5 | 14.3 | 0.55 |
| nearest | look | 38.2 | 21.9 | 60.0 | 80.9 | 24.2 | 0.51 |
| nearest | scan | 45.1 | 28.5 | 64.5 | 78.5 | 31.0 | 0.56 |
| round_robin | look | 42.4 | 26.3 | 54.0 | 63.0 | 28.3 | 0.72 |
| round_robin | scan | 47.6 | 31.4 | 60.1 | 66.0 | 33.6 | 0.74 |
| zone | look | 34.2 | 18.3 | 50.2 | 64.2 | 20.1 | 0.57 |
| zone | scan | 47.0 | 30.7 | 60.0 | 72.6 | 32.9 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.2 | 2.0 | 16% / 16 | 14% | 6.6 / 3.6 | 90% | 9.4 | 1.51 | 0.09 | 0.0% |
| cost | scan | 11.9 | 2.3 | 13% / 24 | 16% | 7.7 / 3.9 | 86% | 9.0 | 1.55 | 0.13 | 0.0% |
| nearest | look | 21.9 | 2.3 | 39% / 41 | 9% | 3.9 / 3.9 | 88% | 9.5 | 1.49 | 0.14 | 0.4% |
| nearest | scan | 28.5 | 2.5 | 42% / 51 | 6% | 3.7 / 3.7 | 90% | 9.9 | 1.55 | 0.16 | 0.2% |
| round_robin | look | 26.3 | 2.0 | 48% / 38 | 3% | 10.6 / 4.0 | 97% | 10.5 | 1.50 | 0.01 | 0.0% |
| round_robin | scan | 31.4 | 2.2 | 48% / 44 | 2% | 11.7 / 7.1 | 97% | 10.7 | 1.54 | 0.01 | 0.0% |
| zone | look | 18.3 | 1.9 | 39% / 31 | 15% | 7.9 / 3.2 | 84% | 8.8 | 1.47 | 0.09 | 0.0% |
| zone | scan | 30.7 | 2.3 | 46% / 45 | 5% | 10.7 / 4.3 | 93% | 10.2 | 1.70 | 0.09 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 7.9 / 23 | 120, 9.9 / 25 | 46, 10.2 / 25 |
| cost | scan | 114, 9.8 / 30 | 120, 13.7 / 36 | 46, 12.5 / 31 |
| nearest | look | 114, 19.7 / 59 | 120, 24.0 / 59 | 46, 22.1 / 61 |
| nearest | scan | 114, 27.1 / 64 | 120, 30.2 / 64 | 46, 27.5 / 65 |
| round_robin | look | 114, 25.3 / 54 | 120, 26.7 / 53 | 46, 27.7 / 53 |
| round_robin | scan | 114, 31.1 / 60 | 120, 31.7 / 60 | 46, 31.0 / 59 |
| zone | look | 114, 16.7 / 49 | 120, 17.8 / 49 | 46, 23.4 / 51 |
| zone | scan | 114, 29.3 / 59 | 120, 31.8 / 60 | 46, 31.3 / 60 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 53.6; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.2 ± 1.0 | -47.4% | [-26.01, -24.84] | 20/20 | 73% | better ✓ |
| nearest | 46.1 ± 2.3 | -14.1% | [-8.50, -6.72] | 20/20 | 22% | better ✓ |
| zone | 42.7 ± 1.3 | -20.4% | [-11.53, -10.34] | 20/20 | 31% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.2 | -7.7% | [-2.79, -1.92] | 20/20 | better ✓ |
| nearest | look | 46.1 | -18.4% | [-11.73, -9.13] | 20/20 | better ✓ |
| round_robin | look | 53.6 | -13.5% | [-9.30, -7.43] | 20/20 | better ✓ |
| zone | look | 42.7 | -30.2% | [-19.26, -17.77] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.2 | 7.5 | 21.4 | 37.8 | 9.5 | 0.53 |
| cost | scan | 30.6 | 9.6 | 28.6 | 66.2 | 11.8 | 0.47 |
| nearest | look | 46.1 | 25.2 | 77.6 | 91.7 | 27.3 | 0.45 |
| nearest | scan | 56.4 | 35.4 | 83.7 | 94.8 | 37.7 | 0.52 |
| round_robin | look | 53.6 | 33.1 | 69.7 | 81.6 | 34.9 | 0.71 |
| round_robin | scan | 62.0 | 41.2 | 77.9 | 84.2 | 43.3 | 0.74 |
| zone | look | 42.7 | 22.2 | 63.8 | 83.8 | 24.0 | 0.54 |
| zone | scan | 61.2 | 40.3 | 78.4 | 85.5 | 42.5 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.5 | 2.0 | 10% / 14 | 23% | 6.0 / 3.3 | 82% | 13.0 | 1.45 | 0.13 | 0.0% |
| cost | scan | 9.6 | 2.2 | 6% / 24 | 24% | 7.0 / 3.3 | 79% | 12.4 | 1.47 | 0.14 | 0.0% |
| nearest | look | 25.2 | 2.1 | 36% / 52 | 13% | 3.5 / 3.5 | 83% | 13.7 | 1.43 | 0.17 | 0.1% |
| nearest | scan | 35.4 | 2.3 | 39% / 68 | 8% | 3.5 / 3.5 | 87% | 14.8 | 1.49 | 0.21 | 0.1% |
| round_robin | look | 33.1 | 1.9 | 46% / 49 | 4% | 14.3 / 3.9 | 95% | 16.0 | 1.43 | 0.01 | 0.0% |
| round_robin | scan | 41.2 | 2.1 | 49% / 58 | 3% | 15.7 / 7.4 | 97% | 16.4 | 1.48 | 0.01 | 0.0% |
| zone | look | 22.2 | 1.8 | 38% / 39 | 21% | 10.2 / 3.0 | 77% | 12.6 | 1.42 | 0.16 | 0.0% |
| zone | scan | 40.3 | 2.1 | 46% / 59 | 8% | 14.5 / 4.3 | 88% | 15.1 | 1.65 | 0.16 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 6.6 / 20 | 116, 8.1 / 22 | 48, 8.5 / 23 |
| cost | scan | 124, 7.5 / 23 | 116, 11.5 / 34 | 48, 10.4 / 27 |
| nearest | look | 124, 20.7 / 77 | 116, 29.4 / 77 | 48, 26.6 / 75 |
| nearest | scan | 124, 32.7 / 83 | 116, 39.1 / 84 | 48, 33.6 / 83 |
| round_robin | look | 124, 32.6 / 69 | 116, 33.3 / 69 | 48, 33.3 / 68 |
| round_robin | scan | 124, 40.6 / 77 | 116, 42.3 / 78 | 48, 40.5 / 76 |
| zone | look | 124, 21.0 / 62 | 116, 20.8 / 61 | 48, 28.9 / 68 |
| zone | scan | 124, 39.2 / 78 | 116, 41.8 / 78 | 48, 39.7 / 77 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.7; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.5 ± 1.3 | -36.2% | [-16.75, -15.57] | 20/20 | 53% | better ✓ |
| nearest | 49.3 ± 9.6 | +10.4% | [+1.29, +9.39] | 7/20 | -15% | - |
| zone | 35.7 ± 1.9 | -20.0% | [-9.75, -8.22] | 20/20 | 29% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.5 | -22.0% | [-8.92, -7.27] | 20/20 | better ✓ |
| nearest | look | 49.3 | -8.8% | [-8.09, -0.33] | 18/20 | better ✓ |
| round_robin | look | 44.7 | -9.0% | [-5.16, -3.82] | 20/20 | better ✓ |
| zone | look | 35.7 | -29.7% | [-16.28, -14.06] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.5 | 11.8 | 31.2 | 49.9 | 14.3 | 0.58 |
| cost | scan | 36.6 | 18.9 | 44.9 | 67.8 | 22.3 | 0.63 |
| nearest | look | 49.3 | 32.1 | 99.0 | 270.2 | 35.1 | 0.43 |
| nearest | scan | 54.1 | 36.7 | 82.5 | 260.9 | 39.9 | 0.50 |
| round_robin | look | 44.7 | 27.7 | 55.8 | 75.1 | 30.4 | 0.73 |
| round_robin | scan | 49.1 | 31.9 | 61.3 | 85.7 | 34.9 | 0.74 |
| zone | look | 35.7 | 19.3 | 51.2 | 107.7 | 21.5 | 0.56 |
| zone | scan | 50.9 | 33.9 | 62.5 | 147.7 | 36.6 | 0.69 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.8 | 2.4 | 23% / 19 | 13% | 7.3 / 3.9 | 92% | 8.7 | 1.57 | 0.07 | 0.1% |
| cost | scan | 18.9 | 3.4 | 24% / 29 | 14% | 8.5 / 3.8 | 76% | 7.0 | 1.71 | 0.16 | 0.1% |
| nearest | look | 32.1 | 2.9 | 40% / 49 | 10% | 4.0 / 4.0 | 78% | 7.5 | 1.60 | 0.25 | 8.3% |
| nearest | scan | 36.7 | 3.1 | 42% / 54 | 4% | 3.3 / 3.3 | 90% | 9.0 | 1.67 | 0.17 | 5.7% |
| round_robin | look | 27.7 | 2.7 | 48% / 38 | 3% | 9.8 / 3.9 | 97% | 9.4 | 1.57 | 0.00 | 0.2% |
| round_robin | scan | 31.9 | 2.9 | 47% / 44 | 2% | 10.2 / 6.4 | 98% | 9.6 | 1.62 | 0.00 | 0.2% |
| zone | look | 19.3 | 2.2 | 40% / 30 | 13% | 7.7 / 4.4 | 85% | 8.1 | 1.59 | 0.10 | 0.9% |
| zone | scan | 33.9 | 2.7 | 46% / 45 | 4% | 9.6 / 4.4 | 94% | 9.4 | 1.92 | 0.10 | 2.7% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 6.0 / 19 | 242, 12.1 / 31 | 46, 13.2 / 32 |
| cost | scan | 23, 3.9 / 16 | 242, 21.4 / 46 | 46, 12.7 / 32 |
| nearest | look | 23, 8.2 / 45 | 242, 35.4 / 116 | 46, 25.8 / 66 |
| nearest | scan | 23, 23.7 / 63 | 242, 39.7 / 95 | 46, 27.5 / 65 |
| round_robin | look | 23, 25.2 / 51 | 242, 27.8 / 56 | 46, 28.6 / 55 |
| round_robin | scan | 23, 29.3 / 56 | 242, 32.4 / 61 | 46, 30.7 / 60 |
| zone | look | 23, 16.2 / 43 | 242, 18.8 / 51 | 46, 23.7 / 53 |
| zone | scan | 23, 30.4 / 57 | 242, 34.6 / 64 | 46, 32.6 / 62 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.3; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.5 ± 0.8 | -41.2% | [-23.50, -21.99] | 20/20 | 63% | better ✓ |
| nearest | 59.1 ± 6.8 | +6.9% | [+1.23, +6.89] | 7/20 | -10% | - |
| zone | 44.3 ± 1.3 | -19.9% | [-11.62, -10.37] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 32.5 | -29.5% | [-14.87, -12.30] | 20/20 | better ✓ |
| nearest | look | 59.1 | -8.0% | [-7.16, -2.97] | 17/20 | better ✓ |
| round_robin | look | 55.3 | -12.7% | [-8.91, -7.24] | 20/20 | better ✓ |
| zone | look | 44.3 | -30.5% | [-20.00, -18.83] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.5 | 11.4 | 32.6 | 50.7 | 13.7 | 0.54 |
| cost | scan | 46.1 | 23.8 | 59.3 | 78.3 | 27.2 | 0.60 |
| nearest | look | 59.1 | 37.3 | 107.3 | 332.1 | 40.2 | 0.41 |
| nearest | scan | 64.2 | 42.4 | 91.0 | 242.7 | 45.4 | 0.53 |
| round_robin | look | 55.3 | 34.1 | 70.5 | 81.5 | 36.4 | 0.72 |
| round_robin | scan | 63.3 | 41.8 | 78.5 | 85.0 | 44.5 | 0.75 |
| zone | look | 44.3 | 23.4 | 63.9 | 93.2 | 25.4 | 0.57 |
| zone | scan | 63.7 | 42.4 | 79.3 | 138.3 | 44.9 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.4 | 2.2 | 15% / 17 | 25% | 8.5 / 4.0 | 83% | 12.4 | 1.44 | 0.12 | 0.0% |
| cost | scan | 23.8 | 3.5 | 24% / 38 | 18% | 10.6 / 4.1 | 63% | 9.2 | 1.64 | 0.32 | 0.0% |
| nearest | look | 37.3 | 3.0 | 39% / 59 | 13% | 4.2 / 4.2 | 69% | 10.6 | 1.51 | 0.39 | 6.2% |
| nearest | scan | 42.4 | 2.9 | 40% / 66 | 7% | 3.1 / 3.1 | 86% | 13.7 | 1.57 | 0.23 | 3.0% |
| round_robin | look | 34.1 | 2.4 | 47% / 47 | 4% | 13.2 / 3.7 | 95% | 14.8 | 1.48 | 0.01 | 0.0% |
| round_robin | scan | 41.8 | 2.6 | 48% / 56 | 3% | 13.9 / 7.1 | 97% | 15.2 | 1.54 | 0.01 | 0.0% |
| zone | look | 23.4 | 2.0 | 39% / 39 | 18% | 10.2 / 4.5 | 79% | 12.1 | 1.49 | 0.15 | 0.3% |
| zone | scan | 42.4 | 2.4 | 46% / 56 | 6% | 13.1 / 4.3 | 91% | 14.6 | 1.84 | 0.15 | 1.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 2.8 / 12 | 236, 12.2 / 33 | 48, 12.3 / 32 |
| cost | scan | 25, 1.9 / 11 | 236, 27.9 / 62 | 48, 14.7 / 42 |
| nearest | look | 25, 4.6 / 30 | 236, 41.5 / 121 | 48, 33.0 / 82 |
| nearest | scan | 25, 23.2 / 81 | 236, 45.7 / 98 | 48, 35.9 / 85 |
| round_robin | look | 25, 31.9 / 67 | 236, 33.8 / 70 | 48, 36.4 / 70 |
| round_robin | scan | 25, 40.4 / 74 | 236, 42.0 / 78 | 48, 41.8 / 77 |
| zone | look | 25, 22.3 / 58 | 236, 22.4 / 63 | 48, 29.2 / 66 |
| zone | scan | 25, 37.9 / 75 | 236, 43.5 / 80 | 48, 39.7 / 77 |
