# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| uniform · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks | 28.7 | 16.7 | -41.7% | [-12.4, -11.5] | 20/20 | 65% | 10.3 |
| uniform · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks | 28.5 | 16.5 | -42.2% | [-12.7, -11.5] | 20/20 | 66% | 10.3 |
| uniform · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 34.4 | 20.1 | -41.6% | [-14.9, -13.7] | 20/20 | 59% | 10.3 |
| uniform · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks | 34.2 | 19.9 | -41.8% | [-15.0, -13.5] | 20/20 | 60% | 10.3 |
| uniform · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks | 41.0 | 24.8 | -39.4% | [-16.9, -15.2] | 20/20 | 53% | 10.3 |
| uniform · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks | 40.5 | 24.7 | -39.0% | [-16.5, -15.1] | 20/20 | 52% | 10.3 |
| uniform · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks | 36.7 | 19.7 | -46.3% | [-17.8, -16.2] | 20/20 | 74% | 13.6 |
| uniform · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks | 36.7 | 19.0 | -48.0% | [-18.4, -16.8] | 20/20 | 76% | 13.6 |
| uniform · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 40.6 | 22.2 | -45.3% | [-19.3, -17.5] | 20/20 | 68% | 13.6 |
| uniform · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks | 40.3 | 21.6 | -46.4% | [-19.6, -17.8] | 20/20 | 70% | 13.6 |
| uniform · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks | 45.9 | 25.1 | -45.3% | [-21.6, -19.9] | 20/20 | 64% | 13.6 |
| uniform · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks | 45.3 | 24.6 | -45.8% | [-21.7, -19.8] | 20/20 | 66% | 13.6 |
| mixed · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks | 34.9 | 20.2 | -42.2% | [-15.3, -14.2] | 20/20 | 70% | 14.0 |
| mixed · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks | 35.0 | 20.2 | -42.3% | [-15.3, -14.3] | 20/20 | 70% | 14.0 |
| mixed · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 38.5 | 23.1 | -40.1% | [-15.8, -15.0] | 20/20 | 63% | 14.0 |
| mixed · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks | 38.7 | 22.9 | -40.8% | [-16.3, -15.4] | 20/20 | 64% | 14.0 |
| mixed · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks | 43.6 | 26.6 | -39.0% | [-17.6, -16.4] | 20/20 | 57% | 14.0 |
| mixed · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks | 43.4 | 26.5 | -39.0% | [-17.6, -16.1] | 20/20 | 58% | 14.0 |
| mixed · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks | 44.9 | 24.3 | -45.8% | [-21.1, -20.0] | 20/20 | 78% | 18.4 |
| mixed · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks | 44.8 | 24.1 | -46.1% | [-21.3, -20.0] | 20/20 | 78% | 18.4 |
| mixed · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 48.4 | 26.7 | -44.9% | [-22.6, -20.9] | 20/20 | 72% | 18.4 |
| mixed · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks | 48.6 | 26.2 | -46.1% | [-23.2, -21.6] | 20/20 | 74% | 18.4 |
| mixed · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks | 52.1 | 28.6 | -45.0% | [-24.1, -22.8] | 20/20 | 70% | 18.4 |
| mixed · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks | 52.0 | 28.3 | -45.6% | [-24.5, -23.0] | 20/20 | 70% | 18.4 |
| morning_rush · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks | 35.4 | 24.2 | -31.6% | [-11.7, -10.7] | 20/20 | 53% | 14.3 |
| morning_rush · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks | 35.6 | 24.3 | -31.7% | [-12.0, -10.6] | 20/20 | 53% | 14.3 |
| morning_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 39.3 | 27.0 | -31.2% | [-13.0, -11.4] | 20/20 | 49% | 14.3 |
| morning_rush · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks | 39.5 | 27.1 | -31.4% | [-13.3, -11.5] | 20/20 | 49% | 14.3 |
| morning_rush · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks | 43.3 | 29.9 | -30.9% | [-14.2, -12.4] | 20/20 | 46% | 14.3 |
| morning_rush · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks | 43.5 | 29.8 | -31.5% | [-14.5, -13.0] | 20/20 | 47% | 14.3 |
| morning_rush · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks | 46.6 | 32.3 | -30.7% | [-15.1, -13.5] | 20/20 | 52% | 19.0 |
| morning_rush · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks | 47.1 | 32.5 | -31.0% | [-15.4, -13.8] | 20/20 | 52% | 19.0 |
| morning_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 49.6 | 34.7 | -30.1% | [-15.8, -14.1] | 20/20 | 49% | 19.0 |
| morning_rush · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks | 50.0 | 35.0 | -30.0% | [-15.9, -14.0] | 20/20 | 48% | 19.0 |
| morning_rush · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks | 52.8 | 36.7 | -30.5% | [-17.0, -15.1] | 20/20 | 48% | 19.0 |
| morning_rush · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks | 52.9 | 36.9 | -30.3% | [-17.0, -15.0] | 20/20 | 47% | 19.0 |
| evening_rush · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks | 34.9 | 23.7 | -32.2% | [-11.9, -10.7] | 20/20 | 55% | 14.3 |
| evening_rush · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks | 34.9 | 23.5 | -32.8% | [-12.0, -10.9] | 20/20 | 56% | 14.3 |
| evening_rush · 30 floors x 4 cars · door_time 1 · lobby · 200 requests / 800 ticks | 39.4 | 26.7 | -32.3% | [-13.3, -12.2] | 20/20 | 51% | 14.3 |
| evening_rush · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks | 39.2 | 26.4 | -32.7% | [-13.5, -12.1] | 20/20 | 51% | 14.3 |
| evening_rush · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks | 43.7 | 29.8 | -31.8% | [-14.7, -13.1] | 20/20 | 47% | 14.3 |
| evening_rush · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks | 43.6 | 29.6 | -32.2% | [-14.8, -13.3] | 20/20 | 48% | 14.3 |
| evening_rush · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks | 45.3 | 29.6 | -34.7% | [-16.5, -14.9] | 20/20 | 60% | 19.0 |
| evening_rush · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks | 45.4 | 29.2 | -35.7% | [-17.0, -15.4] | 20/20 | 61% | 19.0 |
| evening_rush · 40 floors x 6 cars · door_time 1 · lobby · 200 requests / 800 ticks | 49.1 | 31.8 | -35.2% | [-18.0, -16.5] | 20/20 | 57% | 19.0 |
| evening_rush · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks | 48.9 | 31.4 | -35.9% | [-18.3, -16.7] | 20/20 | 59% | 19.0 |
| evening_rush · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks | 52.9 | 34.4 | -34.9% | [-19.2, -17.6] | 20/20 | 54% | 19.0 |
| evening_rush · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks | 52.7 | 33.9 | -35.7% | [-19.6, -17.9] | 20/20 | 56% | 19.0 |

## Sensitivity: which conclusions survive

Varying: door_time, placement. Cells: Δ mean total time vs the baseline; ✓ better, ✗ worse, ? inconclusive (claim rule above).

### `cost` vs `round_robin` (LOOK)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | -42% ✓ | -42% ✓ | -42% ✓ | -42% ✓ | -39% ✓ | -39% ✓ |
| uniform | 40 x 6 | -46% ✓ | -48% ✓ | -45% ✓ | -46% ✓ | -45% ✓ | -46% ✓ |
| mixed | 30 x 4 | -42% ✓ | -42% ✓ | -40% ✓ | -41% ✓ | -39% ✓ | -39% ✓ |
| mixed | 40 x 6 | -46% ✓ | -46% ✓ | -45% ✓ | -46% ✓ | -45% ✓ | -46% ✓ |
| morning_rush | 30 x 4 | -32% ✓ | -32% ✓ | -31% ✓ | -31% ✓ | -31% ✓ | -32% ✓ |
| morning_rush | 40 x 6 | -31% ✓ | -31% ✓ | -30% ✓ | -30% ✓ | -30% ✓ | -30% ✓ |
| evening_rush | 30 x 4 | -32% ✓ | -33% ✓ | -32% ✓ | -33% ✓ | -32% ✓ | -32% ✓ |
| evening_rush | 40 x 6 | -35% ✓ | -36% ✓ | -35% ✓ | -36% ✓ | -35% ✓ | -36% ✓ |

### `nearest` vs `round_robin` (LOOK)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | -14% ✓ | -17% ✓ | -11% ✓ | -12% ✓ | -9% ✓ | -8% ✓ |
| uniform | 40 x 6 | -17% ✓ | -20% ✓ | -11% ✓ | -16% ✓ | -6% ? | -14% ✓ |
| mixed | 30 x 4 | -15% ✓ | -15% ✓ | -12% ✓ | -13% ✓ | -11% ✓ | -11% ✓ |
| mixed | 40 x 6 | -19% ✓ | -18% ✓ | -16% ✓ | -16% ✓ | -15% ✓ | -15% ✓ |
| morning_rush | 30 x 4 | -3% ? | -3% ? | +1% ? | -0% ? | +10% ? | +8% ✗ |
| morning_rush | 40 x 6 | +1% ? | -1% ? | +3% ? | +2% ? | +12% ? | +10% ✗ |
| evening_rush | 30 x 4 | -4% ? | -3% ? | +1% ? | -1% ? | +5% ✗ | +3% ? |
| evening_rush | 40 x 6 | +2% ? | -2% ? | +6% ? | +2% ? | +12% ✗ | +6% ? |

### `zone` vs `round_robin` (LOOK)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | -6% ✓ | -6% ✓ | -3% ? | -5% ? | +1% ? | +1% ? |
| uniform | 40 x 6 | -8% ✓ | -9% ✓ | -3% ? | -4% ? | -1% ? | -0% ? |
| mixed | 30 x 4 | -14% ✓ | -15% ✓ | -15% ✓ | -15% ✓ | -16% ✓ | -15% ✓ |
| mixed | 40 x 6 | -15% ✓ | -15% ✓ | -16% ✓ | -16% ✓ | -14% ✓ | -15% ✓ |
| morning_rush | 30 x 4 | -15% ✓ | -15% ✓ | -17% ✓ | -17% ✓ | -17% ✓ | -18% ✓ |
| morning_rush | 40 x 6 | -17% ✓ | -18% ✓ | -17% ✓ | -17% ✓ | -17% ✓ | -17% ✓ |
| evening_rush | 30 x 4 | -13% ✓ | -14% ✓ | -15% ✓ | -14% ✓ | -16% ✓ | -15% ✓ |
| evening_rush | 40 x 6 | -13% ✓ | -14% ✓ | -14% ✓ | -15% ✓ | -15% ✓ | -16% ✓ |

### LOOK vs SCAN with `cost`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | -11% ✓ | -11% ✓ | -14% ✓ | -13% ✓ | -18% ✓ | -16% ✓ |
| uniform | 40 x 6 | -11% ✓ | -10% ✓ | -13% ✓ | -11% ✓ | -14% ✓ | -13% ✓ |
| mixed | 30 x 4 | -9% ✓ | -7% ✓ | -9% ✓ | -8% ✓ | -11% ✓ | -9% ✓ |
| mixed | 40 x 6 | -7% ✓ | -5% ✓ | -8% ✓ | -7% ✓ | -11% ✓ | -8% ✓ |
| morning_rush | 30 x 4 | -2% ? | -1% ? | -2% ? | -1% ? | -2% ✓ | -2% ? |
| morning_rush | 40 x 6 | +0% ? | +0% ? | -1% ? | +0% ? | -2% ✓ | -1% ? |
| evening_rush | 30 x 4 | -23% ✓ | -22% ✓ | -24% ✓ | -22% ✓ | -22% ✓ | -20% ✓ |
| evening_rush | 40 x 6 | -30% ✓ | -27% ✓ | -31% ✓ | -29% ✓ | -29% ✓ | -27% ✓ |

### LOOK vs SCAN with `nearest`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | -26% ✓ | -28% ✓ | -22% ✓ | -22% ✓ | -20% ✓ | -19% ✓ |
| uniform | 40 x 6 | -29% ✓ | -30% ✓ | -26% ✓ | -28% ✓ | -21% ✓ | -27% ✓ |
| mixed | 30 x 4 | -23% ✓ | -23% ✓ | -21% ✓ | -20% ✓ | -18% ✓ | -19% ✓ |
| mixed | 40 x 6 | -26% ✓ | -26% ✓ | -23% ✓ | -22% ✓ | -23% ✓ | -22% ✓ |
| morning_rush | 30 x 4 | -16% ✓ | -17% ✓ | -12% ✓ | -15% ✓ | -13% ✓ | -13% ✓ |
| morning_rush | 40 x 6 | -14% ✓ | -15% ✓ | -14% ✓ | -17% ✓ | -14% ✓ | -13% ✓ |
| evening_rush | 30 x 4 | -19% ✓ | -17% ✓ | -15% ✓ | -16% ✓ | -13% ✓ | -13% ✓ |
| evening_rush | 40 x 6 | -17% ✓ | -17% ✓ | -13% ✓ | -14% ✓ | -8% ✓ | -12% ✓ |

### LOOK vs SCAN with `round_robin`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | -25% ✓ | -25% ✓ | -21% ✓ | -21% ✓ | -18% ✓ | -19% ✓ |
| uniform | 40 x 6 | -28% ✓ | -27% ✓ | -26% ✓ | -28% ✓ | -25% ✓ | -25% ✓ |
| mixed | 30 x 4 | -17% ✓ | -16% ✓ | -16% ✓ | -15% ✓ | -12% ✓ | -12% ✓ |
| mixed | 40 x 6 | -19% ✓ | -20% ✓ | -18% ✓ | -17% ✓ | -18% ✓ | -18% ✓ |
| morning_rush | 30 x 4 | -16% ✓ | -15% ✓ | -14% ✓ | -14% ✓ | -13% ✓ | -13% ✓ |
| morning_rush | 40 x 6 | -16% ✓ | -15% ✓ | -16% ✓ | -16% ✓ | -16% ✓ | -17% ✓ |
| evening_rush | 30 x 4 | -19% ✓ | -19% ✓ | -17% ✓ | -16% ✓ | -16% ✓ | -16% ✓ |
| evening_rush | 40 x 6 | -21% ✓ | -20% ✓ | -21% ✓ | -19% ✓ | -20% ✓ | -19% ✓ |

### LOOK vs SCAN with `zone`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | -29% ✓ | -29% ✓ | -26% ✓ | -28% ✓ | -24% ✓ | -24% ✓ |
| uniform | 40 x 6 | -34% ✓ | -34% ✓ | -31% ✓ | -32% ✓ | -30% ✓ | -29% ✓ |
| mixed | 30 x 4 | -27% ✓ | -28% ✓ | -27% ✓ | -27% ✓ | -27% ✓ | -27% ✓ |
| mixed | 40 x 6 | -31% ✓ | -31% ✓ | -31% ✓ | -30% ✓ | -29% ✓ | -30% ✓ |
| morning_rush | 30 x 4 | -26% ✓ | -25% ✓ | -27% ✓ | -26% ✓ | -27% ✓ | -27% ✓ |
| morning_rush | 40 x 6 | -26% ✓ | -27% ✓ | -28% ✓ | -28% ✓ | -28% ✓ | -28% ✓ |
| evening_rush | 30 x 4 | -32% ✓ | -32% ✓ | -30% ✓ | -30% ✓ | -29% ✓ | -29% ✓ |
| evening_rush | 40 x 6 | -34% ✓ | -34% ✓ | -32% ✓ | -32% ✓ | -32% ✓ | -33% ✓ |

### Ranking by mean total time (LOOK, best first)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| uniform | 30 x 4 | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > round_robin > zone | cost > nearest > round_robin > zone |
| uniform | 40 x 6 | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin |
| mixed | 30 x 4 | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin |
| mixed | 40 x 6 | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > zone > nearest > round_robin | cost > nearest > zone > round_robin | cost > zone > nearest > round_robin |
| morning_rush | 30 x 4 | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |
| morning_rush | 40 x 6 | cost > zone > round_robin > nearest | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |
| evening_rush | 30 x 4 | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |
| evening_rush | 40 x 6 | cost > zone > round_robin > nearest | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |

## uniform · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.7; B0 floor = 10.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 16.7 ± 0.6 | -41.7% | [-12.44, -11.45] | 20/20 | 65% | better ✓ |
| nearest | 24.5 ± 2.0 | -14.4% | [-4.95, -3.33] | 20/20 | 23% | better ✓ |
| zone | 27.0 ± 1.5 | -5.7% | [-2.39, -0.81] | 17/20 | 9% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 16.7 | -10.8% | [-2.33, -1.73] | 20/20 | better ✓ |
| nearest | look | 24.5 | -26.3% | [-9.74, -7.70] | 20/20 | better ✓ |
| round_robin | look | 28.7 | -24.9% | [-10.28, -8.79] | 20/20 | better ✓ |
| zone | look | 27.0 | -28.8% | [-11.63, -10.23] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 16.7 | 6.4 | 17.6 | 28.4 | 6.4 | 0.56 |
| cost | scan | 18.7 | 8.4 | 22.4 | 38.2 | 8.4 | 0.57 |
| nearest | look | 24.5 | 14.2 | 44.9 | 54.7 | 14.2 | 0.47 |
| nearest | scan | 33.3 | 22.9 | 56.3 | 57.0 | 22.9 | 0.54 |
| round_robin | look | 28.7 | 18.3 | 42.3 | 53.0 | 18.3 | 0.68 |
| round_robin | scan | 38.2 | 27.9 | 53.6 | 57.0 | 27.9 | 0.74 |
| zone | look | 27.0 | 16.7 | 43.7 | 55.7 | 16.7 | 0.60 |
| zone | scan | 37.9 | 27.6 | 54.1 | 58.5 | 27.6 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.4 | 0.0 | 13% / 10 | 40% | 5.1 / 3.2 | 67% | 11.0 | 1.06 | 0.12 | 0.0% |
| cost | scan | 8.4 | 0.0 | 11% / 13 | 39% | 5.6 / 3.2 | 63% | 10.4 | 1.07 | 0.12 | 0.0% |
| nearest | look | 14.2 | 0.0 | 33% / 28 | 26% | 3.6 / 3.6 | 67% | 11.2 | 1.06 | 0.19 | 0.0% |
| nearest | scan | 22.9 | 0.0 | 37% / 41 | 15% | 3.2 / 3.2 | 79% | 13.3 | 1.07 | 0.19 | 0.0% |
| round_robin | look | 18.3 | 0.0 | 40% / 27 | 19% | 9.4 / 3.6 | 89% | 14.8 | 1.05 | 0.00 | 0.0% |
| round_robin | scan | 27.9 | 0.0 | 48% / 38 | 8% | 10.1 / 4.3 | 94% | 15.9 | 1.06 | 0.00 | 0.0% |
| zone | look | 16.7 | 0.0 | 39% / 27 | 24% | 7.6 / 4.0 | 59% | 9.8 | 1.11 | 0.50 | 0.1% |
| zone | scan | 27.6 | 0.0 | 44% / 39 | 13% | 9.3 / 3.8 | 74% | 12.5 | 1.14 | 0.50 | 0.0% |

