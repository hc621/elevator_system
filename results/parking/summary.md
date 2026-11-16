# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking lobby | 28.4 | 20.7 | -27.3% | [-8.4, -7.1] | 20/20 | 48% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking spread | 27.9 | 18.5 | -33.7% | [-10.0, -8.8] | 20/20 | 60% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking demand | 27.8 | 18.9 | -32.1% | [-9.5, -8.4] | 20/20 | 58% | 12.4 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 35.7 | 23.2 | -34.8% | [-13.3, -11.5] | 20/20 | 65% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking lobby | 35.3 | 25.5 | -27.6% | [-10.9, -8.6] | 20/20 | 52% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking spread | 34.8 | 22.0 | -36.9% | [-13.5, -12.1] | 20/20 | 70% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking demand | 35.1 | 22.5 | -36.0% | [-13.2, -12.0] | 20/20 | 68% | 16.6 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 43.6 | 28.3 | -35.1% | [-15.8, -14.7] | 20/20 | 52% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby | 43.6 | 26.5 | -39.3% | [-17.7, -16.6] | 20/20 | 58% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread | 43.4 | 26.9 | -38.0% | [-17.0, -16.0] | 20/20 | 56% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand | 43.6 | 26.7 | -38.8% | [-17.4, -16.5] | 20/20 | 57% | 14.1 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.9 | 36.8 | -34.2% | [-20.0, -18.1] | 20/20 | 52% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby | 55.8 | 30.5 | -45.4% | [-26.1, -24.6] | 20/20 | 69% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread | 55.8 | 31.3 | -43.9% | [-25.0, -24.0] | 20/20 | 67% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand | 55.9 | 31.8 | -43.1% | [-24.7, -23.5] | 20/20 | 65% | 18.9 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 42.4 | 25.3 | -40.4% | [-17.7, -16.6] | 20/20 | 60% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking lobby | 42.2 | 25.2 | -40.4% | [-17.6, -16.5] | 20/20 | 61% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking spread | 42.3 | 24.8 | -41.3% | [-18.0, -17.0] | 20/20 | 62% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking demand | 42.3 | 25.3 | -40.2% | [-17.6, -16.4] | 20/20 | 60% | 14.1 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 53.6 | 28.2 | -47.4% | [-26.0, -24.8] | 20/20 | 73% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking lobby | 53.7 | 28.5 | -47.0% | [-25.8, -24.7] | 20/20 | 72% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking spread | 54.1 | 28.2 | -47.8% | [-26.5, -25.2] | 20/20 | 73% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking demand | 53.9 | 28.1 | -47.9% | [-26.4, -25.1] | 20/20 | 73% | 18.7 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 44.7 | 28.5 | -36.2% | [-16.8, -15.6] | 20/20 | 53% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby | 44.7 | 28.7 | -35.9% | [-16.6, -15.4] | 20/20 | 53% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread | 44.8 | 27.9 | -37.7% | [-17.4, -16.3] | 20/20 | 55% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand | 44.8 | 28.4 | -36.5% | [-17.0, -15.6] | 20/20 | 54% | 14.3 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.3 | 32.5 | -41.2% | [-23.5, -22.0] | 20/20 | 63% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby | 55.3 | 32.4 | -41.4% | [-23.7, -22.1] | 20/20 | 63% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread | 54.9 | 31.2 | -43.1% | [-24.1, -23.3] | 20/20 | 66% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand | 55.2 | 31.5 | -42.9% | [-24.4, -22.9] | 20/20 | 65% | 18.9 |

## Parking: each policy vs `stay`

Paired by seed on the same passengers, LOOK motion. Cells: Δ mean total time (verdict); Δ mean wait; change in floors travelled per passenger (the cost of parking moves).

