# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

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

## uniform · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.4; B0 floor = 10.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.1 ± 0.7 | -41.6% | [-14.94, -13.74] | 20/20 | 59% | better ✓ |
| nearest | 30.7 ± 2.0 | -10.9% | [-4.61, -2.73] | 19/20 | 16% | better ✓ |
| zone | 33.2 ± 2.3 | -3.5% | [-2.09, -0.18] | 13/20 | 5% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 20.1 | -13.9% | [-3.72, -2.80] | 20/20 | better ✓ |
| nearest | look | 30.7 | -22.1% | [-9.71, -7.69] | 20/20 | better ✓ |
| round_robin | look | 34.4 | -20.5% | [-9.68, -8.15] | 20/20 | better ✓ |
| zone | look | 33.2 | -26.4% | [-12.83, -11.04] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 20.1 | 8.0 | 21.4 | 33.5 | 9.8 | 0.58 |
| cost | scan | 23.3 | 10.8 | 28.6 | 45.2 | 13.0 | 0.59 |
| nearest | look | 30.7 | 18.3 | 55.2 | 69.5 | 20.3 | 0.49 |
| nearest | scan | 39.3 | 26.7 | 65.4 | 73.3 | 29.0 | 0.56 |
| round_robin | look | 34.4 | 22.4 | 49.4 | 61.5 | 24.1 | 0.69 |
| round_robin | scan | 43.3 | 31.0 | 60.6 | 66.2 | 33.0 | 0.73 |
| zone | look | 33.2 | 20.6 | 54.5 | 71.9 | 22.9 | 0.59 |
| zone | scan | 45.1 | 32.0 | 63.8 | 81.5 | 34.8 | 0.70 |

## uniform · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 40.6; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 22.2 ± 0.9 | -45.3% | [-19.30, -17.50] | 20/20 | 68% | better ✓ |
| nearest | 36.0 ± 2.2 | -11.3% | [-6.04, -3.16] | 18/20 | 17% | better ✓ |
| zone | 39.2 ± 1.9 | -3.4% | [-2.60, -0.15] | 12/20 | 5% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 22.2 | -13.0% | [-3.70, -2.93] | 20/20 | better ✓ |
| nearest | look | 36.0 | -25.7% | [-13.55, -11.37] | 20/20 | better ✓ |
| round_robin | look | 40.6 | -26.4% | [-15.55, -13.50] | 20/20 | better ✓ |
| zone | look | 39.2 | -31.3% | [-18.78, -16.98] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 22.2 | 7.0 | 20.0 | 37.1 | 8.6 | 0.53 |
| cost | scan | 25.5 | 9.8 | 28.5 | 58.2 | 11.9 | 0.50 |
| nearest | look | 36.0 | 20.4 | 69.8 | 85.5 | 22.4 | 0.43 |
| nearest | scan | 48.4 | 32.6 | 85.6 | 94.3 | 34.8 | 0.52 |
| round_robin | look | 40.6 | 25.5 | 57.4 | 75.2 | 27.0 | 0.68 |
| round_robin | scan | 55.1 | 39.8 | 77.3 | 84.4 | 41.5 | 0.73 |
| zone | look | 39.2 | 23.5 | 64.5 | 83.0 | 25.6 | 0.58 |
| zone | scan | 57.0 | 40.8 | 80.9 | 93.9 | 43.4 | 0.71 |

## mixed · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.5; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.1 ± 0.8 | -40.1% | [-15.85, -15.04] | 20/20 | 63% | better ✓ |
| nearest | 33.9 ± 1.7 | -12.0% | [-5.24, -3.99] | 20/20 | 19% | better ✓ |
| zone | 32.9 ± 1.9 | -14.6% | [-6.27, -4.98] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 23.1 | -9.2% | [-2.82, -1.89] | 20/20 | better ✓ |
| nearest | look | 33.9 | -20.7% | [-9.94, -7.81] | 20/20 | better ✓ |
| round_robin | look | 38.5 | -15.8% | [-8.06, -6.44] | 20/20 | better ✓ |
| zone | look | 32.9 | -27.4% | [-13.20, -11.71] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.1 | 7.4 | 21.0 | 35.1 | 9.1 | 0.53 |
| cost | scan | 25.4 | 9.5 | 28.1 | 48.9 | 11.4 | 0.51 |
| nearest | look | 33.9 | 18.1 | 56.3 | 64.8 | 19.9 | 0.45 |
| nearest | scan | 42.8 | 26.7 | 62.3 | 67.4 | 28.8 | 0.55 |
| round_robin | look | 38.5 | 22.9 | 51.6 | 60.5 | 24.5 | 0.68 |
| round_robin | scan | 45.8 | 29.9 | 58.3 | 63.1 | 31.8 | 0.72 |
| zone | look | 32.9 | 17.2 | 48.2 | 62.8 | 18.9 | 0.55 |
| zone | scan | 45.3 | 29.3 | 58.3 | 64.5 | 31.3 | 0.70 |