## uniform · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.5; B0 floor = 10.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 16.5 ± 0.6 | -42.2% | [-12.65, -11.48] | 20/20 | 66% | better ✓ |
| nearest | 23.7 ± 1.5 | -16.9% | [-5.70, -3.95] | 20/20 | 26% | better ✓ |
| zone | 26.8 ± 1.6 | -5.8% | [-2.46, -0.82] | 18/20 | 9% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 16.5 | -10.5% | [-2.22, -1.62] | 20/20 | better ✓ |
| nearest | look | 23.7 | -28.1% | [-9.95, -8.48] | 20/20 | better ✓ |
| round_robin | look | 28.5 | -25.0% | [-10.21, -8.70] | 20/20 | better ✓ |
| zone | look | 26.8 | -28.8% | [-11.67, -10.03] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 16.5 | 6.1 | 16.9 | 27.6 | 6.1 | 0.56 |
| cost | scan | 18.4 | 8.1 | 21.8 | 31.9 | 8.1 | 0.57 |
| nearest | look | 23.7 | 13.4 | 44.2 | 54.1 | 13.4 | 0.46 |
| nearest | scan | 32.9 | 22.6 | 56.5 | 57.0 | 22.6 | 0.54 |
| round_robin | look | 28.5 | 18.2 | 42.4 | 52.5 | 18.2 | 0.67 |
| round_robin | scan | 38.0 | 27.6 | 53.6 | 57.0 | 27.6 | 0.74 |
| zone | look | 26.8 | 16.5 | 43.6 | 55.9 | 16.5 | 0.59 |
| zone | scan | 37.7 | 27.4 | 54.3 | 61.6 | 27.4 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.1 | 0.0 | 14% / 9 | 41% | 4.9 / 3.0 | 67% | 10.9 | 1.06 | 0.11 | 0.0% |
| cost | scan | 8.1 | 0.0 | 12% / 13 | 40% | 5.3 / 3.0 | 63% | 10.4 | 1.07 | 0.12 | 0.0% |
| nearest | look | 13.4 | 0.0 | 33% / 27 | 27% | 3.4 / 3.4 | 68% | 11.2 | 1.06 | 0.14 | 0.0% |
| nearest | scan | 22.6 | 0.0 | 37% / 40 | 16% | 3.2 / 3.2 | 79% | 13.4 | 1.07 | 0.17 | 0.0% |
| round_robin | look | 18.2 | 0.0 | 40% / 27 | 19% | 9.3 / 3.5 | 88% | 14.7 | 1.04 | 0.00 | 0.0% |
| round_robin | scan | 27.6 | 0.0 | 46% / 38 | 8% | 10.1 / 3.3 | 94% | 15.9 | 1.05 | 0.00 | 0.0% |
| zone | look | 16.5 | 0.0 | 40% / 27 | 25% | 7.6 / 3.8 | 59% | 9.8 | 1.11 | 0.50 | 0.0% |
| zone | scan | 27.4 | 0.0 | 44% / 39 | 13% | 8.9 / 3.4 | 74% | 12.5 | 1.14 | 0.50 | 0.1% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.0 | 1.7 | 16% / 13 | 33% | 5.6 / 3.4 | 78% | 10.9 | 1.08 | 0.08 | 0.0% |
| cost | scan | 10.8 | 2.2 | 15% / 17 | 30% | 6.2 / 3.3 | 75% | 10.6 | 1.09 | 0.12 | 0.0% |
| nearest | look | 18.3 | 2.1 | 36% / 34 | 20% | 3.7 / 3.7 | 74% | 10.6 | 1.08 | 0.18 | 0.0% |
| nearest | scan | 26.7 | 2.3 | 39% / 46 | 12% | 3.5 / 3.5 | 82% | 12.2 | 1.09 | 0.19 | 0.0% |
| round_robin | look | 22.4 | 1.7 | 44% / 32 | 12% | 9.4 / 3.6 | 93% | 13.7 | 1.05 | 0.00 | 0.0% |
| round_robin | scan | 31.0 | 2.0 | 47% / 43 | 5% | 9.8 / 4.7 | 95% | 14.4 | 1.06 | 0.00 | 0.0% |
| zone | look | 20.6 | 2.3 | 39% / 33 | 21% | 7.6 / 3.9 | 63% | 8.9 | 1.13 | 0.50 | 0.1% |
| zone | scan | 32.0 | 2.8 | 44% / 46 | 11% | 8.9 / 3.6 | 77% | 11.4 | 1.16 | 0.50 | 0.3% |

## uniform · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.2; B0 floor = 10.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.9 ± 0.7 | -41.8% | [-15.04, -13.51] | 20/20 | 60% | better ✓ |
| nearest | 30.0 ± 1.9 | -12.2% | [-4.92, -3.51] | 20/20 | 18% | better ✓ |
| zone | 32.5 ± 2.2 | -4.8% | [-2.54, -0.72] | 14/20 | 7% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 19.9 | -13.0% | [-3.44, -2.51] | 20/20 | better ✓ |
| nearest | look | 30.0 | -21.7% | [-9.10, -7.49] | 20/20 | better ✓ |
| round_robin | look | 34.2 | -21.4% | [-10.08, -8.48] | 20/20 | better ✓ |
| zone | look | 32.5 | -27.8% | [-13.45, -11.49] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.9 | 7.8 | 20.2 | 32.6 | 9.5 | 0.58 |
| cost | scan | 22.9 | 10.4 | 27.1 | 41.3 | 12.5 | 0.59 |
| nearest | look | 30.0 | 17.7 | 55.0 | 69.3 | 19.6 | 0.47 |
| nearest | scan | 38.3 | 25.7 | 65.2 | 72.5 | 27.9 | 0.54 |
| round_robin | look | 34.2 | 22.1 | 48.8 | 61.1 | 23.8 | 0.69 |
| round_robin | scan | 43.5 | 31.2 | 60.1 | 66.2 | 33.2 | 0.74 |
| zone | look | 32.5 | 19.9 | 53.0 | 74.8 | 22.2 | 0.58 |
| zone | scan | 45.0 | 31.9 | 63.3 | 82.2 | 34.7 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.8 | 1.7 | 16% / 13 | 33% | 5.5 / 3.2 | 78% | 10.9 | 1.08 | 0.09 | 0.0% |
| cost | scan | 10.4 | 2.1 | 15% / 17 | 32% | 6.1 / 3.2 | 74% | 10.4 | 1.09 | 0.10 | 0.0% |
| nearest | look | 17.7 | 1.9 | 35% / 34 | 22% | 3.3 / 3.3 | 75% | 10.7 | 1.08 | 0.17 | 0.1% |
| nearest | scan | 25.7 | 2.2 | 38% / 46 | 12% | 3.1 / 3.1 | 84% | 12.5 | 1.08 | 0.17 | 0.0% |
| round_robin | look | 22.1 | 1.7 | 44% / 32 | 12% | 9.4 / 3.5 | 93% | 13.7 | 1.05 | 0.00 | 0.0% |
| round_robin | scan | 31.2 | 2.0 | 47% / 43 | 5% | 10.1 / 3.4 | 96% | 14.5 | 1.06 | 0.00 | 0.0% |
| zone | look | 19.9 | 2.3 | 38% / 33 | 21% | 7.5 / 3.8 | 63% | 8.9 | 1.13 | 0.50 | 0.2% |
| zone | scan | 31.9 | 2.8 | 45% / 45 | 11% | 8.8 / 3.5 | 77% | 11.4 | 1.16 | 0.50 | 0.2% |

## uniform · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 41.0; B0 floor = 10.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.8 ± 1.3 | -39.4% | [-16.94, -15.24] | 20/20 | 53% | better ✓ |
| nearest | 37.2 ± 2.6 | -9.1% | [-4.92, -2.34] | 18/20 | 12% | better ✓ |
| zone | 41.2 ± 2.6 | +0.6% | [-0.77, +1.28] | 8/20 | -1% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.8 | -17.9% | [-7.37, -3.78] | 20/20 | better ✓ |
| nearest | look | 37.2 | -19.8% | [-10.61, -7.64] | 20/20 | better ✓ |
| round_robin | look | 41.0 | -18.3% | [-9.99, -8.29] | 20/20 | better ✓ |
| zone | look | 41.2 | -24.3% | [-14.30, -12.29] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.8 | 11.0 | 27.9 | 45.1 | 14.5 | 0.60 |
| cost | scan | 30.3 | 15.8 | 41.2 | 54.5 | 20.0 | 0.60 |
| nearest | look | 37.2 | 22.4 | 68.2 | 92.1 | 26.9 | 0.49 |
| nearest | scan | 46.4 | 31.3 | 78.2 | 94.5 | 36.1 | 0.56 |
| round_robin | look | 41.0 | 26.8 | 58.4 | 73.1 | 30.6 | 0.70 |
| round_robin | scan | 50.1 | 35.5 | 69.0 | 79.5 | 39.8 | 0.74 |
| zone | look | 41.2 | 25.6 | 68.8 | 108.3 | 30.9 | 0.57 |
| zone | scan | 54.5 | 38.1 | 77.2 | 117.9 | 44.1 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.0 | 3.5 | 20% / 18 | 24% | 6.4 / 3.5 | 88% | 10.9 | 1.11 | 0.07 | 0.0% |
| cost | scan | 15.8 | 4.2 | 19% / 25 | 19% | 7.2 / 3.9 | 86% | 10.7 | 1.13 | 0.09 | 0.0% |
| nearest | look | 22.4 | 4.5 | 35% / 42 | 16% | 3.5 / 3.5 | 79% | 9.7 | 1.10 | 0.19 | 0.1% |
| nearest | scan | 31.3 | 4.9 | 39% / 53 | 9% | 3.4 / 3.4 | 87% | 11.4 | 1.10 | 0.17 | 0.1% |
| round_robin | look | 26.8 | 3.8 | 44% / 38 | 7% | 9.6 / 3.8 | 95% | 12.3 | 1.07 | 0.00 | 0.0% |
| round_robin | scan | 35.5 | 4.3 | 47% / 48 | 4% | 10.1 / 5.1 | 97% | 12.8 | 1.07 | 0.00 | 0.0% |
| zone | look | 25.6 | 5.2 | 39% / 41 | 18% | 7.6 / 3.9 | 67% | 8.0 | 1.16 | 0.50 | 0.4% |
| zone | scan | 38.1 | 6.0 | 44% / 53 | 9% | 9.1 / 3.8 | 79% | 10.4 | 1.19 | 0.50 | 0.5% |

## uniform · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 40.5; B0 floor = 10.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.7 ± 1.1 | -39.0% | [-16.52, -15.14] | 20/20 | 52% | better ✓ |
| nearest | 37.1 ± 2.2 | -8.4% | [-4.44, -2.21] | 18/20 | 11% | better ✓ |
| zone | 41.1 ± 2.6 | +1.5% | [-0.31, +1.52] | 6/20 | -2% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.7 | -15.8% | [-6.96, -2.78] | 20/20 | better ✓ |
| nearest | look | 37.1 | -19.4% | [-10.34, -7.54] | 20/20 | better ✓ |
| round_robin | look | 40.5 | -18.7% | [-10.33, -8.28] | 20/20 | better ✓ |
| zone | look | 41.1 | -24.1% | [-14.24, -11.95] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.7 | 10.9 | 28.0 | 45.1 | 14.4 | 0.59 |
| cost | scan | 29.3 | 14.8 | 39.2 | 53.8 | 19.0 | 0.59 |
| nearest | look | 37.1 | 22.4 | 69.4 | 96.8 | 26.8 | 0.48 |
| nearest | scan | 46.1 | 30.9 | 78.4 | 94.3 | 35.7 | 0.55 |
| round_robin | look | 40.5 | 26.4 | 57.9 | 72.7 | 30.2 | 0.69 |
| round_robin | scan | 49.8 | 35.2 | 69.2 | 78.6 | 39.5 | 0.73 |
| zone | look | 41.1 | 25.5 | 69.3 | 114.5 | 30.8 | 0.56 |
| zone | scan | 54.2 | 37.8 | 76.8 | 119.3 | 43.8 | 0.69 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.9 | 3.5 | 21% / 18 | 23% | 6.2 / 3.4 | 88% | 10.8 | 1.11 | 0.07 | 0.0% |
| cost | scan | 14.8 | 4.2 | 19% / 24 | 20% | 6.7 / 3.6 | 84% | 10.5 | 1.12 | 0.08 | 0.0% |
| nearest | look | 22.4 | 4.3 | 38% / 41 | 17% | 3.4 / 3.4 | 80% | 9.9 | 1.10 | 0.15 | 0.1% |
| nearest | scan | 30.9 | 4.9 | 39% / 53 | 10% | 3.3 / 3.3 | 86% | 11.3 | 1.10 | 0.14 | 0.0% |
| round_robin | look | 26.4 | 3.8 | 43% / 38 | 7% | 9.4 / 3.5 | 95% | 12.3 | 1.06 | 0.00 | 0.0% |
| round_robin | scan | 35.2 | 4.3 | 47% / 49 | 3% | 10.0 / 3.1 | 97% | 12.8 | 1.07 | 0.00 | 0.0% |
| zone | look | 25.5 | 5.2 | 38% / 42 | 19% | 7.5 / 3.7 | 67% | 7.9 | 1.16 | 0.50 | 0.5% |
| zone | scan | 37.8 | 6.0 | 44% / 53 | 9% | 8.8 / 3.4 | 80% | 10.4 | 1.19 | 0.50 | 0.5% |

## uniform · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 36.7; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.7 ± 0.7 | -46.3% | [-17.75, -16.19] | 20/20 | 74% | better ✓ |
| nearest | 30.4 ± 2.4 | -17.1% | [-7.51, -4.97] | 20/20 | 27% | better ✓ |
| zone | 33.9 ± 2.1 | -7.6% | [-3.57, -1.98] | 18/20 | 12% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 19.7 | -10.8% | [-2.66, -2.05] | 20/20 | better ✓ |
| nearest | look | 30.4 | -28.9% | [-13.36, -11.50] | 20/20 | better ✓ |
| round_robin | look | 36.7 | -28.2% | [-15.39, -13.41] | 20/20 | better ✓ |
| zone | look | 33.9 | -33.6% | [-18.27, -16.10] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.7 | 6.1 | 17.8 | 34.2 | 6.1 | 0.51 |
| cost | scan | 22.1 | 8.4 | 24.1 | 51.2 | 8.4 | 0.50 |
| nearest | look | 30.4 | 16.8 | 58.6 | 72.0 | 16.8 | 0.43 |
| nearest | scan | 42.8 | 29.2 | 76.6 | 77.0 | 29.2 | 0.51 |
| round_robin | look | 36.7 | 23.0 | 53.9 | 69.0 | 23.0 | 0.68 |
| round_robin | scan | 51.1 | 37.4 | 72.5 | 76.9 | 37.4 | 0.74 |
| zone | look | 33.9 | 20.2 | 54.7 | 73.9 | 20.2 | 0.57 |
| zone | scan | 51.0 | 37.4 | 73.4 | 76.9 | 37.4 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.1 | 0.0 | 9% / 9 | 49% | 5.1 / 3.3 | 56% | 13.9 | 1.05 | 0.18 | 0.0% |
| cost | scan | 8.4 | 0.0 | 9% / 16 | 46% | 5.8 / 3.3 | 54% | 13.3 | 1.06 | 0.21 | 0.0% |
| nearest | look | 16.8 | 0.0 | 30% / 35 | 29% | 3.7 / 3.7 | 58% | 14.6 | 1.05 | 0.26 | 0.0% |
| nearest | scan | 29.2 | 0.0 | 36% / 54 | 18% | 3.4 / 3.4 | 68% | 17.9 | 1.05 | 0.33 | 0.0% |
| round_robin | look | 23.0 | 0.0 | 38% / 35 | 25% | 12.4 / 3.7 | 86% | 21.7 | 1.03 | 0.01 | 0.0% |
| round_robin | scan | 37.4 | 0.0 | 45% / 52 | 11% | 13.5 / 4.1 | 92% | 23.9 | 1.03 | 0.01 | 0.0% |
| zone | look | 20.2 | 0.0 | 36% / 35 | 28% | 9.9 / 4.2 | 53% | 13.7 | 1.09 | 0.55 | 0.1% |
| zone | scan | 37.4 | 0.0 | 44% / 52 | 15% | 12.0 / 3.7 | 69% | 18.0 | 1.12 | 0.55 | 0.0% |

