# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| quiet · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.0579 requests/tick) · 800 ticks | 12.8 | 9.9 | -22.7% | [-3.2, -2.5] | 20/20 | 45% | 6.3 |
| quiet · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.182 requests/tick) · 800 ticks | 56.6 | 32.1 | -43.3% | [-25.3, -23.7] | 20/20 | 65% | 18.7 |
| quiet · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.244 requests/tick) · 800 ticks | 83.9 | 49.1 | -41.5% | [-36.1, -33.6] | 20/20 | 59% | 24.7 |
| quiet · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 38.1 | 28.0 | -26.4% | [-11.0, -9.1] | 20/20 | 39% | 12.4 |
| quiet · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 31.7 | 21.9 | -30.9% | [-10.7, -8.9] | 20/20 | 51% | 12.4 |
| quiet · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 25.1 | 17.7 | -29.5% | [-7.9, -7.0] | 20/20 | 58% | 12.4 |
| quiet · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 24.6 | 16.9 | -31.0% | [-8.1, -7.1] | 20/20 | 62% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.2% | [-9.7, -8.1] | 20/20 | 55% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 43.6 | 28.3 | -35.1% | [-15.8, -14.7] | 20/20 | 52% | 14.1 |
| morning_rush · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.188 requests/tick) · 800 ticks | 16.0 | 13.5 | -15.4% | [-2.7, -2.3] | 20/20 | 28% | 7.1 |
| morning_rush · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.592 requests/tick) · 800 ticks | 168.7 | 142.4 | -15.6% | [-29.6, -23.0] | 20/20 | 18% | 21.5 |
| morning_rush · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.793 requests/tick) · 800 ticks | 482.7 | 442.9 | -8.2% | [-45.0, -35.0] | 20/20 | 9% | 28.4 |
| morning_rush · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 113.2 | 98.9 | -12.6% | [-16.4, -12.2] | 20/20 | 14% | 14.1 |
| morning_rush · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 48.2 | 34.0 | -29.5% | [-14.9, -13.4] | 20/20 | 42% | 14.1 |
| morning_rush · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 39.5 | 26.2 | -33.7% | [-14.0, -12.5] | 20/20 | 52% | 14.1 |
| morning_rush · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 36.2 | 25.5 | -29.5% | [-11.3, -9.9] | 20/20 | 48% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 71.6 | 49.8 | -30.4% | [-25.0, -18.7] | 20/20 | 38% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 44.5 | 30.5 | -31.5% | [-14.6, -13.4] | 20/20 | 46% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 43.6 | 27.5 | -36.8% | [-16.6, -15.4] | 20/20 | 54% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 42.4 | 25.3 | -40.4% | [-17.7, -16.6] | 20/20 | 60% | 14.1 |
| lunch · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.174 requests/tick) · 800 ticks | 14.6 | 10.9 | -25.1% | [-4.0, -3.3] | 20/20 | 49% | 7.1 |
| lunch · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.546 requests/tick) · 800 ticks | 74.3 | 46.4 | -37.6% | [-29.2, -26.5] | 20/20 | 53% | 21.4 |
| lunch · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.732 requests/tick) · 800 ticks | 191.5 | 119.7 | -37.5% | [-77.1, -66.7] | 20/20 | 44% | 28.3 |
| lunch · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 50.9 | 41.0 | -19.4% | [-11.3, -8.6] | 20/20 | 27% | 14.1 |
| lunch · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 45.5 | 30.6 | -32.8% | [-15.5, -14.4] | 20/20 | 47% | 14.1 |
| lunch · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 37.7 | 20.8 | -44.7% | [-17.6, -16.1] | 20/20 | 71% | 14.1 |
| lunch · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 33.8 | 19.0 | -43.6% | [-15.2, -14.3] | 20/20 | 75% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 43.3 | 25.7 | -40.8% | [-18.5, -16.9] | 20/20 | 60% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 42.4 | 25.4 | -40.2% | [-17.5, -16.5] | 20/20 | 60% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 42.4 | 25.3 | -40.4% | [-17.7, -16.6] | 20/20 | 60% | 14.1 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 44.7 | 28.5 | -36.2% | [-16.8, -15.6] | 20/20 | 53% | 14.3 |
| evening_rush · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.188 requests/tick) · 800 ticks | 15.9 | 13.3 | -16.1% | [-2.8, -2.3] | 20/20 | 29% | 7.1 |
| evening_rush · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.592 requests/tick) · 800 ticks | 155.1 | 62.8 | -59.5% | [-97.5, -87.2] | 20/20 | 69% | 21.3 |
| evening_rush · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.793 requests/tick) · 800 ticks | 395.7 | 230.4 | -41.8% | [-171.5, -158.9] | 20/20 | 45% | 28.3 |
| evening_rush · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 116.4 | 59.0 | -49.3% | [-62.7, -52.4] | 20/20 | 56% | 14.3 |
| evening_rush · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 49.7 | 33.9 | -31.8% | [-16.9, -14.8] | 20/20 | 45% | 14.3 |
| evening_rush · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 39.9 | 24.9 | -37.6% | [-15.4, -14.6] | 20/20 | 59% | 14.3 |
| evening_rush · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 36.3 | 24.3 | -33.0% | [-12.3, -11.6] | 20/20 | 54% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 74.8 | 33.0 | -55.9% | [-46.6, -37.3] | 20/20 | 69% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 46.2 | 29.3 | -36.6% | [-17.8, -16.0] | 20/20 | 53% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 44.6 | 28.3 | -36.5% | [-16.8, -15.8] | 20/20 | 54% | 14.3 |

## Building sweep: one setting at a time

Cells: mean total time per passenger, round_robin → cost (Δ, verdict), LOOK; then the ranking of all dispatch policies (C cost, N nearest, Z zone, R round_robin).

### Varying floors

| scenario | floors 15 | floors 30 | floors 45 | floors 60 |
|---|---:|---:|---:|---:|
| quiet | 12.8 → 9.9 (-23% ✓) CNZR | 28.5 → 19.6 (-31% ✓) CNZR | 56.6 → 32.1 (-43% ✓) CNZR | 83.9 → 49.1 (-42% ✓) CZNR |
| morning_rush | 16.0 → 13.5 (-15% ✓) CZRN | 43.6 → 28.3 (-35% ✓) CZRN | 168.7 → 142.4 (-16% ✓) ZCRN | 482.7 → 442.9 (-8% ✓) ZCRN |
| lunch | 14.6 → 10.9 (-25% ✓) CNZR | 42.4 → 25.3 (-40% ✓) CZNR | 74.3 → 46.4 (-38% ✓) CZRN | 191.5 → 119.7 (-38% ✓) CZRN |
| evening_rush | 15.9 → 13.3 (-16% ✓) CRZN | 44.7 → 28.5 (-36% ✓) CZRN | 155.1 → 62.8 (-60% ✓) CZRN | 395.7 → 230.4 (-42% ✓) CZRN |

### Varying cars

| scenario | cars 2 | cars 3 | cars 4 | cars 6 | cars 8 |
|---|---:|---:|---:|---:|---:|
| quiet | 38.1 → 28.0 (-26% ✓) CZNR | 31.7 → 21.9 (-31% ✓) CNZR | 28.5 → 19.6 (-31% ✓) CNZR | 25.1 → 17.7 (-30% ✓) CNRZ | 24.6 → 16.9 (-31% ✓) CNRZ |
| morning_rush | 113.2 → 98.9 (-13% ✓) ZCRN | 48.2 → 34.0 (-29% ✓) CZRN | 43.6 → 28.3 (-35% ✓) CZRN | 39.5 → 26.2 (-34% ✓) CZRN | 36.2 → 25.5 (-29% ✓) CZRN |
| lunch | 50.9 → 41.0 (-19% ✓) CZRN | 45.5 → 30.6 (-33% ✓) CZNR | 42.4 → 25.3 (-40% ✓) CZNR | 37.7 → 20.8 (-45% ✓) CZNR | 33.8 → 19.0 (-44% ✓) CNZR |
| evening_rush | 116.4 → 59.0 (-49% ✓) CZRN | 49.7 → 33.9 (-32% ✓) CZRN | 44.7 → 28.5 (-36% ✓) CZRN | 39.9 → 24.9 (-38% ✓) CZRN | 36.3 → 24.3 (-33% ✓) CZRN |

### Varying capacity

| scenario | capacity 4 | capacity 6 | capacity 8 | capacity 12 |
|---|---:|---:|---:|---:|
| quiet | 28.5 → 19.6 (-31% ✓) CNRZ | 28.5 → 19.6 (-31% ✓) CNZR | 28.5 → 19.6 (-31% ✓) CNZR | 28.5 → 19.6 (-31% ✓) CNZR |
| morning_rush | 71.6 → 49.8 (-30% ✓) CZRN | 44.5 → 30.5 (-31% ✓) CZRN | 43.6 → 28.3 (-35% ✓) CZRN | 43.6 → 27.5 (-37% ✓) CZNR |
| lunch | 43.3 → 25.7 (-41% ✓) CZNR | 42.4 → 25.4 (-40% ✓) CZNR | 42.4 → 25.3 (-40% ✓) CZNR | 42.4 → 25.3 (-40% ✓) CZNR |
| evening_rush | 74.8 → 33.0 (-56% ✓) CZRN | 46.2 → 29.3 (-37% ✓) CZRN | 44.7 → 28.5 (-36% ✓) CZRN | 44.6 → 28.3 (-36% ✓) CZNR |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.6 ± 1.4 | -31.1% | [-9.71, -8.04] | 20/20 | 55% | better ✓ |
| nearest | 25.4 ± 1.6 | -10.7% | [-3.92, -2.16] | 20/20 | 19% | better ✓ |
| zone | 28.5 ± 2.5 | -0.1% | [-1.00, +0.81] | 7/20 | 0% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.6 | 6.0 | 18.3 | 26.4 | 7.3 | 0.49 |
| nearest | look | 25.4 | 11.7 | 46.0 | 57.3 | 13.1 | 0.38 |
| round_robin | look | 28.5 | 15.0 | 36.2 | 47.8 | 16.1 | 0.63 |
| zone | look | 28.5 | 14.7 | 43.0 | 55.9 | 16.1 | 0.53 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.0 | 1.3 | 6% / 11 | 67% | 5.2 / 3.6 | 47% | 14.7 | 1.08 | 0.17 | 0.0% |
| nearest | look | 11.7 | 1.4 | 23% / 29 | 48% | 3.7 / 3.7 | 46% | 14.5 | 1.09 | 0.28 | 0.0% |
| round_robin | look | 15.0 | 1.1 | 21% / 27 | 60% | 10.6 / 3.9 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |
| zone | look | 14.7 | 1.4 | 25% / 31 | 47% | 8.0 / 3.6 | 49% | 15.6 | 1.09 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.4 / 16 | 24, 6.4 / 18 | 46, 6.4 / 17 |
| nearest | look | 23, 7.6 / 34 | 24, 13.1 / 41 | 46, 12.6 / 45 |
| round_robin | look | 23, 14.0 / 33 | 24, 15.2 / 34 | 46, 15.3 / 36 |
| zone | look | 23, 12.2 / 34 | 24, 12.7 / 37 | 46, 16.8 / 45 |