## mixed · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 48.4; B0 floor = 18.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.7 ± 1.4 | -44.9% | [-22.55, -20.94] | 20/20 | 72% | better ✓ |
| nearest | 40.7 ± 2.0 | -15.9% | [-8.65, -6.66] | 20/20 | 26% | better ✓ |
| zone | 40.9 ± 1.4 | -15.6% | [-8.56, -6.59] | 20/20 | 25% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 26.7 | -8.4% | [-2.91, -1.97] | 20/20 | better ✓ |
| nearest | look | 40.7 | -23.1% | [-13.50, -10.83] | 20/20 | better ✓ |
| round_robin | look | 48.4 | -18.3% | [-11.54, -10.00] | 20/20 | better ✓ |
| zone | look | 40.9 | -31.0% | [-19.15, -17.64] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.7 | 6.7 | 20.6 | 36.5 | 8.3 | 0.47 |
| cost | scan | 29.1 | 8.9 | 28.2 | 63.1 | 10.7 | 0.42 |
| nearest | look | 40.7 | 20.6 | 71.7 | 82.5 | 22.3 | 0.40 |
| nearest | scan | 52.9 | 32.6 | 81.8 | 87.0 | 34.5 | 0.49 |
| round_robin | look | 48.4 | 28.5 | 64.6 | 77.0 | 30.0 | 0.67 |
| round_robin | scan | 59.2 | 39.2 | 76.3 | 81.9 | 40.8 | 0.73 |
| zone | look | 40.9 | 20.9 | 61.0 | 78.2 | 22.5 | 0.54 |
| zone | scan | 59.3 | 39.0 | 77.5 | 82.8 | 40.9 | 0.70 |

## morning_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.3; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 27.0 ± 1.4 | -31.2% | [-12.99, -11.43] | 20/20 | 49% | better ✓ |
| nearest | 39.8 ± 3.6 | +1.3% | [-1.19, +2.40] | 12/20 | -2% | - |
| zone | 32.7 ± 1.8 | -16.6% | [-7.07, -5.90] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 27.0 | -2.0% | [-0.97, -0.11] | 14/20 | - |
| nearest | look | 39.8 | -12.2% | [-6.89, -4.14] | 19/20 | better ✓ |
| round_robin | look | 39.3 | -14.1% | [-7.42, -5.59] | 20/20 | better ✓ |
| zone | look | 32.7 | -27.2% | [-12.94, -11.58] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 27.0 | 10.2 | 24.5 | 29.6 | 12.7 | 0.62 |
| cost | scan | 27.6 | 10.6 | 25.7 | 41.2 | 13.3 | 0.61 |
| nearest | look | 39.8 | 22.9 | 60.3 | 84.2 | 25.5 | 0.51 |
| nearest | scan | 45.3 | 28.3 | 63.3 | 84.8 | 31.0 | 0.54 |
| round_robin | look | 39.3 | 23.1 | 50.4 | 59.0 | 25.0 | 0.68 |
| round_robin | scan | 45.7 | 29.3 | 58.0 | 62.7 | 31.4 | 0.71 |
| zone | look | 32.7 | 16.7 | 46.4 | 61.8 | 18.4 | 0.56 |
| zone | scan | 45.0 | 28.6 | 58.1 | 65.2 | 30.7 | 0.69 |