## uniform · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 36.7; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.0 ± 0.7 | -48.0% | [-18.36, -16.85] | 20/20 | 76% | better ✓ |
| nearest | 29.3 ± 2.0 | -19.9% | [-8.28, -6.38] | 20/20 | 32% | better ✓ |
| zone | 33.4 ± 2.1 | -8.9% | [-4.17, -2.36] | 18/20 | 14% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 19.0 | -9.5% | [-2.26, -1.70] | 20/20 | better ✓ |
| nearest | look | 29.3 | -30.4% | [-14.28, -11.29] | 20/20 | better ✓ |
| round_robin | look | 36.7 | -27.5% | [-14.78, -12.92] | 20/20 | better ✓ |
| zone | look | 33.4 | -34.4% | [-18.68, -16.32] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.0 | 5.4 | 15.9 | 27.4 | 5.4 | 0.52 |
| cost | scan | 21.0 | 7.4 | 21.2 | 32.5 | 7.4 | 0.54 |
| nearest | look | 29.3 | 15.7 | 60.3 | 72.7 | 15.7 | 0.39 |
| nearest | scan | 42.1 | 28.5 | 76.4 | 77.0 | 28.5 | 0.50 |
| round_robin | look | 36.7 | 23.0 | 53.7 | 69.3 | 23.0 | 0.68 |
| round_robin | scan | 50.5 | 36.9 | 72.0 | 76.8 | 36.9 | 0.74 |
| zone | look | 33.4 | 19.8 | 55.2 | 71.5 | 19.8 | 0.56 |
| zone | scan | 50.9 | 37.3 | 73.0 | 77.2 | 37.3 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.4 | 0.0 | 8% / 9 | 53% | 4.6 / 2.9 | 57% | 14.1 | 1.05 | 0.14 | 0.0% |
| cost | scan | 7.4 | 0.0 | 8% / 14 | 49% | 5.2 / 2.8 | 55% | 13.6 | 1.05 | 0.16 | 0.0% |
| nearest | look | 15.7 | 0.0 | 29% / 36 | 33% | 3.3 / 3.3 | 60% | 15.1 | 1.05 | 0.21 | 0.0% |
| nearest | scan | 28.5 | 0.0 | 35% / 55 | 21% | 2.9 / 2.9 | 72% | 18.8 | 1.05 | 0.20 | 0.0% |
| round_robin | look | 23.0 | 0.0 | 39% / 35 | 25% | 12.3 / 3.3 | 86% | 21.7 | 1.03 | 0.01 | 0.0% |
| round_robin | scan | 36.9 | 0.0 | 44% / 51 | 11% | 13.4 / 3.1 | 92% | 23.9 | 1.03 | 0.01 | 0.0% |
| zone | look | 19.8 | 0.0 | 36% / 35 | 28% | 9.5 / 3.7 | 53% | 13.6 | 1.09 | 0.55 | 0.0% |
| zone | scan | 37.3 | 0.0 | 44% / 52 | 16% | 11.9 / 3.5 | 69% | 18.0 | 1.12 | 0.55 | 0.0% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.0 | 1.6 | 10% / 11 | 47% | 5.5 / 3.2 | 66% | 14.4 | 1.06 | 0.15 | 0.0% |
| cost | scan | 9.8 | 2.0 | 11% / 18 | 41% | 6.1 / 3.3 | 62% | 13.6 | 1.06 | 0.15 | 0.0% |
| nearest | look | 20.4 | 2.0 | 32% / 43 | 26% | 3.7 / 3.7 | 62% | 13.9 | 1.07 | 0.28 | 0.0% |
| nearest | scan | 32.6 | 2.2 | 36% / 60 | 15% | 3.4 / 3.4 | 72% | 17.2 | 1.06 | 0.30 | 0.0% |
| round_robin | look | 25.5 | 1.5 | 39% / 38 | 20% | 12.4 / 3.8 | 89% | 20.8 | 1.03 | 0.01 | 0.0% |
| round_robin | scan | 39.8 | 1.8 | 45% / 55 | 8% | 13.2 / 4.8 | 93% | 22.4 | 1.04 | 0.01 | 0.0% |
| zone | look | 23.5 | 2.1 | 35% / 40 | 25% | 9.9 / 4.1 | 57% | 12.7 | 1.10 | 0.55 | 0.0% |
| zone | scan | 40.8 | 2.6 | 44% / 58 | 13% | 11.9 / 3.9 | 71% | 16.8 | 1.13 | 0.55 | 0.1% |

## uniform · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 40.3; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 21.6 ± 0.8 | -46.4% | [-19.59, -17.82] | 20/20 | 70% | better ✓ |
| nearest | 33.8 ± 2.6 | -16.2% | [-7.55, -5.58] | 20/20 | 24% | better ✓ |
| zone | 38.6 ± 2.1 | -4.3% | [-2.85, -0.56] | 13/20 | 6% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 21.6 | -11.5% | [-3.07, -2.52] | 20/20 | better ✓ |
| nearest | look | 33.8 | -28.3% | [-14.62, -12.04] | 20/20 | better ✓ |
| round_robin | look | 40.3 | -27.5% | [-16.54, -14.06] | 20/20 | better ✓ |
| zone | look | 38.6 | -31.9% | [-18.87, -17.26] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 21.6 | 6.4 | 18.3 | 30.4 | 8.0 | 0.54 |
| cost | scan | 24.4 | 8.7 | 24.3 | 37.8 | 10.7 | 0.55 |
| nearest | look | 33.8 | 18.3 | 67.3 | 84.5 | 20.1 | 0.41 |
| nearest | scan | 47.1 | 31.4 | 84.0 | 91.8 | 33.5 | 0.51 |
| round_robin | look | 40.3 | 25.2 | 56.9 | 75.6 | 26.7 | 0.68 |
| round_robin | scan | 55.6 | 40.2 | 77.6 | 84.0 | 41.9 | 0.74 |
| zone | look | 38.6 | 22.8 | 62.1 | 81.4 | 24.9 | 0.57 |
| zone | scan | 56.6 | 40.4 | 80.7 | 95.6 | 43.0 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.4 | 1.6 | 9% / 11 | 50% | 5.0 / 2.9 | 66% | 14.5 | 1.05 | 0.12 | 0.0% |
| cost | scan | 8.7 | 2.0 | 10% / 17 | 45% | 5.7 / 2.9 | 63% | 13.7 | 1.06 | 0.14 | 0.0% |
| nearest | look | 18.3 | 1.8 | 31% / 40 | 29% | 3.2 / 3.2 | 65% | 14.6 | 1.05 | 0.21 | 0.0% |
| nearest | scan | 31.4 | 2.1 | 37% / 58 | 18% | 2.9 / 2.9 | 76% | 18.2 | 1.05 | 0.18 | 0.0% |
| round_robin | look | 25.2 | 1.5 | 39% / 38 | 20% | 12.4 / 3.4 | 89% | 20.7 | 1.03 | 0.01 | 0.0% |
| round_robin | scan | 40.2 | 1.8 | 46% / 55 | 8% | 13.1 / 3.1 | 93% | 22.5 | 1.04 | 0.01 | 0.0% |
| zone | look | 22.8 | 2.1 | 35% / 40 | 26% | 9.7 / 3.7 | 56% | 12.6 | 1.11 | 0.55 | 0.0% |
| zone | scan | 40.4 | 2.6 | 43% / 58 | 14% | 11.6 / 3.3 | 71% | 16.8 | 1.14 | 0.55 | 0.1% |

## uniform · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 45.9; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.1 ± 1.2 | -45.3% | [-21.64, -19.86] | 20/20 | 64% | better ✓ |
| nearest | 43.1 ± 3.9 | -6.2% | [-4.37, -1.17] | 15/20 | 9% | - |
| zone | 45.5 ± 2.6 | -0.8% | [-1.30, +0.57] | 12/20 | 1% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 25.1 | -14.0% | [-4.54, -3.67] | 20/20 | better ✓ |
| nearest | look | 43.1 | -20.9% | [-12.80, -9.98] | 20/20 | better ✓ |
| round_robin | look | 45.9 | -24.9% | [-16.38, -14.21] | 20/20 | better ✓ |
| zone | look | 45.5 | -30.2% | [-21.22, -18.19] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.1 | 8.4 | 23.8 | 41.4 | 11.5 | 0.54 |
| cost | scan | 29.2 | 11.7 | 33.2 | 63.1 | 15.6 | 0.52 |
| nearest | look | 43.1 | 25.1 | 84.0 | 106.2 | 29.5 | 0.44 |
| nearest | scan | 54.5 | 36.2 | 95.7 | 116.6 | 40.9 | 0.52 |
| round_robin | look | 45.9 | 29.1 | 64.2 | 83.2 | 32.3 | 0.69 |
| round_robin | scan | 61.2 | 43.8 | 83.6 | 94.2 | 47.6 | 0.74 |
| zone | look | 45.5 | 27.4 | 74.6 | 103.9 | 31.9 | 0.57 |
| zone | scan | 65.3 | 46.1 | 92.5 | 125.3 | 51.6 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.4 | 3.1 | 11% / 15 | 43% | 6.1 / 3.2 | 75% | 14.9 | 1.07 | 0.12 | 0.0% |
| cost | scan | 11.7 | 3.9 | 11% / 20 | 37% | 6.6 / 3.3 | 72% | 14.2 | 1.07 | 0.13 | 0.0% |
| nearest | look | 25.1 | 4.4 | 33% / 51 | 22% | 3.8 / 3.8 | 66% | 13.3 | 1.07 | 0.31 | 0.0% |
| nearest | scan | 36.2 | 4.6 | 36% / 66 | 13% | 3.5 / 3.5 | 76% | 16.3 | 1.07 | 0.29 | 0.1% |
| round_robin | look | 29.1 | 3.2 | 40% / 42 | 15% | 12.6 / 3.7 | 92% | 19.6 | 1.04 | 0.01 | 0.0% |
| round_robin | scan | 43.8 | 3.8 | 47% / 60 | 6% | 13.5 / 5.4 | 94% | 20.9 | 1.04 | 0.01 | 0.0% |
| zone | look | 27.4 | 4.6 | 37% / 46 | 22% | 9.8 / 4.0 | 60% | 11.9 | 1.12 | 0.55 | 0.1% |
| zone | scan | 46.1 | 5.5 | 44% / 66 | 12% | 11.8 / 3.7 | 73% | 15.9 | 1.15 | 0.55 | 0.3% |

## uniform · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 45.3; B0 floor = 13.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.6 ± 1.3 | -45.8% | [-21.66, -19.77] | 20/20 | 66% | better ✓ |
| nearest | 38.8 ± 2.5 | -14.3% | [-7.85, -5.37] | 20/20 | 21% | better ✓ |
| zone | 45.2 ± 2.3 | -0.3% | [-1.01, +0.72] | 10/20 | 0% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.6 | -12.9% | [-4.13, -3.15] | 20/20 | better ✓ |
| nearest | look | 38.8 | -27.3% | [-15.89, -13.26] | 20/20 | better ✓ |
| round_robin | look | 45.3 | -25.3% | [-16.62, -14.08] | 20/20 | better ✓ |
| zone | look | 45.2 | -29.2% | [-19.89, -17.41] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.6 | 7.9 | 22.2 | 36.0 | 10.9 | 0.54 |
| cost | scan | 28.2 | 10.6 | 29.7 | 45.4 | 14.6 | 0.56 |
| nearest | look | 38.8 | 21.3 | 77.3 | 106.8 | 25.2 | 0.41 |
| nearest | scan | 53.4 | 35.3 | 95.5 | 111.7 | 39.7 | 0.50 |
| round_robin | look | 45.3 | 28.5 | 64.6 | 83.8 | 31.7 | 0.68 |
| round_robin | scan | 60.7 | 43.3 | 84.3 | 94.5 | 47.1 | 0.74 |
| zone | look | 45.2 | 27.0 | 74.4 | 101.7 | 31.5 | 0.56 |
| zone | scan | 63.8 | 44.7 | 91.7 | 116.2 | 50.2 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.9 | 3.1 | 10% / 14 | 46% | 5.6 / 2.9 | 75% | 14.8 | 1.07 | 0.10 | 0.0% |
| cost | scan | 10.6 | 3.9 | 11% / 19 | 38% | 6.3 / 2.9 | 71% | 14.1 | 1.07 | 0.13 | 0.0% |
| nearest | look | 21.3 | 3.9 | 31% / 46 | 26% | 3.1 / 3.1 | 69% | 14.1 | 1.06 | 0.21 | 0.1% |
| nearest | scan | 35.3 | 4.5 | 38% / 65 | 16% | 2.9 / 2.9 | 78% | 16.9 | 1.07 | 0.21 | 0.0% |
| round_robin | look | 28.5 | 3.2 | 40% / 42 | 16% | 12.5 / 3.3 | 92% | 19.5 | 1.04 | 0.01 | 0.0% |
| round_robin | scan | 43.3 | 3.7 | 46% / 60 | 6% | 13.3 / 3.0 | 94% | 20.9 | 1.04 | 0.01 | 0.0% |
| zone | look | 27.0 | 4.5 | 36% / 47 | 23% | 9.5 / 3.7 | 59% | 11.8 | 1.12 | 0.55 | 0.1% |
| zone | scan | 44.7 | 5.5 | 44% / 63 | 12% | 11.6 / 3.3 | 72% | 15.7 | 1.15 | 0.55 | 0.2% |

## mixed · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.9; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.2 ± 0.9 | -42.2% | [-15.33, -14.15] | 20/20 | 70% | better ✓ |
| nearest | 29.6 ± 1.5 | -15.2% | [-6.14, -4.48] | 20/20 | 25% | better ✓ |
| zone | 30.0 ± 1.5 | -14.2% | [-5.64, -4.28] | 20/20 | 24% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 20.2 | -8.8% | [-2.27, -1.65] | 20/20 | better ✓ |
| nearest | look | 29.6 | -23.1% | [-9.88, -7.85] | 20/20 | better ✓ |
| round_robin | look | 34.9 | -17.2% | [-8.08, -6.46] | 20/20 | better ✓ |
| zone | look | 30.0 | -27.2% | [-11.89, -10.45] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 20.2 | 6.2 | 17.8 | 30.0 | 6.2 | 0.53 |
| cost | scan | 22.1 | 8.1 | 23.6 | 43.6 | 8.1 | 0.51 |
| nearest | look | 29.6 | 15.6 | 49.8 | 56.2 | 15.6 | 0.45 |
| nearest | scan | 38.5 | 24.5 | 56.5 | 57.0 | 24.5 | 0.55 |
| round_robin | look | 34.9 | 20.9 | 46.9 | 54.9 | 20.9 | 0.68 |
| round_robin | scan | 42.2 | 28.2 | 54.3 | 57.0 | 28.2 | 0.73 |
| zone | look | 30.0 | 16.0 | 43.8 | 55.0 | 16.0 | 0.56 |
| zone | scan | 41.2 | 27.2 | 54.4 | 57.0 | 27.2 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.2 | 0.0 | 11% / 10 | 34% | 5.3 / 3.2 | 72% | 11.8 | 1.31 | 0.14 | 0.0% |
| cost | scan | 8.1 | 0.0 | 7% / 17 | 34% | 6.3 / 3.2 | 68% | 11.2 | 1.35 | 0.14 | 0.0% |
| nearest | look | 15.6 | 0.0 | 34% / 33 | 21% | 3.6 / 3.6 | 75% | 12.6 | 1.31 | 0.13 | 0.0% |
| nearest | scan | 24.5 | 0.0 | 39% / 46 | 13% | 3.8 / 3.8 | 82% | 14.0 | 1.39 | 0.19 | 0.0% |
| round_robin | look | 20.9 | 0.0 | 44% / 32 | 12% | 10.3 / 4.0 | 92% | 15.4 | 1.30 | 0.00 | 0.0% |
| round_robin | scan | 28.2 | 0.0 | 47% / 40 | 7% | 11.5 / 4.5 | 94% | 16.2 | 1.37 | 0.00 | 0.0% |
| zone | look | 16.0 | 0.0 | 36% / 28 | 27% | 8.0 / 3.3 | 70% | 11.7 | 1.30 | 0.14 | 0.0% |
| zone | scan | 27.2 | 0.0 | 42% / 41 | 14% | 10.6 / 4.0 | 83% | 14.0 | 1.46 | 0.14 | 0.0% |

## mixed · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.0; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.2 ± 0.8 | -42.3% | [-15.30, -14.33] | 20/20 | 70% | better ✓ |
| nearest | 29.8 ± 1.7 | -15.0% | [-5.88, -4.61] | 20/20 | 25% | better ✓ |
| zone | 29.8 ± 1.3 | -15.0% | [-5.72, -4.78] | 20/20 | 25% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 20.2 | -7.3% | [-1.92, -1.27] | 20/20 | better ✓ |
| nearest | look | 29.8 | -23.4% | [-10.02, -8.08] | 20/20 | better ✓ |
| round_robin | look | 35.0 | -16.5% | [-7.48, -6.39] | 20/20 | better ✓ |
| zone | look | 29.8 | -28.3% | [-12.37, -11.14] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 20.2 | 6.2 | 17.4 | 28.6 | 6.2 | 0.54 |
| cost | scan | 21.8 | 7.8 | 21.8 | 34.5 | 7.8 | 0.54 |
| nearest | look | 29.8 | 15.8 | 50.0 | 56.6 | 15.8 | 0.46 |
| nearest | scan | 38.9 | 24.9 | 56.7 | 57.0 | 24.9 | 0.55 |
| round_robin | look | 35.0 | 21.0 | 46.9 | 55.0 | 21.0 | 0.68 |
| round_robin | scan | 41.9 | 27.9 | 54.5 | 56.9 | 27.9 | 0.73 |
| zone | look | 29.8 | 15.8 | 43.8 | 55.0 | 15.8 | 0.56 |
| zone | scan | 41.5 | 27.5 | 54.5 | 57.0 | 27.5 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.2 | 0.0 | 10% / 10 | 33% | 5.4 / 3.1 | 72% | 11.8 | 1.31 | 0.13 | 0.0% |
| cost | scan | 7.8 | 0.0 | 7% / 15 | 35% | 6.3 / 3.2 | 69% | 11.3 | 1.35 | 0.12 | 0.0% |
| nearest | look | 15.8 | 0.0 | 36% / 33 | 21% | 3.7 / 3.7 | 75% | 12.7 | 1.31 | 0.16 | 0.0% |
| nearest | scan | 24.9 | 0.0 | 41% / 46 | 12% | 3.6 / 3.6 | 83% | 14.1 | 1.39 | 0.18 | 0.0% |
| round_robin | look | 21.0 | 0.0 | 44% / 32 | 12% | 10.3 / 3.9 | 92% | 15.4 | 1.30 | 0.00 | 0.0% |
| round_robin | scan | 27.9 | 0.0 | 46% / 41 | 7% | 11.3 / 4.1 | 94% | 16.2 | 1.37 | 0.00 | 0.0% |
| zone | look | 15.8 | 0.0 | 36% / 28 | 27% | 8.1 / 3.3 | 70% | 11.8 | 1.30 | 0.14 | 0.0% |
| zone | scan | 27.5 | 0.0 | 44% / 41 | 14% | 10.6 / 3.8 | 83% | 14.1 | 1.46 | 0.14 | 0.0% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.4 | 1.7 | 12% / 13 | 29% | 5.8 / 3.3 | 79% | 11.5 | 1.36 | 0.10 | 0.0% |
| cost | scan | 9.5 | 1.9 | 9% / 21 | 28% | 6.5 / 3.4 | 76% | 11.1 | 1.39 | 0.10 | 0.0% |
| nearest | look | 18.1 | 1.8 | 35% / 38 | 18% | 3.5 / 3.5 | 79% | 11.8 | 1.34 | 0.15 | 0.0% |
| nearest | scan | 26.7 | 2.1 | 39% / 50 | 11% | 3.9 / 3.9 | 84% | 13.1 | 1.42 | 0.18 | 0.0% |
| round_robin | look | 22.9 | 1.6 | 43% / 35 | 9% | 10.4 / 3.9 | 94% | 14.4 | 1.33 | 0.00 | 0.0% |
| round_robin | scan | 29.9 | 1.8 | 47% / 44 | 5% | 11.2 / 5.1 | 96% | 15.0 | 1.40 | 0.00 | 0.0% |
| zone | look | 17.2 | 1.7 | 35% / 31 | 24% | 8.0 / 3.2 | 74% | 11.0 | 1.33 | 0.14 | 0.0% |
| zone | scan | 29.3 | 2.0 | 42% / 44 | 12% | 10.6 / 4.0 | 86% | 13.4 | 1.50 | 0.14 | 0.0% |