## quiet · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.0579 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 12.8; B0 floor = 6.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 9.9 ± 1.2 | -22.7% | [-3.24, -2.53] | 20/20 | 45% | better ✓ |
| nearest | 10.9 ± 1.8 | -14.6% | [-2.44, -1.24] | 18/20 | 29% | better ✓ |
| zone | 12.2 ± 1.3 | -4.2% | [-0.93, -0.20] | 14/20 | 8% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 9.9 | 2.5 | 7.9 | 11.2 | 3.6 | 0.45 |
| nearest | look | 10.9 | 3.5 | 12.5 | 19.5 | 4.6 | 0.37 |
| round_robin | look | 12.8 | 5.5 | 12.2 | 14.7 | 6.5 | 0.64 |
| zone | look | 12.2 | 4.9 | 13.5 | 20.3 | 5.9 | 0.50 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 2.5 | 1.0 | 1% / 2 | 92% | 2.4 / 2.1 | 15% | 8.4 | 1.03 | 0.36 | 0.0% |
| nearest | look | 3.5 | 1.1 | 9% / 14 | 81% | 2.2 / 2.2 | 14% | 8.3 | 1.03 | 0.49 | 0.0% |
| round_robin | look | 5.5 | 1.0 | 1% / 4 | 99% | 5.4 / 1.8 | 19% | 11.7 | 1.00 | 0.03 | 0.0% |
| zone | look | 4.9 | 1.1 | 6% / 13 | 84% | 4.0 / 1.8 | 17% | 9.9 | 1.03 | 0.32 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 11, 1.1 / 5 | 12, 2.9 / 7 | 22, 2.8 / 8 |
| nearest | look | 11, 1.4 / 6 | 12, 3.9 / 11 | 22, 4.0 / 12 |
| round_robin | look | 11, 5.1 / 12 | 12, 5.4 / 11 | 22, 5.5 / 12 |
| zone | look | 11, 4.4 / 12 | 12, 4.1 / 10 | 22, 5.3 / 14 |

## quiet · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.182 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 56.6; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.1 ± 1.9 | -43.3% | [-25.27, -23.73] | 20/20 | 65% | better ✓ |
| nearest | 48.6 ± 3.9 | -14.1% | [-9.11, -6.90] | 20/20 | 21% | better ✓ |
| zone | 49.0 ± 3.7 | -13.4% | [-9.09, -6.15] | 20/20 | 20% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.1 | 11.5 | 30.8 | 50.9 | 13.4 | 0.56 |
| nearest | look | 48.6 | 27.8 | 82.2 | 94.2 | 29.9 | 0.48 |
| round_robin | look | 56.6 | 36.1 | 77.0 | 89.2 | 37.9 | 0.70 |
| zone | look | 49.0 | 28.2 | 74.6 | 102.7 | 30.3 | 0.56 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.5 | 1.8 | 14% / 20 | 30% | 8.5 / 5.0 | 79% | 17.1 | 1.17 | 0.12 | 0.0% |
| nearest | look | 27.8 | 2.0 | 37% / 54 | 18% | 5.3 / 5.3 | 77% | 17.5 | 1.17 | 0.15 | 0.0% |
| round_robin | look | 36.1 | 1.8 | 46% / 53 | 9% | 15.2 / 5.9 | 94% | 21.5 | 1.15 | 0.01 | 0.0% |
| zone | look | 28.2 | 2.1 | 37% / 49 | 23% | 12.1 / 5.5 | 68% | 15.2 | 1.18 | 0.32 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 36, 9.7 / 28 | 33, 11.7 / 30 | 72, 12.3 / 31 |
| nearest | look | 36, 23.3 / 77 | 33, 30.5 / 80 | 72, 29.1 / 82 |
| round_robin | look | 36, 34.9 / 74 | 33, 35.6 / 75 | 72, 37.0 / 77 |
| zone | look | 36, 23.1 / 68 | 33, 24.4 / 67 | 72, 32.5 / 77 |

## quiet · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.244 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 83.9; B0 floor = 24.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 49.1 ± 4.1 | -41.5% | [-36.05, -33.59] | 20/20 | 59% | better ✓ |
| nearest | 77.4 ± 5.4 | -7.8% | [-8.54, -4.24] | 19/20 | 11% | better ✓ |
| zone | 70.1 ± 5.3 | -16.5% | [-15.11, -12.47] | 20/20 | 23% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 49.1 | 21.5 | 53.2 | 94.3 | 24.4 | 0.61 |
| nearest | look | 77.4 | 49.7 | 121.3 | 137.8 | 52.7 | 0.56 |
| round_robin | look | 83.9 | 56.5 | 111.2 | 124.7 | 59.2 | 0.73 |
| zone | look | 70.1 | 42.4 | 108.8 | 166.7 | 45.4 | 0.58 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 21.5 | 2.9 | 21% / 35 | 8% | 13.8 / 7.8 | 92% | 15.2 | 1.28 | 0.11 | 0.0% |
| nearest | look | 49.7 | 3.0 | 44% / 84 | 5% | 7.7 / 7.7 | 90% | 15.8 | 1.26 | 0.15 | 0.2% |
| round_robin | look | 56.5 | 2.7 | 49% / 80 | 3% | 21.1 / 8.3 | 96% | 16.9 | 1.26 | 0.01 | 0.0% |
| zone | look | 42.4 | 3.0 | 43% / 66 | 13% | 15.9 / 7.3 | 80% | 13.6 | 1.25 | 0.25 | 0.8% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 49, 19.5 / 48 | 48, 22.4 / 53 | 95, 22.1 / 54 |
| nearest | look | 49, 44.9 / 120 | 48, 54.3 / 119 | 95, 49.6 / 120 |
| round_robin | look | 49, 57.1 / 110 | 48, 56.7 / 110 | 95, 56.1 / 110 |
| zone | look | 49, 35.9 / 97 | 48, 36.7 / 99 | 95, 48.6 / 113 |

## quiet · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.1; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.0 ± 1.9 | -26.4% | [-11.02, -9.11] | 20/20 | 39% | better ✓ |
| nearest | 35.6 ± 3.0 | -6.6% | [-3.29, -1.77] | 19/20 | 10% | better ✓ |
| zone | 34.2 ± 2.1 | -10.2% | [-4.95, -2.76] | 19/20 | 15% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.0 | 13.9 | 34.3 | 46.5 | 15.7 | 0.63 |
| nearest | look | 35.6 | 21.3 | 54.3 | 62.2 | 23.2 | 0.59 |
| round_robin | look | 38.1 | 24.0 | 52.5 | 60.0 | 25.7 | 0.69 |
| zone | look | 34.2 | 19.9 | 51.0 | 63.3 | 21.8 | 0.59 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.9 | 1.7 | 26% / 23 | 23% | 8.5 / 6.1 | 83% | 13.0 | 1.18 | 0.07 | 0.0% |
| nearest | look | 21.3 | 1.9 | 39% / 36 | 17% | 6.5 / 6.5 | 82% | 13.0 | 1.18 | 0.06 | 0.0% |
| round_robin | look | 24.0 | 1.7 | 43% / 36 | 13% | 10.2 / 6.7 | 92% | 14.8 | 1.16 | 0.00 | 0.0% |
| zone | look | 19.9 | 2.0 | 35% / 34 | 23% | 8.7 / 6.1 | 74% | 11.5 | 1.17 | 0.20 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 13.2 / 32 | 24, 13.6 / 30 | 46, 14.3 / 34 |
| nearest | look | 23, 19.6 / 51 | 24, 21.4 / 51 | 46, 22.2 / 53 |
| round_robin | look | 23, 23.2 / 48 | 24, 23.5 / 49 | 46, 24.7 / 52 |
| zone | look | 23, 16.9 / 45 | 24, 18.4 / 47 | 46, 21.8 / 52 |

## quiet · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 31.7; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 21.9 ± 1.4 | -30.9% | [-10.74, -8.91] | 20/20 | 51% | better ✓ |
| nearest | 28.3 ± 2.2 | -10.6% | [-4.60, -2.15] | 18/20 | 17% | better ✓ |
| zone | 30.9 ± 2.4 | -2.5% | [-1.70, +0.09] | 13/20 | 4% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 21.9 | 8.2 | 22.2 | 30.6 | 9.6 | 0.56 |
| nearest | look | 28.3 | 14.4 | 47.9 | 58.5 | 16.0 | 0.45 |
| round_robin | look | 31.7 | 18.1 | 41.6 | 54.0 | 19.4 | 0.66 |
| zone | look | 30.9 | 17.0 | 46.3 | 57.5 | 18.6 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.2 | 1.4 | 12% / 15 | 51% | 6.5 / 4.5 | 62% | 14.6 | 1.11 | 0.11 | 0.0% |
| nearest | look | 14.4 | 1.5 | 27% / 31 | 38% | 4.6 / 4.6 | 59% | 14.1 | 1.12 | 0.22 | 0.0% |
| round_robin | look | 18.1 | 1.3 | 31% / 30 | 37% | 10.2 / 4.7 | 79% | 19.4 | 1.07 | 0.01 | 0.0% |
| zone | look | 17.0 | 1.6 | 31% / 32 | 36% | 8.2 / 4.4 | 60% | 14.2 | 1.12 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 6.9 / 20 | 24, 8.3 / 21 | 46, 8.6 / 21 |
| nearest | look | 23, 10.5 / 39 | 24, 16.6 / 45 | 46, 14.9 / 47 |
| round_robin | look | 23, 17.2 / 40 | 24, 17.4 / 38 | 46, 18.7 / 41 |
| zone | look | 23, 14.2 / 38 | 24, 14.6 / 40 | 46, 19.3 / 48 |

## quiet · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 25.1; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 17.7 ± 1.5 | -29.5% | [-7.87, -6.97] | 20/20 | 58% | better ✓ |
| nearest | 22.4 ± 1.9 | -10.8% | [-3.49, -1.96] | 20/20 | 21% | better ✓ |
| zone | 25.8 ± 2.7 | +2.8% | [+0.00, +1.45] | 7/20 | -6% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 17.7 | 4.2 | 14.7 | 22.7 | 5.3 | 0.41 |
| nearest | look | 22.4 | 8.7 | 39.8 | 55.9 | 10.0 | 0.30 |
| round_robin | look | 25.1 | 11.7 | 27.1 | 39.9 | 12.7 | 0.63 |
| zone | look | 25.8 | 12.2 | 35.3 | 49.5 | 13.4 | 0.52 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 4.2 | 1.1 | 3% / 7 | 79% | 3.8 / 2.7 | 32% | 14.6 | 1.05 | 0.31 | 0.0% |
| nearest | look | 8.7 | 1.3 | 15% / 29 | 60% | 3.0 / 3.0 | 31% | 14.4 | 1.06 | 0.39 | 0.0% |
| round_robin | look | 11.7 | 1.0 | 7% / 24 | 87% | 10.6 / 2.6 | 47% | 22.8 | 1.01 | 0.02 | 0.0% |
| zone | look | 12.2 | 1.2 | 19% / 27 | 60% | 7.8 / 2.4 | 36% | 17.1 | 1.07 | 0.30 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 1.9 / 9 | 24, 5.2 / 15 | 46, 4.7 / 14 |
| nearest | look | 23, 3.6 / 17 | 24, 10.6 / 38 | 46, 9.9 / 40 |
| round_robin | look | 23, 11.1 / 28 | 24, 11.9 / 26 | 46, 11.8 / 26 |
| zone | look | 23, 10.9 / 30 | 24, 11.0 / 32 | 46, 13.6 / 36 |