| scenario | building | dispatch | policy | total: stay → policy | Δ total | Δ wait | Δ floors / passenger |
|---|---|---|---|---:|---:|---:|---:|
| quiet | 30 x 4 | cost | lobby | 19.6 → 20.7 | +5.4% ✗ | +1.0 ✗ | +4.3 |
| quiet | 30 x 4 | cost | spread | 19.6 → 18.5 | -5.5% ✓ | -1.0 ✓ | +5.9 |
| quiet | 30 x 4 | cost | demand | 19.6 → 18.9 | -3.6% ✓ | -0.7 ✓ | +3.6 |
| quiet | 30 x 4 | round_robin | lobby | 28.5 → 28.4 | -0.1% ? | -0.0 ? | +4.0 |
| quiet | 30 x 4 | round_robin | spread | 28.5 → 27.9 | -1.9% ? | -0.5 ? | +4.5 |
| quiet | 30 x 4 | round_robin | demand | 28.5 → 27.8 | -2.2% ? | -0.6 ? | +2.7 |
| quiet | 40 x 6 | cost | lobby | 23.2 → 25.5 | +9.8% ✗ | +2.2 ✗ | +6.5 |
| quiet | 40 x 6 | cost | spread | 23.2 → 22.0 | -5.5% ✓ | -1.2 ✓ | +10.0 |
| quiet | 40 x 6 | cost | demand | 23.2 → 22.5 | -3.4% ✓ | -0.7 ✓ | +5.4 |
| quiet | 40 x 6 | round_robin | lobby | 35.7 → 35.3 | -1.2% ? | -0.4 ? | +7.4 |
| quiet | 40 x 6 | round_robin | spread | 35.7 → 34.8 | -2.5% ? | -0.9 ? | +8.1 |
| quiet | 40 x 6 | round_robin | demand | 35.7 → 35.1 | -1.7% ? | -0.6 ? | +4.5 |
| morning_rush | 30 x 4 | cost | lobby | 28.3 → 26.5 | -6.4% ✓ | -1.5 ✓ | +1.8 |
| morning_rush | 30 x 4 | cost | spread | 28.3 → 26.9 | -5.0% ✓ | -1.2 ✓ | +1.4 |
| morning_rush | 30 x 4 | cost | demand | 28.3 → 26.7 | -5.7% ✓ | -1.3 ✓ | +1.4 |
| morning_rush | 30 x 4 | round_robin | lobby | 43.6 → 43.6 | +0.1% ? | +0.0 ? | +0.1 |
| morning_rush | 30 x 4 | round_robin | spread | 43.6 → 43.4 | -0.5% ? | -0.2 ? | +0.2 |
| morning_rush | 30 x 4 | round_robin | demand | 43.6 → 43.6 | +0.1% ? | +0.0 ? | +0.1 |
| morning_rush | 40 x 6 | cost | lobby | 36.8 → 30.5 | -17.1% ✓ | -5.5 ✓ | +4.7 |
| morning_rush | 40 x 6 | cost | spread | 36.8 → 31.3 | -15.0% ✓ | -5.0 ✓ | +3.1 |
| morning_rush | 40 x 6 | cost | demand | 36.8 → 31.8 | -13.5% ✓ | -4.5 ✓ | +2.7 |
| morning_rush | 40 x 6 | round_robin | lobby | 55.9 → 55.8 | -0.0% ? | -0.0 ? | +0.3 |
| morning_rush | 40 x 6 | round_robin | spread | 55.9 → 55.8 | -0.1% ? | -0.1 ? | +0.4 |
| morning_rush | 40 x 6 | round_robin | demand | 55.9 → 55.9 | +0.1% ? | +0.0 ? | +0.2 |
| lunch | 30 x 4 | cost | lobby | 25.3 → 25.2 | -0.4% ? | -0.1 ? | +0.6 |
| lunch | 30 x 4 | cost | spread | 25.3 → 24.8 | -1.8% ? | -0.4 ? | +0.7 |
| lunch | 30 x 4 | cost | demand | 25.3 → 25.3 | -0.1% ? | +0.0 ? | +0.6 |
| lunch | 30 x 4 | round_robin | lobby | 42.4 → 42.2 | -0.4% ? | -0.2 ? | +0.1 |
| lunch | 30 x 4 | round_robin | spread | 42.4 → 42.3 | -0.2% ? | -0.1 ? | +0.2 |
| lunch | 30 x 4 | round_robin | demand | 42.4 → 42.3 | -0.4% ? | -0.1 ? | +0.1 |
| lunch | 40 x 6 | cost | lobby | 28.2 → 28.5 | +1.0% ? | +0.4 ? | +1.9 |
| lunch | 40 x 6 | cost | spread | 28.2 → 28.2 | +0.1% ? | +0.1 ? | +2.0 |
| lunch | 40 x 6 | cost | demand | 28.2 → 28.1 | -0.5% ? | -0.1 ? | +1.7 |
| lunch | 40 x 6 | round_robin | lobby | 53.6 → 53.7 | +0.2% ? | +0.1 ? | +0.2 |
| lunch | 40 x 6 | round_robin | spread | 53.6 → 54.1 | +0.8% ? | +0.4 ? | +0.5 |
| lunch | 40 x 6 | round_robin | demand | 53.6 → 53.9 | +0.4% ? | +0.2 ? | +0.2 |
| evening_rush | 30 x 4 | cost | lobby | 28.5 → 28.7 | +0.5% ? | +0.2 ? | +0.0 |
| evening_rush | 30 x 4 | cost | spread | 28.5 → 27.9 | -2.2% ? | -0.6 ? | +0.4 |
| evening_rush | 30 x 4 | cost | demand | 28.5 → 28.4 | -0.3% ? | -0.1 ? | +0.3 |
| evening_rush | 30 x 4 | round_robin | lobby | 44.7 → 44.7 | +0.0% ? | +0.0 ? | +0.0 |
| evening_rush | 30 x 4 | round_robin | spread | 44.7 → 44.8 | +0.1% ? | +0.1 ? | +0.2 |
| evening_rush | 30 x 4 | round_robin | demand | 44.7 → 44.8 | +0.2% ? | +0.1 ? | +0.1 |
| evening_rush | 40 x 6 | cost | lobby | 32.5 → 32.4 | -0.4% ? | -0.1 ? | +0.0 |
| evening_rush | 40 x 6 | cost | spread | 32.5 → 31.2 | -3.9% ✓ | -1.1 ✓ | +1.7 |
| evening_rush | 40 x 6 | cost | demand | 32.5 → 31.5 | -3.0% ✓ | -0.9 ✓ | +1.0 |
| evening_rush | 40 x 6 | round_robin | lobby | 55.3 → 55.3 | +0.0% ? | +0.0 ? | +0.1 |
| evening_rush | 40 x 6 | round_robin | spread | 55.3 → 54.9 | -0.6% ? | -0.3 ? | +0.4 |
| evening_rush | 40 x 6 | round_robin | demand | 55.3 → 55.2 | -0.1% ? | -0.1 ? | +0.2 |