## mixed · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.7; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 22.9 ± 0.9 | -40.8% | [-16.27, -15.37] | 20/20 | 64% | better ✓ |
| nearest | 33.7 ± 1.9 | -12.9% | [-5.75, -4.18] | 20/20 | 20% | better ✓ |
| zone | 33.0 ± 1.6 | -14.8% | [-6.30, -5.17] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 22.9 | -7.9% | [-2.41, -1.56] | 20/20 | better ✓ |
| nearest | look | 33.7 | -20.4% | [-9.74, -7.42] | 20/20 | better ✓ |
| round_robin | look | 38.7 | -14.9% | [-7.66, -5.87] | 20/20 | better ✓ |
| zone | look | 33.0 | -27.4% | [-13.25, -11.70] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 22.9 | 7.2 | 20.5 | 33.9 | 8.9 | 0.53 |
| cost | scan | 24.9 | 9.0 | 25.5 | 40.3 | 10.9 | 0.53 |
| nearest | look | 33.7 | 17.9 | 55.7 | 64.2 | 19.7 | 0.46 |
| nearest | scan | 42.4 | 26.4 | 62.3 | 66.8 | 28.4 | 0.54 |
| round_robin | look | 38.7 | 23.1 | 51.2 | 61.0 | 24.7 | 0.69 |
| round_robin | scan | 45.5 | 29.7 | 58.1 | 63.3 | 31.5 | 0.73 |
| zone | look | 33.0 | 17.3 | 49.1 | 62.8 | 19.0 | 0.55 |
| zone | scan | 45.5 | 29.5 | 58.5 | 64.1 | 31.5 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.2 | 1.7 | 11% / 14 | 29% | 5.7 / 3.2 | 79% | 11.5 | 1.36 | 0.11 | 0.0% |
| cost | scan | 9.0 | 1.9 | 8% / 20 | 29% | 6.4 / 3.3 | 75% | 11.0 | 1.38 | 0.12 | 0.0% |
| nearest | look | 17.9 | 1.8 | 35% / 37 | 18% | 3.5 / 3.5 | 79% | 12.0 | 1.35 | 0.15 | 0.0% |
| nearest | scan | 26.4 | 2.0 | 39% / 50 | 11% | 3.8 / 3.8 | 84% | 13.0 | 1.42 | 0.18 | 0.0% |
| round_robin | look | 23.1 | 1.6 | 43% / 35 | 9% | 10.5 / 3.8 | 94% | 14.5 | 1.33 | 0.00 | 0.0% |
| round_robin | scan | 29.7 | 1.8 | 45% / 43 | 5% | 11.6 / 4.1 | 96% | 14.9 | 1.40 | 0.00 | 0.0% |
| zone | look | 17.3 | 1.7 | 36% / 31 | 24% | 8.1 / 3.1 | 74% | 11.0 | 1.33 | 0.14 | 0.0% |
| zone | scan | 29.5 | 2.0 | 44% / 44 | 11% | 10.4 / 3.7 | 86% | 13.4 | 1.50 | 0.14 | 0.0% |

## mixed · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.6 ± 1.7 | -39.0% | [-17.62, -16.42] | 20/20 | 57% | better ✓ |
| nearest | 38.6 ± 2.4 | -11.4% | [-5.84, -4.09] | 20/20 | 17% | better ✓ |
| zone | 36.5 ± 1.6 | -16.2% | [-7.72, -6.39] | 20/20 | 24% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 26.6 | -11.2% | [-4.58, -2.15] | 18/20 | better ✓ |
| nearest | look | 38.6 | -18.1% | [-9.78, -7.33] | 20/20 | better ✓ |
| round_robin | look | 43.6 | -12.3% | [-6.88, -5.27] | 20/20 | better ✓ |
| zone | look | 36.5 | -27.4% | [-14.52, -12.96] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.6 | 9.2 | 25.6 | 40.6 | 12.6 | 0.54 |
| cost | scan | 29.9 | 12.0 | 33.6 | 53.0 | 15.9 | 0.53 |
| nearest | look | 38.6 | 20.7 | 64.2 | 77.9 | 24.6 | 0.46 |
| nearest | scan | 47.1 | 28.8 | 69.6 | 80.5 | 33.1 | 0.54 |
| round_robin | look | 43.6 | 26.1 | 55.5 | 68.3 | 29.6 | 0.70 |
| round_robin | scan | 49.7 | 31.9 | 63.2 | 72.5 | 35.7 | 0.72 |
| zone | look | 36.5 | 18.9 | 53.2 | 70.5 | 22.5 | 0.55 |
| zone | scan | 50.2 | 32.1 | 63.2 | 76.4 | 36.2 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.2 | 3.4 | 14% / 18 | 22% | 6.3 / 3.5 | 85% | 11.2 | 1.41 | 0.09 | 0.0% |
| cost | scan | 12.0 | 3.9 | 12% / 25 | 22% | 7.3 / 3.8 | 83% | 11.0 | 1.44 | 0.11 | 0.0% |
| nearest | look | 20.7 | 3.9 | 35% / 42 | 16% | 3.6 / 3.6 | 82% | 11.0 | 1.39 | 0.16 | 0.2% |
| nearest | scan | 28.8 | 4.3 | 39% / 54 | 9% | 3.8 / 3.8 | 86% | 12.1 | 1.45 | 0.15 | 0.1% |
| round_robin | look | 26.1 | 3.5 | 44% / 39 | 7% | 10.7 / 3.9 | 95% | 13.3 | 1.37 | 0.00 | 0.0% |
| round_robin | scan | 31.9 | 3.8 | 47% / 46 | 4% | 11.4 / 5.4 | 96% | 13.8 | 1.43 | 0.00 | 0.0% |
| zone | look | 18.9 | 3.6 | 35% / 34 | 21% | 8.0 / 3.3 | 78% | 10.3 | 1.37 | 0.14 | 0.0% |
| zone | scan | 32.1 | 4.2 | 43% / 47 | 9% | 10.6 / 3.9 | 89% | 12.6 | 1.54 | 0.14 | 0.0% |

## mixed · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.4; B0 floor = 14.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.5 ± 1.4 | -39.0% | [-17.61, -16.14] | 20/20 | 58% | better ✓ |
| nearest | 38.7 ± 1.4 | -10.9% | [-5.56, -3.86] | 20/20 | 16% | better ✓ |
| zone | 36.9 ± 2.0 | -15.0% | [-7.45, -5.63] | 20/20 | 22% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 26.5 | -9.2% | [-3.64, -1.82] | 18/20 | better ✓ |
| nearest | look | 38.7 | -18.5% | [-10.00, -7.55] | 20/20 | better ✓ |
| round_robin | look | 43.4 | -11.6% | [-6.68, -4.79] | 20/20 | better ✓ |
| zone | look | 36.9 | -26.7% | [-14.50, -12.42] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.5 | 9.1 | 25.1 | 41.8 | 12.5 | 0.54 |
| cost | scan | 29.2 | 11.3 | 33.0 | 46.1 | 15.2 | 0.54 |
| nearest | look | 38.7 | 20.8 | 63.8 | 76.8 | 24.7 | 0.46 |
| nearest | scan | 47.5 | 29.2 | 70.1 | 84.5 | 33.5 | 0.54 |
| round_robin | look | 43.4 | 26.0 | 55.5 | 67.8 | 29.4 | 0.70 |
| round_robin | scan | 49.1 | 31.3 | 63.4 | 72.2 | 35.1 | 0.71 |
| zone | look | 36.9 | 19.3 | 54.4 | 73.2 | 22.9 | 0.55 |
| zone | scan | 50.3 | 32.2 | 64.1 | 75.5 | 36.4 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.1 | 3.4 | 13% / 18 | 23% | 6.2 / 3.4 | 85% | 11.3 | 1.41 | 0.10 | 0.0% |
| cost | scan | 11.3 | 3.9 | 10% / 25 | 22% | 7.3 / 3.6 | 83% | 10.9 | 1.44 | 0.13 | 0.0% |
| nearest | look | 20.8 | 3.9 | 34% / 43 | 16% | 3.6 / 3.6 | 83% | 11.1 | 1.39 | 0.15 | 0.1% |
| nearest | scan | 29.2 | 4.3 | 39% / 55 | 10% | 3.9 / 3.9 | 87% | 12.2 | 1.44 | 0.17 | 0.1% |
| round_robin | look | 26.0 | 3.4 | 42% / 39 | 7% | 10.8 / 3.8 | 95% | 13.3 | 1.37 | 0.00 | 0.0% |
| round_robin | scan | 31.3 | 3.8 | 45% / 46 | 4% | 11.3 / 3.7 | 96% | 13.7 | 1.43 | 0.00 | 0.0% |
| zone | look | 19.3 | 3.6 | 36% / 34 | 21% | 8.0 / 3.1 | 78% | 10.3 | 1.37 | 0.14 | 0.0% |
| zone | scan | 32.2 | 4.1 | 43% / 48 | 9% | 10.5 / 3.8 | 89% | 12.6 | 1.54 | 0.14 | 0.0% |

## mixed · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.9; B0 floor = 18.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.3 ± 1.2 | -45.8% | [-21.15, -19.99] | 20/20 | 78% | better ✓ |
| nearest | 36.4 ± 2.6 | -18.9% | [-9.44, -7.56] | 20/20 | 32% | better ✓ |
| zone | 38.3 ± 1.8 | -14.7% | [-7.32, -5.91] | 20/20 | 25% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.3 | -7.1% | [-2.17, -1.55] | 20/20 | better ✓ |
| nearest | look | 36.4 | -26.1% | [-14.31, -11.51] | 20/20 | better ✓ |
| round_robin | look | 44.9 | -19.4% | [-11.65, -9.81] | 20/20 | better ✓ |
| zone | look | 38.3 | -30.7% | [-17.72, -16.12] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.3 | 5.9 | 18.0 | 33.8 | 5.9 | 0.47 |
| cost | scan | 26.2 | 7.8 | 24.7 | 58.6 | 7.8 | 0.42 |
| nearest | look | 36.4 | 18.0 | 66.1 | 77.0 | 18.0 | 0.39 |
| nearest | scan | 49.2 | 30.9 | 76.4 | 80.5 | 30.9 | 0.50 |
| round_robin | look | 44.9 | 26.5 | 60.2 | 72.8 | 26.5 | 0.67 |
| round_robin | scan | 55.7 | 37.3 | 73.5 | 77.0 | 37.3 | 0.73 |
| zone | look | 38.3 | 19.9 | 56.7 | 74.4 | 19.9 | 0.54 |
| zone | scan | 55.2 | 36.8 | 73.9 | 77.0 | 36.8 | 0.69 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.9 | 0.0 | 8% / 10 | 44% | 5.3 / 3.1 | 64% | 15.9 | 1.25 | 0.15 | 0.0% |
| cost | scan | 7.8 | 0.0 | 5% / 21 | 45% | 5.9 / 3.0 | 61% | 15.1 | 1.27 | 0.20 | 0.0% |
| nearest | look | 18.0 | 0.0 | 30% / 41 | 28% | 3.3 / 3.3 | 68% | 17.3 | 1.25 | 0.20 | 0.0% |
| nearest | scan | 30.9 | 0.0 | 36% / 63 | 17% | 3.6 / 3.6 | 76% | 19.9 | 1.33 | 0.24 | 0.0% |
| round_robin | look | 26.5 | 0.0 | 42% / 41 | 18% | 13.6 / 3.7 | 88% | 22.8 | 1.23 | 0.01 | 0.0% |
| round_robin | scan | 37.3 | 0.0 | 45% / 54 | 10% | 15.3 / 4.6 | 92% | 24.2 | 1.32 | 0.01 | 0.0% |
| zone | look | 19.9 | 0.0 | 35% / 36 | 31% | 10.4 / 3.3 | 65% | 16.8 | 1.25 | 0.17 | 0.0% |
| zone | scan | 36.8 | 0.0 | 42% / 56 | 17% | 13.6 / 3.5 | 80% | 21.0 | 1.41 | 0.17 | 0.0% |

## mixed · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.8; B0 floor = 18.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.1 ± 1.1 | -46.1% | [-21.31, -19.99] | 20/20 | 78% | better ✓ |
| nearest | 36.9 ± 2.6 | -17.7% | [-8.99, -6.96] | 20/20 | 30% | better ✓ |
| zone | 38.0 ± 1.8 | -15.2% | [-7.45, -6.22] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.1 | -5.2% | [-1.63, -1.04] | 20/20 | better ✓ |
| nearest | look | 36.9 | -26.2% | [-14.51, -11.69] | 20/20 | better ✓ |
| round_robin | look | 44.8 | -19.9% | [-12.29, -9.98] | 20/20 | better ✓ |
| zone | look | 38.0 | -31.3% | [-18.12, -16.58] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.1 | 5.7 | 17.0 | 30.4 | 5.7 | 0.49 |
| cost | scan | 25.5 | 7.1 | 21.9 | 36.5 | 7.1 | 0.48 |
| nearest | look | 36.9 | 18.5 | 66.3 | 75.5 | 18.5 | 0.39 |
| nearest | scan | 49.9 | 31.6 | 76.5 | 77.0 | 31.6 | 0.51 |
| round_robin | look | 44.8 | 26.4 | 60.4 | 72.2 | 26.4 | 0.67 |
| round_robin | scan | 55.9 | 37.5 | 73.3 | 76.8 | 37.5 | 0.73 |
| zone | look | 38.0 | 19.6 | 56.5 | 74.2 | 19.6 | 0.53 |
| zone | scan | 55.3 | 36.9 | 73.7 | 77.0 | 36.9 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.7 | 0.0 | 8% / 10 | 44% | 5.2 / 2.9 | 64% | 15.8 | 1.25 | 0.15 | 0.0% |
| cost | scan | 7.1 | 0.0 | 5% / 17 | 46% | 5.8 / 2.9 | 61% | 15.2 | 1.27 | 0.17 | 0.0% |
| nearest | look | 18.5 | 0.0 | 32% / 42 | 27% | 3.2 / 3.2 | 68% | 17.4 | 1.25 | 0.20 | 0.0% |
| nearest | scan | 31.6 | 0.0 | 38% / 63 | 17% | 3.4 / 3.4 | 78% | 20.2 | 1.34 | 0.21 | 0.0% |
| round_robin | look | 26.4 | 0.0 | 41% / 41 | 18% | 13.7 / 3.5 | 88% | 22.8 | 1.24 | 0.01 | 0.0% |
| round_robin | scan | 37.5 | 0.0 | 46% / 55 | 10% | 15.4 / 3.8 | 92% | 24.2 | 1.32 | 0.01 | 0.0% |
| zone | look | 19.6 | 0.0 | 34% / 36 | 31% | 10.3 / 3.0 | 65% | 16.7 | 1.25 | 0.17 | 0.0% |
| zone | scan | 36.9 | 0.0 | 42% / 55 | 17% | 13.5 / 3.4 | 80% | 21.0 | 1.41 | 0.17 | 0.0% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.7 | 1.6 | 7% / 13 | 42% | 5.6 / 3.1 | 70% | 16.0 | 1.28 | 0.16 | 0.0% |
| cost | scan | 8.9 | 1.8 | 6% / 24 | 39% | 6.4 / 3.1 | 67% | 15.1 | 1.31 | 0.18 | 0.0% |
| nearest | look | 20.6 | 1.7 | 32% / 48 | 26% | 3.3 / 3.3 | 70% | 16.7 | 1.28 | 0.21 | 0.0% |
| nearest | scan | 32.6 | 1.9 | 35% / 67 | 15% | 3.4 / 3.4 | 78% | 19.1 | 1.35 | 0.24 | 0.0% |
| round_robin | look | 28.5 | 1.5 | 42% / 44 | 15% | 13.7 / 3.6 | 90% | 21.8 | 1.26 | 0.01 | 0.0% |
| round_robin | scan | 39.2 | 1.7 | 46% / 57 | 8% | 15.3 / 5.3 | 93% | 22.9 | 1.34 | 0.01 | 0.0% |
| zone | look | 20.9 | 1.5 | 34% / 39 | 29% | 10.3 / 3.1 | 68% | 16.0 | 1.28 | 0.17 | 0.0% |
| zone | scan | 39.0 | 1.9 | 42% / 58 | 14% | 13.6 / 3.5 | 82% | 20.1 | 1.44 | 0.17 | 0.0% |