## quiet · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 24.6; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 16.9 ± 1.7 | -31.0% | [-8.09, -7.11] | 20/20 | 62% | better ✓ |
| nearest | 20.9 ± 2.4 | -14.7% | [-4.38, -2.84] | 19/20 | 30% | better ✓ |
| zone | 25.0 ± 2.6 | +1.8% | [-0.35, +1.25] | 7/20 | -4% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 16.9 | 3.5 | 12.5 | 22.7 | 4.6 | 0.37 |
| nearest | look | 20.9 | 7.3 | 35.7 | 56.4 | 8.6 | 0.26 |
| round_robin | look | 24.6 | 11.2 | 26.0 | 32.5 | 12.2 | 0.64 |
| zone | look | 25.0 | 11.5 | 33.8 | 47.6 | 12.6 | 0.51 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 3.5 | 1.1 | 2% / 5 | 84% | 3.2 / 2.4 | 23% | 14.3 | 1.04 | 0.46 | 0.0% |
| nearest | look | 7.3 | 1.3 | 13% / 28 | 66% | 2.5 / 2.5 | 23% | 14.1 | 1.05 | 0.54 | 0.0% |
| round_robin | look | 11.2 | 1.0 | 2% / 18 | 96% | 10.9 / 1.9 | 36% | 23.2 | 1.00 | 0.03 | 0.0% |
| zone | look | 11.5 | 1.1 | 16% / 27 | 67% | 8.0 / 2.0 | 28% | 18.1 | 1.06 | 0.35 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 0.8 / 5 | 24, 4.6 / 14 | 46, 4.0 / 13 |
| nearest | look | 23, 1.8 / 10 | 24, 9.8 / 36 | 46, 8.4 / 35 |
| round_robin | look | 23, 10.3 / 26 | 24, 11.5 / 24 | 46, 11.4 / 25 |
| zone | look | 23, 10.2 / 29 | 24, 10.5 / 31 | 46, 12.4 / 33 |

## quiet · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.6 ± 1.4 | -31.2% | [-9.72, -8.07] | 20/20 | 55% | better ✓ |
| nearest | 25.6 ± 1.6 | -10.2% | [-3.77, -2.05] | 20/20 | 18% | better ✓ |
| zone | 28.5 ± 2.6 | +0.1% | [-0.96, +0.90] | 7/20 | -0% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.6 | 6.0 | 18.3 | 26.4 | 7.2 | 0.49 |
| nearest | look | 25.6 | 11.8 | 46.8 | 60.0 | 13.2 | 0.38 |
| round_robin | look | 28.5 | 15.0 | 36.2 | 47.8 | 16.1 | 0.63 |
| zone | look | 28.5 | 14.8 | 43.3 | 58.7 | 16.2 | 0.53 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.0 | 1.3 | 6% / 11 | 67% | 5.3 / 3.6 | 48% | 14.8 | 1.08 | 0.16 | 0.0% |
| nearest | look | 11.8 | 1.4 | 22% / 30 | 48% | 3.7 / 3.7 | 46% | 14.5 | 1.09 | 0.28 | 0.3% |
| round_robin | look | 15.0 | 1.1 | 21% / 27 | 60% | 10.6 / 3.9 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |
| zone | look | 14.8 | 1.4 | 25% / 31 | 47% | 8.0 / 3.6 | 49% | 15.6 | 1.09 | 0.25 | 0.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.5 / 16 | 24, 6.4 / 18 | 46, 6.4 / 17 |
| nearest | look | 23, 7.7 / 34 | 24, 13.3 / 41 | 46, 12.8 / 47 |
| round_robin | look | 23, 14.0 / 33 | 24, 15.2 / 34 | 46, 15.3 / 36 |
| zone | look | 23, 12.2 / 34 | 24, 12.9 / 37 | 46, 16.8 / 45 |

## quiet · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.6 ± 1.4 | -31.1% | [-9.71, -8.04] | 20/20 | 55% | better ✓ |
| nearest | 25.4 ± 1.6 | -10.7% | [-3.92, -2.16] | 20/20 | 19% | better ✓ |
| zone | 28.5 ± 2.5 | -0.1% | [-1.00, +0.81] | 7/20 | 0% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.6 | 6.0 | 18.3 | 26.4 | 7.3 | 0.49 |
| nearest | look | 25.4 | 11.7 | 46.0 | 57.3 | 13.1 | 0.38 |
| round_robin | look | 28.5 | 15.0 | 36.2 | 47.8 | 16.1 | 0.63 |
| zone | look | 28.5 | 14.7 | 43.0 | 55.9 | 16.1 | 0.53 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.0 | 1.3 | 6% / 11 | 67% | 5.2 / 3.6 | 47% | 14.7 | 1.08 | 0.17 | 0.0% |
| nearest | look | 11.7 | 1.4 | 23% / 29 | 48% | 3.7 / 3.7 | 46% | 14.5 | 1.09 | 0.28 | 0.0% |
| round_robin | look | 15.0 | 1.1 | 21% / 27 | 60% | 10.6 / 3.9 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |
| zone | look | 14.7 | 1.4 | 25% / 31 | 47% | 8.0 / 3.6 | 49% | 15.6 | 1.09 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.4 / 16 | 24, 6.4 / 18 | 46, 6.4 / 17 |
| nearest | look | 23, 7.6 / 34 | 24, 13.1 / 41 | 46, 12.6 / 45 |
| round_robin | look | 23, 14.0 / 33 | 24, 15.2 / 34 | 46, 15.3 / 36 |
| zone | look | 23, 12.2 / 34 | 24, 12.7 / 37 | 46, 16.8 / 45 |

## quiet · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.6 ± 1.4 | -31.1% | [-9.71, -8.04] | 20/20 | 55% | better ✓ |
| nearest | 25.4 ± 1.6 | -10.7% | [-3.92, -2.16] | 20/20 | 19% | better ✓ |
| zone | 28.5 ± 2.5 | -0.1% | [-1.00, +0.81] | 7/20 | 0% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.6 | 6.0 | 18.3 | 26.4 | 7.3 | 0.49 |
| nearest | look | 25.4 | 11.7 | 46.0 | 57.3 | 13.1 | 0.38 |
| round_robin | look | 28.5 | 15.0 | 36.2 | 47.8 | 16.1 | 0.63 |
| zone | look | 28.5 | 14.7 | 43.0 | 55.9 | 16.1 | 0.53 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.0 | 1.3 | 6% / 11 | 67% | 5.2 / 3.6 | 47% | 14.7 | 1.08 | 0.17 | 0.0% |
| nearest | look | 11.7 | 1.4 | 23% / 29 | 48% | 3.7 / 3.7 | 46% | 14.5 | 1.09 | 0.28 | 0.0% |
| round_robin | look | 15.0 | 1.1 | 21% / 27 | 60% | 10.6 / 3.9 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |
| zone | look | 14.7 | 1.4 | 25% / 31 | 47% | 8.0 / 3.6 | 49% | 15.6 | 1.09 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.4 / 16 | 24, 6.4 / 18 | 46, 6.4 / 17 |
| nearest | look | 23, 7.6 / 34 | 24, 13.1 / 41 | 46, 12.6 / 45 |
| round_robin | look | 23, 14.0 / 33 | 24, 15.2 / 34 | 46, 15.3 / 36 |
| zone | look | 23, 12.2 / 34 | 24, 12.7 / 37 | 46, 16.8 / 45 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.3 ± 1.1 | -35.1% | [-15.84, -14.71] | 20/20 | 52% | better ✓ |
| nearest | 47.7 ± 5.5 | +9.4% | [+2.04, +6.81] | 2/20 | -14% | worse ✗ |
| zone | 34.7 ± 1.1 | -20.5% | [-9.39, -8.50] | 20/20 | 30% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.3 | 11.2 | 25.9 | 38.0 | 14.2 | 0.64 |
| nearest | look | 47.7 | 30.5 | 74.5 | 126.5 | 33.6 | 0.54 |
| round_robin | look | 43.6 | 26.9 | 55.2 | 64.1 | 29.5 | 0.71 |
| zone | look | 34.7 | 18.4 | 50.2 | 93.5 | 20.6 | 0.55 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.2 | 3.0 | 8% / 19 | 14% | 9.8 / 4.4 | 79% | 7.5 | 1.67 | 0.11 | 0.0% |
| nearest | look | 30.5 | 3.2 | 42% / 50 | 6% | 5.0 / 5.0 | 80% | 7.9 | 1.63 | 0.23 | 9.7% |
| round_robin | look | 26.9 | 2.6 | 50% / 40 | 2% | 11.8 / 4.6 | 98% | 9.7 | 1.56 | 0.01 | 0.0% |
| zone | look | 18.4 | 2.1 | 42% / 31 | 13% | 8.6 / 2.7 | 85% | 8.3 | 1.56 | 0.08 | 0.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 11.8 / 26 | 24, 8.7 / 20 | 46, 9.5 / 25 |
| nearest | look | 234, 32.6 / 78 | 24, 22.8 / 58 | 46, 23.5 / 64 |
| round_robin | look | 234, 26.7 / 55 | 24, 27.1 / 53 | 46, 28.0 / 54 |
| zone | look | 234, 17.2 / 49 | 24, 17.4 / 45 | 46, 24.9 / 61 |

## morning_rush · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.188 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 16.0; B0 floor = 7.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 13.5 ± 0.7 | -15.4% | [-2.68, -2.27] | 20/20 | 28% | better ✓ |
| nearest | 17.3 ± 1.4 | +8.4% | [+0.82, +1.86] | 4/20 | -15% | worse ✗ |
| zone | 15.4 ± 0.7 | -3.6% | [-0.86, -0.28] | 16/20 | 6% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 13.5 | 4.8 | 12.2 | 14.6 | 6.4 | 0.58 |
| nearest | look | 17.3 | 8.4 | 26.0 | 33.2 | 10.2 | 0.47 |
| round_robin | look | 16.0 | 7.8 | 19.2 | 25.8 | 8.9 | 0.63 |
| zone | look | 15.4 | 7.1 | 20.2 | 27.7 | 8.3 | 0.55 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 4.8 | 1.6 | 5% / 8 | 47% | 4.5 / 2.9 | 39% | 7.3 | 1.35 | 0.30 | 0.0% |
| nearest | look | 8.4 | 1.8 | 30% / 19 | 29% | 3.3 / 3.3 | 37% | 6.8 | 1.39 | 0.48 | 0.3% |
| round_robin | look | 7.8 | 1.1 | 21% / 15 | 65% | 5.7 / 1.8 | 64% | 12.4 | 1.07 | 0.01 | 0.0% |
| zone | look | 7.1 | 1.2 | 22% / 15 | 54% | 4.6 / 1.4 | 48% | 9.2 | 1.19 | 0.16 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 111, 5.3 / 12 | 12, 3.2 / 7 | 22, 3.3 / 9 |
| nearest | look | 111, 9.0 / 26 | 12, 7.4 / 20 | 22, 6.3 / 21 |
| round_robin | look | 111, 8.0 / 19 | 12, 7.0 / 15 | 22, 6.7 / 16 |
| zone | look | 111, 7.1 / 20 | 12, 4.9 / 14 | 22, 7.7 / 21 |

## morning_rush · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.592 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 168.7; B0 floor = 21.5)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 142.4 ± 18.3 | -15.6% | [-29.59, -22.97] | 20/20 | 18% | better ✓ |
| nearest | 213.4 ± 27.8 | +26.5% | [+33.06, +58.44] | 0/20 | -30% | worse ✗ |
| zone | 126.0 ± 21.8 | -25.3% | [-50.02, -35.14] | 20/20 | 29% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 142.4 | 116.8 | 250.6 | 292.1 | 121.0 | 0.66 |
| nearest | look | 213.4 | 187.9 | 536.3 | 783.7 | 191.9 | 0.55 |
| round_robin | look | 168.7 | 143.1 | 305.2 | 538.6 | 147.2 | 0.68 |
| zone | look | 126.0 | 101.5 | 359.4 | 1119.5 | 104.5 | 0.28 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 116.8 | 4.2 | 45% / 134 | 1% | 18.7 / 6.9 | 96% | 8.0 | 1.78 | 0.05 | 54.8% |
| nearest | look | 187.9 | 4.1 | 47% / 221 | 2% | 6.9 / 6.9 | 79% | 8.6 | 1.71 | 0.20 | 58.4% |
| round_robin | look | 143.1 | 4.1 | 51% / 150 | 1% | 18.9 / 7.1 | 95% | 8.4 | 1.72 | 0.00 | 58.8% |
| zone | look | 101.5 | 3.0 | 49% / 114 | 3% | 13.3 / 3.9 | 76% | 7.1 | 1.83 | 0.12 | 32.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 364, 142.7 / 253 | 33, 18.9 / 45 | 72, 29.9 / 92 |
| nearest | look | 364, 225.0 / 554 | 33, 44.5 / 93 | 72, 64.9 / 210 |
| round_robin | look | 364, 166.2 / 310 | 33, 47.3 / 88 | 72, 69.7 / 212 |
| zone | look | 364, 84.6 / 295 | 33, 28.5 / 73 | 72, 221.3 / 922 |