## Sensitivity: which conclusions survive

Varying: parking. Cells: Δ mean total time vs the baseline; ✓ better, ✗ worse, ? inconclusive (claim rule above).

### `cost` vs `round_robin` (LOOK)

| scenario | building | demand | lobby | spread | stay |
|---|---|---:|---:|---:|---:|
| quiet | 30 x 4 | -32% ✓ | -27% ✓ | -34% ✓ | -31% ✓ |
| quiet | 40 x 6 | -36% ✓ | -28% ✓ | -37% ✓ | -35% ✓ |
| morning_rush | 30 x 4 | -39% ✓ | -39% ✓ | -38% ✓ | -35% ✓ |
| morning_rush | 40 x 6 | -43% ✓ | -45% ✓ | -44% ✓ | -34% ✓ |
| lunch | 30 x 4 | -40% ✓ | -40% ✓ | -41% ✓ | -40% ✓ |
| lunch | 40 x 6 | -48% ✓ | -47% ✓ | -48% ✓ | -47% ✓ |
| evening_rush | 30 x 4 | -37% ✓ | -36% ✓ | -38% ✓ | -36% ✓ |
| evening_rush | 40 x 6 | -43% ✓ | -41% ✓ | -43% ✓ | -41% ✓ |

### Ranking by mean total time (LOOK, best first)