## morning_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.6; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 34.7 ± 2.0 | -30.1% | [-15.79, -14.07] | 20/20 | 49% | better ✓ |
| nearest | 51.0 ± 6.1 | +2.8% | [-0.97, +4.13] | 11/20 | -5% | - |
| zone | 41.3 ± 2.6 | -16.8% | [-9.22, -7.56] | 20/20 | 27% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 34.7 | -1.0% | [-0.62, -0.06] | 14/20 | - |
| nearest | look | 51.0 | -14.2% | [-10.48, -6.44] | 19/20 | better ✓ |
| round_robin | look | 49.6 | -15.8% | [-10.21, -8.40] | 20/20 | better ✓ |
| zone | look | 41.3 | -27.7% | [-17.13, -14.70] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 34.7 | 12.8 | 31.5 | 38.5 | 15.7 | 0.62 |
| cost | scan | 35.0 | 13.1 | 32.0 | 49.1 | 16.0 | 0.61 |
| nearest | look | 51.0 | 29.4 | 80.3 | 105.8 | 32.0 | 0.48 |
| nearest | scan | 59.5 | 37.8 | 85.1 | 127.0 | 40.5 | 0.52 |
| round_robin | look | 49.6 | 29.0 | 64.3 | 77.3 | 30.6 | 0.67 |
| round_robin | scan | 58.9 | 38.0 | 76.0 | 81.1 | 39.9 | 0.71 |
| zone | look | 41.3 | 20.7 | 58.3 | 79.7 | 22.3 | 0.54 |
| zone | scan | 57.1 | 36.2 | 76.5 | 90.2 | 38.1 | 0.66 |

## evening_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.4; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.7 ± 1.6 | -32.3% | [-13.27, -12.17] | 20/20 | 51% | better ✓ |
| nearest | 39.7 ± 2.6 | +0.9% | [-0.81, +1.47] | 8/20 | -1% | - |
| zone | 33.6 ± 1.3 | -14.6% | [-6.35, -5.21] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 26.7 | -23.5% | [-9.13, -7.26] | 20/20 | better ✓ |
| nearest | look | 39.7 | -14.6% | [-8.02, -5.73] | 20/20 | better ✓ |
| round_robin | look | 39.4 | -16.5% | [-8.62, -6.84] | 20/20 | better ✓ |
| zone | look | 33.6 | -30.1% | [-15.09, -13.82] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.7 | 10.5 | 27.8 | 42.4 | 12.4 | 0.57 |
| cost | scan | 34.8 | 17.5 | 42.5 | 57.5 | 20.5 | 0.61 |
| nearest | look | 39.7 | 22.9 | 61.2 | 125.7 | 25.4 | 0.49 |
| nearest | scan | 46.6 | 29.7 | 62.5 | 109.2 | 32.3 | 0.58 |
| round_robin | look | 39.4 | 23.1 | 49.9 | 60.2 | 25.1 | 0.70 |
| round_robin | scan | 47.2 | 30.7 | 58.1 | 63.0 | 32.9 | 0.74 |
| zone | look | 33.6 | 17.6 | 47.2 | 65.6 | 19.3 | 0.58 |
| zone | scan | 48.1 | 31.6 | 58.7 | 77.8 | 33.8 | 0.74 |

## evening_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.1; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.8 ± 1.5 | -35.2% | [-17.98, -16.45] | 20/20 | 57% | better ✓ |
| nearest | 52.0 ± 3.8 | +5.9% | [+1.05, +4.84] | 6/20 | -10% | - |
| zone | 42.2 ± 2.1 | -14.1% | [-7.66, -6.11] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 31.8 | -30.6% | [-15.61, -12.52] | 20/20 | better ✓ |
| nearest | look | 52.0 | -12.7% | [-9.16, -5.92] | 19/20 | better ✓ |
| round_robin | look | 49.1 | -20.6% | [-13.76, -11.83] | 20/20 | better ✓ |
| zone | look | 42.2 | -32.4% | [-20.80, -19.52] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 31.8 | 11.0 | 33.0 | 43.5 | 12.8 | 0.52 |
| cost | scan | 45.8 | 23.6 | 57.9 | 77.8 | 26.8 | 0.60 |
| nearest | look | 52.0 | 30.3 | 88.7 | 206.6 | 33.0 | 0.43 |
| nearest | scan | 59.6 | 38.0 | 82.6 | 140.5 | 40.5 | 0.56 |
| round_robin | look | 49.1 | 28.4 | 62.9 | 77.8 | 30.1 | 0.69 |
| round_robin | scan | 61.8 | 40.8 | 76.5 | 82.1 | 42.8 | 0.75 |
| zone | look | 42.2 | 21.5 | 59.4 | 77.2 | 23.2 | 0.57 |
| zone | scan | 62.4 | 41.3 | 77.1 | 91.6 | 43.4 | 0.74 |