## morning_rush · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.793 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 482.7; B0 floor = 28.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 442.9 ± 32.5 | -8.2% | [-44.99, -35.04] | 20/20 | 9% | better ✓ |
| nearest | 531.5 ± 45.7 | +10.1% | [+33.53, +63.15] | 1/20 | -11% | worse ✗ |
| zone | 326.7 ± 27.3 | -32.3% | [-169.36, -143.05] | 20/20 | 34% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 442.9 | 410.2 | 920.2 | 991.6 | 414.6 | 0.62 |
| nearest | look | 531.5 | 498.7 | 1331.3 | 1684.8 | 503.1 | 0.58 |
| round_robin | look | 482.7 | 449.9 | 986.0 | 1321.8 | 454.3 | 0.65 |
| zone | look | 326.7 | 294.7 | 1027.0 | 1902.5 | 298.3 | 0.39 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 410.2 | 4.4 | 47% / 445 | 1% | 24.5 / 11.2 | 98% | 10.4 | 1.77 | 0.05 | 70.1% |
| nearest | look | 498.7 | 4.4 | 47% / 530 | 1% | 10.1 / 10.1 | 78% | 10.9 | 1.71 | 0.20 | 69.9% |
| round_robin | look | 449.9 | 4.4 | 52% / 453 | 1% | 25.7 / 11.5 | 96% | 10.8 | 1.71 | 0.00 | 71.6% |
| zone | look | 294.7 | 3.6 | 50% / 296 | 1% | 17.8 / 5.5 | 69% | 8.0 | 1.88 | 0.09 | 56.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 482, 518.3 / 934 | 48, 32.2 / 78 | 95, 49.2 / 144 |
| nearest | look | 482, 620.0 / 1382 | 48, 64.9 / 132 | 95, 98.8 / 326 |
| round_robin | look | 482, 554.2 / 1002 | 48, 64.1 / 121 | 95, 112.3 / 367 |
| zone | look | 482, 280.4 / 867 | 48, 41.4 / 99 | 95, 498.0 / 1667 |

## morning_rush · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 113.2; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 98.9 ± 23.0 | -12.6% | [-16.40, -12.20] | 20/20 | 14% | better ✓ |
| nearest | 125.6 ± 23.0 | +10.9% | [+7.35, +17.56] | 3/20 | -12% | worse ✗ |
| zone | 91.2 ± 19.2 | -19.5% | [-30.64, -14.17] | 18/20 | 22% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 98.9 | 80.9 | 166.1 | 212.9 | 84.9 | 0.70 |
| nearest | look | 125.6 | 107.6 | 260.3 | 347.7 | 111.5 | 0.63 |
| round_robin | look | 113.2 | 95.2 | 196.4 | 303.1 | 99.1 | 0.70 |
| zone | look | 91.2 | 73.8 | 209.8 | 876.6 | 77.1 | 0.28 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 80.9 | 3.9 | 48% / 91 | 1% | 12.5 / 8.0 | 98% | 5.3 | 1.85 | 0.04 | 51.5% |
| nearest | look | 107.6 | 3.9 | 50% / 122 | 1% | 8.5 / 8.5 | 93% | 5.5 | 1.80 | 0.07 | 57.3% |
| round_robin | look | 95.2 | 4.0 | 52% / 101 | 1% | 12.5 / 8.3 | 98% | 5.5 | 1.80 | 0.00 | 56.2% |
| zone | look | 73.8 | 3.3 | 51% / 81 | 1% | 9.9 / 5.8 | 88% | 5.1 | 1.86 | 0.05 | 30.3% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 96.9 / 169 | 24, 23.6 / 49 | 46, 29.7 / 70 |
| nearest | look | 234, 127.9 / 266 | 24, 32.7 / 64 | 46, 43.3 / 111 |
| round_robin | look | 234, 111.7 / 199 | 24, 32.1 / 61 | 46, 44.1 / 119 |
| zone | look | 234, 61.5 / 179 | 24, 23.3 / 55 | 46, 163.0 / 730 |

## morning_rush · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 48.2; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 34.0 ± 2.9 | -29.5% | [-14.95, -13.43] | 20/20 | 42% | better ✓ |
| nearest | 62.7 ± 14.1 | +30.2% | [+9.49, +20.10] | 0/20 | -43% | worse ✗ |
| zone | 40.0 ± 2.6 | -16.9% | [-9.55, -6.81] | 20/20 | 24% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 34.0 | 16.4 | 35.8 | 57.3 | 19.9 | 0.69 |
| nearest | look | 62.7 | 45.2 | 118.6 | 186.2 | 48.7 | 0.57 |
| round_robin | look | 48.2 | 30.8 | 60.6 | 88.2 | 34.1 | 0.73 |
| zone | look | 40.0 | 23.4 | 60.2 | 209.7 | 26.0 | 0.48 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 16.4 | 3.5 | 18% / 29 | 7% | 12.4 / 5.4 | 92% | 6.5 | 1.74 | 0.06 | 0.2% |
| nearest | look | 45.2 | 3.4 | 46% / 62 | 3% | 6.0 / 6.0 | 89% | 6.8 | 1.71 | 0.18 | 22.5% |
| round_robin | look | 30.8 | 3.3 | 50% / 43 | 1% | 12.2 / 5.7 | 98% | 7.2 | 1.68 | 0.00 | 2.5% |
| zone | look | 23.4 | 2.6 | 46% / 35 | 7% | 8.8 / 3.6 | 91% | 6.5 | 1.68 | 0.08 | 3.5% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 17.1 / 35 | 24, 13.1 / 31 | 46, 14.8 / 35 |
| nearest | look | 234, 50.2 / 123 | 24, 26.3 / 60 | 46, 28.9 / 73 |
| round_robin | look | 234, 30.9 / 61 | 24, 29.2 / 56 | 46, 31.2 / 59 |
| zone | look | 234, 20.8 / 57 | 24, 20.3 / 48 | 46, 38.1 / 129 |

## morning_rush · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.5; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.2 ± 1.0 | -33.7% | [-14.02, -12.54] | 20/20 | 52% | better ✓ |
| nearest | 41.0 ± 4.0 | +4.0% | [-0.07, +3.56] | 8/20 | -6% | - |
| zone | 31.9 ± 1.1 | -19.1% | [-8.05, -6.99] | 20/20 | 30% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.2 | 9.3 | 23.7 | 31.2 | 12.1 | 0.60 |
| nearest | look | 41.0 | 24.2 | 67.0 | 111.5 | 27.0 | 0.47 |
| round_robin | look | 39.5 | 23.5 | 50.9 | 60.2 | 25.4 | 0.69 |
| zone | look | 31.9 | 16.2 | 46.1 | 60.6 | 17.9 | 0.55 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.3 | 2.8 | 5% / 14 | 21% | 8.5 / 3.9 | 57% | 8.1 | 1.62 | 0.25 | 0.0% |
| nearest | look | 24.2 | 2.8 | 40% / 46 | 12% | 3.8 / 3.8 | 61% | 9.1 | 1.55 | 0.39 | 5.1% |
| round_robin | look | 23.5 | 1.8 | 47% / 36 | 7% | 11.2 / 2.8 | 95% | 14.6 | 1.37 | 0.01 | 0.0% |
| zone | look | 16.2 | 1.7 | 36% / 30 | 24% | 8.3 / 1.8 | 74% | 11.0 | 1.42 | 0.14 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 10.1 / 24 | 24, 6.2 / 16 | 46, 7.0 / 20 |
| nearest | look | 234, 26.2 / 68 | 24, 18.5 / 55 | 46, 17.1 / 58 |
| round_robin | look | 234, 23.3 / 51 | 24, 24.0 / 48 | 46, 24.6 / 50 |
| zone | look | 234, 15.4 / 44 | 24, 16.1 / 44 | 46, 20.4 / 48 |

## morning_rush · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 36.2; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.5 ± 1.1 | -29.5% | [-11.34, -9.93] | 20/20 | 48% | better ✓ |
| nearest | 37.8 ± 3.7 | +4.5% | [-0.02, +3.58] | 9/20 | -7% | - |
| zone | 31.1 ± 0.9 | -14.1% | [-5.63, -4.56] | 20/20 | 23% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.5 | 8.7 | 22.8 | 30.5 | 11.4 | 0.58 |
| nearest | look | 37.8 | 21.2 | 64.4 | 100.5 | 23.7 | 0.44 |
| round_robin | look | 36.2 | 20.6 | 47.5 | 58.8 | 22.1 | 0.66 |
| zone | look | 31.1 | 15.5 | 44.1 | 61.0 | 17.0 | 0.55 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.7 | 2.7 | 4% / 15 | 24% | 8.0 / 3.8 | 44% | 8.3 | 1.60 | 0.40 | 0.0% |
| nearest | look | 21.2 | 2.6 | 36% / 45 | 17% | 3.5 / 3.5 | 49% | 9.7 | 1.51 | 0.50 | 4.0% |
| round_robin | look | 20.6 | 1.5 | 42% / 33 | 17% | 10.7 / 2.0 | 91% | 18.7 | 1.24 | 0.01 | 0.0% |
| zone | look | 15.5 | 1.5 | 34% / 29 | 32% | 8.4 / 1.3 | 66% | 13.3 | 1.35 | 0.18 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 9.4 / 23 | 24, 5.7 / 14 | 46, 6.6 / 20 |
| nearest | look | 234, 23.0 / 65 | 24, 16.3 / 52 | 46, 14.7 / 54 |
| round_robin | look | 234, 20.4 / 47 | 24, 21.3 / 45 | 46, 21.3 / 46 |
| zone | look | 234, 14.9 / 42 | 24, 14.1 / 40 | 46, 19.1 / 49 |

## morning_rush · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 71.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 49.8 ± 12.5 | -30.4% | [-25.05, -18.73] | 20/20 | 38% | better ✓ |
| nearest | 113.1 ± 20.8 | +57.9% | [+32.82, +50.45] | 0/20 | -72% | worse ✗ |
| zone | 63.3 ± 10.8 | -11.7% | [-14.00, -2.71] | 16/20 | 15% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 49.8 | 33.4 | 70.6 | 114.2 | 35.8 | 0.69 |
| nearest | look | 113.1 | 96.7 | 289.3 | 443.3 | 99.0 | 0.52 |
| round_robin | look | 71.6 | 55.2 | 122.4 | 319.1 | 57.5 | 0.64 |
| zone | look | 63.3 | 47.3 | 145.3 | 717.5 | 49.2 | 0.24 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 33.4 | 2.4 | 38% / 43 | 6% | 12.2 / 4.2 | 94% | 9.5 | 1.58 | 0.04 | 20.7% |
| nearest | look | 96.7 | 2.3 | 43% / 116 | 5% | 4.5 / 4.5 | 80% | 10.3 | 1.54 | 0.21 | 53.9% |
| round_robin | look | 55.2 | 2.3 | 49% / 61 | 2% | 11.8 / 4.5 | 96% | 10.4 | 1.53 | 0.01 | 38.5% |
| zone | look | 47.3 | 1.9 | 42% / 59 | 12% | 8.5 / 2.7 | 80% | 9.0 | 1.52 | 0.08 | 24.3% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 38.8 / 72 | 24, 11.6 / 28 | 46, 16.9 / 47 |
| nearest | look | 234, 114.8 / 296 | 24, 25.0 / 58 | 46, 42.9 / 154 |
| round_robin | look | 234, 60.0 / 123 | 24, 26.8 / 51 | 46, 45.5 / 138 |
| zone | look | 234, 37.5 / 127 | 24, 18.7 / 49 | 46, 112.7 / 515 |