## mixed · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 48.6; B0 floor = 18.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.2 ± 1.2 | -46.1% | [-23.19, -21.60] | 20/20 | 74% | better ✓ |
| nearest | 40.9 ± 2.8 | -15.9% | [-8.81, -6.71] | 20/20 | 26% | better ✓ |
| zone | 40.7 ± 1.4 | -16.4% | [-9.02, -6.95] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 26.2 | -7.0% | [-2.37, -1.59] | 20/20 | better ✓ |
| nearest | look | 40.9 | -21.8% | [-12.58, -10.31] | 20/20 | better ✓ |
| round_robin | look | 48.6 | -17.4% | [-11.39, -9.07] | 20/20 | better ✓ |
| zone | look | 40.7 | -30.4% | [-18.61, -16.99] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.2 | 6.3 | 19.3 | 33.9 | 7.8 | 0.48 |
| cost | scan | 28.2 | 8.0 | 24.6 | 43.4 | 9.8 | 0.47 |
| nearest | look | 40.9 | 20.8 | 72.4 | 82.6 | 22.5 | 0.39 |
| nearest | scan | 52.3 | 32.0 | 81.4 | 86.8 | 33.9 | 0.48 |
| round_robin | look | 48.6 | 28.8 | 65.0 | 76.8 | 30.3 | 0.68 |
| round_robin | scan | 58.9 | 38.8 | 76.1 | 81.8 | 40.5 | 0.73 |
| zone | look | 40.7 | 20.8 | 60.6 | 80.3 | 22.3 | 0.53 |
| zone | scan | 58.4 | 38.2 | 77.4 | 83.7 | 40.0 | 0.69 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.3 | 1.6 | 7% / 13 | 42% | 5.3 / 2.9 | 69% | 15.8 | 1.29 | 0.15 | 0.0% |
| cost | scan | 8.0 | 1.8 | 6% / 21 | 40% | 6.1 / 3.0 | 66% | 15.0 | 1.31 | 0.16 | 0.0% |
| nearest | look | 20.8 | 1.7 | 32% / 49 | 25% | 3.1 / 3.1 | 71% | 16.6 | 1.29 | 0.22 | 0.0% |
| nearest | scan | 32.0 | 1.9 | 35% / 66 | 15% | 3.2 / 3.2 | 78% | 19.2 | 1.36 | 0.23 | 0.0% |
| round_robin | look | 28.8 | 1.5 | 42% / 44 | 14% | 13.8 / 3.4 | 91% | 21.9 | 1.26 | 0.01 | 0.0% |
| round_robin | scan | 38.8 | 1.7 | 46% / 57 | 8% | 15.3 / 4.0 | 93% | 23.0 | 1.34 | 0.01 | 0.0% |
| zone | look | 20.8 | 1.5 | 33% / 39 | 29% | 10.3 / 3.0 | 68% | 16.0 | 1.28 | 0.17 | 0.0% |
| zone | scan | 38.2 | 1.9 | 41% / 58 | 15% | 13.4 / 3.2 | 82% | 20.1 | 1.43 | 0.17 | 0.0% |

## mixed · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.1; B0 floor = 18.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.6 ± 1.3 | -45.0% | [-24.06, -22.82] | 20/20 | 70% | better ✓ |
| nearest | 44.2 ± 2.4 | -15.1% | [-8.76, -6.85] | 20/20 | 23% | better ✓ |
| zone | 44.6 ± 1.6 | -14.3% | [-8.27, -6.66] | 20/20 | 22% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.6 | -11.3% | [-4.08, -3.26] | 20/20 | better ✓ |
| nearest | look | 44.2 | -22.9% | [-14.69, -11.62] | 20/20 | better ✓ |
| round_robin | look | 52.1 | -17.5% | [-12.14, -10.08] | 20/20 | better ✓ |
| zone | look | 44.6 | -29.2% | [-19.28, -17.56] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.6 | 7.2 | 22.7 | 37.2 | 10.2 | 0.47 |
| cost | scan | 32.3 | 10.4 | 34.3 | 67.8 | 13.9 | 0.42 |
| nearest | look | 44.2 | 22.3 | 77.7 | 90.9 | 25.8 | 0.40 |
| nearest | scan | 57.3 | 35.0 | 88.3 | 98.4 | 39.0 | 0.50 |
| round_robin | look | 52.1 | 30.6 | 68.8 | 84.0 | 33.7 | 0.67 |
| round_robin | scan | 63.1 | 41.3 | 80.3 | 88.4 | 44.7 | 0.72 |
| zone | look | 44.6 | 23.1 | 65.5 | 88.2 | 26.2 | 0.54 |
| zone | scan | 63.0 | 40.8 | 81.9 | 92.7 | 44.6 | 0.69 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.2 | 3.0 | 8% / 13 | 38% | 5.7 / 3.0 | 76% | 15.9 | 1.31 | 0.13 | 0.0% |
| cost | scan | 10.4 | 3.5 | 7% / 28 | 34% | 6.8 / 3.2 | 72% | 15.2 | 1.34 | 0.14 | 0.0% |
| nearest | look | 22.3 | 3.5 | 31% / 52 | 22% | 3.3 / 3.3 | 73% | 16.2 | 1.31 | 0.21 | 0.0% |
| nearest | scan | 35.0 | 4.0 | 36% / 70 | 14% | 3.4 / 3.4 | 81% | 18.3 | 1.38 | 0.24 | 0.0% |
| round_robin | look | 30.6 | 3.1 | 42% / 48 | 12% | 13.8 / 3.5 | 92% | 20.8 | 1.29 | 0.01 | 0.0% |
| round_robin | scan | 41.3 | 3.5 | 47% / 60 | 6% | 15.2 / 5.1 | 94% | 22.0 | 1.36 | 0.01 | 0.0% |
| zone | look | 23.1 | 3.1 | 34% / 43 | 27% | 10.4 / 3.0 | 71% | 15.4 | 1.30 | 0.17 | 0.0% |
| zone | scan | 40.8 | 3.8 | 42% / 62 | 13% | 13.4 / 3.5 | 83% | 19.3 | 1.46 | 0.17 | 0.0% |

## mixed · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.0; B0 floor = 18.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.3 ± 1.2 | -45.6% | [-24.46, -22.96] | 20/20 | 70% | better ✓ |
| nearest | 44.2 ± 3.1 | -15.1% | [-9.29, -6.50] | 20/20 | 23% | better ✓ |
| zone | 44.1 ± 1.7 | -15.3% | [-8.81, -7.09] | 20/20 | 24% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.3 | -8.3% | [-3.20, -1.89] | 19/20 | better ✓ |
| nearest | look | 44.2 | -22.4% | [-14.66, -10.86] | 20/20 | better ✓ |
| round_robin | look | 52.0 | -17.8% | [-12.44, -10.16] | 20/20 | better ✓ |
| zone | look | 44.1 | -30.1% | [-19.95, -17.99] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.3 | 6.9 | 21.7 | 37.1 | 9.9 | 0.47 |
| cost | scan | 30.9 | 9.0 | 27.9 | 47.0 | 12.5 | 0.47 |
| nearest | look | 44.2 | 22.3 | 76.7 | 93.9 | 25.8 | 0.39 |
| nearest | scan | 56.9 | 34.6 | 88.0 | 99.0 | 38.5 | 0.49 |
| round_robin | look | 52.0 | 30.6 | 69.5 | 84.0 | 33.7 | 0.67 |
| round_robin | scan | 63.3 | 41.5 | 81.2 | 88.6 | 44.9 | 0.73 |
| zone | look | 44.1 | 22.5 | 64.2 | 86.2 | 25.7 | 0.54 |
| zone | scan | 63.1 | 40.9 | 82.0 | 90.9 | 44.7 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.9 | 3.0 | 8% / 14 | 39% | 5.5 / 2.8 | 76% | 15.9 | 1.31 | 0.12 | 0.0% |
| cost | scan | 9.0 | 3.5 | 6% / 22 | 35% | 6.4 / 2.9 | 72% | 15.1 | 1.34 | 0.12 | 0.0% |
| nearest | look | 22.3 | 3.5 | 32% / 52 | 24% | 3.2 / 3.2 | 74% | 16.2 | 1.31 | 0.20 | 0.1% |
| nearest | scan | 34.6 | 3.9 | 36% / 70 | 14% | 3.3 / 3.3 | 81% | 18.7 | 1.38 | 0.20 | 0.0% |
| round_robin | look | 30.6 | 3.1 | 42% / 47 | 12% | 13.7 / 3.3 | 92% | 20.9 | 1.29 | 0.01 | 0.0% |
| round_robin | scan | 41.5 | 3.5 | 47% / 60 | 6% | 15.3 / 3.6 | 94% | 22.0 | 1.36 | 0.01 | 0.0% |
| zone | look | 22.5 | 3.2 | 33% / 43 | 27% | 10.5 / 2.9 | 70% | 15.3 | 1.30 | 0.17 | 0.0% |
| zone | scan | 40.9 | 3.8 | 41% / 62 | 13% | 13.6 / 3.2 | 84% | 19.5 | 1.46 | 0.17 | 0.0% |

## morning_rush · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.4; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.2 ± 1.1 | -31.6% | [-11.70, -10.67] | 20/20 | 53% | better ✓ |
| nearest | 34.5 ± 2.8 | -2.6% | [-2.04, +0.22] | 12/20 | 4% | - |
| zone | 30.0 ± 1.6 | -15.2% | [-5.89, -4.85] | 20/20 | 25% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.2 | -2.1% | [-0.82, -0.25] | 15/20 | - |
| nearest | look | 34.5 | -16.3% | [-8.17, -5.09] | 18/20 | better ✓ |
| round_robin | look | 35.4 | -15.9% | [-7.42, -5.96] | 20/20 | better ✓ |
| zone | look | 30.0 | -26.3% | [-11.41, -9.99] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.2 | 9.9 | 23.7 | 28.8 | 9.9 | 0.64 |
| cost | scan | 24.7 | 10.4 | 24.6 | 38.6 | 10.4 | 0.63 |
| nearest | look | 34.5 | 20.2 | 55.0 | 71.8 | 20.2 | 0.51 |
| nearest | scan | 41.2 | 26.9 | 56.8 | 73.8 | 26.9 | 0.57 |
| round_robin | look | 35.4 | 21.1 | 46.4 | 55.0 | 21.1 | 0.68 |
| round_robin | scan | 42.1 | 27.8 | 54.4 | 57.0 | 27.8 | 0.72 |
| zone | look | 30.0 | 15.7 | 41.9 | 55.1 | 15.7 | 0.58 |
| zone | scan | 40.7 | 26.4 | 54.5 | 57.4 | 26.4 | 0.68 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.9 | 0.0 | 6% / 14 | 24% | 9.5 / 5.3 | 56% | 9.3 | 1.58 | 0.22 | 0.0% |
| cost | scan | 10.4 | 0.0 | 2% / 18 | 26% | 9.9 / 5.1 | 56% | 9.3 | 1.58 | 0.20 | 0.0% |
| nearest | look | 20.2 | 0.0 | 41% / 38 | 13% | 5.3 / 5.3 | 63% | 10.6 | 1.52 | 0.29 | 2.0% |
| nearest | scan | 26.9 | 0.0 | 44% / 50 | 9% | 5.2 / 5.2 | 71% | 12.2 | 1.56 | 0.29 | 1.2% |
| round_robin | look | 21.1 | 0.0 | 46% / 33 | 10% | 10.9 / 4.1 | 93% | 15.6 | 1.35 | 0.00 | 0.0% |
| round_robin | scan | 27.8 | 0.0 | 47% / 42 | 7% | 13.0 / 5.4 | 94% | 16.1 | 1.45 | 0.00 | 0.0% |
| zone | look | 15.7 | 0.0 | 37% / 27 | 25% | 8.7 / 2.8 | 72% | 12.1 | 1.37 | 0.11 | 0.0% |
| zone | scan | 26.4 | 0.0 | 43% / 43 | 16% | 11.8 / 4.3 | 81% | 13.9 | 1.55 | 0.11 | 0.0% |

## morning_rush · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.6; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.3 ± 1.0 | -31.7% | [-12.05, -10.59] | 20/20 | 53% | better ✓ |
| nearest | 34.6 ± 1.7 | -2.8% | [-2.05, +0.06] | 12/20 | 5% | - |
| zone | 30.4 ± 1.5 | -14.7% | [-5.82, -4.68] | 20/20 | 25% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.3 | -1.1% | [-0.55, -0.02] | 12/20 | - |
| nearest | look | 34.6 | -16.8% | [-7.92, -6.03] | 20/20 | better ✓ |
| round_robin | look | 35.6 | -15.4% | [-7.06, -5.86] | 20/20 | better ✓ |
| zone | look | 30.4 | -25.5% | [-11.00, -9.78] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.3 | 10.0 | 23.9 | 28.8 | 10.0 | 0.65 |
| cost | scan | 24.6 | 10.3 | 24.0 | 29.9 | 10.3 | 0.65 |
| nearest | look | 34.6 | 20.3 | 52.4 | 63.0 | 20.3 | 0.53 |
| nearest | scan | 41.6 | 27.3 | 56.8 | 68.9 | 27.3 | 0.57 |
| round_robin | look | 35.6 | 21.3 | 46.2 | 55.3 | 21.3 | 0.69 |
| round_robin | scan | 42.1 | 27.8 | 54.8 | 57.0 | 27.8 | 0.73 |
| zone | look | 30.4 | 16.1 | 42.7 | 54.7 | 16.1 | 0.58 |
| zone | scan | 40.7 | 26.4 | 54.8 | 58.8 | 26.4 | 0.68 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.0 | 0.0 | 6% / 14 | 23% | 9.6 / 5.3 | 56% | 9.2 | 1.59 | 0.21 | 0.0% |
| cost | scan | 10.3 | 0.0 | 1% / 14 | 26% | 10.0 / 5.2 | 56% | 9.2 | 1.59 | 0.20 | 0.0% |
| nearest | look | 20.3 | 0.0 | 42% / 38 | 12% | 5.3 / 5.3 | 64% | 10.8 | 1.52 | 0.30 | 0.8% |
| nearest | scan | 27.3 | 0.0 | 45% / 50 | 8% | 5.2 / 5.2 | 72% | 12.3 | 1.57 | 0.34 | 1.6% |
| round_robin | look | 21.3 | 0.0 | 46% / 33 | 9% | 11.0 / 4.0 | 93% | 15.7 | 1.36 | 0.00 | 0.0% |
| round_robin | scan | 27.8 | 0.0 | 47% / 42 | 6% | 13.1 / 5.1 | 95% | 16.2 | 1.45 | 0.00 | 0.0% |
| zone | look | 16.1 | 0.0 | 38% / 28 | 25% | 8.8 / 2.8 | 72% | 12.1 | 1.37 | 0.11 | 0.0% |
| zone | scan | 26.4 | 0.0 | 43% / 43 | 16% | 11.8 / 4.0 | 82% | 13.9 | 1.55 | 0.11 | 0.1% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.2 | 2.5 | 5% / 16 | 23% | 9.4 / 4.9 | 63% | 9.3 | 1.60 | 0.17 | 0.0% |
| cost | scan | 10.6 | 2.6 | 2% / 22 | 24% | 9.6 / 4.8 | 63% | 9.3 | 1.59 | 0.15 | 0.0% |
| nearest | look | 22.9 | 2.6 | 41% / 44 | 11% | 5.2 / 5.2 | 65% | 9.8 | 1.56 | 0.33 | 2.5% |
| nearest | scan | 28.3 | 2.7 | 42% / 55 | 9% | 5.1 / 5.1 | 73% | 11.3 | 1.58 | 0.30 | 2.1% |
| round_robin | look | 23.1 | 1.8 | 47% / 36 | 8% | 11.1 / 4.1 | 94% | 14.6 | 1.39 | 0.00 | 0.0% |
| round_robin | scan | 29.3 | 2.1 | 49% / 45 | 5% | 12.8 / 5.2 | 95% | 15.0 | 1.48 | 0.00 | 0.0% |
| zone | look | 16.7 | 1.7 | 37% / 30 | 23% | 8.7 / 2.6 | 76% | 11.5 | 1.40 | 0.11 | 0.1% |
| zone | scan | 28.6 | 2.1 | 46% / 45 | 13% | 11.8 / 4.0 | 85% | 13.3 | 1.60 | 0.11 | 0.1% |

## morning_rush · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.5; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 27.1 ± 1.2 | -31.4% | [-13.32, -11.51] | 20/20 | 49% | better ✓ |
| nearest | 39.4 ± 2.7 | -0.2% | [-1.43, +1.24] | 12/20 | 0% | - |
| zone | 32.8 ± 1.4 | -16.9% | [-7.28, -6.06] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 27.1 | -1.3% | [-0.72, +0.01] | 11/20 | - |
| nearest | look | 39.4 | -14.7% | [-7.88, -5.73] | 20/20 | better ✓ |
| round_robin | look | 39.5 | -13.8% | [-7.26, -5.46] | 20/20 | better ✓ |
| zone | look | 32.8 | -26.2% | [-12.27, -11.16] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 27.1 | 10.2 | 24.5 | 30.4 | 12.8 | 0.64 |
| cost | scan | 27.5 | 10.5 | 24.8 | 32.7 | 13.2 | 0.64 |
| nearest | look | 39.4 | 22.6 | 58.8 | 78.0 | 25.1 | 0.51 |
| nearest | scan | 46.2 | 29.3 | 63.4 | 77.2 | 31.9 | 0.56 |
| round_robin | look | 39.5 | 23.4 | 50.8 | 59.4 | 25.2 | 0.69 |
| round_robin | scan | 45.8 | 29.5 | 57.7 | 62.6 | 31.6 | 0.72 |
| zone | look | 32.8 | 16.8 | 46.5 | 60.5 | 18.6 | 0.56 |
| zone | scan | 44.5 | 28.2 | 58.3 | 63.9 | 30.2 | 0.68 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.2 | 2.6 | 5% / 16 | 23% | 9.5 / 4.8 | 64% | 9.3 | 1.60 | 0.17 | 0.0% |
| cost | scan | 10.5 | 2.6 | 2% / 17 | 24% | 9.8 / 4.8 | 64% | 9.4 | 1.59 | 0.15 | 0.0% |
| nearest | look | 22.6 | 2.6 | 42% / 43 | 11% | 5.3 / 5.3 | 66% | 9.9 | 1.57 | 0.32 | 1.7% |
| nearest | scan | 29.3 | 2.7 | 44% / 55 | 7% | 4.7 / 4.7 | 74% | 11.6 | 1.59 | 0.32 | 1.6% |
| round_robin | look | 23.4 | 1.8 | 48% / 36 | 7% | 11.2 / 4.1 | 95% | 14.6 | 1.40 | 0.00 | 0.0% |
| round_robin | scan | 29.5 | 2.1 | 48% / 45 | 4% | 13.0 / 4.6 | 95% | 15.0 | 1.48 | 0.00 | 0.0% |
| zone | look | 16.8 | 1.7 | 36% / 30 | 23% | 8.8 / 2.6 | 76% | 11.5 | 1.40 | 0.11 | 0.1% |
| zone | scan | 28.2 | 2.1 | 44% / 45 | 13% | 11.9 / 4.1 | 85% | 13.2 | 1.61 | 0.11 | 0.2% |