| scenario | building | demand | lobby | spread | stay |
|---|---|---:|---:|---:|---:|
| quiet | 30 x 4 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |
| quiet | 40 x 6 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |
| morning_rush | 30 x 4 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |
| morning_rush | 40 x 6 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |
| lunch | 30 x 4 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |
| lunch | 40 x 6 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |
| evening_rush | 30 x 4 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |
| evening_rush | 40 x 6 | cost > round_robin | cost > round_robin | cost > round_robin | cost > round_robin |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.6 ± 1.4 | -31.1% | [-9.71, -8.04] | 20/20 | 55% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.6 | 6.0 | 18.3 | 26.4 | 7.3 | 0.49 |
| round_robin | look | 28.5 | 15.0 | 36.2 | 47.8 | 16.1 | 0.63 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.0 | 1.3 | 6% / 11 | 67% | 5.2 / 3.6 | 47% | 14.7 | 1.08 | 0.17 | 0.0% |
| round_robin | look | 15.0 | 1.1 | 21% / 27 | 60% | 10.6 / 3.9 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.4 / 16 | 24, 6.4 / 18 | 46, 6.4 / 17 |
| round_robin | look | 23, 14.0 / 33 | 24, 15.2 / 34 | 46, 15.3 / 36 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.4; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.7 ± 1.6 | -27.3% | [-8.35, -7.14] | 20/20 | 48% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 20.7 | 7.0 | 21.8 | 30.8 | 8.3 | 0.48 |
| round_robin | look | 28.4 | 14.9 | 37.0 | 49.0 | 16.1 | 0.61 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.0 | 1.3 | 18% / 10 | 46% | 5.9 / 4.2 | 60% | 19.1 | 1.07 | 0.27 | 0.0% |
| round_robin | look | 14.9 | 1.1 | 29% / 23 | 42% | 10.4 / 4.1 | 77% | 25.4 | 1.04 | 0.02 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 1.3 / 7 | 24, 8.7 / 21 | 46, 8.8 / 22 |
| round_robin | look | 23, 10.9 / 34 | 24, 15.7 / 34 | 46, 16.5 / 37 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 27.9; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 18.5 ± 1.2 | -33.7% | [-10.05, -8.76] | 20/20 | 60% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 18.5 | 5.0 | 14.6 | 21.9 | 6.2 | 0.52 |
| round_robin | look | 27.9 | 14.4 | 35.9 | 49.0 | 15.6 | 0.63 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.0 | 1.2 | 14% / 7 | 50% | 4.3 / 3.2 | 64% | 20.6 | 1.07 | 0.14 | 0.0% |
| round_robin | look | 14.4 | 1.1 | 29% / 22 | 42% | 10.1 / 3.8 | 78% | 25.9 | 1.04 | 0.02 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.3 / 13 | 24, 5.1 / 12 | 46, 5.2 / 14 |
| round_robin | look | 23, 14.7 / 33 | 24, 14.3 / 34 | 46, 14.3 / 34 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 27.8; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 18.9 ± 1.3 | -32.1% | [-9.51, -8.39] | 20/20 | 58% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 18.9 | 5.3 | 16.6 | 24.8 | 6.5 | 0.48 |
| round_robin | look | 27.8 | 14.4 | 36.7 | 48.6 | 15.5 | 0.61 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.3 | 1.2 | 12% / 8 | 55% | 4.6 / 3.2 | 58% | 18.4 | 1.07 | 0.14 | 0.0% |
| round_robin | look | 14.4 | 1.1 | 25% / 24 | 47% | 10.1 / 3.7 | 73% | 24.1 | 1.04 | 0.02 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 2.7 / 11 | 24, 5.8 / 15 | 46, 6.2 / 18 |
| round_robin | look | 23, 13.4 / 34 | 24, 14.3 / 33 | 46, 15.0 / 36 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.7; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.2 ± 1.3 | -34.8% | [-13.31, -11.53] | 20/20 | 65% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.2 | 5.4 | 17.7 | 29.9 | 6.7 | 0.44 |
| round_robin | look | 35.7 | 18.0 | 43.2 | 62.1 | 19.1 | 0.63 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.4 | 1.3 | 5% / 11 | 71% | 4.9 / 3.3 | 39% | 18.5 | 1.07 | 0.26 | 0.0% |
| round_robin | look | 18.0 | 1.1 | 16% / 34 | 71% | 14.2 / 3.6 | 60% | 30.0 | 1.02 | 0.03 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 3.6 / 15 | 22, 6.1 / 16 | 48, 6.0 / 17 |
| round_robin | look | 25, 17.2 / 42 | 22, 17.8 / 41 | 48, 18.4 / 41 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.3; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.5 ± 1.6 | -27.6% | [-10.88, -8.55] | 20/20 | 52% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.5 | 7.7 | 26.2 | 37.5 | 9.0 | 0.43 |
| round_robin | look | 35.3 | 17.6 | 43.1 | 60.0 | 18.7 | 0.59 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.7 | 1.3 | 18% / 11 | 46% | 6.7 / 4.7 | 51% | 25.0 | 1.05 | 0.52 | 0.0% |
| round_robin | look | 17.6 | 1.1 | 25% / 27 | 52% | 14.0 / 4.3 | 73% | 37.4 | 1.02 | 0.03 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 0.4 / 2 | 22, 10.2 / 25 | 48, 10.2 / 28 |
| round_robin | look | 25, 10.9 / 37 | 22, 19.9 / 40 | 48, 20.1 / 43 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.8; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 22.0 ± 1.6 | -36.9% | [-13.49, -12.14] | 20/20 | 70% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 22.0 | 4.3 | 13.4 | 22.9 | 5.4 | 0.47 |
| round_robin | look | 34.8 | 17.1 | 41.1 | 62.8 | 18.2 | 0.62 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 4.3 | 1.2 | 12% / 5 | 56% | 4.0 / 3.0 | 58% | 28.4 | 1.06 | 0.22 | 0.0% |
| round_robin | look | 17.1 | 1.1 | 24% / 26 | 53% | 13.7 / 3.7 | 74% | 38.1 | 1.02 | 0.03 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 4.3 / 13 | 22, 4.3 / 11 | 48, 4.2 / 13 |
| round_robin | look | 25, 19.2 / 42 | 22, 16.0 / 36 | 48, 16.6 / 41 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.1; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 22.5 ± 1.6 | -36.0% | [-13.17, -12.03] | 20/20 | 68% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 22.5 | 4.7 | 15.7 | 28.5 | 5.9 | 0.42 |
| round_robin | look | 35.1 | 17.4 | 42.2 | 61.9 | 18.5 | 0.61 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 4.7 | 1.2 | 8% / 7 | 64% | 4.2 / 3.0 | 49% | 23.9 | 1.06 | 0.21 | 0.0% |
| round_robin | look | 17.4 | 1.1 | 20% / 29 | 61% | 13.9 / 3.4 | 68% | 34.5 | 1.02 | 0.03 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 2.5 / 10 | 22, 5.5 / 15 | 48, 5.4 / 16 |
| round_robin | look | 25, 16.3 / 43 | 22, 17.4 / 38 | 48, 18.1 / 41 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.3 ± 1.1 | -35.1% | [-15.84, -14.71] | 20/20 | 52% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.3 | 11.2 | 25.9 | 38.0 | 14.2 | 0.64 |
| round_robin | look | 43.6 | 26.9 | 55.2 | 64.1 | 29.5 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.2 | 3.0 | 8% / 19 | 14% | 9.8 / 4.4 | 79% | 7.5 | 1.67 | 0.11 | 0.0% |
| round_robin | look | 26.9 | 2.6 | 50% / 40 | 2% | 11.8 / 4.6 | 98% | 9.7 | 1.56 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 11.8 / 26 | 24, 8.7 / 20 | 46, 9.5 / 25 |
| round_robin | look | 234, 26.7 / 55 | 24, 27.1 / 53 | 46, 28.0 / 54 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.5 ± 1.1 | -39.3% | [-17.67, -16.59] | 20/20 | 58% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.5 | 9.7 | 25.7 | 38.8 | 12.4 | 0.58 |
| round_robin | look | 43.6 | 26.9 | 55.3 | 64.0 | 29.5 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.7 | 2.7 | 13% / 18 | 4% | 8.1 / 4.2 | 97% | 9.4 | 1.62 | 0.08 | 0.0% |
| round_robin | look | 26.9 | 2.6 | 50% / 40 | 2% | 11.8 / 4.6 | 99% | 9.8 | 1.56 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 9.8 / 25 | 24, 9.3 / 22 | 46, 9.4 / 25 |
| round_robin | look | 234, 26.8 / 55 | 24, 27.1 / 53 | 46, 27.9 / 54 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.9 ± 1.0 | -38.0% | [-17.05, -15.98] | 20/20 | 56% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.9 | 10.0 | 25.0 | 36.7 | 12.8 | 0.61 |
| round_robin | look | 43.4 | 26.7 | 55.1 | 63.7 | 29.3 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.0 | 2.8 | 12% / 17 | 7% | 8.5 / 4.3 | 93% | 9.0 | 1.63 | 0.09 | 0.0% |
| round_robin | look | 26.7 | 2.6 | 50% / 39 | 1% | 11.9 / 4.4 | 99% | 9.9 | 1.56 | 0.01 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 10.3 / 25 | 24, 8.7 / 21 | 46, 9.3 / 23 |
| round_robin | look | 234, 26.5 / 55 | 24, 27.0 / 51 | 46, 27.6 / 55 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.7 ± 1.3 | -38.8% | [-17.41, -16.46] | 20/20 | 57% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.7 | 9.8 | 25.0 | 37.0 | 12.6 | 0.60 |
| round_robin | look | 43.6 | 27.0 | 55.4 | 64.0 | 29.5 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.8 | 2.8 | 12% / 17 | 6% | 8.3 / 4.2 | 93% | 9.0 | 1.63 | 0.10 | 0.0% |
| round_robin | look | 27.0 | 2.6 | 50% / 40 | 2% | 11.8 / 4.6 | 99% | 9.8 | 1.56 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 10.1 / 25 | 24, 8.8 / 19 | 46, 9.3 / 24 |
| round_robin | look | 234, 26.8 / 55 | 24, 27.0 / 53 | 46, 28.0 / 54 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.8 ± 1.8 | -34.2% | [-20.03, -18.08] | 20/20 | 52% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 36.8 | 14.5 | 33.3 | 42.6 | 17.9 | 0.65 |
| round_robin | look | 55.9 | 34.5 | 70.9 | 81.9 | 36.9 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.5 | 3.4 | 6% / 23 | 16% | 13.4 / 5.0 | 65% | 9.3 | 1.67 | 0.18 | 0.0% |
| round_robin | look | 34.5 | 2.4 | 49% / 52 | 3% | 15.8 / 4.1 | 96% | 14.6 | 1.50 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 15.8 / 34 | 22, 8.7 / 21 | 48, 9.9 / 27 |
| round_robin | look | 249, 34.0 / 71 | 22, 37.0 / 67 | 48, 36.1 / 71 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.8; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 30.5 ± 1.1 | -45.4% | [-26.06, -24.63] | 20/20 | 69% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 30.5 | 9.0 | 25.5 | 37.6 | 11.6 | 0.54 |
| round_robin | look | 55.8 | 34.5 | 71.0 | 82.2 | 36.9 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.0 | 2.6 | 11% / 15 | 5% | 8.0 / 3.9 | 96% | 14.0 | 1.55 | 0.13 | 0.0% |
| round_robin | look | 34.5 | 2.4 | 49% / 52 | 2% | 15.7 / 4.0 | 98% | 14.9 | 1.50 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 9.3 / 26 | 22, 8.0 / 19 | 48, 7.7 / 22 |
| round_robin | look | 249, 33.9 / 71 | 22, 37.6 / 68 | 48, 36.1 / 70 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.8; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.3 ± 1.0 | -43.9% | [-25.03, -24.00] | 20/20 | 67% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 31.3 | 9.5 | 23.8 | 36.1 | 12.3 | 0.61 |
| round_robin | look | 55.8 | 34.4 | 71.0 | 82.4 | 36.8 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.5 | 2.9 | 7% / 12 | 10% | 8.8 / 4.2 | 86% | 12.4 | 1.62 | 0.17 | 0.0% |
| round_robin | look | 34.4 | 2.4 | 51% / 50 | 1% | 15.8 / 4.2 | 98% | 15.0 | 1.50 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 10.0 / 24 | 22, 6.9 / 17 | 48, 7.7 / 20 |
| round_robin | look | 249, 34.0 / 71 | 22, 36.4 / 67 | 48, 35.7 / 70 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.8 ± 1.1 | -43.1% | [-24.68, -23.49] | 20/20 | 65% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 31.8 | 10.0 | 26.5 | 35.8 | 12.9 | 0.59 |
| round_robin | look | 55.9 | 34.6 | 70.8 | 81.9 | 37.0 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.0 | 2.9 | 7% / 15 | 10% | 9.2 / 4.2 | 83% | 12.0 | 1.60 | 0.13 | 0.0% |
| round_robin | look | 34.6 | 2.4 | 49% / 52 | 2% | 15.8 / 4.0 | 97% | 14.8 | 1.50 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 10.6 / 27 | 22, 8.1 / 20 | 48, 7.7 / 22 |
| round_robin | look | 249, 34.0 / 71 | 22, 38.3 / 68 | 48, 36.1 / 70 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.3 ± 1.3 | -40.4% | [-17.67, -16.55] | 20/20 | 60% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.3 | 9.2 | 24.5 | 37.0 | 11.2 | 0.57 |
| round_robin | look | 42.4 | 26.3 | 54.0 | 63.0 | 28.3 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.2 | 2.0 | 16% / 16 | 14% | 6.6 / 3.6 | 90% | 9.4 | 1.51 | 0.09 | 0.0% |
| round_robin | look | 26.3 | 2.0 | 48% / 38 | 3% | 10.6 / 4.0 | 97% | 10.5 | 1.50 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 7.9 / 23 | 120, 9.9 / 25 | 46, 10.2 / 25 |
| round_robin | look | 114, 25.3 / 54 | 120, 26.7 / 53 | 46, 27.7 / 53 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.2; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.2 ± 1.1 | -40.4% | [-17.64, -16.55] | 20/20 | 61% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.2 | 9.1 | 24.0 | 39.3 | 11.1 | 0.57 |
| round_robin | look | 42.2 | 26.2 | 53.8 | 62.9 | 28.2 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.1 | 2.0 | 18% / 15 | 10% | 6.4 / 3.6 | 95% | 10.0 | 1.50 | 0.09 | 0.0% |
| round_robin | look | 26.2 | 2.0 | 47% / 38 | 2% | 10.6 / 3.9 | 97% | 10.6 | 1.50 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 7.6 / 23 | 120, 10.1 / 24 | 46, 10.1 / 24 |
| round_robin | look | 114, 25.1 / 54 | 120, 26.7 / 53 | 46, 27.5 / 53 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.3; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.8 ± 1.1 | -41.3% | [-17.99, -17.00] | 20/20 | 62% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.8 | 8.7 | 22.9 | 35.5 | 10.8 | 0.58 |
| round_robin | look | 42.3 | 26.2 | 54.1 | 63.4 | 28.2 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.7 | 2.0 | 18% / 13 | 7% | 6.3 / 3.6 | 96% | 10.1 | 1.51 | 0.10 | 0.0% |
| round_robin | look | 26.2 | 2.0 | 47% / 37 | 1% | 10.7 / 4.0 | 98% | 10.7 | 1.49 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 7.6 / 21 | 120, 9.6 / 24 | 46, 9.4 / 23 |
| round_robin | look | 114, 25.2 / 53 | 120, 26.7 / 54 | 46, 27.6 / 53 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.3; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.3 ± 1.4 | -40.2% | [-17.61, -16.40] | 20/20 | 60% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.3 | 9.2 | 24.4 | 40.0 | 11.2 | 0.57 |
| round_robin | look | 42.3 | 26.2 | 54.1 | 63.0 | 28.2 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.2 | 2.0 | 18% / 15 | 9% | 6.4 / 3.6 | 96% | 10.0 | 1.50 | 0.07 | 0.0% |
| round_robin | look | 26.2 | 2.0 | 47% / 38 | 2% | 10.6 / 4.0 | 98% | 10.6 | 1.50 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 7.6 / 22 | 120, 10.2 / 25 | 46, 10.3 / 24 |
| round_robin | look | 114, 25.2 / 54 | 120, 26.6 / 53 | 46, 27.6 / 53 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 53.6; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.2 ± 1.0 | -47.4% | [-26.01, -24.84] | 20/20 | 73% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.2 | 7.5 | 21.4 | 37.8 | 9.5 | 0.53 |
| round_robin | look | 53.6 | 33.1 | 69.7 | 81.6 | 34.9 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.5 | 2.0 | 10% / 14 | 23% | 6.0 / 3.3 | 82% | 13.0 | 1.45 | 0.13 | 0.0% |
| round_robin | look | 33.1 | 1.9 | 46% / 49 | 4% | 14.3 / 3.9 | 95% | 16.0 | 1.43 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 6.6 / 20 | 116, 8.1 / 22 | 48, 8.5 / 23 |
| round_robin | look | 124, 32.6 / 69 | 116, 33.3 / 69 | 48, 33.3 / 68 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 53.7; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.5 ± 1.1 | -47.0% | [-25.84, -24.72] | 20/20 | 72% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.5 | 7.9 | 23.1 | 40.3 | 9.8 | 0.51 |
| round_robin | look | 53.7 | 33.2 | 69.6 | 81.6 | 35.0 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.9 | 1.8 | 15% / 13 | 13% | 6.1 / 3.4 | 93% | 14.9 | 1.43 | 0.13 | 0.0% |
| round_robin | look | 33.2 | 1.9 | 46% / 49 | 3% | 14.3 / 3.9 | 96% | 16.2 | 1.43 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 6.1 / 20 | 116, 9.3 / 25 | 48, 9.5 / 24 |
| round_robin | look | 124, 32.5 / 69 | 116, 33.7 / 69 | 48, 33.2 / 68 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 54.1; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.2 ± 1.1 | -47.8% | [-26.46, -25.16] | 20/20 | 73% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.2 | 7.6 | 21.2 | 33.5 | 9.5 | 0.54 |
| round_robin | look | 54.1 | 33.5 | 69.9 | 81.2 | 35.3 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.6 | 1.9 | 15% / 11 | 11% | 6.2 / 3.4 | 94% | 15.0 | 1.45 | 0.13 | 0.0% |
| round_robin | look | 33.5 | 1.9 | 49% / 48 | 2% | 14.2 / 4.0 | 98% | 16.5 | 1.43 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 6.7 / 20 | 116, 8.2 / 22 | 48, 8.7 / 22 |
| round_robin | look | 124, 33.2 / 70 | 116, 33.8 / 69 | 48, 33.4 / 68 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 53.9; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.1 ± 1.1 | -47.9% | [-26.41, -25.15] | 20/20 | 73% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.1 | 7.5 | 22.0 | 38.1 | 9.3 | 0.51 |
| round_robin | look | 53.9 | 33.3 | 69.6 | 81.5 | 35.1 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.5 | 1.9 | 15% / 12 | 14% | 5.9 / 3.3 | 92% | 14.7 | 1.42 | 0.11 | 0.0% |
| round_robin | look | 33.3 | 1.9 | 47% / 48 | 4% | 14.3 / 3.9 | 96% | 16.2 | 1.43 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 6.0 / 20 | 116, 8.5 / 23 | 48, 8.8 / 24 |
| round_robin | look | 124, 32.7 / 69 | 116, 33.8 / 69 | 48, 33.5 / 68 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.7; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.5 ± 1.3 | -36.2% | [-16.75, -15.57] | 20/20 | 53% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.5 | 11.8 | 31.2 | 49.9 | 14.3 | 0.58 |
| round_robin | look | 44.7 | 27.7 | 55.8 | 75.1 | 30.4 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.8 | 2.4 | 23% / 19 | 13% | 7.3 / 3.9 | 92% | 8.7 | 1.57 | 0.07 | 0.1% |
| round_robin | look | 27.7 | 2.7 | 48% / 38 | 3% | 9.8 / 3.9 | 97% | 9.4 | 1.57 | 0.00 | 0.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 6.0 / 19 | 242, 12.1 / 31 | 46, 13.2 / 32 |
| round_robin | look | 23, 25.2 / 51 | 242, 27.8 / 56 | 46, 28.6 / 55 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.7; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.7 ± 1.1 | -35.9% | [-16.63, -15.43] | 20/20 | 53% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.7 | 12.0 | 31.2 | 50.4 | 14.4 | 0.59 |
| round_robin | look | 44.7 | 27.7 | 55.9 | 75.1 | 30.4 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.0 | 2.4 | 25% / 19 | 12% | 7.3 / 4.0 | 92% | 8.8 | 1.57 | 0.08 | 0.1% |
| round_robin | look | 27.7 | 2.7 | 48% / 38 | 2% | 9.7 / 3.9 | 97% | 9.4 | 1.57 | 0.00 | 0.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 6.1 / 20 | 242, 12.3 / 31 | 46, 13.4 / 32 |
| round_robin | look | 23, 25.5 / 51 | 242, 27.8 / 56 | 46, 28.7 / 55 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.8; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 27.9 ± 1.1 | -37.7% | [-17.41, -16.26] | 20/20 | 55% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 27.9 | 11.2 | 29.9 | 49.5 | 13.6 | 0.58 |
| round_robin | look | 44.8 | 27.8 | 55.7 | 70.2 | 30.5 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.2 | 2.4 | 25% / 17 | 6% | 6.9 / 3.8 | 96% | 9.1 | 1.56 | 0.07 | 0.1% |
| round_robin | look | 27.8 | 2.7 | 49% / 38 | 1% | 9.8 / 3.9 | 98% | 9.6 | 1.57 | 0.00 | 0.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 5.9 / 18 | 242, 11.5 / 30 | 46, 12.6 / 31 |
| round_robin | look | 23, 24.9 / 51 | 242, 28.0 / 56 | 46, 28.3 / 54 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.8; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.4 ± 1.3 | -36.5% | [-17.04, -15.62] | 20/20 | 54% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.4 | 11.8 | 30.3 | 51.0 | 14.2 | 0.59 |
| round_robin | look | 44.8 | 27.8 | 55.8 | 74.8 | 30.5 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.8 | 2.4 | 25% / 18 | 8% | 7.2 / 4.0 | 95% | 9.0 | 1.57 | 0.09 | 0.2% |
| round_robin | look | 27.8 | 2.7 | 48% / 38 | 2% | 9.8 / 3.9 | 98% | 9.5 | 1.57 | 0.00 | 0.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 6.5 / 19 | 242, 12.0 / 31 | 46, 13.1 / 31 |
| round_robin | look | 23, 25.4 / 52 | 242, 27.9 / 56 | 46, 28.7 / 55 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.3; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.5 ± 0.8 | -41.2% | [-23.50, -21.99] | 20/20 | 63% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.5 | 11.4 | 32.6 | 50.7 | 13.7 | 0.54 |
| round_robin | look | 55.3 | 34.1 | 70.5 | 81.5 | 36.4 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.4 | 2.2 | 15% / 17 | 25% | 8.5 / 4.0 | 83% | 12.4 | 1.44 | 0.12 | 0.0% |
| round_robin | look | 34.1 | 2.4 | 47% / 47 | 4% | 13.2 / 3.7 | 95% | 14.8 | 1.48 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 2.8 / 12 | 236, 12.2 / 33 | 48, 12.3 / 32 |
| round_robin | look | 25, 31.9 / 67 | 236, 33.8 / 70 | 48, 36.4 / 70 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking lobby

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.3; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.4 ± 0.8 | -41.4% | [-23.67, -22.08] | 20/20 | 63% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.4 | 11.3 | 32.3 | 51.2 | 13.5 | 0.54 |
| round_robin | look | 55.3 | 34.1 | 70.6 | 81.7 | 36.4 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.3 | 2.2 | 14% / 15 | 24% | 8.4 / 4.0 | 84% | 12.4 | 1.44 | 0.13 | 0.0% |
| round_robin | look | 34.1 | 2.4 | 48% / 47 | 4% | 13.2 / 3.7 | 96% | 14.9 | 1.48 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 3.0 / 12 | 236, 12.0 / 33 | 48, 12.2 / 32 |
| round_robin | look | 25, 32.2 / 67 | 236, 33.7 / 70 | 48, 36.6 / 69 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking spread

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 54.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.2 ± 1.1 | -43.1% | [-24.14, -23.26] | 20/20 | 66% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 31.2 | 10.3 | 31.0 | 48.6 | 12.4 | 0.52 |
| round_robin | look | 54.9 | 33.7 | 70.1 | 82.2 | 36.1 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.3 | 2.1 | 18% / 13 | 10% | 7.6 / 3.8 | 94% | 14.0 | 1.43 | 0.10 | 0.0% |
| round_robin | look | 33.7 | 2.4 | 48% / 46 | 2% | 13.2 / 3.6 | 98% | 15.3 | 1.48 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 3.6 / 12 | 236, 10.8 / 31 | 48, 11.4 / 32 |
| round_robin | look | 25, 32.4 / 66 | 236, 33.6 / 70 | 48, 34.8 / 68 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks · parking demand

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.2; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.5 ± 0.8 | -42.9% | [-24.39, -22.90] | 20/20 | 65% | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 31.5 | 10.5 | 31.1 | 50.9 | 12.7 | 0.52 |
| round_robin | look | 55.2 | 34.0 | 70.7 | 81.2 | 36.3 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.5 | 2.1 | 17% / 14 | 16% | 7.7 / 3.8 | 89% | 13.3 | 1.43 | 0.11 | 0.0% |
| round_robin | look | 34.0 | 2.4 | 48% / 47 | 3% | 13.1 / 3.7 | 97% | 15.0 | 1.48 | 0.01 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 2.8 / 11 | 236, 11.1 / 32 | 48, 11.7 / 31 |
| round_robin | look | 25, 33.1 / 68 | 236, 33.6 / 70 | 48, 36.0 / 69 |