## morning_rush · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.5; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 30.5 ± 1.7 | -31.5% | [-14.59, -13.38] | 20/20 | 46% | better ✓ |
| nearest | 62.2 ± 12.2 | +39.7% | [+12.80, +23.19] | 0/20 | -58% | worse ✗ |
| zone | 37.8 ± 2.7 | -15.0% | [-7.63, -5.53] | 20/20 | 22% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 30.5 | 13.6 | 29.3 | 44.6 | 16.4 | 0.68 |
| nearest | look | 62.2 | 45.3 | 125.5 | 217.0 | 48.1 | 0.54 |
| round_robin | look | 44.5 | 27.9 | 56.7 | 96.5 | 30.4 | 0.71 |
| zone | look | 37.8 | 21.7 | 58.6 | 214.7 | 23.8 | 0.45 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.6 | 2.8 | 12% / 23 | 13% | 11.8 / 4.2 | 84% | 8.0 | 1.64 | 0.07 | 0.0% |
| nearest | look | 45.3 | 2.8 | 44% / 63 | 6% | 4.7 / 4.7 | 80% | 8.5 | 1.61 | 0.23 | 25.9% |
| round_robin | look | 27.9 | 2.6 | 50% / 40 | 2% | 11.8 / 4.5 | 98% | 9.7 | 1.56 | 0.01 | 1.5% |
| zone | look | 21.7 | 2.1 | 42% / 33 | 13% | 8.6 / 2.7 | 85% | 8.4 | 1.55 | 0.08 | 4.7% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 14.7 / 30 | 24, 9.0 / 21 | 46, 10.1 / 26 |
| nearest | look | 234, 50.6 / 129 | 24, 22.4 / 57 | 46, 29.9 / 86 |
| round_robin | look | 234, 27.7 / 57 | 24, 27.3 / 53 | 46, 29.2 / 55 |
| zone | look | 234, 19.4 / 55 | 24, 17.1 / 43 | 46, 35.6 / 121 |

## morning_rush · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 27.5 ± 1.1 | -36.8% | [-16.63, -15.44] | 20/20 | 54% | better ✓ |
| nearest | 42.1 ± 2.6 | -3.4% | [-2.70, -0.41] | 14/20 | 5% | - |
| zone | 34.1 ± 0.9 | -21.7% | [-9.93, -9.00] | 20/20 | 32% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 27.5 | 10.2 | 25.1 | 36.7 | 13.5 | 0.62 |
| nearest | look | 42.1 | 24.7 | 63.7 | 81.0 | 28.0 | 0.52 |
| round_robin | look | 43.6 | 26.9 | 55.2 | 64.1 | 29.5 | 0.71 |
| zone | look | 34.1 | 17.9 | 48.6 | 66.3 | 20.1 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.2 | 3.2 | 7% / 17 | 15% | 9.1 / 4.6 | 77% | 7.3 | 1.69 | 0.14 | 0.0% |
| nearest | look | 24.7 | 3.3 | 43% / 47 | 7% | 4.9 / 4.9 | 79% | 7.7 | 1.65 | 0.25 | 1.7% |
| round_robin | look | 26.9 | 2.6 | 50% / 40 | 2% | 11.8 / 4.6 | 98% | 9.7 | 1.56 | 0.01 | 0.0% |
| zone | look | 17.9 | 2.1 | 42% / 30 | 13% | 8.7 / 2.7 | 85% | 8.3 | 1.56 | 0.08 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 10.7 / 26 | 24, 8.4 / 19 | 46, 9.0 / 23 |
| nearest | look | 234, 25.7 / 64 | 24, 22.7 / 57 | 46, 20.6 / 59 |
| round_robin | look | 234, 26.7 / 55 | 24, 27.1 / 53 | 46, 28.0 / 54 |
| zone | look | 234, 16.9 / 48 | 24, 17.5 / 45 | 46, 23.0 / 51 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.3 ± 1.3 | -40.4% | [-17.67, -16.55] | 20/20 | 60% | better ✓ |
| nearest | 38.2 ± 2.2 | -9.8% | [-5.11, -3.19] | 19/20 | 15% | better ✓ |
| zone | 34.2 ± 1.5 | -19.3% | [-8.70, -7.63] | 20/20 | 29% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.3 | 9.2 | 24.5 | 37.0 | 11.2 | 0.57 |
| nearest | look | 38.2 | 21.9 | 60.0 | 80.9 | 24.2 | 0.51 |
| round_robin | look | 42.4 | 26.3 | 54.0 | 63.0 | 28.3 | 0.72 |
| zone | look | 34.2 | 18.3 | 50.2 | 64.2 | 20.1 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.2 | 2.0 | 16% / 16 | 14% | 6.6 / 3.6 | 90% | 9.4 | 1.51 | 0.09 | 0.0% |
| nearest | look | 21.9 | 2.3 | 39% / 41 | 9% | 3.9 / 3.9 | 88% | 9.5 | 1.49 | 0.14 | 0.4% |
| round_robin | look | 26.3 | 2.0 | 48% / 38 | 3% | 10.6 / 4.0 | 97% | 10.5 | 1.50 | 0.01 | 0.0% |
| zone | look | 18.3 | 1.9 | 39% / 31 | 15% | 7.9 / 3.2 | 84% | 8.8 | 1.47 | 0.09 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 7.9 / 23 | 120, 9.9 / 25 | 46, 10.2 / 25 |
| nearest | look | 114, 19.7 / 59 | 120, 24.0 / 59 | 46, 22.1 / 61 |
| round_robin | look | 114, 25.3 / 54 | 120, 26.7 / 53 | 46, 27.7 / 53 |
| zone | look | 114, 16.7 / 49 | 120, 17.8 / 49 | 46, 23.4 / 51 |

## lunch · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.174 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 14.6; B0 floor = 7.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 10.9 ± 0.5 | -25.1% | [-4.00, -3.32] | 20/20 | 49% | better ✓ |
| nearest | 13.4 ± 0.9 | -8.3% | [-1.64, -0.80] | 16/20 | 16% | better ✓ |
| zone | 14.5 ± 1.0 | -0.4% | [-0.33, +0.19] | 10/20 | 1% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 10.9 | 2.7 | 9.2 | 13.9 | 3.9 | 0.42 |
| nearest | look | 13.4 | 5.1 | 22.2 | 29.4 | 6.3 | 0.32 |
| round_robin | look | 14.6 | 6.5 | 16.0 | 24.8 | 7.5 | 0.58 |
| zone | look | 14.5 | 6.3 | 19.2 | 27.6 | 7.4 | 0.49 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 2.7 | 1.1 | 4% / 5 | 71% | 2.5 / 1.7 | 41% | 8.1 | 1.16 | 0.24 | 0.0% |
| nearest | look | 5.1 | 1.2 | 18% / 16 | 55% | 1.8 / 1.8 | 40% | 7.8 | 1.17 | 0.32 | 0.0% |
| round_robin | look | 6.5 | 1.0 | 14% / 14 | 75% | 5.2 / 1.6 | 57% | 11.7 | 1.05 | 0.01 | 0.0% |
| zone | look | 6.3 | 1.1 | 19% / 15 | 59% | 4.0 / 1.5 | 44% | 8.9 | 1.16 | 0.19 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 59, 2.0 / 8 | 54, 3.1 / 9 | 22, 3.5 / 9 |
| nearest | look | 59, 3.4 / 19 | 54, 6.3 / 22 | 22, 6.2 / 21 |
| round_robin | look | 59, 5.7 / 16 | 54, 6.9 / 16 | 22, 7.3 / 16 |
| zone | look | 59, 5.8 / 18 | 54, 6.1 / 18 | 22, 8.0 / 21 |

## lunch · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.546 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 74.3; B0 floor = 21.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 46.4 ± 3.5 | -37.6% | [-29.23, -26.51] | 20/20 | 53% | better ✓ |
| nearest | 82.9 ± 7.7 | +11.5% | [+5.71, +11.66] | 2/20 | -16% | worse ✗ |
| zone | 63.4 ± 5.9 | -14.8% | [-12.91, -8.57] | 19/20 | 21% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 46.4 | 21.2 | 50.0 | 96.3 | 25.0 | 0.63 |
| nearest | look | 82.9 | 57.5 | 140.5 | 343.9 | 61.5 | 0.53 |
| round_robin | look | 74.3 | 49.0 | 95.7 | 196.5 | 52.9 | 0.72 |
| zone | look | 63.4 | 39.0 | 106.8 | 434.9 | 42.0 | 0.41 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 21.2 | 3.8 | 20% / 36 | 1% | 13.2 / 6.4 | 97% | 6.7 | 1.81 | 0.08 | 0.3% |
| nearest | look | 57.5 | 4.0 | 45% / 86 | 2% | 6.3 / 6.3 | 93% | 7.1 | 1.74 | 0.13 | 11.8% |
| round_robin | look | 49.0 | 3.9 | 48% / 68 | 1% | 17.1 / 7.4 | 98% | 7.0 | 1.72 | 0.00 | 2.2% |
| zone | look | 39.0 | 3.0 | 45% / 55 | 5% | 12.0 / 4.8 | 87% | 6.6 | 1.78 | 0.12 | 5.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 184, 21.0 / 49 | 177, 21.2 / 50 | 72, 21.6 / 51 |
| nearest | look | 184, 61.0 / 146 | 177, 55.4 / 144 | 72, 53.5 / 142 |
| round_robin | look | 184, 48.8 / 95 | 177, 49.7 / 96 | 72, 47.6 / 92 |
| zone | look | 184, 32.2 / 88 | 177, 34.9 / 97 | 72, 66.1 / 244 |

## lunch · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.732 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 191.5; B0 floor = 28.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 119.7 ± 19.2 | -37.5% | [-77.13, -66.66] | 20/20 | 44% | better ✓ |
| nearest | 229.0 ± 33.1 | +19.5% | [+25.57, +50.24] | 0/20 | -23% | worse ✗ |
| zone | 151.6 ± 18.0 | -20.9% | [-47.62, -32.62] | 20/20 | 24% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 119.7 | 86.6 | 198.4 | 474.7 | 91.4 | 0.64 |
| nearest | look | 229.0 | 196.0 | 636.4 | 1123.0 | 200.6 | 0.46 |
| round_robin | look | 191.5 | 158.4 | 467.2 | 945.2 | 163.2 | 0.52 |
| zone | look | 151.6 | 119.7 | 591.6 | 1132.6 | 123.2 | 0.28 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 86.6 | 4.8 | 45% / 102 | 1% | 22.2 / 9.4 | 95% | 5.9 | 1.93 | 0.05 | 23.4% |
| nearest | look | 196.0 | 4.7 | 46% / 236 | 1% | 8.6 / 8.6 | 82% | 7.0 | 1.85 | 0.20 | 43.3% |
| round_robin | look | 158.4 | 4.9 | 49% / 171 | 1% | 23.3 / 12.1 | 95% | 6.7 | 1.83 | 0.00 | 38.9% |
| zone | look | 119.7 | 3.6 | 47% / 136 | 2% | 16.2 / 6.8 | 76% | 6.1 | 1.98 | 0.10 | 24.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 237, 94.9 / 176 | 244, 89.1 / 241 | 95, 57.2 / 151 |
| nearest | look | 237, 210.1 / 529 | 244, 206.7 / 769 | 95, 129.3 / 508 |
| round_robin | look | 237, 159.2 / 322 | 244, 172.6 / 621 | 95, 115.6 / 380 |
| zone | look | 237, 70.3 / 210 | 244, 116.4 / 596 | 95, 253.3 / 853 |