## morning_rush · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.3; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.9 ± 1.5 | -30.9% | [-14.17, -12.42] | 20/20 | 46% | better ✓ |
| nearest | 47.6 ± 6.2 | +9.9% | [+1.39, +7.48] | 7/20 | -15% | - |
| zone | 35.8 ± 1.8 | -17.4% | [-8.13, -6.90] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.9 | -2.4% | [-1.15, -0.40] | 16/20 | better ✓ |
| nearest | look | 47.6 | -13.4% | [-10.86, -4.31] | 18/20 | better ✓ |
| round_robin | look | 43.3 | -13.2% | [-7.32, -5.91] | 20/20 | better ✓ |
| zone | look | 35.8 | -26.5% | [-13.69, -12.03] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.9 | 10.7 | 26.0 | 36.6 | 15.6 | 0.61 |
| cost | scan | 30.7 | 11.3 | 28.9 | 45.9 | 16.4 | 0.58 |
| nearest | look | 47.6 | 27.9 | 76.8 | 120.6 | 33.3 | 0.49 |
| nearest | scan | 55.0 | 35.0 | 84.5 | 131.4 | 40.7 | 0.54 |
| round_robin | look | 43.3 | 25.1 | 55.5 | 65.9 | 29.0 | 0.68 |
| round_robin | scan | 49.9 | 31.2 | 62.1 | 69.3 | 35.6 | 0.71 |
| zone | look | 35.8 | 17.9 | 50.4 | 68.0 | 21.5 | 0.55 |
| zone | scan | 48.7 | 30.1 | 61.8 | 73.0 | 34.4 | 0.68 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.7 | 4.9 | 7% / 20 | 22% | 9.4 / 4.4 | 73% | 9.6 | 1.60 | 0.14 | 0.0% |
| cost | scan | 11.3 | 5.0 | 4% / 29 | 22% | 9.6 / 4.5 | 72% | 9.5 | 1.61 | 0.11 | 0.0% |
| nearest | look | 27.9 | 5.4 | 41% / 52 | 10% | 5.0 / 5.0 | 69% | 9.3 | 1.59 | 0.31 | 5.5% |
| nearest | scan | 35.0 | 5.7 | 43% / 62 | 8% | 5.2 / 5.2 | 76% | 10.7 | 1.60 | 0.27 | 6.3% |
| round_robin | look | 25.1 | 3.9 | 46% / 39 | 6% | 11.3 / 4.0 | 96% | 13.4 | 1.43 | 0.00 | 0.0% |
| round_robin | scan | 31.2 | 4.4 | 50% / 47 | 3% | 12.9 / 5.5 | 97% | 14.0 | 1.51 | 0.00 | 0.0% |
| zone | look | 17.9 | 3.6 | 37% / 33 | 21% | 8.7 / 2.5 | 79% | 10.7 | 1.45 | 0.11 | 0.1% |
| zone | scan | 30.1 | 4.3 | 45% / 48 | 10% | 11.9 / 4.3 | 88% | 12.7 | 1.66 | 0.11 | 0.3% |

## morning_rush · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.5; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.8 ± 1.3 | -31.5% | [-14.52, -12.96] | 20/20 | 47% | better ✓ |
| nearest | 46.8 ± 4.3 | +7.6% | [+1.49, +5.13] | 4/20 | -11% | worse ✗ |
| zone | 35.8 ± 1.4 | -17.7% | [-8.44, -7.01] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.8 | -1.8% | [-1.00, -0.08] | 14/20 | - |
| nearest | look | 46.8 | -12.5% | [-8.89, -4.67] | 18/20 | better ✓ |
| round_robin | look | 43.5 | -13.0% | [-7.37, -5.77] | 20/20 | better ✓ |
| zone | look | 35.8 | -27.4% | [-14.13, -12.95] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.8 | 10.6 | 25.9 | 35.0 | 15.5 | 0.61 |
| cost | scan | 30.3 | 10.9 | 26.8 | 37.4 | 16.0 | 0.61 |
| nearest | look | 46.8 | 27.1 | 68.7 | 105.8 | 32.5 | 0.52 |
| nearest | scan | 53.5 | 33.6 | 79.7 | 115.6 | 39.2 | 0.55 |
| round_robin | look | 43.5 | 25.3 | 55.7 | 65.7 | 29.2 | 0.68 |
| round_robin | scan | 50.0 | 31.3 | 62.2 | 69.8 | 35.7 | 0.71 |
| zone | look | 35.8 | 17.9 | 50.7 | 70.7 | 21.5 | 0.55 |
| zone | scan | 49.4 | 30.8 | 61.9 | 77.7 | 35.1 | 0.69 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.6 | 4.9 | 6% / 20 | 21% | 9.2 / 4.5 | 72% | 9.5 | 1.62 | 0.10 | 0.0% |
| cost | scan | 10.9 | 5.2 | 2% / 22 | 22% | 9.5 / 4.3 | 71% | 9.4 | 1.62 | 0.11 | 0.0% |
| nearest | look | 27.1 | 5.4 | 42% / 49 | 10% | 5.1 / 5.1 | 69% | 9.4 | 1.59 | 0.33 | 3.9% |
| nearest | scan | 33.6 | 5.6 | 43% / 60 | 8% | 5.1 / 5.1 | 76% | 10.9 | 1.61 | 0.28 | 4.8% |
| round_robin | look | 25.3 | 3.9 | 46% / 39 | 6% | 11.3 / 4.0 | 96% | 13.5 | 1.44 | 0.00 | 0.0% |
| round_robin | scan | 31.3 | 4.4 | 49% / 47 | 3% | 13.0 / 4.6 | 97% | 14.0 | 1.51 | 0.00 | 0.0% |
| zone | look | 17.9 | 3.6 | 36% / 33 | 20% | 8.9 / 2.6 | 80% | 10.7 | 1.45 | 0.11 | 0.1% |
| zone | scan | 30.8 | 4.3 | 47% / 48 | 10% | 12.1 / 4.1 | 89% | 12.8 | 1.66 | 0.11 | 0.3% |

## morning_rush · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 46.6; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.3 ± 2.0 | -30.7% | [-15.07, -13.47] | 20/20 | 52% | better ✓ |
| nearest | 46.8 ± 2.8 | +0.5% | [-0.97, +1.60] | 10/20 | -1% | - |
| zone | 38.8 ± 2.1 | -16.7% | [-8.51, -7.07] | 20/20 | 28% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 32.3 | +0.3% | [-0.34, +0.53] | 7/20 | - |
| nearest | look | 46.8 | -14.3% | [-9.19, -6.28] | 20/20 | better ✓ |
| round_robin | look | 46.6 | -15.7% | [-9.46, -7.93] | 20/20 | better ✓ |
| zone | look | 38.8 | -26.2% | [-14.74, -12.92] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.3 | 13.3 | 31.0 | 37.5 | 13.3 | 0.64 |
| cost | scan | 32.2 | 13.2 | 31.4 | 45.9 | 13.2 | 0.63 |
| nearest | look | 46.8 | 27.8 | 72.0 | 89.0 | 27.8 | 0.51 |
| nearest | scan | 54.6 | 35.6 | 76.8 | 95.2 | 35.6 | 0.54 |
| round_robin | look | 46.6 | 27.6 | 61.5 | 74.5 | 27.6 | 0.68 |
| round_robin | scan | 55.3 | 36.3 | 73.1 | 76.8 | 36.3 | 0.70 |
| zone | look | 38.8 | 19.8 | 55.4 | 73.5 | 19.8 | 0.56 |
| zone | scan | 52.6 | 33.6 | 73.6 | 78.6 | 33.6 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.3 | 0.0 | 4% / 18 | 22% | 12.8 / 6.3 | 43% | 10.9 | 1.61 | 0.42 | 0.0% |
| cost | scan | 13.2 | 0.0 | 1% / 20 | 24% | 12.7 / 6.1 | 44% | 11.1 | 1.60 | 0.37 | 0.0% |
| nearest | look | 27.8 | 0.0 | 43% / 53 | 14% | 5.6 / 5.6 | 54% | 14.0 | 1.51 | 0.50 | 2.1% |
| nearest | scan | 35.6 | 0.0 | 43% / 69 | 11% | 5.4 / 5.4 | 63% | 16.5 | 1.53 | 0.47 | 1.5% |
| round_robin | look | 27.6 | 0.0 | 45% / 43 | 14% | 14.4 / 3.7 | 90% | 23.2 | 1.30 | 0.01 | 0.0% |
| round_robin | scan | 36.3 | 0.0 | 46% / 57 | 9% | 17.1 / 5.2 | 92% | 24.1 | 1.40 | 0.01 | 0.0% |
| zone | look | 19.8 | 0.0 | 35% / 36 | 31% | 11.2 / 2.4 | 66% | 17.1 | 1.32 | 0.17 | 0.0% |
| zone | scan | 33.6 | 0.0 | 39% / 59 | 21% | 14.8 / 3.4 | 76% | 19.9 | 1.48 | 0.17 | 0.1% |

## morning_rush · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 47.1; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.5 ± 1.7 | -31.0% | [-15.36, -13.81] | 20/20 | 52% | better ✓ |
| nearest | 46.8 ± 3.7 | -0.8% | [-2.00, +1.32] | 12/20 | 1% | - |
| zone | 38.7 ± 1.9 | -17.9% | [-9.04, -7.87] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 32.5 | +0.2% | [-0.27, +0.44] | 10/20 | - |
| nearest | look | 46.8 | -14.5% | [-9.37, -6.60] | 20/20 | better ✓ |
| round_robin | look | 47.1 | -15.4% | [-9.53, -7.68] | 20/20 | better ✓ |
| zone | look | 38.7 | -27.2% | [-15.19, -13.71] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.5 | 13.5 | 31.4 | 37.9 | 13.5 | 0.65 |
| cost | scan | 32.4 | 13.4 | 31.2 | 38.4 | 13.4 | 0.66 |
| nearest | look | 46.8 | 27.7 | 72.2 | 101.2 | 27.7 | 0.50 |
| nearest | scan | 54.7 | 35.7 | 76.8 | 84.3 | 35.7 | 0.55 |
| round_robin | look | 47.1 | 28.1 | 61.8 | 74.0 | 28.1 | 0.69 |
| round_robin | scan | 55.7 | 36.7 | 73.5 | 77.0 | 36.7 | 0.72 |
| zone | look | 38.7 | 19.7 | 55.2 | 73.3 | 19.7 | 0.56 |
| zone | scan | 53.1 | 34.1 | 74.1 | 81.8 | 34.1 | 0.65 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.5 | 0.0 | 4% / 21 | 21% | 13.1 / 6.3 | 43% | 10.8 | 1.64 | 0.43 | 0.0% |
| cost | scan | 13.4 | 0.0 | 1% / 15 | 22% | 13.1 / 6.3 | 43% | 10.7 | 1.63 | 0.38 | 0.0% |
| nearest | look | 27.7 | 0.0 | 42% / 53 | 12% | 5.9 / 5.9 | 52% | 13.3 | 1.54 | 0.49 | 2.8% |
| nearest | scan | 35.7 | 0.0 | 43% / 69 | 10% | 5.4 / 5.4 | 63% | 16.5 | 1.56 | 0.48 | 1.5% |
| round_robin | look | 28.1 | 0.0 | 45% / 43 | 13% | 14.7 / 3.8 | 91% | 23.3 | 1.31 | 0.01 | 0.0% |
| round_robin | scan | 36.7 | 0.0 | 46% / 57 | 9% | 17.4 / 4.6 | 92% | 24.3 | 1.40 | 0.01 | 0.0% |
| zone | look | 19.7 | 0.0 | 34% / 36 | 31% | 11.5 / 2.5 | 67% | 17.2 | 1.33 | 0.17 | 0.0% |
| zone | scan | 34.1 | 0.0 | 39% / 59 | 21% | 15.1 / 3.4 | 77% | 20.1 | 1.49 | 0.17 | 0.1% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.8 | 2.9 | 4% / 20 | 22% | 12.1 / 5.5 | 49% | 11.1 | 1.62 | 0.37 | 0.0% |
| cost | scan | 13.1 | 3.0 | 1% / 19 | 23% | 12.3 / 5.5 | 49% | 11.0 | 1.61 | 0.36 | 0.0% |
| nearest | look | 29.4 | 2.6 | 39% / 57 | 14% | 5.4 / 5.4 | 55% | 13.2 | 1.54 | 0.43 | 4.0% |
| nearest | scan | 37.8 | 2.6 | 42% / 74 | 11% | 5.0 / 5.0 | 64% | 15.7 | 1.55 | 0.48 | 3.0% |
| round_robin | look | 29.0 | 1.6 | 45% / 46 | 11% | 14.4 / 3.6 | 92% | 22.3 | 1.33 | 0.01 | 0.0% |
| round_robin | scan | 38.0 | 1.9 | 46% / 59 | 7% | 17.2 / 5.2 | 93% | 23.2 | 1.42 | 0.01 | 0.0% |
| zone | look | 20.7 | 1.6 | 34% / 39 | 29% | 11.0 / 2.2 | 69% | 16.4 | 1.35 | 0.17 | 0.1% |
| zone | scan | 36.2 | 1.9 | 42% / 61 | 18% | 15.4 / 3.5 | 79% | 19.5 | 1.54 | 0.17 | 0.1% |

## morning_rush · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 50.0; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 35.0 ± 2.0 | -30.0% | [-15.92, -13.98] | 20/20 | 48% | better ✓ |
| nearest | 50.9 ± 3.2 | +1.9% | [-0.42, +2.47] | 10/20 | -3% | - |
| zone | 41.3 ± 2.4 | -17.3% | [-9.40, -8.01] | 20/20 | 28% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 35.0 | +0.3% | [-0.42, +0.57] | 9/20 | - |
| nearest | look | 50.9 | -17.4% | [-12.64, -8.96] | 20/20 | better ✓ |
| round_robin | look | 50.0 | -16.0% | [-10.25, -8.76] | 20/20 | better ✓ |
| zone | look | 41.3 | -27.8% | [-17.18, -14.76] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 35.0 | 13.1 | 32.0 | 39.1 | 16.0 | 0.63 |
| cost | scan | 34.9 | 12.9 | 30.9 | 38.9 | 15.9 | 0.63 |
| nearest | look | 50.9 | 29.3 | 79.2 | 111.0 | 31.9 | 0.49 |
| nearest | scan | 61.7 | 39.9 | 88.0 | 130.7 | 42.7 | 0.54 |
| round_robin | look | 50.0 | 29.3 | 64.7 | 77.8 | 31.0 | 0.68 |
| round_robin | scan | 59.4 | 38.5 | 76.0 | 81.3 | 40.4 | 0.72 |
| zone | look | 41.3 | 20.7 | 58.1 | 78.0 | 22.3 | 0.55 |
| zone | scan | 57.2 | 36.3 | 76.8 | 85.5 | 38.2 | 0.66 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.1 | 2.9 | 3% / 20 | 21% | 12.4 / 5.5 | 48% | 11.0 | 1.64 | 0.31 | 0.0% |
| cost | scan | 12.9 | 3.0 | 1% / 15 | 22% | 12.2 / 5.5 | 48% | 10.8 | 1.63 | 0.34 | 0.0% |
| nearest | look | 29.3 | 2.6 | 41% / 58 | 12% | 5.4 / 5.4 | 55% | 13.1 | 1.55 | 0.45 | 2.5% |
| nearest | scan | 39.9 | 2.8 | 43% / 75 | 9% | 5.2 / 5.2 | 62% | 15.4 | 1.58 | 0.47 | 3.9% |
| round_robin | look | 29.3 | 1.6 | 45% / 46 | 11% | 14.6 / 3.6 | 92% | 22.3 | 1.33 | 0.01 | 0.0% |
| round_robin | scan | 38.5 | 1.9 | 48% / 59 | 7% | 17.5 / 4.9 | 93% | 23.2 | 1.43 | 0.01 | 0.0% |
| zone | look | 20.7 | 1.6 | 33% / 38 | 29% | 11.4 / 2.2 | 69% | 16.4 | 1.35 | 0.17 | 0.0% |
| zone | scan | 36.3 | 1.9 | 42% / 61 | 17% | 15.5 / 3.4 | 79% | 19.6 | 1.54 | 0.17 | 0.1% |

## morning_rush · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.8; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.7 ± 2.1 | -30.5% | [-17.00, -15.14] | 20/20 | 48% | better ✓ |
| nearest | 59.1 ± 13.5 | +11.9% | [+1.66, +12.68] | 5/20 | -19% | - |
| zone | 44.0 ± 2.6 | -16.6% | [-9.75, -7.85] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 36.7 | -1.8% | [-1.14, -0.22] | 16/20 | better ✓ |
| nearest | look | 59.1 | -14.0% | [-13.17, -4.70] | 19/20 | better ✓ |
| round_robin | look | 52.8 | -16.3% | [-11.02, -9.48] | 20/20 | better ✓ |
| zone | look | 44.0 | -28.2% | [-18.49, -16.29] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 36.7 | 12.3 | 31.7 | 39.4 | 17.7 | 0.59 |
| cost | scan | 37.4 | 12.9 | 32.6 | 53.0 | 18.4 | 0.58 |
| nearest | look | 59.1 | 34.7 | 97.3 | 149.9 | 40.1 | 0.46 |
| nearest | scan | 68.7 | 44.1 | 108.0 | 173.3 | 49.7 | 0.52 |
| round_robin | look | 52.8 | 30.4 | 67.9 | 81.8 | 33.8 | 0.67 |
| round_robin | scan | 63.0 | 40.1 | 79.7 | 87.0 | 44.0 | 0.71 |
| zone | look | 44.0 | 21.8 | 63.0 | 83.0 | 25.0 | 0.54 |
| zone | scan | 61.3 | 38.5 | 80.2 | 92.6 | 42.3 | 0.66 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.3 | 5.3 | 4% / 22 | 23% | 11.3 / 5.0 | 56% | 11.6 | 1.61 | 0.28 | 0.0% |
| cost | scan | 12.9 | 5.4 | 1% / 28 | 23% | 11.7 / 5.1 | 56% | 11.7 | 1.61 | 0.28 | 0.0% |
| nearest | look | 34.7 | 5.4 | 38% / 67 | 13% | 5.1 / 5.1 | 58% | 12.6 | 1.56 | 0.45 | 6.7% |
| nearest | scan | 44.1 | 5.6 | 42% / 82 | 10% | 5.3 / 5.3 | 64% | 14.7 | 1.58 | 0.46 | 6.4% |
| round_robin | look | 30.4 | 3.4 | 45% / 48 | 10% | 14.6 / 3.5 | 93% | 21.1 | 1.36 | 0.01 | 0.0% |
| round_robin | scan | 40.1 | 3.9 | 48% / 61 | 6% | 17.1 / 5.5 | 93% | 22.1 | 1.44 | 0.01 | 0.0% |
| zone | look | 21.8 | 3.2 | 35% / 41 | 27% | 11.1 / 2.2 | 72% | 15.8 | 1.37 | 0.17 | 0.1% |
| zone | scan | 38.5 | 3.8 | 44% / 63 | 16% | 15.4 / 3.5 | 82% | 18.9 | 1.56 | 0.17 | 0.3% |