## lunch · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 50.9; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 41.0 ± 3.3 | -19.4% | [-11.28, -8.61] | 20/20 | 27% | better ✓ |
| nearest | 51.7 ± 3.3 | +1.6% | [-0.33, +2.01] | 8/20 | -2% | - |
| zone | 44.7 ± 2.7 | -12.2% | [-7.24, -5.23] | 20/20 | 17% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 41.0 | 23.5 | 51.2 | 75.7 | 27.0 | 0.67 |
| nearest | look | 51.7 | 34.1 | 71.0 | 141.2 | 37.7 | 0.64 |
| round_robin | look | 50.9 | 33.3 | 65.0 | 116.7 | 36.9 | 0.71 |
| zone | look | 44.7 | 27.6 | 67.6 | 168.1 | 30.7 | 0.56 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 23.5 | 3.4 | 35% / 37 | 1% | 10.4 / 7.4 | 99% | 4.9 | 1.83 | 0.05 | 0.3% |
| nearest | look | 34.1 | 3.6 | 46% / 50 | 1% | 7.7 / 7.7 | 98% | 5.0 | 1.78 | 0.08 | 4.3% |
| round_robin | look | 33.3 | 3.5 | 47% / 47 | 1% | 11.3 / 7.1 | 99% | 5.0 | 1.77 | 0.00 | 1.6% |
| zone | look | 27.6 | 3.1 | 48% / 38 | 2% | 8.9 / 5.9 | 96% | 4.8 | 1.78 | 0.06 | 3.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 22.7 / 50 | 120, 24.1 / 51 | 46, 24.2 / 52 |
| nearest | look | 114, 34.3 / 72 | 120, 33.9 / 69 | 46, 34.2 / 76 |
| round_robin | look | 114, 32.2 / 64 | 120, 34.3 / 66 | 46, 33.8 / 64 |
| zone | look | 114, 24.2 / 63 | 120, 27.2 / 67 | 46, 37.2 / 104 |

## lunch · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 45.5; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 30.6 ± 1.7 | -32.8% | [-15.49, -14.36] | 20/20 | 47% | better ✓ |
| nearest | 43.6 ± 1.8 | -4.3% | [-2.72, -1.13] | 17/20 | 6% | better ✓ |
| zone | 36.9 ± 1.5 | -18.9% | [-9.00, -8.16] | 20/20 | 27% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 30.6 | 14.0 | 33.9 | 55.8 | 16.5 | 0.62 |
| nearest | look | 43.6 | 26.8 | 63.2 | 98.0 | 29.5 | 0.58 |
| round_robin | look | 45.5 | 28.9 | 58.0 | 68.8 | 31.5 | 0.73 |
| zone | look | 36.9 | 20.6 | 54.7 | 77.8 | 22.9 | 0.58 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.0 | 2.5 | 23% / 24 | 4% | 8.5 / 5.0 | 96% | 7.4 | 1.65 | 0.08 | 0.0% |
| nearest | look | 26.8 | 2.7 | 44% / 45 | 4% | 5.2 / 5.2 | 94% | 7.4 | 1.62 | 0.12 | 0.8% |
| round_robin | look | 28.9 | 2.5 | 49% / 42 | 1% | 11.0 / 5.1 | 98% | 7.8 | 1.61 | 0.00 | 0.0% |
| zone | look | 20.6 | 2.3 | 44% / 33 | 9% | 7.9 / 4.1 | 90% | 6.9 | 1.58 | 0.09 | 0.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 12.6 / 32 | 120, 14.8 / 34 | 46, 15.2 / 36 |
| nearest | look | 114, 24.8 / 61 | 120, 28.4 / 63 | 46, 27.8 / 64 |
| round_robin | look | 114, 28.4 / 57 | 120, 29.1 / 58 | 46, 29.7 / 57 |
| zone | look | 114, 18.8 / 52 | 120, 20.3 / 53 | 46, 25.9 / 58 |

## lunch · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 37.7; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.8 ± 0.9 | -44.7% | [-17.60, -16.05] | 20/20 | 71% | better ✓ |
| nearest | 31.8 ± 1.4 | -15.5% | [-6.77, -4.87] | 20/20 | 25% | better ✓ |
| zone | 31.6 ± 1.2 | -16.1% | [-6.79, -5.36] | 20/20 | 26% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 20.8 | 5.2 | 16.1 | 29.2 | 6.8 | 0.48 |
| nearest | look | 31.8 | 16.0 | 56.2 | 66.9 | 17.8 | 0.40 |
| round_robin | look | 37.7 | 22.1 | 48.7 | 59.3 | 23.6 | 0.68 |
| zone | look | 31.6 | 16.0 | 45.9 | 58.7 | 17.5 | 0.54 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.2 | 1.6 | 7% / 10 | 38% | 4.3 / 2.4 | 75% | 11.8 | 1.34 | 0.12 | 0.0% |
| nearest | look | 16.0 | 1.8 | 31% / 37 | 24% | 2.5 / 2.5 | 73% | 11.8 | 1.35 | 0.22 | 0.0% |
| round_robin | look | 22.1 | 1.5 | 42% / 34 | 11% | 10.4 / 2.7 | 93% | 15.5 | 1.32 | 0.01 | 0.0% |
| zone | look | 16.0 | 1.5 | 34% / 30 | 27% | 7.8 / 2.3 | 71% | 11.6 | 1.36 | 0.15 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 3.7 / 14 | 120, 6.2 / 17 | 46, 6.2 / 16 |
| nearest | look | 114, 12.3 / 55 | 120, 18.6 / 56 | 46, 18.2 / 55 |
| round_robin | look | 114, 20.8 / 48 | 120, 22.7 / 48 | 46, 23.4 / 47 |
| zone | look | 114, 14.7 / 44 | 120, 15.6 / 45 | 46, 20.3 / 48 |

## lunch · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 33.8; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.0 ± 0.7 | -43.6% | [-15.22, -14.27] | 20/20 | 75% | better ✓ |
| nearest | 27.6 ± 1.5 | -18.4% | [-6.79, -5.57] | 20/20 | 31% | better ✓ |
| zone | 29.9 ± 1.3 | -11.6% | [-4.39, -3.43] | 20/20 | 20% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.0 | 3.6 | 12.8 | 27.4 | 5.0 | 0.38 |
| nearest | look | 27.6 | 12.0 | 52.0 | 64.3 | 13.5 | 0.31 |
| round_robin | look | 33.8 | 18.5 | 44.4 | 56.9 | 19.7 | 0.64 |
| zone | look | 29.9 | 14.5 | 42.7 | 57.8 | 15.8 | 0.52 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 3.6 | 1.3 | 4% / 8 | 53% | 3.2 / 1.8 | 61% | 12.8 | 1.25 | 0.18 | 0.0% |
| nearest | look | 12.0 | 1.5 | 23% / 35 | 36% | 1.8 / 1.8 | 60% | 12.9 | 1.26 | 0.27 | 0.0% |
| round_robin | look | 18.5 | 1.3 | 35% / 31 | 28% | 10.3 / 2.0 | 87% | 19.3 | 1.20 | 0.01 | 0.0% |
| zone | look | 14.5 | 1.3 | 30% / 29 | 37% | 7.7 / 1.9 | 63% | 13.7 | 1.29 | 0.19 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 2.1 / 10 | 120, 4.7 / 14 | 46, 4.6 / 13 |
| nearest | look | 114, 8.2 / 50 | 120, 14.8 / 52 | 46, 13.8 / 50 |
| round_robin | look | 114, 17.0 / 45 | 120, 18.9 / 43 | 46, 21.0 / 45 |
| zone | look | 114, 13.2 / 41 | 120, 13.9 / 41 | 46, 18.9 / 46 |

## lunch · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.3; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.7 ± 1.2 | -40.8% | [-18.47, -16.91] | 20/20 | 60% | better ✓ |
| nearest | 43.3 ± 4.5 | -0.1% | [-1.58, +1.57] | 11/20 | 0% | - |
| zone | 37.3 ± 2.0 | -13.9% | [-6.87, -5.06] | 20/20 | 21% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.7 | 9.6 | 25.1 | 42.0 | 11.6 | 0.58 |
| nearest | look | 43.3 | 27.2 | 73.3 | 189.1 | 29.2 | 0.47 |
| round_robin | look | 43.3 | 27.3 | 55.5 | 113.8 | 29.3 | 0.69 |
| zone | look | 37.3 | 21.5 | 58.6 | 215.9 | 23.3 | 0.43 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.6 | 2.0 | 16% / 16 | 14% | 6.9 / 3.6 | 91% | 9.5 | 1.51 | 0.08 | 0.5% |
| nearest | look | 27.2 | 2.0 | 40% / 45 | 8% | 3.8 / 3.8 | 89% | 9.6 | 1.49 | 0.12 | 7.6% |
| round_robin | look | 27.3 | 2.0 | 48% / 39 | 3% | 10.6 / 4.0 | 97% | 10.5 | 1.50 | 0.01 | 1.7% |
| zone | look | 21.5 | 1.8 | 39% / 34 | 15% | 7.9 / 3.2 | 83% | 8.9 | 1.47 | 0.09 | 4.4% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 8.6 / 24 | 120, 10.3 / 26 | 46, 10.2 / 25 |
| nearest | look | 114, 23.8 / 67 | 120, 30.3 / 81 | 46, 26.8 / 69 |
| round_robin | look | 114, 25.8 / 55 | 120, 28.1 / 55 | 46, 29.0 / 54 |
| zone | look | 114, 18.0 / 52 | 120, 20.1 / 56 | 46, 33.9 / 96 |

## lunch · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.4 ± 1.0 | -40.2% | [-17.54, -16.53] | 20/20 | 60% | better ✓ |
| nearest | 39.3 ± 2.1 | -7.2% | [-3.98, -2.13] | 19/20 | 11% | better ✓ |
| zone | 34.4 ± 1.6 | -18.9% | [-8.52, -7.47] | 20/20 | 28% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.4 | 9.3 | 24.6 | 40.6 | 11.3 | 0.57 |
| nearest | look | 39.3 | 23.1 | 61.1 | 102.2 | 25.3 | 0.51 |
| round_robin | look | 42.4 | 26.3 | 54.0 | 63.0 | 28.4 | 0.72 |
| zone | look | 34.4 | 18.5 | 50.9 | 82.2 | 20.3 | 0.56 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.3 | 2.0 | 16% / 16 | 14% | 6.7 / 3.6 | 91% | 9.4 | 1.51 | 0.08 | 0.0% |
| nearest | look | 23.1 | 2.2 | 40% / 42 | 9% | 3.9 / 3.9 | 88% | 9.5 | 1.49 | 0.14 | 1.7% |
| round_robin | look | 26.3 | 2.0 | 48% / 38 | 3% | 10.6 / 4.0 | 97% | 10.5 | 1.50 | 0.01 | 0.0% |
| zone | look | 18.5 | 1.9 | 39% / 31 | 15% | 7.9 / 3.2 | 84% | 8.8 | 1.47 | 0.09 | 0.3% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 8.2 / 24 | 120, 10.0 / 25 | 46, 10.1 / 23 |
| nearest | look | 114, 20.9 / 61 | 120, 25.1 / 60 | 46, 23.4 / 61 |
| round_robin | look | 114, 25.3 / 54 | 120, 26.7 / 53 | 46, 27.8 / 53 |
| zone | look | 114, 16.8 / 49 | 120, 18.0 / 50 | 46, 24.3 / 54 |

## lunch · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.3 ± 1.3 | -40.4% | [-17.66, -16.55] | 20/20 | 60% | better ✓ |
| nearest | 38.0 ± 2.0 | -10.4% | [-5.30, -3.53] | 19/20 | 16% | better ✓ |
| zone | 34.2 ± 1.5 | -19.3% | [-8.70, -7.63] | 20/20 | 29% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.3 | 9.2 | 24.5 | 37.0 | 11.2 | 0.57 |
| nearest | look | 38.0 | 21.7 | 59.4 | 68.8 | 23.9 | 0.51 |
| round_robin | look | 42.4 | 26.3 | 54.0 | 63.0 | 28.3 | 0.72 |
| zone | look | 34.2 | 18.3 | 50.2 | 64.2 | 20.1 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.2 | 2.0 | 16% / 16 | 14% | 6.5 / 3.7 | 90% | 9.4 | 1.51 | 0.10 | 0.0% |
| nearest | look | 21.7 | 2.3 | 39% / 41 | 9% | 3.8 / 3.8 | 88% | 9.5 | 1.50 | 0.15 | 0.0% |
| round_robin | look | 26.3 | 2.0 | 48% / 38 | 3% | 10.6 / 4.0 | 97% | 10.5 | 1.50 | 0.01 | 0.0% |
| zone | look | 18.3 | 1.9 | 39% / 31 | 15% | 7.9 / 3.2 | 84% | 8.8 | 1.47 | 0.09 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 7.9 / 23 | 120, 10.0 / 25 | 46, 10.2 / 25 |
| nearest | look | 114, 19.6 / 59 | 120, 23.5 / 59 | 46, 22.1 / 60 |
| round_robin | look | 114, 25.3 / 54 | 120, 26.7 / 53 | 46, 27.7 / 53 |
| zone | look | 114, 16.7 / 49 | 120, 17.8 / 49 | 46, 23.4 / 51 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.7; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.5 ± 1.3 | -36.2% | [-16.75, -15.57] | 20/20 | 53% | better ✓ |
| nearest | 49.3 ± 9.6 | +10.4% | [+1.29, +9.39] | 7/20 | -15% | - |
| zone | 35.7 ± 1.9 | -20.0% | [-9.75, -8.22] | 20/20 | 29% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.5 | 11.8 | 31.2 | 49.9 | 14.3 | 0.58 |
| nearest | look | 49.3 | 32.1 | 99.0 | 270.2 | 35.1 | 0.43 |
| round_robin | look | 44.7 | 27.7 | 55.8 | 75.1 | 30.4 | 0.73 |
| zone | look | 35.7 | 19.3 | 51.2 | 107.7 | 21.5 | 0.56 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.8 | 2.4 | 23% / 19 | 13% | 7.3 / 3.9 | 92% | 8.7 | 1.57 | 0.07 | 0.1% |
| nearest | look | 32.1 | 2.9 | 40% / 49 | 10% | 4.0 / 4.0 | 78% | 7.5 | 1.60 | 0.25 | 8.3% |
| round_robin | look | 27.7 | 2.7 | 48% / 38 | 3% | 9.8 / 3.9 | 97% | 9.4 | 1.57 | 0.00 | 0.2% |
| zone | look | 19.3 | 2.2 | 40% / 30 | 13% | 7.7 / 4.4 | 85% | 8.1 | 1.59 | 0.10 | 0.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 6.0 / 19 | 242, 12.1 / 31 | 46, 13.2 / 32 |
| nearest | look | 23, 8.2 / 45 | 242, 35.4 / 116 | 46, 25.8 / 66 |
| round_robin | look | 23, 25.2 / 51 | 242, 27.8 / 56 | 46, 28.6 / 55 |
| zone | look | 23, 16.2 / 43 | 242, 18.8 / 51 | 46, 23.7 / 53 |

## evening_rush · 15 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 0.483 (0.188 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 15.9; B0 floor = 7.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 13.3 ± 0.7 | -16.1% | [-2.80, -2.33] | 20/20 | 29% | better ✓ |
| nearest | 19.0 ± 1.4 | +19.2% | [+2.61, +3.58] | 0/20 | -35% | worse ✗ |
| zone | 15.9 ± 1.1 | +0.3% | [-0.20, +0.29] | 10/20 | -0% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 13.3 | 5.0 | 13.3 | 17.2 | 6.2 | 0.57 |
| nearest | look | 19.0 | 9.9 | 27.1 | 36.5 | 11.8 | 0.53 |
| round_robin | look | 15.9 | 7.6 | 17.7 | 24.6 | 8.8 | 0.65 |
| zone | look | 15.9 | 7.6 | 21.0 | 28.1 | 8.8 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.0 | 1.3 | 6% / 6 | 67% | 4.5 / 2.9 | 48% | 9.2 | 1.17 | 0.36 | 0.0% |
| nearest | look | 9.9 | 1.9 | 31% / 18 | 30% | 3.2 / 3.2 | 35% | 6.4 | 1.35 | 0.82 | 0.2% |
| round_robin | look | 7.6 | 1.1 | 18% / 14 | 67% | 5.8 / 2.4 | 62% | 12.1 | 1.08 | 0.01 | 0.0% |
| zone | look | 7.6 | 1.3 | 23% / 15 | 53% | 4.7 / 2.7 | 48% | 9.3 | 1.19 | 0.18 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 11, 0.2 / 1 | 112, 5.3 / 13 | 22, 5.6 / 13 |
| nearest | look | 11, 0.0 / 0 | 112, 10.8 / 28 | 22, 10.3 / 25 |
| round_robin | look | 11, 3.5 / 12 | 112, 7.9 / 18 | 22, 8.6 / 18 |
| zone | look | 11, 4.7 / 15 | 112, 7.6 / 21 | 22, 8.9 / 21 |

## evening_rush · 45 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1.52 (0.592 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 155.1; B0 floor = 21.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 62.8 ± 5.9 | -59.5% | [-97.54, -87.22] | 20/20 | 69% | better ✓ |
| nearest | 170.9 ± 19.1 | +10.1% | [+8.51, +22.81] | 5/20 | -12% | - |
| zone | 111.8 ± 14.5 | -27.9% | [-49.59, -37.44] | 20/20 | 32% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 62.8 | 37.9 | 96.8 | 241.3 | 41.6 | 0.57 |
| nearest | look | 170.9 | 146.1 | 596.9 | 963.3 | 149.6 | 0.36 |
| round_robin | look | 155.1 | 130.1 | 551.0 | 852.5 | 133.9 | 0.36 |
| zone | look | 111.8 | 87.7 | 491.3 | 986.2 | 90.6 | 0.22 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 37.9 | 3.7 | 37% / 51 | 1% | 12.8 / 5.8 | 96% | 6.3 | 1.96 | 0.06 | 16.1% |
| nearest | look | 146.1 | 3.5 | 44% / 175 | 2% | 5.4 / 5.4 | 88% | 6.8 | 1.96 | 0.16 | 34.6% |
| round_robin | look | 130.1 | 3.8 | 48% / 147 | 1% | 15.1 / 6.5 | 97% | 6.9 | 1.91 | 0.00 | 28.2% |
| zone | look | 87.7 | 2.9 | 46% / 101 | 4% | 10.8 / 6.1 | 76% | 6.8 | 1.99 | 0.10 | 17.8% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 36, 18.6 / 51 | 365, 41.0 / 105 | 72, 31.4 / 77 |
| nearest | look | 36, 35.1 / 92 | 365, 170.2 / 633 | 72, 78.5 / 307 |
| round_robin | look | 36, 44.4 / 87 | 365, 151.7 / 594 | 72, 62.8 / 148 |
| zone | look | 36, 28.1 / 72 | 365, 93.5 / 529 | 72, 87.8 / 408 |

## evening_rush · 60 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 2.03 (0.793 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 395.7; B0 floor = 28.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 230.4 ± 25.5 | -41.8% | [-171.47, -158.87] | 20/20 | 45% | better ✓ |
| nearest | 416.7 ± 33.2 | +5.3% | [+12.82, +29.67] | 2/20 | -6% | worse ✗ |
| zone | 298.9 ± 25.9 | -24.5% | [-106.08, -87.38] | 20/20 | 26% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 230.4 | 198.8 | 739.5 | 1328.2 | 202.1 | 0.40 |
| nearest | look | 416.7 | 384.9 | 1123.4 | 1481.0 | 388.4 | 0.49 |
| round_robin | look | 395.7 | 363.8 | 1032.8 | 1280.5 | 367.4 | 0.51 |
| zone | look | 298.9 | 267.6 | 1176.9 | 1713.1 | 270.5 | 0.31 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 198.8 | 3.3 | 41% / 236 | 1% | 16.5 / 7.9 | 80% | 6.9 | 2.41 | 0.06 | 52.5% |
| nearest | look | 384.9 | 3.4 | 45% / 418 | 1% | 6.9 / 6.9 | 83% | 7.4 | 2.20 | 0.17 | 54.4% |
| round_robin | look | 363.8 | 3.5 | 47% / 385 | 1% | 20.3 / 11.2 | 96% | 7.3 | 2.17 | 0.00 | 51.5% |
| zone | look | 267.6 | 3.0 | 47% / 283 | 1% | 14.4 / 8.1 | 67% | 7.5 | 2.34 | 0.08 | 35.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 49, 30.7 / 87 | 486, 231.0 / 784 | 95, 121.4 / 538 |
| nearest | look | 49, 49.9 / 126 | 486, 457.3 / 1164 | 95, 187.0 / 833 |
| round_robin | look | 49, 62.0 / 118 | 486, 431.8 / 1062 | 95, 170.7 / 752 |
| zone | look | 49, 38.7 / 95 | 486, 299.9 / 1212 | 95, 222.3 / 1095 |

## evening_rush · 30 floors x 2 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 116.4; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 59.0 ± 8.2 | -49.3% | [-62.67, -52.41] | 20/20 | 56% | better ✓ |
| nearest | 117.9 ± 20.6 | +1.2% | [-3.59, +6.28] | 11/20 | -1% | - |
| zone | 97.2 ± 13.2 | -16.6% | [-28.80, -10.06] | 16/20 | 19% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 59.0 | 41.2 | 119.9 | 297.3 | 44.8 | 0.51 |
| nearest | look | 117.9 | 100.2 | 460.2 | 776.6 | 103.6 | 0.31 |
| round_robin | look | 116.4 | 98.7 | 463.3 | 764.1 | 102.2 | 0.31 |
| zone | look | 97.2 | 79.9 | 474.7 | 838.5 | 82.9 | 0.21 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 41.2 | 3.5 | 42% / 52 | 1% | 9.1 / 6.2 | 98% | 4.5 | 2.01 | 0.04 | 22.1% |
| nearest | look | 100.2 | 3.4 | 44% / 116 | 1% | 6.5 / 6.5 | 96% | 4.7 | 2.05 | 0.08 | 29.5% |
| round_robin | look | 98.7 | 3.5 | 47% / 108 | 1% | 9.9 / 6.8 | 99% | 4.7 | 2.01 | 0.00 | 27.1% |
| zone | look | 79.9 | 3.0 | 46% / 90 | 2% | 7.8 / 6.1 | 89% | 4.9 | 2.03 | 0.07 | 18.3% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 21.9 / 50 | 242, 45.0 / 133 | 46, 30.8 / 75 |
| nearest | look | 23, 26.5 / 60 | 242, 117.4 / 505 | 46, 45.1 / 134 |
| round_robin | look | 23, 30.5 / 58 | 242, 116.0 / 507 | 46, 40.9 / 97 |
| zone | look | 23, 22.8 / 52 | 242, 87.3 / 510 | 46, 69.0 / 309 |