## morning_rush · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.9; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.9 ± 2.0 | -30.3% | [-16.97, -15.02] | 20/20 | 47% | better ✓ |
| nearest | 58.1 ± 5.0 | +9.7% | [+2.76, +7.80] | 3/20 | -15% | worse ✗ |
| zone | 44.0 ± 2.6 | -16.9% | [-9.65, -8.24] | 20/20 | 26% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 36.9 | -0.7% | [-0.68, +0.15] | 11/20 | - |
| nearest | look | 58.1 | -12.9% | [-12.09, -5.79] | 18/20 | better ✓ |
| round_robin | look | 52.9 | -16.7% | [-11.21, -10.00] | 20/20 | better ✓ |
| zone | look | 44.0 | -27.8% | [-18.08, -15.95] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 36.9 | 12.5 | 31.5 | 39.4 | 17.9 | 0.60 |
| cost | scan | 37.1 | 12.6 | 31.8 | 42.8 | 18.1 | 0.60 |
| nearest | look | 58.1 | 33.5 | 88.4 | 133.1 | 39.1 | 0.49 |
| nearest | scan | 66.7 | 42.1 | 97.4 | 126.2 | 47.7 | 0.53 |
| round_robin | look | 52.9 | 30.5 | 67.7 | 81.9 | 33.9 | 0.68 |
| round_robin | scan | 63.5 | 40.6 | 80.3 | 87.2 | 44.5 | 0.72 |
| zone | look | 44.0 | 21.8 | 61.8 | 83.6 | 25.0 | 0.55 |
| zone | scan | 60.9 | 38.1 | 80.1 | 92.1 | 41.9 | 0.66 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.5 | 5.4 | 3% / 20 | 22% | 11.6 / 5.1 | 55% | 11.6 | 1.63 | 0.31 | 0.0% |
| cost | scan | 12.6 | 5.5 | 1% / 16 | 22% | 11.7 / 5.1 | 55% | 11.5 | 1.62 | 0.26 | 0.0% |
| nearest | look | 33.5 | 5.5 | 41% / 63 | 11% | 5.4 / 5.4 | 57% | 12.4 | 1.58 | 0.50 | 4.5% |
| nearest | scan | 42.1 | 5.5 | 43% / 80 | 9% | 4.9 / 4.9 | 65% | 15.1 | 1.59 | 0.47 | 3.5% |
| round_robin | look | 30.5 | 3.4 | 44% / 48 | 9% | 14.8 / 3.4 | 94% | 21.2 | 1.37 | 0.01 | 0.0% |
| round_robin | scan | 40.6 | 3.9 | 49% / 62 | 6% | 17.3 / 4.5 | 94% | 22.2 | 1.45 | 0.01 | 0.0% |
| zone | look | 21.8 | 3.2 | 34% / 41 | 27% | 11.5 / 2.2 | 72% | 15.9 | 1.38 | 0.17 | 0.0% |
| zone | scan | 38.1 | 3.8 | 43% / 63 | 16% | 15.5 / 3.3 | 82% | 19.1 | 1.57 | 0.17 | 0.1% |

## evening_rush · 30 floors x 4 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.9; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.7 ± 1.1 | -32.2% | [-11.88, -10.65] | 20/20 | 55% | better ✓ |
| nearest | 33.7 ± 2.4 | -3.6% | [-2.24, -0.31] | 15/20 | 6% | - |
| zone | 30.3 ± 1.4 | -13.2% | [-5.18, -4.05] | 20/20 | 22% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 23.7 | -23.5% | [-7.91, -6.64] | 20/20 | better ✓ |
| nearest | look | 33.7 | -19.0% | [-8.86, -6.91] | 20/20 | better ✓ |
| round_robin | look | 34.9 | -18.7% | [-8.88, -7.18] | 20/20 | better ✓ |
| zone | look | 30.3 | -31.5% | [-14.67, -13.30] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.7 | 9.4 | 26.0 | 35.4 | 9.4 | 0.56 |
| cost | scan | 30.9 | 16.6 | 39.9 | 52.9 | 16.6 | 0.61 |
| nearest | look | 33.7 | 19.4 | 52.2 | 103.8 | 19.4 | 0.49 |
| nearest | scan | 41.6 | 27.3 | 57.1 | 88.6 | 27.3 | 0.59 |
| round_robin | look | 34.9 | 20.6 | 45.2 | 54.1 | 20.6 | 0.70 |
| round_robin | scan | 43.0 | 28.7 | 54.5 | 57.0 | 28.7 | 0.75 |
| zone | look | 30.3 | 16.0 | 43.0 | 55.2 | 16.0 | 0.59 |
| zone | scan | 44.3 | 30.0 | 54.9 | 69.8 | 30.0 | 0.75 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.4 | 0.0 | 14% / 13 | 34% | 7.6 / 4.4 | 72% | 12.0 | 1.36 | 0.15 | 0.0% |
| cost | scan | 16.6 | 0.0 | 22% / 25 | 25% | 8.3 / 4.2 | 50% | 8.3 | 1.57 | 0.46 | 0.0% |
| nearest | look | 19.4 | 0.0 | 35% / 34 | 20% | 4.9 / 4.9 | 58% | 9.8 | 1.43 | 0.40 | 2.3% |
| nearest | scan | 27.3 | 0.0 | 38% / 43 | 13% | 3.5 / 3.5 | 78% | 13.2 | 1.51 | 0.23 | 0.9% |
| round_robin | look | 20.6 | 0.0 | 43% / 29 | 15% | 10.0 / 4.1 | 90% | 15.1 | 1.36 | 0.00 | 0.0% |
| round_robin | scan | 28.7 | 0.0 | 47% / 38 | 8% | 10.4 / 4.3 | 94% | 15.9 | 1.48 | 0.00 | 0.0% |
| zone | look | 16.0 | 0.0 | 36% / 27 | 26% | 8.4 / 4.7 | 72% | 12.1 | 1.37 | 0.11 | 0.0% |
| zone | scan | 30.0 | 0.0 | 45% / 39 | 12% | 10.0 / 3.8 | 86% | 14.7 | 1.66 | 0.11 | 0.2% |

## evening_rush · 30 floors x 4 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.9; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.5 ± 1.1 | -32.8% | [-12.04, -10.89] | 20/20 | 56% | better ✓ |
| nearest | 34.0 ± 2.3 | -2.7% | [-1.84, +0.07] | 14/20 | 5% | - |
| zone | 30.2 ± 1.5 | -13.7% | [-5.35, -4.20] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 23.5 | -22.2% | [-7.32, -6.14] | 20/20 | better ✓ |
| nearest | look | 34.0 | -17.3% | [-8.03, -6.21] | 20/20 | better ✓ |
| round_robin | look | 34.9 | -18.8% | [-8.87, -7.30] | 20/20 | better ✓ |
| zone | look | 30.2 | -31.6% | [-14.69, -13.22] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.5 | 9.2 | 26.1 | 35.0 | 9.2 | 0.55 |
| cost | scan | 30.2 | 15.9 | 38.8 | 52.0 | 15.9 | 0.60 |
| nearest | look | 34.0 | 19.7 | 52.6 | 107.7 | 19.7 | 0.48 |
| nearest | scan | 41.1 | 26.8 | 56.7 | 78.7 | 26.8 | 0.59 |
| round_robin | look | 34.9 | 20.6 | 45.5 | 54.4 | 20.6 | 0.70 |
| round_robin | scan | 43.0 | 28.7 | 54.4 | 57.0 | 28.7 | 0.75 |
| zone | look | 30.2 | 15.9 | 42.5 | 55.0 | 15.9 | 0.58 |
| zone | scan | 44.1 | 29.8 | 54.8 | 68.7 | 29.8 | 0.75 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.2 | 0.0 | 14% / 13 | 35% | 7.5 / 4.2 | 72% | 12.0 | 1.35 | 0.12 | 0.0% |
| cost | scan | 15.9 | 0.0 | 21% / 25 | 26% | 8.2 / 4.1 | 51% | 8.4 | 1.55 | 0.42 | 0.0% |
| nearest | look | 19.7 | 0.0 | 36% / 35 | 21% | 4.7 / 4.7 | 59% | 9.9 | 1.43 | 0.31 | 2.5% |
| nearest | scan | 26.8 | 0.0 | 39% / 43 | 14% | 3.4 / 3.4 | 79% | 13.6 | 1.49 | 0.17 | 0.6% |
| round_robin | look | 20.6 | 0.0 | 44% / 29 | 15% | 10.0 / 3.9 | 90% | 15.1 | 1.36 | 0.00 | 0.0% |
| round_robin | scan | 28.7 | 0.0 | 48% / 39 | 8% | 10.3 / 3.9 | 93% | 15.9 | 1.47 | 0.00 | 0.0% |
| zone | look | 15.9 | 0.0 | 38% / 26 | 26% | 8.1 / 4.4 | 72% | 12.1 | 1.37 | 0.11 | 0.0% |
| zone | scan | 29.8 | 0.0 | 46% / 39 | 12% | 9.8 / 3.5 | 87% | 14.7 | 1.65 | 0.11 | 0.2% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.5 | 1.9 | 17% / 17 | 29% | 7.6 / 4.2 | 81% | 12.1 | 1.40 | 0.11 | 0.0% |
| cost | scan | 17.5 | 3.0 | 21% / 27 | 22% | 8.6 / 4.1 | 61% | 8.9 | 1.60 | 0.31 | 0.0% |
| nearest | look | 22.9 | 2.5 | 36% / 40 | 18% | 4.5 / 4.5 | 65% | 9.6 | 1.46 | 0.32 | 2.5% |
| nearest | scan | 29.7 | 2.5 | 39% / 47 | 10% | 3.5 / 3.5 | 81% | 12.7 | 1.54 | 0.23 | 1.1% |
| round_robin | look | 23.1 | 1.9 | 44% / 33 | 12% | 10.1 / 4.0 | 92% | 14.2 | 1.40 | 0.00 | 0.0% |
| round_robin | scan | 30.7 | 2.2 | 47% / 42 | 6% | 10.3 / 4.6 | 96% | 14.9 | 1.50 | 0.00 | 0.0% |
| zone | look | 17.6 | 1.7 | 38% / 29 | 23% | 8.0 / 4.4 | 76% | 11.5 | 1.41 | 0.11 | 0.2% |
| zone | scan | 31.6 | 2.2 | 45% / 43 | 10% | 9.8 / 3.9 | 88% | 13.9 | 1.70 | 0.11 | 0.3% |

## evening_rush · 30 floors x 4 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 39.2; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 26.4 ± 1.7 | -32.7% | [-13.47, -12.09] | 20/20 | 51% | better ✓ |
| nearest | 38.8 ± 2.3 | -1.0% | [-1.67, +0.77] | 11/20 | 2% | - |
| zone | 33.7 ± 1.4 | -13.8% | [-6.23, -4.66] | 20/20 | 22% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 26.4 | -22.2% | [-8.48, -6.64] | 20/20 | better ✓ |
| nearest | look | 38.8 | -16.1% | [-8.39, -6.56] | 20/20 | better ✓ |
| round_robin | look | 39.2 | -16.3% | [-8.45, -6.73] | 20/20 | better ✓ |
| zone | look | 33.7 | -29.5% | [-14.95, -13.40] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 26.4 | 10.2 | 27.5 | 42.0 | 12.1 | 0.56 |
| cost | scan | 33.9 | 16.6 | 40.3 | 55.4 | 19.6 | 0.60 |
| nearest | look | 38.8 | 22.0 | 59.8 | 122.5 | 24.5 | 0.48 |
| nearest | scan | 46.2 | 29.4 | 62.4 | 104.8 | 31.9 | 0.58 |
| round_robin | look | 39.2 | 22.9 | 49.8 | 60.8 | 24.9 | 0.69 |
| round_robin | scan | 46.8 | 30.3 | 58.6 | 63.0 | 32.5 | 0.74 |
| zone | look | 33.7 | 17.7 | 47.6 | 64.8 | 19.4 | 0.58 |
| zone | scan | 47.9 | 31.4 | 58.8 | 78.8 | 33.6 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.2 | 1.8 | 17% / 17 | 30% | 7.4 / 4.0 | 81% | 12.0 | 1.38 | 0.12 | 0.1% |
| cost | scan | 16.6 | 3.0 | 20% / 27 | 24% | 8.5 / 4.0 | 60% | 8.8 | 1.58 | 0.28 | 0.0% |
| nearest | look | 22.0 | 2.4 | 36% / 39 | 19% | 4.4 / 4.4 | 66% | 9.7 | 1.45 | 0.27 | 2.5% |
| nearest | scan | 29.4 | 2.5 | 40% / 47 | 12% | 3.3 / 3.3 | 82% | 12.8 | 1.53 | 0.15 | 0.9% |
| round_robin | look | 22.9 | 1.9 | 44% / 33 | 12% | 10.0 / 3.9 | 92% | 14.1 | 1.39 | 0.00 | 0.0% |
| round_robin | scan | 30.3 | 2.2 | 46% / 42 | 6% | 10.2 / 3.6 | 95% | 14.9 | 1.50 | 0.00 | 0.0% |
| zone | look | 17.7 | 1.7 | 38% / 30 | 23% | 7.9 / 4.3 | 77% | 11.4 | 1.40 | 0.11 | 0.1% |
| zone | scan | 31.4 | 2.1 | 45% / 43 | 10% | 9.6 / 3.5 | 88% | 13.9 | 1.70 | 0.11 | 0.3% |

## evening_rush · 30 floors x 4 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.7; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.8 ± 1.6 | -31.8% | [-14.65, -13.10] | 20/20 | 47% | better ✓ |
| nearest | 45.7 ± 3.1 | +4.6% | [+0.57, +3.64] | 4/20 | -7% | worse ✗ |
| zone | 36.9 ± 1.9 | -15.5% | [-7.61, -5.90] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.8 | -22.3% | [-9.57, -7.52] | 20/20 | better ✓ |
| nearest | look | 45.7 | -13.1% | [-8.63, -5.08] | 19/20 | better ✓ |
| round_robin | look | 43.7 | -16.4% | [-9.37, -7.76] | 20/20 | better ✓ |
| zone | look | 36.9 | -28.7% | [-15.84, -13.95] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.8 | 11.9 | 31.3 | 47.0 | 15.5 | 0.58 |
| cost | scan | 38.4 | 18.5 | 45.0 | 63.1 | 24.1 | 0.61 |
| nearest | look | 45.7 | 26.3 | 72.1 | 151.6 | 31.4 | 0.47 |
| nearest | scan | 52.6 | 33.1 | 75.5 | 126.8 | 38.3 | 0.57 |
| round_robin | look | 43.7 | 25.3 | 55.0 | 65.7 | 29.4 | 0.70 |
| round_robin | scan | 52.3 | 33.4 | 63.1 | 73.7 | 38.0 | 0.75 |
| zone | look | 36.9 | 19.0 | 51.7 | 71.3 | 22.6 | 0.57 |
| zone | scan | 51.8 | 33.0 | 62.9 | 87.9 | 37.5 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.9 | 3.7 | 20% / 20 | 24% | 7.7 / 4.1 | 88% | 11.8 | 1.44 | 0.09 | 0.1% |
| cost | scan | 18.5 | 5.5 | 20% / 30 | 20% | 8.7 / 4.1 | 71% | 9.4 | 1.64 | 0.20 | 0.1% |
| nearest | look | 26.3 | 5.1 | 37% / 45 | 16% | 4.5 / 4.5 | 69% | 9.2 | 1.50 | 0.31 | 3.4% |
| nearest | scan | 33.1 | 5.2 | 39% / 53 | 9% | 3.6 / 3.6 | 84% | 11.9 | 1.58 | 0.18 | 1.9% |
| round_robin | look | 25.3 | 4.1 | 44% / 37 | 10% | 10.1 / 3.9 | 94% | 13.1 | 1.44 | 0.00 | 0.0% |
| round_robin | scan | 33.4 | 4.6 | 46% / 46 | 4% | 10.4 / 5.0 | 96% | 13.9 | 1.53 | 0.00 | 0.1% |
| zone | look | 19.0 | 3.6 | 36% / 32 | 21% | 7.7 / 4.2 | 80% | 10.8 | 1.46 | 0.11 | 0.2% |
| zone | scan | 33.0 | 4.5 | 43% / 45 | 8% | 9.5 / 3.7 | 90% | 13.1 | 1.74 | 0.11 | 0.5% |

## evening_rush · 30 floors x 4 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.6 ± 1.8 | -32.2% | [-14.79, -13.32] | 20/20 | 48% | better ✓ |
| nearest | 44.9 ± 3.4 | +3.0% | [-0.40, +3.19] | 8/20 | -4% | - |
| zone | 37.0 ± 2.0 | -15.1% | [-7.44, -5.79] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.6 | -20.4% | [-8.64, -6.50] | 20/20 | better ✓ |
| nearest | look | 44.9 | -12.7% | [-8.00, -5.03] | 20/20 | better ✓ |
| round_robin | look | 43.6 | -16.3% | [-9.43, -7.41] | 20/20 | better ✓ |
| zone | look | 37.0 | -29.0% | [-15.92, -14.20] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.6 | 11.6 | 31.1 | 49.9 | 15.3 | 0.57 |
| cost | scan | 37.1 | 17.3 | 43.1 | 61.4 | 22.8 | 0.59 |
| nearest | look | 44.9 | 25.6 | 68.9 | 145.0 | 30.6 | 0.48 |
| nearest | scan | 51.4 | 32.0 | 70.2 | 128.8 | 37.1 | 0.58 |
| round_robin | look | 43.6 | 25.2 | 54.7 | 66.1 | 29.3 | 0.70 |
| round_robin | scan | 52.1 | 33.2 | 63.9 | 74.5 | 37.8 | 0.74 |
| zone | look | 37.0 | 19.1 | 51.4 | 68.9 | 22.7 | 0.57 |
| zone | scan | 52.1 | 33.3 | 63.4 | 93.5 | 37.8 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.6 | 3.6 | 21% / 20 | 24% | 7.5 / 3.9 | 88% | 11.8 | 1.44 | 0.08 | 0.1% |
| cost | scan | 17.3 | 5.5 | 18% / 29 | 21% | 8.4 / 3.8 | 70% | 9.3 | 1.62 | 0.18 | 0.1% |
| nearest | look | 25.6 | 5.0 | 38% / 46 | 16% | 4.2 / 4.2 | 72% | 9.6 | 1.48 | 0.25 | 3.0% |
| nearest | scan | 32.0 | 5.2 | 40% / 52 | 10% | 3.5 / 3.5 | 84% | 11.9 | 1.56 | 0.17 | 1.1% |
| round_robin | look | 25.2 | 4.1 | 44% / 37 | 10% | 10.1 / 3.8 | 94% | 13.1 | 1.44 | 0.00 | 0.0% |
| round_robin | scan | 33.2 | 4.6 | 47% / 46 | 4% | 10.3 / 3.6 | 95% | 13.8 | 1.52 | 0.00 | 0.1% |
| zone | look | 19.1 | 3.6 | 37% / 32 | 21% | 7.6 / 4.2 | 80% | 10.7 | 1.45 | 0.11 | 0.1% |
| zone | scan | 33.3 | 4.5 | 44% / 46 | 9% | 9.3 / 3.6 | 90% | 13.1 | 1.73 | 0.11 | 0.5% |

## evening_rush · 40 floors x 6 cars · door_time 0 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 45.3; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.6 ± 1.3 | -34.7% | [-16.49, -14.94] | 20/20 | 60% | better ✓ |
| nearest | 46.1 ± 3.2 | +1.7% | [-0.60, +2.18] | 10/20 | -3% | - |
| zone | 39.3 ± 2.0 | -13.3% | [-6.64, -5.39] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.6 | -29.8% | [-14.12, -11.14] | 20/20 | better ✓ |
| nearest | look | 46.1 | -17.1% | [-11.19, -7.89] | 20/20 | better ✓ |
| round_robin | look | 45.3 | -21.0% | [-13.21, -10.97] | 20/20 | better ✓ |
| zone | look | 39.3 | -33.6% | [-20.61, -19.14] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.6 | 10.6 | 31.8 | 42.0 | 10.6 | 0.52 |
| cost | scan | 42.2 | 23.2 | 55.9 | 72.2 | 23.2 | 0.61 |
| nearest | look | 46.1 | 27.1 | 76.9 | 156.8 | 27.1 | 0.45 |
| nearest | scan | 55.6 | 36.6 | 76.8 | 131.9 | 36.6 | 0.57 |
| round_robin | look | 45.3 | 26.3 | 58.8 | 72.7 | 26.3 | 0.68 |
| round_robin | scan | 57.4 | 38.4 | 73.2 | 76.8 | 38.4 | 0.74 |
| zone | look | 39.3 | 20.3 | 54.9 | 72.8 | 20.3 | 0.58 |
| zone | scan | 59.2 | 40.2 | 73.8 | 82.8 | 40.2 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.6 | 0.0 | 10% / 11 | 40% | 8.9 / 4.8 | 60% | 15.1 | 1.33 | 0.33 | 0.0% |
| cost | scan | 23.2 | 0.0 | 25% / 33 | 25% | 10.6 / 4.9 | 40% | 10.1 | 1.56 | 0.70 | 0.0% |
| nearest | look | 27.1 | 0.0 | 36% / 47 | 21% | 5.3 / 5.3 | 48% | 12.4 | 1.42 | 0.63 | 3.8% |
| nearest | scan | 36.6 | 0.0 | 37% / 59 | 16% | 3.5 / 3.5 | 70% | 18.6 | 1.46 | 0.32 | 1.4% |
| round_robin | look | 26.3 | 0.0 | 41% / 39 | 21% | 13.6 / 4.1 | 86% | 22.3 | 1.31 | 0.01 | 0.0% |
| round_robin | scan | 38.4 | 0.0 | 45% / 51 | 11% | 14.0 / 4.7 | 91% | 24.0 | 1.44 | 0.01 | 0.0% |
| zone | look | 20.3 | 0.0 | 35% / 35 | 30% | 10.9 / 4.9 | 67% | 17.2 | 1.33 | 0.17 | 0.0% |
| zone | scan | 40.2 | 0.0 | 42% / 53 | 15% | 13.0 / 3.7 | 82% | 21.7 | 1.62 | 0.17 | 0.1% |

## evening_rush · 40 floors x 6 cars · door_time 0 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 45.4; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.2 ± 1.4 | -35.7% | [-17.02, -15.40] | 20/20 | 61% | better ✓ |
| nearest | 44.6 ± 4.1 | -1.8% | [-2.84, +1.91] | 14/20 | 3% | - |
| zone | 38.9 ± 2.0 | -14.2% | [-7.19, -5.79] | 20/20 | 25% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.2 | -27.1% | [-12.51, -9.43] | 20/20 | better ✓ |
| nearest | look | 44.6 | -17.5% | [-11.06, -7.59] | 19/20 | better ✓ |
| round_robin | look | 45.4 | -19.9% | [-12.40, -10.27] | 20/20 | better ✓ |
| zone | look | 38.9 | -33.5% | [-20.51, -18.70] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.2 | 10.2 | 31.2 | 41.6 | 10.2 | 0.51 |
| cost | scan | 40.0 | 21.0 | 53.0 | 70.7 | 21.0 | 0.58 |
| nearest | look | 44.6 | 25.6 | 75.6 | 156.1 | 25.6 | 0.43 |
| nearest | scan | 54.0 | 35.0 | 76.6 | 112.9 | 35.0 | 0.56 |
| round_robin | look | 45.4 | 26.4 | 59.5 | 72.8 | 26.4 | 0.68 |
| round_robin | scan | 56.7 | 37.7 | 73.1 | 76.8 | 37.7 | 0.73 |
| zone | look | 38.9 | 19.9 | 55.6 | 74.0 | 19.9 | 0.56 |
| zone | scan | 58.5 | 39.5 | 74.0 | 81.5 | 39.5 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.2 | 0.0 | 10% / 11 | 41% | 8.6 / 4.5 | 59% | 15.0 | 1.32 | 0.31 | 0.0% |
| cost | scan | 21.0 | 0.0 | 22% / 32 | 27% | 10.1 / 4.6 | 41% | 10.3 | 1.53 | 0.61 | 0.0% |
| nearest | look | 25.6 | 0.0 | 36% / 46 | 23% | 5.0 / 5.0 | 49% | 12.5 | 1.40 | 0.53 | 3.3% |
| nearest | scan | 35.0 | 0.0 | 37% / 58 | 17% | 3.0 / 3.0 | 72% | 19.1 | 1.44 | 0.24 | 0.5% |
| round_robin | look | 26.4 | 0.0 | 43% / 39 | 20% | 13.6 / 3.8 | 87% | 22.3 | 1.31 | 0.01 | 0.0% |
| round_robin | scan | 37.7 | 0.0 | 45% / 51 | 12% | 13.9 / 3.7 | 92% | 24.1 | 1.43 | 0.01 | 0.0% |
| zone | look | 19.9 | 0.0 | 35% / 35 | 31% | 10.5 / 4.5 | 66% | 17.0 | 1.33 | 0.17 | 0.0% |
| zone | scan | 39.5 | 0.0 | 43% / 53 | 15% | 12.6 / 3.2 | 83% | 21.6 | 1.61 | 0.17 | 0.1% |

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

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.0 | 1.8 | 9% / 14 | 42% | 8.9 / 4.5 | 68% | 15.6 | 1.33 | 0.22 | 0.0% |
| cost | scan | 23.6 | 3.2 | 23% / 36 | 24% | 10.6 / 4.8 | 47% | 10.7 | 1.58 | 0.54 | 0.0% |
| nearest | look | 30.3 | 2.7 | 34% / 53 | 20% | 5.2 / 5.2 | 51% | 11.9 | 1.45 | 0.59 | 4.6% |
| nearest | scan | 38.0 | 2.6 | 36% / 61 | 15% | 3.5 / 3.5 | 72% | 17.7 | 1.48 | 0.33 | 1.5% |
| round_robin | look | 28.4 | 1.7 | 43% / 41 | 17% | 13.6 / 4.0 | 89% | 21.5 | 1.33 | 0.01 | 0.0% |
| round_robin | scan | 40.8 | 2.0 | 46% / 55 | 8% | 14.0 / 5.3 | 93% | 22.9 | 1.45 | 0.01 | 0.0% |
| zone | look | 21.5 | 1.6 | 34% / 38 | 29% | 10.8 / 4.8 | 70% | 16.5 | 1.36 | 0.17 | 0.0% |
| zone | scan | 41.3 | 2.0 | 42% / 55 | 14% | 12.8 / 3.8 | 84% | 20.8 | 1.64 | 0.17 | 0.1% |

## evening_rush · 40 floors x 6 cars · door_time 1 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 48.9; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.4 ± 1.4 | -35.9% | [-18.32, -16.68] | 20/20 | 59% | better ✓ |
| nearest | 49.7 ± 3.7 | +1.6% | [-1.21, +2.93] | 11/20 | -3% | - |
| zone | 41.7 ± 2.0 | -14.9% | [-8.10, -6.44] | 20/20 | 24% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 31.4 | -28.6% | [-14.08, -11.08] | 20/20 | better ✓ |
| nearest | look | 49.7 | -14.3% | [-9.63, -6.65] | 19/20 | better ✓ |
| round_robin | look | 48.9 | -19.4% | [-12.72, -10.85] | 20/20 | better ✓ |
| zone | look | 41.7 | -32.4% | [-20.97, -18.94] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 31.4 | 10.6 | 32.2 | 44.2 | 12.4 | 0.51 |
| cost | scan | 43.9 | 21.8 | 55.8 | 75.4 | 24.9 | 0.58 |
| nearest | look | 49.7 | 28.2 | 84.4 | 174.1 | 30.7 | 0.44 |
| nearest | scan | 58.0 | 36.6 | 81.9 | 122.2 | 39.0 | 0.55 |
| round_robin | look | 48.9 | 28.2 | 63.0 | 77.9 | 29.9 | 0.69 |
| round_robin | scan | 60.7 | 39.7 | 76.7 | 82.2 | 41.7 | 0.74 |
| zone | look | 41.7 | 21.0 | 59.9 | 77.0 | 22.7 | 0.55 |
| zone | scan | 61.6 | 40.6 | 77.1 | 94.8 | 42.6 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.6 | 1.8 | 8% / 14 | 43% | 8.6 / 4.2 | 67% | 15.5 | 1.33 | 0.20 | 0.0% |
| cost | scan | 21.8 | 3.2 | 21% / 35 | 25% | 10.1 / 4.5 | 47% | 10.7 | 1.56 | 0.51 | 0.0% |
| nearest | look | 28.2 | 2.5 | 36% / 53 | 22% | 4.6 / 4.6 | 55% | 12.7 | 1.41 | 0.45 | 3.0% |
| nearest | scan | 36.6 | 2.4 | 36% / 62 | 16% | 3.1 / 3.1 | 74% | 18.3 | 1.47 | 0.24 | 0.5% |
| round_robin | look | 28.2 | 1.7 | 43% / 41 | 17% | 13.3 / 3.7 | 89% | 21.5 | 1.33 | 0.01 | 0.0% |
| round_robin | scan | 39.7 | 2.0 | 45% / 55 | 9% | 13.7 / 3.7 | 92% | 22.8 | 1.45 | 0.01 | 0.0% |
| zone | look | 21.0 | 1.6 | 34% / 38 | 29% | 10.3 / 4.4 | 69% | 16.4 | 1.35 | 0.17 | 0.0% |
| zone | scan | 40.6 | 2.0 | 41% / 55 | 14% | 12.5 / 3.5 | 83% | 20.8 | 1.64 | 0.17 | 0.2% |

## evening_rush · 40 floors x 6 cars · door_time 2 · lobby · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.9; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 34.4 ± 1.8 | -34.9% | [-19.23, -17.63] | 20/20 | 54% | better ✓ |
| nearest | 59.4 ± 8.9 | +12.4% | [+3.27, +10.87] | 3/20 | -19% | worse ✗ |
| zone | 45.1 ± 2.4 | -14.6% | [-8.70, -6.86] | 20/20 | 23% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 34.4 | -28.5% | [-15.24, -12.47] | 20/20 | better ✓ |
| nearest | look | 59.4 | -8.0% | [-7.79, -1.40] | 19/20 | better ✓ |
| round_robin | look | 52.9 | -19.9% | [-14.24, -12.06] | 20/20 | better ✓ |
| zone | look | 45.1 | -32.5% | [-22.71, -20.77] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 34.4 | 12.0 | 34.3 | 48.5 | 15.4 | 0.54 |
| cost | scan | 48.2 | 23.1 | 58.1 | 80.8 | 29.2 | 0.58 |
| nearest | look | 59.4 | 35.1 | 107.0 | 240.1 | 40.4 | 0.44 |
| nearest | scan | 64.6 | 40.4 | 90.0 | 171.0 | 45.6 | 0.54 |
| round_robin | look | 52.9 | 30.3 | 67.4 | 81.3 | 33.9 | 0.69 |
| round_robin | scan | 66.0 | 42.9 | 80.9 | 86.8 | 47.0 | 0.75 |
| zone | look | 45.1 | 22.8 | 62.5 | 85.9 | 26.1 | 0.57 |
| zone | scan | 66.9 | 43.7 | 81.5 | 104.3 | 47.9 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.0 | 3.4 | 11% / 17 | 40% | 9.3 / 4.5 | 75% | 16.2 | 1.34 | 0.15 | 0.0% |
| cost | scan | 23.1 | 6.1 | 21% / 38 | 23% | 10.5 / 4.5 | 54% | 11.3 | 1.60 | 0.41 | 0.0% |
| nearest | look | 35.1 | 5.4 | 36% / 60 | 19% | 4.9 / 4.9 | 56% | 11.9 | 1.46 | 0.53 | 4.4% |
| nearest | scan | 40.4 | 5.2 | 35% / 66 | 13% | 3.4 / 3.4 | 75% | 17.2 | 1.51 | 0.33 | 1.9% |
| round_robin | look | 30.3 | 3.5 | 43% / 45 | 15% | 13.5 / 3.9 | 91% | 20.5 | 1.36 | 0.01 | 0.0% |
| round_robin | scan | 42.9 | 4.1 | 47% / 58 | 7% | 14.0 / 5.2 | 93% | 22.0 | 1.47 | 0.01 | 0.0% |
| zone | look | 22.8 | 3.3 | 34% / 40 | 27% | 10.7 / 4.7 | 73% | 15.8 | 1.39 | 0.17 | 0.1% |
| zone | scan | 43.7 | 4.1 | 42% / 58 | 12% | 12.7 / 3.6 | 85% | 20.1 | 1.67 | 0.17 | 0.3% |

## evening_rush · 40 floors x 6 cars · door_time 2 · spread · 200 requests / 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.7; B0 floor = 19.0)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 33.9 ± 1.7 | -35.7% | [-19.59, -17.91] | 20/20 | 56% | better ✓ |
| nearest | 55.6 ± 5.2 | +5.5% | [+0.71, +5.37] | 5/20 | -9% | - |
| zone | 44.4 ± 2.2 | -15.8% | [-9.01, -7.63] | 20/20 | 25% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 33.9 | -27.0% | [-13.95, -11.41] | 20/20 | better ✓ |
| nearest | look | 55.6 | -12.5% | [-9.75, -5.87] | 19/20 | better ✓ |
| round_robin | look | 52.7 | -19.1% | [-13.55, -11.32] | 20/20 | better ✓ |
| zone | look | 44.4 | -32.7% | [-22.54, -20.65] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 33.9 | 11.5 | 34.0 | 49.5 | 14.9 | 0.53 |
| cost | scan | 46.5 | 21.5 | 56.0 | 78.7 | 27.5 | 0.56 |
| nearest | look | 55.6 | 31.6 | 95.3 | 209.4 | 36.6 | 0.43 |
| nearest | scan | 63.6 | 39.6 | 89.3 | 156.8 | 44.6 | 0.54 |
| round_robin | look | 52.7 | 30.2 | 67.3 | 81.3 | 33.7 | 0.69 |
| round_robin | scan | 65.1 | 42.1 | 80.4 | 87.7 | 46.1 | 0.74 |
| zone | look | 44.4 | 22.1 | 61.6 | 83.3 | 25.4 | 0.56 |
| zone | scan | 66.0 | 42.9 | 80.8 | 98.5 | 47.0 | 0.73 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.5 | 3.4 | 10% / 17 | 41% | 8.9 / 4.2 | 75% | 16.0 | 1.33 | 0.13 | 0.0% |
| cost | scan | 21.5 | 6.0 | 19% / 37 | 24% | 10.0 / 4.2 | 54% | 11.3 | 1.57 | 0.38 | 0.0% |
| nearest | look | 31.6 | 5.0 | 37% / 57 | 21% | 4.5 / 4.5 | 59% | 12.6 | 1.43 | 0.40 | 3.0% |
| nearest | scan | 39.6 | 4.9 | 37% / 68 | 14% | 3.0 / 3.0 | 76% | 17.7 | 1.49 | 0.24 | 1.3% |
| round_robin | look | 30.2 | 3.5 | 43% / 44 | 15% | 13.4 / 3.7 | 91% | 20.5 | 1.36 | 0.01 | 0.0% |
| round_robin | scan | 42.1 | 4.1 | 46% / 58 | 7% | 13.8 / 3.6 | 94% | 22.1 | 1.46 | 0.01 | 0.0% |
| zone | look | 22.1 | 3.3 | 34% / 39 | 28% | 10.4 / 4.4 | 72% | 15.7 | 1.37 | 0.17 | 0.0% |
| zone | scan | 42.9 | 4.1 | 41% / 59 | 13% | 12.4 / 3.2 | 85% | 20.1 | 1.67 | 0.17 | 0.2% |