## evening_rush · 30 floors x 3 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.7; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 33.9 ± 1.6 | -31.8% | [-16.85, -14.76] | 20/20 | 45% | better ✓ |
| nearest | 60.1 ± 11.9 | +20.9% | [+5.74, +15.49] | 4/20 | -29% | worse ✗ |
| zone | 40.9 ± 2.7 | -17.6% | [-10.28, -7.24] | 20/20 | 25% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 33.9 | 16.7 | 40.2 | 65.2 | 19.7 | 0.63 |
| nearest | look | 60.1 | 42.6 | 145.9 | 426.1 | 45.9 | 0.38 |
| round_robin | look | 49.7 | 32.0 | 64.0 | 168.7 | 35.4 | 0.67 |
| zone | look | 40.9 | 24.1 | 61.3 | 196.2 | 26.7 | 0.49 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 16.7 | 3.0 | 32% / 26 | 4% | 8.2 / 4.9 | 97% | 6.7 | 1.73 | 0.07 | 1.9% |
| nearest | look | 42.6 | 3.3 | 43% / 57 | 5% | 4.9 / 4.9 | 89% | 6.4 | 1.74 | 0.17 | 12.1% |
| round_robin | look | 32.0 | 3.4 | 47% / 44 | 1% | 10.0 / 4.7 | 98% | 7.0 | 1.71 | 0.00 | 3.4% |
| zone | look | 24.1 | 2.6 | 43% / 34 | 8% | 7.6 / 5.0 | 90% | 6.3 | 1.74 | 0.09 | 4.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 12.3 / 31 | 242, 16.9 / 40 | 46, 17.5 / 41 |
| nearest | look | 23, 17.6 / 57 | 242, 47.4 / 172 | 46, 29.5 / 69 |
| round_robin | look | 23, 28.2 / 56 | 242, 32.9 / 66 | 46, 29.3 / 58 |
| zone | look | 23, 17.9 / 45 | 242, 24.0 / 62 | 46, 27.5 / 62 |

## evening_rush · 30 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.9; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.9 ± 1.1 | -37.6% | [-15.41, -14.59] | 20/20 | 59% | better ✓ |
| nearest | 44.5 ± 6.3 | +11.7% | [+2.54, +7.60] | 3/20 | -18% | worse ✗ |
| zone | 33.2 ± 1.3 | -16.7% | [-7.18, -6.19] | 20/20 | 26% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.9 | 8.7 | 25.4 | 36.3 | 10.6 | 0.54 |
| nearest | look | 44.5 | 27.5 | 85.4 | 230.7 | 30.3 | 0.41 |
| round_robin | look | 39.9 | 23.7 | 50.6 | 60.3 | 25.6 | 0.71 |
| zone | look | 33.2 | 17.2 | 47.3 | 64.2 | 18.9 | 0.57 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.7 | 1.9 | 11% / 12 | 34% | 6.8 / 3.3 | 76% | 10.9 | 1.39 | 0.16 | 0.0% |
| nearest | look | 27.5 | 2.8 | 37% / 45 | 15% | 3.6 / 3.6 | 56% | 8.1 | 1.52 | 0.55 | 6.4% |
| round_robin | look | 23.7 | 1.9 | 45% / 33 | 9% | 10.0 / 2.7 | 94% | 14.0 | 1.39 | 0.01 | 0.0% |
| zone | look | 17.2 | 1.7 | 37% / 29 | 23% | 8.0 / 3.5 | 75% | 11.0 | 1.45 | 0.14 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 1.4 / 7 | 242, 9.2 / 26 | 46, 9.5 / 24 |
| nearest | look | 23, 1.0 / 5 | 242, 30.6 / 92 | 46, 23.7 / 63 |
| round_robin | look | 23, 19.6 / 43 | 242, 23.8 / 51 | 46, 24.7 / 50 |
| zone | look | 23, 13.2 / 38 | 242, 16.9 / 47 | 46, 20.8 / 47 |

## evening_rush · 30 floors x 8 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 36.3; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.3 ± 1.2 | -33.0% | [-12.32, -11.60] | 20/20 | 54% | better ✓ |
| nearest | 44.3 ± 6.5 | +22.3% | [+5.82, +11.04] | 0/20 | -37% | worse ✗ |
| zone | 31.9 ± 1.4 | -12.1% | [-4.88, -3.85] | 20/20 | 20% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.3 | 8.2 | 24.7 | 33.6 | 10.0 | 0.53 |
| nearest | look | 44.3 | 27.3 | 85.0 | 224.6 | 30.1 | 0.41 |
| round_robin | look | 36.3 | 20.4 | 46.1 | 58.2 | 22.0 | 0.69 |
| zone | look | 31.9 | 16.1 | 45.2 | 59.5 | 17.6 | 0.56 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.2 | 1.8 | 7% / 9 | 43% | 6.8 / 3.2 | 60% | 11.5 | 1.35 | 0.37 | 0.0% |
| nearest | look | 27.3 | 2.8 | 37% / 45 | 15% | 3.6 / 3.6 | 43% | 8.2 | 1.52 | 0.86 | 6.4% |
| round_robin | look | 20.4 | 1.6 | 40% / 30 | 22% | 10.5 / 2.4 | 89% | 17.9 | 1.27 | 0.01 | 0.0% |
| zone | look | 16.1 | 1.5 | 33% / 29 | 31% | 8.2 / 3.0 | 67% | 13.2 | 1.37 | 0.19 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 0.2 / 1 | 242, 8.9 / 25 | 46, 8.8 / 23 |
| nearest | look | 23, 0.0 / 0 | 242, 30.5 / 92 | 46, 23.3 / 63 |
| round_robin | look | 23, 16.4 / 40 | 242, 20.5 / 46 | 46, 22.2 / 46 |
| zone | look | 23, 12.3 / 37 | 242, 15.8 / 45 | 46, 19.6 / 45 |

## evening_rush · 30 floors x 4 cars · capacity 4 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 74.8; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 33.0 ± 2.4 | -55.9% | [-46.63, -37.31] | 20/20 | 69% | better ✓ |
| nearest | 117.8 ± 26.1 | +57.6% | [+33.66, +53.22] | 0/20 | -71% | worse ✗ |
| zone | 68.1 ± 13.2 | -8.9% | [-12.71, -0.80] | 13/20 | 11% | - |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 33.0 | 16.6 | 40.0 | 89.6 | 18.7 | 0.60 |
| nearest | look | 117.8 | 101.5 | 473.4 | 811.2 | 103.6 | 0.30 |
| round_robin | look | 74.8 | 58.2 | 231.9 | 601.6 | 60.5 | 0.32 |
| zone | look | 68.1 | 52.0 | 269.9 | 738.0 | 53.9 | 0.19 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 16.6 | 2.1 | 29% / 24 | 8% | 8.4 / 3.9 | 95% | 9.1 | 1.56 | 0.06 | 7.3% |
| nearest | look | 101.5 | 2.1 | 41% / 122 | 7% | 3.9 / 3.9 | 79% | 8.8 | 1.62 | 0.22 | 34.8% |
| round_robin | look | 58.2 | 2.3 | 48% / 65 | 2% | 9.7 / 3.9 | 97% | 9.7 | 1.59 | 0.00 | 20.4% |
| zone | look | 52.0 | 1.8 | 41% / 65 | 12% | 7.6 / 4.3 | 76% | 8.9 | 1.59 | 0.10 | 16.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 7.5 / 23 | 242, 17.7 / 41 | 46, 15.3 / 37 |
| nearest | look | 23, 11.0 / 46 | 242, 119.0 / 512 | 46, 53.9 / 223 |
| round_robin | look | 23, 25.1 / 50 | 242, 66.1 / 270 | 46, 32.4 / 63 |
| zone | look | 23, 16.2 / 45 | 242, 55.5 / 293 | 46, 51.2 / 208 |

## evening_rush · 30 floors x 4 cars · capacity 6 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 46.2; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.3 ± 1.3 | -36.6% | [-17.78, -16.04] | 20/20 | 53% | better ✓ |
| nearest | 69.2 ± 21.8 | +49.9% | [+15.25, +33.12] | 1/20 | -72% | worse ✗ |
| zone | 39.5 ± 3.9 | -14.4% | [-8.01, -5.22] | 19/20 | 21% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.3 | 12.7 | 31.4 | 50.1 | 15.0 | 0.61 |
| nearest | look | 69.2 | 52.3 | 227.1 | 522.6 | 55.0 | 0.32 |
| round_robin | look | 46.2 | 29.3 | 58.5 | 131.7 | 31.9 | 0.69 |
| zone | look | 39.5 | 23.2 | 64.6 | 243.3 | 25.3 | 0.42 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.7 | 2.3 | 25% / 20 | 11% | 7.6 / 4.2 | 93% | 8.8 | 1.58 | 0.08 | 0.9% |
| nearest | look | 52.3 | 2.6 | 40% / 71 | 9% | 3.9 / 3.9 | 78% | 7.8 | 1.62 | 0.27 | 17.7% |
| round_robin | look | 29.3 | 2.6 | 48% / 39 | 2% | 9.7 / 3.9 | 97% | 9.4 | 1.57 | 0.00 | 2.8% |
| zone | look | 23.2 | 2.1 | 41% / 35 | 13% | 7.6 / 4.4 | 84% | 8.2 | 1.60 | 0.10 | 4.6% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 7.1 / 21 | 242, 13.0 / 32 | 46, 13.8 / 33 |
| nearest | look | 23, 8.6 / 41 | 242, 59.5 / 253 | 46, 34.6 / 107 |
| round_robin | look | 23, 25.1 / 51 | 242, 29.7 / 60 | 46, 28.9 / 56 |
| zone | look | 23, 16.6 / 45 | 242, 23.1 / 67 | 46, 26.9 / 67 |

## evening_rush · 30 floors x 4 cars · capacity 12 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.6; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.3 ± 1.0 | -36.5% | [-16.82, -15.76] | 20/20 | 54% | better ✓ |
| nearest | 42.7 ± 3.1 | -4.2% | [-3.01, -0.76] | 15/20 | 6% | - |
| zone | 35.2 ± 1.7 | -21.0% | [-10.13, -8.70] | 20/20 | 31% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.3 | 11.6 | 30.2 | 49.0 | 14.1 | 0.59 |
| nearest | look | 42.7 | 25.2 | 64.5 | 125.9 | 28.5 | 0.52 |
| round_robin | look | 44.6 | 27.6 | 55.7 | 64.7 | 30.4 | 0.73 |
| zone | look | 35.2 | 18.8 | 50.0 | 63.6 | 21.0 | 0.59 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.6 | 2.4 | 23% / 19 | 13% | 7.3 / 3.9 | 92% | 8.7 | 1.58 | 0.06 | 0.0% |
| nearest | look | 25.2 | 3.3 | 39% / 42 | 10% | 4.2 / 4.2 | 78% | 7.4 | 1.60 | 0.23 | 1.7% |
| round_robin | look | 27.6 | 2.7 | 48% / 38 | 3% | 9.8 / 3.9 | 97% | 9.4 | 1.57 | 0.00 | 0.0% |
| zone | look | 18.8 | 2.2 | 40% / 30 | 13% | 7.7 / 4.4 | 85% | 8.1 | 1.59 | 0.10 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 6.4 / 20 | 242, 11.9 / 31 | 46, 12.7 / 30 |
| nearest | look | 23, 8.8 / 43 | 242, 26.9 / 66 | 46, 23.9 / 61 |
| round_robin | look | 23, 25.2 / 51 | 242, 27.7 / 56 | 46, 28.6 / 55 |
| zone | look | 23, 16.2 / 43 | 242, 18.2 / 49 | 46, 23.1 / 52 |
