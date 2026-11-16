# Benchmark results

Metric: mean total time per passenger (ticks), lower is better. Claim rule: 95% CI of the difference excludes 0 and >= 80% of seeds go the same way. Paired bootstrap, 2000 resamples.

## Headline: `cost` vs `round_robin` (LOOK motion)

| experiment | round_robin | cost | Δ | 95% CI | wins | gap closed | B0 floor |
|---|---:|---:|---:|---|---:|---:|---:|
| quiet · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 26.2 | 17.9 | -31.9% | [-9.1, -7.7] | 20/20 | 60% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.12 requests/tick) · 800 ticks | 26.2 | 17.6 | -32.6% | [-9.3, -7.8] | 20/20 | 62% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 28.5 | 19.6 | -31.1% | [-9.7, -8.0] | 20/20 | 55% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.12 requests/tick) · 800 ticks | 28.4 | 19.3 | -32.2% | [-9.9, -8.4] | 20/20 | 57% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 30.7 | 21.2 | -31.0% | [-10.4, -8.7] | 20/20 | 52% | 12.4 |
| quiet · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.12 requests/tick) · 800 ticks | 30.6 | 20.9 | -31.7% | [-10.5, -8.9] | 20/20 | 53% | 12.4 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 34.0 | 22.0 | -35.3% | [-12.9, -11.1] | 20/20 | 69% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.12 requests/tick) · 800 ticks | 34.1 | 21.6 | -36.7% | [-13.4, -11.7] | 20/20 | 71% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 35.7 | 23.2 | -34.8% | [-13.3, -11.5] | 20/20 | 65% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.12 requests/tick) · 800 ticks | 35.8 | 23.0 | -35.8% | [-13.8, -11.8] | 20/20 | 67% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.12 requests/tick) · 800 ticks | 37.4 | 24.9 | -33.3% | [-13.6, -11.3] | 20/20 | 60% | 16.6 |
| quiet · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.12 requests/tick) · 800 ticks | 37.5 | 24.6 | -34.5% | [-14.0, -11.8] | 20/20 | 62% | 16.6 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 38.1 | 24.6 | -35.3% | [-14.0, -12.9] | 20/20 | 56% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks | 38.2 | 24.7 | -35.2% | [-14.0, -12.8] | 20/20 | 56% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 43.6 | 28.3 | -35.1% | [-15.8, -14.7] | 20/20 | 52% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks | 43.6 | 28.2 | -35.3% | [-16.1, -14.7] | 20/20 | 52% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 50.7 | 33.3 | -34.3% | [-18.3, -16.6] | 20/20 | 48% | 14.1 |
| morning_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks | 50.8 | 32.7 | -35.6% | [-18.9, -17.3] | 20/20 | 49% | 14.1 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 50.9 | 33.7 | -33.8% | [-18.1, -16.3] | 20/20 | 54% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks | 50.9 | 33.6 | -34.0% | [-18.1, -16.4] | 20/20 | 54% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.9 | 36.8 | -34.2% | [-20.0, -18.1] | 20/20 | 52% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks | 56.0 | 36.5 | -34.8% | [-20.5, -18.4] | 20/20 | 53% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 61.7 | 39.4 | -36.2% | [-23.2, -21.6] | 20/20 | 52% | 18.9 |
| morning_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks | 61.8 | 39.6 | -36.0% | [-23.2, -21.3] | 20/20 | 52% | 18.9 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 37.2 | 21.1 | -43.3% | [-16.6, -15.5] | 20/20 | 70% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.36 requests/tick) · 800 ticks | 36.9 | 20.9 | -43.2% | [-16.6, -15.3] | 20/20 | 70% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 42.4 | 25.3 | -40.4% | [-17.7, -16.6] | 20/20 | 60% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.36 requests/tick) · 800 ticks | 42.5 | 25.0 | -41.1% | [-18.0, -16.9] | 20/20 | 61% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 48.4 | 30.3 | -37.4% | [-18.8, -17.4] | 20/20 | 53% | 14.1 |
| lunch · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.36 requests/tick) · 800 ticks | 48.4 | 29.6 | -38.7% | [-19.6, -17.7] | 20/20 | 55% | 14.1 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 49.3 | 25.2 | -48.9% | [-24.7, -23.4] | 20/20 | 79% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.36 requests/tick) · 800 ticks | 49.3 | 25.0 | -49.3% | [-25.0, -23.6] | 20/20 | 79% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 53.6 | 28.2 | -47.4% | [-26.0, -24.8] | 20/20 | 73% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.36 requests/tick) · 800 ticks | 54.0 | 28.0 | -48.1% | [-26.5, -25.4] | 20/20 | 74% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.36 requests/tick) · 800 ticks | 59.6 | 32.0 | -46.4% | [-28.5, -26.8] | 20/20 | 68% | 18.7 |
| lunch · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.36 requests/tick) · 800 ticks | 59.5 | 31.4 | -47.3% | [-29.0, -27.4] | 20/20 | 69% | 18.7 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 38.4 | 23.8 | -38.0% | [-15.1, -14.1] | 20/20 | 60% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks | 38.3 | 23.6 | -38.2% | [-15.1, -14.1] | 20/20 | 61% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 44.7 | 28.5 | -36.2% | [-16.8, -15.6] | 20/20 | 53% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks | 44.6 | 28.3 | -36.7% | [-16.8, -15.9] | 20/20 | 54% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 52.0 | 34.4 | -33.9% | [-18.5, -16.7] | 20/20 | 47% | 14.3 |
| evening_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks | 52.0 | 33.8 | -35.0% | [-18.9, -17.5] | 20/20 | 48% | 14.3 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 49.9 | 29.1 | -41.7% | [-21.4, -20.2] | 20/20 | 67% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks | 49.5 | 28.8 | -41.9% | [-21.2, -20.2] | 20/20 | 68% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 55.3 | 32.5 | -41.2% | [-23.5, -22.0] | 20/20 | 63% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks | 55.2 | 32.1 | -41.9% | [-23.8, -22.3] | 20/20 | 64% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks | 61.6 | 36.7 | -40.5% | [-25.7, -24.2] | 20/20 | 58% | 18.9 |
| evening_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks | 61.5 | 36.2 | -41.0% | [-26.1, -24.4] | 20/20 | 59% | 18.9 |

## Sensitivity: which conclusions survive

Varying: door_time, placement. Cells: Δ mean total time vs the baseline; ✓ better, ✗ worse, ? inconclusive (claim rule above).

### `cost` vs `round_robin` (LOOK)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | -32% ✓ | -33% ✓ | -31% ✓ | -32% ✓ | -31% ✓ | -32% ✓ |
| quiet | 40 x 6 | -35% ✓ | -37% ✓ | -35% ✓ | -36% ✓ | -33% ✓ | -35% ✓ |
| morning_rush | 30 x 4 | -35% ✓ | -35% ✓ | -35% ✓ | -35% ✓ | -34% ✓ | -36% ✓ |
| morning_rush | 40 x 6 | -34% ✓ | -34% ✓ | -34% ✓ | -35% ✓ | -36% ✓ | -36% ✓ |
| lunch | 30 x 4 | -43% ✓ | -43% ✓ | -40% ✓ | -41% ✓ | -37% ✓ | -39% ✓ |
| lunch | 40 x 6 | -49% ✓ | -49% ✓ | -47% ✓ | -48% ✓ | -46% ✓ | -47% ✓ |
| evening_rush | 30 x 4 | -38% ✓ | -38% ✓ | -36% ✓ | -37% ✓ | -34% ✓ | -35% ✓ |
| evening_rush | 40 x 6 | -42% ✓ | -42% ✓ | -41% ✓ | -42% ✓ | -40% ✓ | -41% ✓ |

### `nearest` vs `round_robin` (LOOK)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | -13% ✓ | -14% ✓ | -11% ✓ | -14% ✓ | -8% ✓ | -11% ✓ |
| quiet | 40 x 6 | -18% ✓ | -19% ✓ | -14% ✓ | -15% ✓ | -11% ✓ | -11% ✓ |
| morning_rush | 30 x 4 | -1% ? | +0% ? | +9% ✗ | +17% ✗ | +26% ✗ | +27% ✗ |
| morning_rush | 40 x 6 | +8% ? | +6% ? | +15% ✗ | +25% ✗ | +29% ✗ | +29% ✗ |
| lunch | 30 x 4 | -12% ✓ | -11% ✓ | -10% ✓ | -11% ✓ | -7% ✓ | -9% ✓ |
| lunch | 40 x 6 | -15% ✓ | -15% ✓ | -14% ✓ | -14% ✓ | -13% ✓ | -13% ✓ |
| evening_rush | 30 x 4 | +2% ? | -2% ? | +10% ? | +1% ? | +16% ✗ | +5% ? |
| evening_rush | 40 x 6 | +4% ? | -4% ? | +7% ? | +2% ? | +11% ✗ | +0% ? |

### `zone` vs `round_robin` (LOOK)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | -2% ? | -2% ? | -0% ? | -0% ? | +2% ? | +1% ? |
| quiet | 40 x 6 | +0% ? | -1% ? | +2% ? | +1% ? | +4% ✗ | +2% ? |
| morning_rush | 30 x 4 | -19% ✓ | -19% ✓ | -20% ✓ | -20% ✓ | -21% ✓ | -21% ✓ |
| morning_rush | 40 x 6 | -20% ✓ | -20% ✓ | -20% ✓ | -21% ✓ | -21% ✓ | -22% ✓ |
| lunch | 30 x 4 | -19% ✓ | -18% ✓ | -19% ✓ | -20% ✓ | -20% ✓ | -20% ✓ |
| lunch | 40 x 6 | -20% ✓ | -21% ✓ | -20% ✓ | -21% ✓ | -22% ✓ | -22% ✓ |
| evening_rush | 30 x 4 | -18% ✓ | -18% ✓ | -20% ✓ | -20% ✓ | -20% ✓ | -20% ✓ |
| evening_rush | 40 x 6 | -19% ✓ | -19% ✓ | -20% ✓ | -20% ✓ | -22% ✓ | -22% ✓ |

### LOOK vs SCAN with `cost`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | -13% ✓ | -11% ✓ | -13% ✓ | -12% ✓ | -15% ✓ | -13% ✓ |
| quiet | 40 x 6 | -11% ✓ | -9% ✓ | -13% ✓ | -11% ✓ | -12% ✓ | -11% ✓ |
| morning_rush | 30 x 4 | -1% ? | +0% ? | -4% ✓ | -3% ? | -18% ✓ | -5% ? |
| morning_rush | 40 x 6 | -2% ? | -0% ? | -2% ? | -2% ? | -5% ✓ | -1% ? |
| lunch | 30 x 4 | -7% ✓ | -6% ✓ | -11% ✓ | -8% ✓ | -22% ✓ | -16% ✓ |
| lunch | 40 x 6 | -6% ✓ | -4% ✓ | -8% ✓ | -4% ✓ | -12% ✓ | -6% ✓ |
| evening_rush | 30 x 4 | -26% ✓ | -24% ✓ | -22% ✓ | -21% ✓ | -19% ✓ | -17% ✓ |
| evening_rush | 40 x 6 | -33% ✓ | -31% ✓ | -29% ✓ | -28% ✓ | -25% ✓ | -23% ✓ |

### LOOK vs SCAN with `nearest`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | -28% ✓ | -29% ✓ | -28% ✓ | -30% ✓ | -25% ✓ | -27% ✓ |
| quiet | 40 x 6 | -31% ✓ | -31% ✓ | -29% ✓ | -30% ✓ | -29% ✓ | -29% ✓ |
| morning_rush | 30 x 4 | -13% ✓ | -16% ✓ | -18% ✓ | -8% ✓ | -19% ✓ | -19% ✓ |
| morning_rush | 40 x 6 | -9% ? | -12% ✓ | -20% ✓ | -10% ? | -17% ✓ | -11% ? |
| lunch | 30 x 4 | -17% ✓ | -17% ✓ | -15% ✓ | -17% ✓ | -14% ✓ | -14% ✓ |
| lunch | 40 x 6 | -19% ✓ | -19% ✓ | -18% ✓ | -18% ✓ | -18% ✓ | -17% ✓ |
| evening_rush | 30 x 4 | -9% ✓ | -11% ✓ | -9% ✓ | -14% ✓ | -9% ? | -16% ✓ |
| evening_rush | 40 x 6 | -8% ✓ | -12% ✓ | -8% ✓ | -9% ✓ | -8% ✓ | -11% ✓ |

### LOOK vs SCAN with `round_robin`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | -29% ✓ | -28% ✓ | -28% ✓ | -27% ✓ | -27% ✓ | -27% ✓ |
| quiet | 40 x 6 | -27% ✓ | -27% ✓ | -27% ✓ | -27% ✓ | -27% ✓ | -27% ✓ |
| morning_rush | 30 x 4 | -10% ✓ | -11% ✓ | -10% ✓ | -9% ✓ | -9% ✓ | -9% ✓ |
| morning_rush | 40 x 6 | -10% ✓ | -10% ✓ | -10% ✓ | -10% ✓ | -9% ✓ | -10% ✓ |
| lunch | 30 x 4 | -12% ✓ | -13% ✓ | -11% ✓ | -10% ✓ | -10% ✓ | -9% ✓ |
| lunch | 40 x 6 | -14% ✓ | -14% ✓ | -14% ✓ | -12% ✓ | -11% ✓ | -10% ✓ |
| evening_rush | 30 x 4 | -11% ✓ | -10% ✓ | -9% ✓ | -9% ✓ | -9% ✓ | -9% ✓ |
| evening_rush | 40 x 6 | -13% ✓ | -14% ✓ | -13% ✓ | -12% ✓ | -11% ✓ | -10% ✓ |

### LOOK vs SCAN with `zone`

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | -32% ✓ | -32% ✓ | -30% ✓ | -31% ✓ | -29% ✓ | -30% ✓ |
| quiet | 40 x 6 | -31% ✓ | -32% ✓ | -30% ✓ | -31% ✓ | -30% ✓ | -31% ✓ |
| morning_rush | 30 x 4 | -28% ✓ | -28% ✓ | -30% ✓ | -29% ✓ | -29% ✓ | -29% ✓ |
| morning_rush | 40 x 6 | -27% ✓ | -27% ✓ | -28% ✓ | -28% ✓ | -29% ✓ | -29% ✓ |
| lunch | 30 x 4 | -29% ✓ | -28% ✓ | -27% ✓ | -28% ✓ | -27% ✓ | -27% ✓ |
| lunch | 40 x 6 | -30% ✓ | -30% ✓ | -30% ✓ | -29% ✓ | -30% ✓ | -30% ✓ |
| evening_rush | 30 x 4 | -30% ✓ | -29% ✓ | -30% ✓ | -29% ✓ | -30% ✓ | -30% ✓ |
| evening_rush | 40 x 6 | -31% ✓ | -32% ✓ | -31% ✓ | -30% ✓ | -31% ✓ | -31% ✓ |

### Ranking by mean total time (LOOK, best first)

| scenario | building | door 0 · lobby | door 0 · spread | door 1 · lobby | door 1 · spread | door 2 · lobby | door 2 · spread |
|---|---|---:|---:|---:|---:|---:|---:|
| quiet | 30 x 4 | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > zone > round_robin | cost > nearest > round_robin > zone | cost > nearest > round_robin > zone |
| quiet | 40 x 6 | cost > nearest > round_robin > zone | cost > nearest > zone > round_robin | cost > nearest > round_robin > zone | cost > nearest > round_robin > zone | cost > nearest > round_robin > zone | cost > nearest > round_robin > zone |
| morning_rush | 30 x 4 | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |
| morning_rush | 40 x 6 | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |
| lunch | 30 x 4 | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin |
| lunch | 40 x 6 | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin | cost > zone > nearest > round_robin |
| evening_rush | 30 x 4 | cost > zone > round_robin > nearest | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |
| evening_rush | 40 x 6 | cost > zone > round_robin > nearest | cost > zone > nearest > round_robin | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest | cost > zone > round_robin > nearest |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 26.2; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 17.9 ± 1.3 | -31.9% | [-9.08, -7.71] | 20/20 | 60% | better ✓ |
| nearest | 22.9 ± 2.2 | -12.7% | [-4.23, -2.35] | 18/20 | 24% | better ✓ |
| zone | 25.7 ± 2.3 | -2.0% | [-1.32, +0.27] | 11/20 | 4% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 17.9 | -13.0% | [-3.07, -2.25] | 20/20 | better ✓ |
| nearest | look | 22.9 | -28.1% | [-10.14, -7.66] | 20/20 | better ✓ |
| round_robin | look | 26.2 | -29.2% | [-11.72, -9.94] | 20/20 | better ✓ |
| zone | look | 25.7 | -31.8% | [-12.82, -11.13] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 17.9 | 5.5 | 16.7 | 25.4 | 5.5 | 0.49 |
| cost | scan | 20.5 | 8.2 | 24.6 | 41.9 | 8.2 | 0.46 |
| nearest | look | 22.9 | 10.5 | 40.4 | 53.3 | 10.5 | 0.39 |
| nearest | scan | 31.9 | 19.5 | 55.1 | 56.9 | 19.5 | 0.48 |
| round_robin | look | 26.2 | 13.9 | 33.0 | 45.8 | 13.9 | 0.63 |
| round_robin | scan | 37.1 | 24.7 | 52.2 | 56.6 | 24.7 | 0.69 |
| zone | look | 25.7 | 13.4 | 38.4 | 50.2 | 13.4 | 0.54 |
| zone | scan | 37.7 | 25.3 | 53.7 | 56.4 | 25.3 | 0.66 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.5 | 0.0 | 6% / 10 | 68% | 4.9 / 3.6 | 42% | 14.5 | 1.07 | 0.19 | 0.0% |
| cost | scan | 8.2 | 0.0 | 7% / 18 | 63% | 5.6 / 3.6 | 41% | 14.5 | 1.09 | 0.19 | 0.0% |
| nearest | look | 10.5 | 0.0 | 22% / 26 | 50% | 3.9 / 3.9 | 42% | 14.7 | 1.07 | 0.26 | 0.0% |
| nearest | scan | 19.5 | 0.0 | 26% / 42 | 40% | 3.9 / 3.9 | 53% | 19.0 | 1.10 | 0.25 | 0.0% |
| round_robin | look | 13.9 | 0.0 | 18% / 26 | 65% | 10.5 / 3.9 | 61% | 21.5 | 1.04 | 0.02 | 0.0% |
| round_robin | scan | 24.7 | 0.0 | 29% / 40 | 44% | 10.9 / 4.2 | 75% | 26.9 | 1.06 | 0.02 | 0.0% |
| zone | look | 13.4 | 0.0 | 24% / 27 | 50% | 7.9 / 3.5 | 45% | 16.0 | 1.09 | 0.25 | 0.0% |
| zone | scan | 25.3 | 0.0 | 32% / 40 | 38% | 9.2 / 3.7 | 59% | 21.3 | 1.13 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 3.7 / 14 | 24, 6.2 / 17 | 46, 5.9 / 16 |
| cost | scan | 23, 3.9 / 14 | 24, 11.3 / 31 | 46, 8.3 / 23 |
| nearest | look | 23, 6.8 / 27 | 24, 12.2 / 37 | 46, 11.2 / 41 |
| nearest | scan | 23, 13.3 / 47 | 24, 24.8 / 55 | 46, 19.2 / 54 |
| round_robin | look | 23, 13.0 / 31 | 24, 14.0 / 32 | 46, 14.1 / 33 |
| round_robin | scan | 23, 19.9 / 47 | 24, 28.2 / 53 | 46, 25.1 / 50 |
| zone | look | 23, 11.8 / 33 | 24, 11.4 / 32 | 46, 14.9 / 39 |
| zone | scan | 23, 19.7 / 48 | 24, 29.4 / 54 | 46, 25.9 / 52 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 26.2; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 17.6 ± 1.3 | -32.6% | [-9.28, -7.83] | 20/20 | 62% | better ✓ |
| nearest | 22.4 ± 2.0 | -14.5% | [-4.87, -2.74] | 18/20 | 27% | better ✓ |
| zone | 25.7 ± 2.4 | -1.8% | [-1.33, +0.39] | 11/20 | 3% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 17.6 | -10.8% | [-2.55, -1.73] | 20/20 | better ✓ |
| nearest | look | 22.4 | -28.9% | [-10.36, -7.93] | 20/20 | better ✓ |
| round_robin | look | 26.2 | -28.4% | [-11.19, -9.57] | 20/20 | better ✓ |
| zone | look | 25.7 | -31.8% | [-12.81, -11.20] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 17.6 | 5.3 | 15.6 | 23.4 | 5.3 | 0.51 |
| cost | scan | 19.8 | 7.4 | 21.7 | 32.1 | 7.4 | 0.50 |
| nearest | look | 22.4 | 10.0 | 39.7 | 51.7 | 10.0 | 0.37 |
| nearest | scan | 31.5 | 19.2 | 55.1 | 56.7 | 19.2 | 0.47 |
| round_robin | look | 26.2 | 13.8 | 32.7 | 46.2 | 13.8 | 0.63 |
| round_robin | scan | 36.6 | 24.3 | 52.0 | 56.5 | 24.3 | 0.68 |
| zone | look | 25.7 | 13.4 | 38.8 | 50.5 | 13.4 | 0.53 |
| zone | scan | 37.7 | 25.4 | 53.7 | 56.5 | 25.4 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.3 | 0.0 | 6% / 9 | 69% | 4.8 / 3.4 | 42% | 14.5 | 1.07 | 0.18 | 0.0% |
| cost | scan | 7.4 | 0.0 | 6% / 15 | 65% | 5.4 / 3.5 | 41% | 14.4 | 1.08 | 0.19 | 0.0% |
| nearest | look | 10.0 | 0.0 | 21% / 27 | 52% | 3.7 / 3.7 | 42% | 14.6 | 1.08 | 0.27 | 0.0% |
| nearest | scan | 19.2 | 0.0 | 26% / 43 | 42% | 3.7 / 3.7 | 54% | 19.0 | 1.10 | 0.22 | 0.0% |
| round_robin | look | 13.8 | 0.0 | 18% / 26 | 65% | 10.5 / 3.7 | 61% | 21.5 | 1.04 | 0.02 | 0.0% |
| round_robin | scan | 24.3 | 0.0 | 29% / 39 | 44% | 10.8 / 3.9 | 74% | 26.7 | 1.06 | 0.02 | 0.0% |
| zone | look | 13.4 | 0.0 | 24% / 27 | 50% | 7.9 / 3.4 | 45% | 15.9 | 1.09 | 0.25 | 0.0% |
| zone | scan | 25.4 | 0.0 | 32% / 40 | 38% | 9.1 / 3.5 | 59% | 21.2 | 1.13 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.0 / 14 | 24, 5.8 / 15 | 46, 5.5 / 15 |
| cost | scan | 23, 4.3 / 15 | 24, 9.1 / 23 | 46, 7.9 / 21 |
| nearest | look | 23, 8.0 / 33 | 24, 11.1 / 34 | 46, 10.3 / 40 |
| nearest | scan | 23, 13.8 / 50 | 24, 23.4 / 55 | 46, 19.4 / 54 |
| round_robin | look | 23, 13.2 / 31 | 24, 13.8 / 32 | 46, 14.0 / 32 |
| round_robin | scan | 23, 20.1 / 47 | 24, 26.3 / 53 | 46, 25.1 / 50 |
| zone | look | 23, 12.4 / 34 | 24, 11.5 / 32 | 46, 14.6 / 39 |
| zone | scan | 23, 20.2 / 49 | 24, 29.7 / 54 | 46, 25.5 / 52 |

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

## quiet · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 28.4; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 19.3 ± 1.4 | -32.2% | [-9.92, -8.36] | 20/20 | 57% | better ✓ |
| nearest | 24.5 ± 2.2 | -13.7% | [-4.74, -2.99] | 20/20 | 24% | better ✓ |
| zone | 28.3 ± 2.7 | -0.2% | [-1.05, +0.83] | 8/20 | 0% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 19.3 | -11.6% | [-2.90, -2.11] | 20/20 | better ✓ |
| nearest | look | 24.5 | -30.2% | [-11.54, -9.70] | 20/20 | better ✓ |
| round_robin | look | 28.4 | -27.1% | [-11.44, -9.64] | 20/20 | better ✓ |
| zone | look | 28.3 | -30.7% | [-13.48, -11.57] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 19.3 | 5.6 | 16.7 | 24.6 | 6.9 | 0.50 |
| cost | scan | 21.8 | 7.9 | 22.8 | 36.6 | 9.4 | 0.50 |
| nearest | look | 24.5 | 10.7 | 43.6 | 55.9 | 12.1 | 0.37 |
| nearest | scan | 35.1 | 21.3 | 59.5 | 63.1 | 22.7 | 0.48 |
| round_robin | look | 28.4 | 14.9 | 35.6 | 48.5 | 16.0 | 0.63 |
| round_robin | scan | 38.9 | 25.3 | 53.9 | 59.4 | 26.6 | 0.69 |
| zone | look | 28.3 | 14.6 | 42.9 | 56.4 | 16.0 | 0.53 |
| zone | scan | 40.8 | 26.9 | 56.9 | 61.2 | 28.5 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.6 | 1.3 | 6% / 11 | 67% | 5.0 / 3.4 | 47% | 14.6 | 1.09 | 0.15 | 0.0% |
| cost | scan | 7.9 | 1.5 | 6% / 17 | 61% | 5.6 / 3.3 | 47% | 14.8 | 1.09 | 0.14 | 0.0% |
| nearest | look | 10.7 | 1.4 | 21% / 29 | 50% | 3.6 / 3.6 | 46% | 14.4 | 1.09 | 0.25 | 0.0% |
| nearest | scan | 21.3 | 1.5 | 28% / 46 | 37% | 3.5 / 3.5 | 59% | 19.4 | 1.10 | 0.21 | 0.0% |
| round_robin | look | 14.9 | 1.1 | 21% / 27 | 61% | 10.6 / 3.7 | 66% | 21.4 | 1.04 | 0.02 | 0.0% |
| round_robin | scan | 25.3 | 1.3 | 30% / 41 | 40% | 10.9 / 3.8 | 78% | 26.2 | 1.06 | 0.02 | 0.0% |
| zone | look | 14.6 | 1.4 | 25% / 30 | 47% | 7.9 / 3.4 | 49% | 15.4 | 1.10 | 0.25 | 0.0% |
| zone | scan | 26.9 | 1.6 | 32% / 42 | 34% | 9.2 / 3.5 | 62% | 20.7 | 1.14 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.5 / 15 | 24, 6.0 / 16 | 46, 5.9 / 16 |
| cost | scan | 23, 4.5 / 16 | 24, 9.7 / 25 | 46, 8.6 / 22 |
| nearest | look | 23, 8.3 / 36 | 24, 12.0 / 39 | 46, 11.1 / 40 |
| nearest | scan | 23, 16.6 / 57 | 24, 24.7 / 58 | 46, 21.6 / 59 |
| round_robin | look | 23, 14.3 / 33 | 24, 14.9 / 34 | 46, 15.1 / 36 |
| round_robin | scan | 23, 20.8 / 50 | 24, 27.9 / 55 | 46, 25.9 / 52 |
| zone | look | 23, 12.7 / 34 | 24, 12.6 / 37 | 46, 16.3 / 45 |
| zone | scan | 23, 22.3 / 52 | 24, 30.6 / 57 | 46, 27.1 / 56 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 30.7; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 21.2 ± 1.4 | -31.0% | [-10.36, -8.71] | 20/20 | 52% | better ✓ |
| nearest | 28.4 ± 2.6 | -7.7% | [-3.43, -1.35] | 17/20 | 13% | better ✓ |
| zone | 31.2 ± 2.7 | +1.5% | [-0.68, +1.47] | 8/20 | -3% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 21.2 | -15.5% | [-4.45, -3.33] | 20/20 | better ✓ |
| nearest | look | 28.4 | -25.1% | [-10.93, -8.16] | 20/20 | better ✓ |
| round_robin | look | 30.7 | -27.3% | [-12.57, -10.47] | 20/20 | better ✓ |
| zone | look | 31.2 | -29.3% | [-14.13, -11.66] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 21.2 | 6.4 | 18.5 | 27.2 | 8.9 | 0.51 |
| cost | scan | 25.1 | 9.8 | 29.4 | 47.9 | 12.7 | 0.48 |
| nearest | look | 28.4 | 13.1 | 50.3 | 63.9 | 16.0 | 0.38 |
| nearest | scan | 37.9 | 22.4 | 63.1 | 71.2 | 25.5 | 0.48 |
| round_robin | look | 30.7 | 16.1 | 39.7 | 52.6 | 18.4 | 0.62 |
| round_robin | scan | 42.3 | 27.3 | 57.5 | 63.6 | 29.9 | 0.69 |
| zone | look | 31.2 | 16.0 | 48.6 | 61.4 | 18.8 | 0.53 |
| zone | scan | 44.1 | 28.5 | 60.5 | 67.6 | 31.7 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.4 | 2.4 | 6% / 12 | 66% | 5.4 / 3.7 | 53% | 15.0 | 1.09 | 0.15 | 0.0% |
| cost | scan | 9.8 | 2.9 | 9% / 22 | 55% | 6.1 / 3.6 | 54% | 15.2 | 1.11 | 0.17 | 0.0% |
| nearest | look | 13.1 | 2.9 | 23% / 33 | 46% | 3.7 / 3.7 | 50% | 14.2 | 1.10 | 0.25 | 0.0% |
| nearest | scan | 22.4 | 3.1 | 27% / 48 | 33% | 3.6 / 3.6 | 61% | 18.2 | 1.12 | 0.24 | 0.0% |
| round_robin | look | 16.1 | 2.3 | 23% / 29 | 56% | 10.5 / 3.9 | 70% | 21.1 | 1.05 | 0.02 | 0.0% |
| round_robin | scan | 27.3 | 2.6 | 33% / 43 | 34% | 10.9 / 4.0 | 81% | 25.8 | 1.08 | 0.02 | 0.0% |
| zone | look | 16.0 | 2.8 | 25% / 33 | 44% | 8.0 / 3.6 | 52% | 15.0 | 1.10 | 0.25 | 0.0% |
| zone | scan | 28.5 | 3.2 | 34% / 45 | 31% | 9.2 / 3.7 | 65% | 20.2 | 1.15 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.6 / 16 | 24, 6.8 / 17 | 46, 7.0 / 19 |
| cost | scan | 23, 5.0 / 17 | 24, 12.9 / 35 | 46, 10.3 / 28 |
| nearest | look | 23, 7.7 / 34 | 24, 16.0 / 49 | 46, 14.0 / 49 |
| nearest | scan | 23, 16.2 / 58 | 24, 26.6 / 62 | 46, 23.0 / 63 |
| round_robin | look | 23, 14.6 / 35 | 24, 16.7 / 38 | 46, 16.4 / 40 |
| round_robin | scan | 23, 22.6 / 54 | 24, 30.3 / 58 | 46, 27.9 / 56 |
| zone | look | 23, 13.1 / 39 | 24, 14.3 / 41 | 46, 18.2 / 49 |
| zone | scan | 23, 22.4 / 54 | 24, 31.2 / 58 | 46, 29.9 / 61 |

## quiet · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 30.6; B0 floor = 12.4)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.9 ± 1.3 | -31.7% | [-10.48, -8.94] | 20/20 | 53% | better ✓ |
| nearest | 27.2 ± 2.4 | -11.1% | [-4.33, -2.57] | 20/20 | 19% | better ✓ |
| zone | 30.9 ± 2.7 | +1.1% | [-0.79, +1.42] | 7/20 | -2% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 20.9 | -12.9% | [-3.47, -2.72] | 20/20 | better ✓ |
| nearest | look | 27.2 | -27.2% | [-11.44, -8.90] | 20/20 | better ✓ |
| round_robin | look | 30.6 | -26.7% | [-12.16, -10.07] | 20/20 | better ✓ |
| zone | look | 30.9 | -30.3% | [-14.72, -12.28] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 20.9 | 6.1 | 18.0 | 25.4 | 8.6 | 0.52 |
| cost | scan | 24.0 | 8.8 | 25.7 | 37.4 | 11.7 | 0.51 |
| nearest | look | 27.2 | 12.1 | 48.4 | 63.0 | 14.9 | 0.36 |
| nearest | scan | 37.4 | 21.9 | 63.2 | 71.8 | 25.0 | 0.47 |
| round_robin | look | 30.6 | 16.0 | 39.6 | 53.5 | 18.3 | 0.62 |
| round_robin | scan | 41.8 | 26.8 | 57.0 | 63.5 | 29.4 | 0.69 |
| zone | look | 30.9 | 15.7 | 47.1 | 61.5 | 18.6 | 0.53 |
| zone | scan | 44.4 | 28.8 | 60.1 | 67.8 | 32.1 | 0.68 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.1 | 2.4 | 6% / 12 | 66% | 5.2 / 3.5 | 53% | 14.8 | 1.10 | 0.13 | 0.0% |
| cost | scan | 8.8 | 2.9 | 7% / 18 | 58% | 5.9 / 3.3 | 53% | 15.0 | 1.11 | 0.15 | 0.0% |
| nearest | look | 12.1 | 2.8 | 23% / 33 | 48% | 3.4 / 3.4 | 51% | 14.4 | 1.09 | 0.22 | 0.0% |
| nearest | scan | 21.9 | 3.2 | 28% / 49 | 34% | 3.5 / 3.5 | 61% | 18.3 | 1.12 | 0.24 | 0.0% |
| round_robin | look | 16.0 | 2.3 | 23% / 29 | 57% | 10.5 / 3.7 | 70% | 21.1 | 1.05 | 0.02 | 0.0% |
| round_robin | scan | 26.8 | 2.6 | 32% / 43 | 34% | 10.9 / 3.7 | 81% | 25.7 | 1.07 | 0.02 | 0.0% |
| zone | look | 15.7 | 2.9 | 25% / 33 | 45% | 8.0 / 3.4 | 52% | 14.9 | 1.11 | 0.25 | 0.0% |
| zone | scan | 28.8 | 3.2 | 34% / 45 | 31% | 9.2 / 3.5 | 66% | 20.3 | 1.15 | 0.25 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 4.5 / 16 | 24, 6.4 / 16 | 46, 6.6 / 17 |
| cost | scan | 23, 5.0 / 17 | 24, 10.7 / 27 | 46, 9.4 / 25 |
| nearest | look | 23, 7.9 / 32 | 24, 13.6 / 46 | 46, 12.9 / 47 |
| nearest | scan | 23, 17.6 / 59 | 24, 25.9 / 62 | 46, 21.3 / 62 |
| round_robin | look | 23, 14.8 / 35 | 24, 16.4 / 38 | 46, 16.3 / 40 |
| round_robin | scan | 23, 22.1 / 53 | 24, 29.2 / 56 | 46, 27.7 / 55 |
| zone | look | 23, 13.3 / 37 | 24, 14.3 / 42 | 46, 17.5 / 48 |
| zone | scan | 23, 23.6 / 56 | 24, 31.7 / 58 | 46, 29.8 / 60 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.0; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 22.0 ± 1.3 | -35.3% | [-12.87, -11.12] | 20/20 | 69% | better ✓ |
| nearest | 27.8 ± 2.6 | -18.0% | [-7.12, -5.09] | 20/20 | 35% | better ✓ |
| zone | 34.0 ± 3.3 | +0.0% | [-0.99, +0.93] | 9/20 | -0% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 22.0 | -10.9% | [-3.23, -2.16] | 19/20 | better ✓ |
| nearest | look | 27.8 | -31.3% | [-14.22, -11.12] | 20/20 | better ✓ |
| round_robin | look | 34.0 | -27.2% | [-13.30, -12.06] | 20/20 | better ✓ |
| zone | look | 34.0 | -30.8% | [-16.24, -13.91] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 22.0 | 5.4 | 17.5 | 30.1 | 5.4 | 0.43 |
| cost | scan | 24.7 | 8.1 | 26.6 | 51.0 | 8.1 | 0.43 |
| nearest | look | 27.8 | 11.3 | 50.7 | 69.0 | 11.3 | 0.31 |
| nearest | scan | 40.5 | 24.0 | 75.2 | 77.0 | 24.0 | 0.43 |
| round_robin | look | 34.0 | 17.4 | 40.9 | 59.6 | 17.4 | 0.63 |
| round_robin | scan | 46.7 | 30.1 | 69.3 | 75.9 | 30.1 | 0.65 |
| zone | look | 34.0 | 17.4 | 49.9 | 66.5 | 17.4 | 0.53 |
| zone | scan | 49.1 | 32.5 | 71.9 | 76.3 | 32.5 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.4 | 0.0 | 5% / 9 | 70% | 5.0 / 3.5 | 35% | 18.3 | 1.06 | 0.34 | 0.0% |
| cost | scan | 8.1 | 0.0 | 5% / 19 | 66% | 5.9 / 3.6 | 35% | 18.5 | 1.08 | 0.30 | 0.0% |
| nearest | look | 11.3 | 0.0 | 18% / 35 | 56% | 3.6 / 3.6 | 36% | 19.1 | 1.06 | 0.34 | 0.0% |
| nearest | scan | 24.0 | 0.0 | 24% / 60 | 47% | 3.8 / 3.8 | 47% | 25.8 | 1.08 | 0.32 | 0.0% |
| round_robin | look | 17.4 | 0.0 | 15% / 33 | 74% | 14.3 / 3.7 | 56% | 30.1 | 1.02 | 0.03 | 0.0% |
| round_robin | scan | 30.1 | 0.0 | 22% / 53 | 57% | 14.3 / 3.6 | 68% | 37.3 | 1.04 | 0.03 | 0.0% |
| zone | look | 17.4 | 0.0 | 25% / 36 | 53% | 10.7 / 3.5 | 39% | 21.2 | 1.07 | 0.36 | 0.0% |
| zone | scan | 32.5 | 0.0 | 28% / 55 | 42% | 11.9 / 3.3 | 53% | 29.3 | 1.10 | 0.36 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 4.0 / 15 | 22, 5.8 / 16 | 48, 5.9 / 17 |
| cost | scan | 25, 4.2 / 16 | 22, 10.8 / 29 | 48, 8.8 / 26 |
| nearest | look | 25, 6.9 / 34 | 22, 13.2 / 47 | 48, 12.4 / 49 |
| nearest | scan | 25, 16.2 / 67 | 22, 30.1 / 70 | 48, 24.6 / 75 |
| round_robin | look | 25, 16.6 / 40 | 22, 17.0 / 38 | 48, 17.9 / 40 |
| round_robin | scan | 25, 23.7 / 63 | 22, 33.9 / 69 | 48, 31.5 / 67 |
| zone | look | 25, 15.8 / 45 | 22, 13.7 / 40 | 48, 19.9 / 51 |
| zone | scan | 25, 23.3 / 67 | 22, 40.5 / 72 | 48, 33.7 / 69 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 34.1; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 21.6 ± 1.4 | -36.7% | [-13.37, -11.66] | 20/20 | 71% | better ✓ |
| nearest | 27.8 ± 2.9 | -18.5% | [-7.42, -5.18] | 19/20 | 36% | better ✓ |
| zone | 33.7 ± 3.1 | -1.2% | [-1.38, +0.57] | 10/20 | 2% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 21.6 | -9.4% | [-2.74, -1.77] | 19/20 | better ✓ |
| nearest | look | 27.8 | -31.2% | [-13.99, -11.24] | 20/20 | better ✓ |
| round_robin | look | 34.1 | -27.3% | [-13.61, -12.03] | 20/20 | better ✓ |
| zone | look | 33.7 | -31.6% | [-16.56, -14.55] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 21.6 | 5.0 | 16.0 | 25.6 | 5.0 | 0.46 |
| cost | scan | 23.8 | 7.3 | 22.0 | 33.2 | 7.3 | 0.49 |
| nearest | look | 27.8 | 11.3 | 49.7 | 68.8 | 11.3 | 0.31 |
| nearest | scan | 40.5 | 23.9 | 75.3 | 76.8 | 23.9 | 0.43 |
| round_robin | look | 34.1 | 17.6 | 40.7 | 60.5 | 17.6 | 0.64 |
| round_robin | scan | 47.0 | 30.4 | 69.0 | 76.0 | 30.4 | 0.67 |
| zone | look | 33.7 | 17.2 | 50.2 | 67.7 | 17.2 | 0.52 |
| zone | scan | 49.3 | 32.8 | 72.1 | 76.2 | 32.8 | 0.65 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.0 | 0.0 | 5% / 8 | 71% | 4.7 / 3.3 | 34% | 18.0 | 1.07 | 0.27 | 0.0% |
| cost | scan | 7.3 | 0.0 | 4% / 15 | 67% | 5.7 / 3.4 | 35% | 18.4 | 1.08 | 0.25 | 0.0% |
| nearest | look | 11.3 | 0.0 | 20% / 34 | 55% | 3.5 / 3.5 | 36% | 19.1 | 1.07 | 0.34 | 0.0% |
| nearest | scan | 23.9 | 0.0 | 23% / 60 | 45% | 3.6 / 3.6 | 48% | 26.2 | 1.08 | 0.27 | 0.0% |
| round_robin | look | 17.6 | 0.0 | 15% / 34 | 74% | 14.4 / 3.4 | 56% | 30.2 | 1.02 | 0.03 | 0.0% |
| round_robin | scan | 30.4 | 0.0 | 23% / 54 | 56% | 14.5 / 3.4 | 68% | 37.7 | 1.04 | 0.03 | 0.0% |
| zone | look | 17.2 | 0.0 | 25% / 36 | 53% | 10.4 / 3.0 | 39% | 21.0 | 1.07 | 0.36 | 0.0% |
| zone | scan | 32.8 | 0.0 | 29% / 55 | 41% | 11.7 / 3.0 | 53% | 29.4 | 1.10 | 0.36 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 5.4 / 18 | 22, 4.8 / 13 | 48, 4.9 / 14 |
| cost | scan | 25, 5.3 / 17 | 22, 7.8 / 20 | 48, 8.0 / 22 |
| nearest | look | 25, 11.6 / 46 | 22, 11.9 / 43 | 48, 10.8 / 47 |
| nearest | scan | 25, 19.2 / 73 | 22, 28.7 / 73 | 48, 23.8 / 74 |
| round_robin | look | 25, 18.2 / 40 | 22, 16.7 / 37 | 48, 17.7 / 39 |
| round_robin | scan | 25, 25.2 / 63 | 22, 33.0 / 68 | 48, 31.8 / 67 |
| zone | look | 25, 16.3 / 43 | 22, 13.0 / 40 | 48, 19.5 / 53 |
| zone | scan | 25, 23.8 / 66 | 22, 39.7 / 72 | 48, 34.2 / 70 |

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

## quiet · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 35.8; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.0 ± 1.5 | -35.8% | [-13.76, -11.77] | 20/20 | 67% | better ✓ |
| nearest | 30.5 ± 2.6 | -14.9% | [-6.46, -4.24] | 20/20 | 28% | better ✓ |
| zone | 36.1 ± 3.3 | +0.7% | [-0.85, +1.35] | 7/20 | -1% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 23.0 | -11.4% | [-3.55, -2.40] | 20/20 | better ✓ |
| nearest | look | 30.5 | -29.7% | [-14.08, -11.80] | 20/20 | better ✓ |
| round_robin | look | 35.8 | -27.3% | [-14.46, -12.39] | 20/20 | better ✓ |
| zone | look | 36.1 | -30.9% | [-17.40, -14.78] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.0 | 5.2 | 16.2 | 24.4 | 6.4 | 0.48 |
| cost | scan | 26.0 | 8.0 | 24.0 | 36.2 | 9.4 | 0.50 |
| nearest | look | 30.5 | 12.6 | 56.4 | 75.2 | 13.9 | 0.32 |
| nearest | scan | 43.3 | 25.3 | 78.5 | 82.4 | 26.8 | 0.44 |
| round_robin | look | 35.8 | 18.2 | 43.0 | 63.9 | 19.3 | 0.63 |
| round_robin | scan | 49.2 | 31.5 | 70.7 | 78.8 | 32.7 | 0.67 |
| zone | look | 36.1 | 18.2 | 54.9 | 70.9 | 19.5 | 0.51 |
| zone | scan | 52.2 | 34.1 | 75.0 | 80.7 | 35.7 | 0.65 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.2 | 1.3 | 5% / 10 | 71% | 4.6 / 3.2 | 38% | 18.0 | 1.08 | 0.23 | 0.0% |
| cost | scan | 8.0 | 1.4 | 4% / 19 | 64% | 5.9 / 3.4 | 38% | 18.5 | 1.10 | 0.24 | 0.0% |
| nearest | look | 12.6 | 1.3 | 21% / 38 | 53% | 3.6 / 3.6 | 40% | 19.2 | 1.08 | 0.29 | 0.0% |
| nearest | scan | 25.3 | 1.4 | 26% / 60 | 43% | 3.5 / 3.5 | 50% | 25.6 | 1.09 | 0.27 | 0.0% |
| round_robin | look | 18.2 | 1.1 | 16% / 34 | 71% | 14.3 / 3.4 | 60% | 30.1 | 1.02 | 0.03 | 0.0% |
| round_robin | scan | 31.5 | 1.2 | 25% / 55 | 52% | 14.4 / 3.4 | 71% | 37.3 | 1.05 | 0.03 | 0.0% |
| zone | look | 18.2 | 1.4 | 24% / 39 | 51% | 10.4 / 3.0 | 42% | 20.7 | 1.08 | 0.36 | 0.0% |
| zone | scan | 34.1 | 1.5 | 29% / 58 | 39% | 11.6 / 2.9 | 55% | 28.9 | 1.11 | 0.36 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 5.4 / 18 | 22, 5.3 / 14 | 48, 5.0 / 14 |
| cost | scan | 25, 5.9 / 18 | 22, 8.7 / 22 | 48, 8.5 / 25 |
| nearest | look | 25, 11.6 / 53 | 22, 13.3 / 43 | 48, 12.8 / 52 |
| nearest | scan | 25, 22.0 / 77 | 22, 28.7 / 77 | 48, 25.7 / 78 |
| round_robin | look | 25, 18.8 / 43 | 22, 17.4 / 40 | 48, 18.2 / 41 |
| round_robin | scan | 25, 26.3 / 64 | 22, 34.2 / 68 | 48, 32.7 / 69 |
| zone | look | 25, 17.4 / 47 | 22, 14.5 / 44 | 48, 20.3 / 55 |
| zone | scan | 25, 23.5 / 66 | 22, 41.1 / 73 | 48, 36.3 / 74 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 37.4; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.9 ± 1.4 | -33.3% | [-13.59, -11.26] | 20/20 | 60% | better ✓ |
| nearest | 33.4 ± 3.1 | -10.7% | [-5.48, -2.53] | 16/20 | 19% | better ✓ |
| zone | 38.9 ± 3.8 | +4.0% | [+0.62, +2.40] | 4/20 | -7% | worse ✗ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.9 | -12.2% | [-3.90, -2.99] | 20/20 | better ✓ |
| nearest | look | 33.4 | -28.8% | [-15.45, -11.69] | 20/20 | better ✓ |
| round_robin | look | 37.4 | -27.1% | [-14.68, -13.16] | 20/20 | better ✓ |
| zone | look | 38.9 | -29.7% | [-17.61, -14.98] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.9 | 6.0 | 18.7 | 32.1 | 8.4 | 0.45 |
| cost | scan | 28.4 | 9.1 | 29.1 | 57.2 | 11.8 | 0.43 |
| nearest | look | 33.4 | 14.0 | 59.7 | 81.3 | 16.8 | 0.32 |
| nearest | scan | 46.9 | 27.2 | 81.9 | 90.8 | 30.3 | 0.44 |
| round_robin | look | 37.4 | 18.7 | 44.6 | 64.9 | 20.8 | 0.62 |
| round_robin | scan | 51.3 | 32.3 | 73.1 | 80.6 | 34.7 | 0.66 |
| zone | look | 38.9 | 19.5 | 58.0 | 78.2 | 22.3 | 0.52 |
| zone | scan | 55.3 | 35.6 | 76.7 | 86.7 | 38.7 | 0.65 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.0 | 2.4 | 5% / 11 | 71% | 5.2 / 3.4 | 43% | 18.9 | 1.08 | 0.25 | 0.0% |
| cost | scan | 9.1 | 2.8 | 6% / 21 | 63% | 6.2 / 3.4 | 43% | 19.1 | 1.09 | 0.25 | 0.0% |
| nearest | look | 14.0 | 2.8 | 20% / 41 | 51% | 3.8 / 3.8 | 42% | 18.6 | 1.08 | 0.36 | 0.0% |
| nearest | scan | 27.2 | 3.1 | 27% / 63 | 39% | 3.8 / 3.8 | 52% | 25.1 | 1.10 | 0.30 | 0.0% |
| round_robin | look | 18.7 | 2.2 | 16% / 37 | 70% | 14.2 / 3.6 | 63% | 29.8 | 1.03 | 0.03 | 0.0% |
| round_robin | scan | 32.3 | 2.4 | 25% / 57 | 50% | 14.3 / 3.6 | 73% | 36.5 | 1.05 | 0.03 | 0.0% |
| zone | look | 19.5 | 2.8 | 24% / 42 | 49% | 10.8 / 3.5 | 45% | 20.4 | 1.08 | 0.36 | 0.0% |
| zone | scan | 35.6 | 3.1 | 28% / 60 | 37% | 12.1 / 3.3 | 57% | 28.2 | 1.12 | 0.36 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 4.3 / 17 | 22, 6.7 / 17 | 48, 6.5 / 18 |
| cost | scan | 25, 4.7 / 16 | 22, 11.5 / 33 | 48, 10.1 / 30 |
| nearest | look | 25, 8.6 / 41 | 22, 16.6 / 57 | 48, 15.4 / 59 |
| nearest | scan | 25, 15.9 / 68 | 22, 34.3 / 80 | 48, 29.8 / 83 |
| round_robin | look | 25, 17.8 / 45 | 22, 18.4 / 42 | 48, 19.1 / 42 |
| round_robin | scan | 25, 25.5 / 66 | 22, 35.9 / 72 | 48, 33.9 / 72 |
| zone | look | 25, 17.8 / 53 | 22, 15.9 / 46 | 48, 22.2 / 60 |
| zone | scan | 25, 25.3 / 72 | 22, 43.7 / 76 | 48, 37.0 / 76 |

## quiet · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.12 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 37.5; B0 floor = 16.6)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.6 ± 1.5 | -34.5% | [-14.01, -11.84] | 20/20 | 62% | better ✓ |
| nearest | 33.5 ± 3.0 | -10.7% | [-5.28, -2.70] | 18/20 | 19% | better ✓ |
| zone | 38.4 ± 3.5 | +2.3% | [-0.08, +1.81] | 7/20 | -4% | - |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.6 | -10.9% | [-3.52, -2.44] | 20/20 | better ✓ |
| nearest | look | 33.5 | -29.4% | [-15.43, -12.45] | 20/20 | better ✓ |
| round_robin | look | 37.5 | -27.1% | [-14.98, -12.95] | 20/20 | better ✓ |
| zone | look | 38.4 | -30.6% | [-18.19, -15.37] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.6 | 5.6 | 17.1 | 27.7 | 8.0 | 0.48 |
| cost | scan | 27.6 | 8.2 | 24.9 | 39.6 | 11.0 | 0.48 |
| nearest | look | 33.5 | 14.2 | 61.7 | 80.3 | 16.9 | 0.33 |
| nearest | scan | 47.4 | 27.9 | 82.6 | 88.5 | 30.9 | 0.45 |
| round_robin | look | 37.5 | 18.8 | 44.8 | 66.2 | 21.0 | 0.63 |
| round_robin | scan | 51.5 | 32.5 | 72.6 | 80.8 | 34.9 | 0.67 |
| zone | look | 38.4 | 19.1 | 57.3 | 75.6 | 21.8 | 0.51 |
| zone | scan | 55.3 | 35.6 | 77.6 | 88.3 | 38.8 | 0.65 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 5.6 | 2.4 | 4% / 10 | 72% | 4.9 / 3.2 | 42% | 18.6 | 1.09 | 0.23 | 0.0% |
| cost | scan | 8.2 | 2.8 | 5% / 20 | 64% | 5.9 / 3.3 | 42% | 18.8 | 1.10 | 0.23 | 0.0% |
| nearest | look | 14.2 | 2.7 | 21% / 41 | 50% | 3.5 / 3.5 | 42% | 19.0 | 1.08 | 0.33 | 0.0% |
| nearest | scan | 27.9 | 3.0 | 28% / 64 | 39% | 3.7 / 3.7 | 52% | 25.3 | 1.10 | 0.29 | 0.0% |
| round_robin | look | 18.8 | 2.2 | 16% / 37 | 70% | 14.3 / 3.4 | 63% | 29.9 | 1.03 | 0.03 | 0.0% |
| round_robin | scan | 32.5 | 2.4 | 25% / 57 | 49% | 14.5 / 3.4 | 74% | 36.8 | 1.05 | 0.03 | 0.0% |
| zone | look | 19.1 | 2.8 | 24% / 41 | 49% | 10.6 / 3.0 | 44% | 20.2 | 1.09 | 0.36 | 0.0% |
| zone | scan | 35.6 | 3.1 | 28% / 61 | 37% | 11.7 / 2.8 | 57% | 28.3 | 1.12 | 0.36 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 5.3 / 18 | 22, 5.8 / 14 | 48, 5.6 / 16 |
| cost | scan | 25, 5.6 / 18 | 22, 9.3 / 24 | 48, 8.9 / 26 |
| nearest | look | 25, 13.6 / 57 | 22, 15.7 / 55 | 48, 13.7 / 56 |
| nearest | scan | 25, 23.7 / 79 | 22, 33.2 / 81 | 48, 27.4 / 81 |
| round_robin | look | 25, 19.4 / 45 | 22, 18.0 / 42 | 48, 18.8 / 42 |
| round_robin | scan | 25, 28.0 / 67 | 22, 34.2 / 70 | 48, 33.9 / 71 |
| zone | look | 25, 18.0 / 50 | 22, 15.1 / 47 | 48, 21.6 / 60 |
| zone | scan | 25, 24.0 / 68 | 22, 43.7 / 77 | 48, 37.6 / 77 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.1; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.6 ± 1.0 | -35.3% | [-14.04, -12.87] | 20/20 | 56% | better ✓ |
| nearest | 37.5 ± 2.7 | -1.4% | [-1.50, +0.55] | 14/20 | 2% | - |
| zone | 30.8 ± 0.9 | -19.1% | [-7.71, -6.88] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.6 | -1.5% | [-0.60, -0.12] | 13/20 | - |
| nearest | look | 37.5 | -13.1% | [-6.64, -4.59] | 20/20 | better ✓ |
| round_robin | look | 38.1 | -10.4% | [-5.01, -3.74] | 20/20 | better ✓ |
| zone | look | 30.8 | -27.7% | [-12.36, -11.35] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.6 | 10.6 | 24.3 | 30.7 | 10.6 | 0.66 |
| cost | scan | 25.0 | 10.9 | 24.9 | 42.4 | 10.9 | 0.64 |
| nearest | look | 37.5 | 23.4 | 56.5 | 99.2 | 23.4 | 0.54 |
| nearest | scan | 43.2 | 29.1 | 58.9 | 107.0 | 29.1 | 0.58 |
| round_robin | look | 38.1 | 24.0 | 49.5 | 56.4 | 24.0 | 0.71 |
| round_robin | scan | 42.5 | 28.4 | 54.5 | 56.9 | 28.4 | 0.74 |
| zone | look | 30.8 | 16.7 | 45.7 | 67.7 | 16.7 | 0.57 |
| zone | scan | 42.6 | 28.5 | 56.0 | 89.4 | 28.5 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.6 | 0.0 | 6% / 14 | 17% | 10.1 / 4.8 | 68% | 7.4 | 1.64 | 0.15 | 0.0% |
| cost | scan | 10.9 | 0.0 | 3% / 21 | 19% | 10.3 / 4.8 | 67% | 7.3 | 1.65 | 0.15 | 0.0% |
| nearest | look | 23.4 | 0.0 | 42% / 41 | 8% | 5.0 / 5.0 | 75% | 8.5 | 1.61 | 0.27 | 5.4% |
| nearest | scan | 29.1 | 0.0 | 44% / 51 | 5% | 4.9 / 4.9 | 82% | 9.4 | 1.62 | 0.25 | 5.8% |
| round_robin | look | 24.0 | 0.0 | 49% / 36 | 2% | 11.5 / 4.3 | 97% | 10.9 | 1.51 | 0.01 | 0.0% |
| round_robin | scan | 28.4 | 0.0 | 49% / 42 | 2% | 13.3 / 8.7 | 98% | 11.0 | 1.56 | 0.01 | 0.0% |
| zone | look | 16.7 | 0.0 | 42% / 27 | 16% | 8.4 / 2.9 | 82% | 9.1 | 1.50 | 0.08 | 0.5% |
| zone | scan | 28.5 | 0.0 | 47% / 43 | 7% | 12.4 / 4.8 | 90% | 10.1 | 1.76 | 0.08 | 1.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 11.6 / 25 | 24, 7.4 / 18 | 46, 7.2 / 18 |
| cost | scan | 234, 11.7 / 25 | 24, 8.4 / 22 | 46, 8.2 / 21 |
| nearest | look | 234, 24.6 / 57 | 24, 19.4 / 52 | 46, 19.9 / 53 |
| nearest | scan | 234, 30.4 / 60 | 24, 25.3 / 55 | 46, 24.6 / 57 |
| round_robin | look | 234, 23.9 / 50 | 24, 24.2 / 47 | 46, 24.2 / 48 |
| round_robin | scan | 234, 28.3 / 54 | 24, 29.5 / 53 | 46, 28.3 / 54 |
| zone | look | 234, 15.9 / 45 | 24, 15.4 / 38 | 46, 21.2 / 50 |
| zone | scan | 234, 28.3 / 56 | 24, 28.5 / 54 | 46, 29.8 / 58 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.2; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 24.7 ± 1.0 | -35.2% | [-14.04, -12.83] | 20/20 | 56% | better ✓ |
| nearest | 38.3 ± 2.9 | +0.5% | [-1.13, +1.64] | 11/20 | -1% | - |
| zone | 30.8 ± 1.1 | -19.4% | [-7.80, -7.05] | 20/20 | 31% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 24.7 | +0.2% | [-0.20, +0.34] | 12/20 | - |
| nearest | look | 38.3 | -16.2% | [-9.17, -5.81] | 20/20 | better ✓ |
| round_robin | look | 38.2 | -10.6% | [-5.14, -3.85] | 20/20 | better ✓ |
| zone | look | 30.8 | -27.5% | [-12.20, -11.14] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 24.7 | 10.6 | 24.4 | 31.6 | 10.6 | 0.66 |
| cost | scan | 24.7 | 10.6 | 24.4 | 29.9 | 10.6 | 0.66 |
| nearest | look | 38.3 | 24.3 | 59.3 | 100.8 | 24.3 | 0.54 |
| nearest | scan | 45.8 | 31.7 | 70.1 | 121.2 | 31.7 | 0.58 |
| round_robin | look | 38.2 | 24.1 | 49.9 | 56.5 | 24.1 | 0.72 |
| round_robin | scan | 42.7 | 28.6 | 54.6 | 57.0 | 28.6 | 0.74 |
| zone | look | 30.8 | 16.7 | 45.5 | 73.2 | 16.7 | 0.57 |
| zone | scan | 42.4 | 28.4 | 55.5 | 85.2 | 28.4 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.6 | 0.0 | 6% / 15 | 17% | 10.2 / 4.8 | 67% | 7.4 | 1.65 | 0.16 | 0.0% |
| cost | scan | 10.6 | 0.0 | 2% / 13 | 18% | 10.2 / 4.8 | 66% | 7.2 | 1.66 | 0.14 | 0.0% |
| nearest | look | 24.3 | 0.0 | 44% / 41 | 7% | 4.9 / 4.9 | 77% | 8.7 | 1.59 | 0.27 | 6.1% |
| nearest | scan | 31.7 | 0.0 | 44% / 53 | 5% | 4.7 / 4.7 | 80% | 9.2 | 1.64 | 0.30 | 9.2% |
| round_robin | look | 24.1 | 0.0 | 49% / 36 | 2% | 11.7 / 4.4 | 97% | 10.9 | 1.51 | 0.01 | 0.0% |
| round_robin | scan | 28.6 | 0.0 | 50% / 42 | 2% | 13.1 / 4.7 | 97% | 11.0 | 1.57 | 0.01 | 0.0% |
| zone | look | 16.7 | 0.0 | 42% / 27 | 16% | 8.5 / 2.9 | 81% | 9.1 | 1.50 | 0.08 | 0.6% |
| zone | scan | 28.4 | 0.0 | 47% / 43 | 7% | 12.4 / 4.5 | 91% | 10.2 | 1.75 | 0.08 | 1.8% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 11.7 / 25 | 24, 7.0 / 18 | 46, 7.0 / 18 |
| cost | scan | 234, 11.4 / 25 | 24, 7.3 / 18 | 46, 8.2 / 21 |
| nearest | look | 234, 25.9 / 60 | 24, 18.5 / 50 | 46, 19.0 / 57 |
| nearest | scan | 234, 33.8 / 74 | 24, 26.4 / 56 | 46, 23.6 / 58 |
| round_robin | look | 234, 24.0 / 50 | 24, 23.4 / 47 | 46, 24.9 / 49 |
| round_robin | scan | 234, 28.6 / 55 | 24, 28.8 / 53 | 46, 28.5 / 55 |
| zone | look | 234, 15.8 / 44 | 24, 15.7 / 39 | 46, 21.8 / 51 |
| zone | scan | 234, 28.1 / 56 | 24, 29.6 / 53 | 46, 29.0 / 57 |

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

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 43.6; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.2 ± 1.4 | -35.3% | [-16.12, -14.65] | 20/20 | 52% | better ✓ |
| nearest | 51.1 ± 9.2 | +17.1% | [+3.71, +11.56] | 3/20 | -25% | worse ✗ |
| zone | 34.9 ± 1.2 | -20.1% | [-9.24, -8.22] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.2 | -2.6% | [-1.31, -0.21] | 14/20 | - |
| nearest | look | 51.1 | -7.9% | [-8.45, -0.17] | 16/20 | better ✓ |
| round_robin | look | 43.6 | -9.5% | [-5.12, -4.05] | 20/20 | better ✓ |
| zone | look | 34.9 | -28.8% | [-14.82, -13.40] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.2 | 11.1 | 25.6 | 35.4 | 14.1 | 0.64 |
| cost | scan | 29.0 | 11.7 | 26.5 | 36.5 | 14.9 | 0.65 |
| nearest | look | 51.1 | 33.8 | 89.4 | 145.1 | 37.0 | 0.54 |
| nearest | scan | 55.4 | 38.1 | 89.1 | 143.4 | 41.3 | 0.57 |
| round_robin | look | 43.6 | 26.9 | 55.1 | 64.2 | 29.5 | 0.72 |
| round_robin | scan | 48.2 | 31.3 | 60.5 | 69.2 | 34.1 | 0.73 |
| zone | look | 34.9 | 18.6 | 50.8 | 84.7 | 20.8 | 0.56 |
| zone | scan | 49.0 | 32.3 | 61.8 | 119.3 | 34.9 | 0.70 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.1 | 3.1 | 8% / 19 | 15% | 9.8 / 4.4 | 79% | 7.5 | 1.67 | 0.11 | 0.0% |
| cost | scan | 11.7 | 3.2 | 4% / 21 | 15% | 10.4 / 4.4 | 76% | 7.2 | 1.69 | 0.08 | 0.0% |
| nearest | look | 33.8 | 3.2 | 44% / 53 | 6% | 5.0 / 5.0 | 79% | 7.9 | 1.65 | 0.29 | 12.5% |
| nearest | scan | 38.1 | 3.2 | 45% / 61 | 4% | 4.6 / 4.6 | 86% | 8.7 | 1.66 | 0.24 | 12.3% |
| round_robin | look | 26.9 | 2.6 | 50% / 40 | 2% | 12.0 / 4.4 | 98% | 9.7 | 1.56 | 0.01 | 0.0% |
| round_robin | scan | 31.3 | 2.8 | 52% / 46 | 1% | 13.1 / 4.5 | 97% | 9.9 | 1.61 | 0.01 | 0.1% |
| zone | look | 18.6 | 2.1 | 42% / 31 | 13% | 8.7 / 2.7 | 85% | 8.3 | 1.56 | 0.08 | 0.8% |
| zone | scan | 32.3 | 2.6 | 49% / 47 | 5% | 12.3 / 4.5 | 92% | 9.4 | 1.84 | 0.08 | 2.8% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 11.8 / 26 | 24, 7.9 / 19 | 46, 9.2 / 26 |
| cost | scan | 234, 12.2 / 27 | 24, 9.0 / 21 | 46, 10.1 / 25 |
| nearest | look | 234, 36.4 / 92 | 24, 22.0 / 57 | 46, 26.2 / 71 |
| nearest | scan | 234, 40.9 / 90 | 24, 27.3 / 62 | 46, 29.3 / 72 |
| round_robin | look | 234, 26.8 / 55 | 24, 26.8 / 52 | 46, 28.0 / 55 |
| round_robin | scan | 234, 31.2 / 60 | 24, 32.9 / 60 | 46, 30.7 / 60 |
| zone | look | 234, 17.5 / 49 | 24, 18.7 / 46 | 46, 24.2 / 59 |
| zone | scan | 234, 31.8 / 62 | 24, 31.9 / 58 | 46, 35.0 / 76 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 50.7; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 33.3 ± 1.7 | -34.3% | [-18.28, -16.64] | 20/20 | 48% | better ✓ |
| nearest | 63.6 ± 12.1 | +25.6% | [+8.30, +18.24] | 2/20 | -35% | worse ✗ |
| zone | 40.3 ± 1.1 | -20.6% | [-11.07, -9.67] | 20/20 | 28% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 33.3 | -17.9% | [-9.67, -4.89] | 19/20 | better ✓ |
| nearest | look | 63.6 | -18.8% | [-24.21, -5.64] | 17/20 | better ✓ |
| round_robin | look | 50.7 | -9.1% | [-5.69, -4.55] | 20/20 | better ✓ |
| zone | look | 40.3 | -28.5% | [-16.76, -15.43] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 33.3 | 13.2 | 31.9 | 52.1 | 19.2 | 0.62 |
| cost | scan | 40.5 | 20.8 | 48.7 | 62.4 | 26.5 | 0.63 |
| nearest | look | 63.6 | 43.1 | 121.0 | 199.7 | 49.6 | 0.52 |
| nearest | scan | 78.4 | 57.6 | 156.8 | 235.1 | 64.3 | 0.55 |
| round_robin | look | 50.7 | 30.9 | 63.3 | 75.4 | 36.6 | 0.71 |
| round_robin | scan | 55.8 | 35.5 | 68.8 | 82.1 | 41.7 | 0.73 |
| zone | look | 40.3 | 21.7 | 58.2 | 147.2 | 26.2 | 0.53 |
| zone | scan | 56.3 | 36.8 | 73.2 | 176.1 | 42.3 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.2 | 6.0 | 12% / 26 | 11% | 10.2 / 4.4 | 89% | 7.5 | 1.71 | 0.08 | 0.0% |
| cost | scan | 20.8 | 5.7 | 24% / 39 | 7% | 12.2 / 6.8 | 92% | 8.0 | 1.79 | 0.09 | 0.0% |
| nearest | look | 43.1 | 6.5 | 44% / 66 | 5% | 4.8 / 4.8 | 83% | 7.4 | 1.67 | 0.25 | 16.1% |
| nearest | scan | 57.6 | 6.7 | 46% / 84 | 4% | 5.0 / 5.0 | 84% | 8.0 | 1.69 | 0.22 | 21.6% |
| round_robin | look | 30.9 | 5.7 | 50% / 46 | 2% | 11.9 / 4.2 | 98% | 8.7 | 1.60 | 0.01 | 0.2% |
| round_robin | scan | 35.5 | 6.2 | 53% / 51 | 2% | 13.2 / 7.8 | 98% | 8.7 | 1.65 | 0.01 | 0.3% |
| zone | look | 21.7 | 4.5 | 44% / 35 | 10% | 8.7 / 2.6 | 88% | 7.5 | 1.62 | 0.08 | 1.5% |
| zone | scan | 36.8 | 5.5 | 51% / 51 | 3% | 12.4 / 5.1 | 94% | 8.7 | 1.92 | 0.08 | 4.6% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 13.4 / 32 | 24, 11.1 / 26 | 46, 13.6 / 34 |
| cost | scan | 234, 20.4 / 47 | 24, 20.6 / 45 | 46, 22.2 / 51 |
| nearest | look | 234, 46.6 / 124 | 24, 29.0 / 68 | 46, 32.4 / 87 |
| nearest | scan | 234, 63.9 / 163 | 24, 34.3 / 73 | 46, 36.1 / 93 |
| round_robin | look | 234, 30.4 / 63 | 24, 33.1 / 62 | 46, 32.6 / 63 |
| round_robin | scan | 234, 35.4 / 68 | 24, 36.1 / 68 | 46, 35.7 / 68 |
| zone | look | 234, 20.0 / 56 | 24, 19.6 / 50 | 46, 31.2 / 81 |
| zone | scan | 234, 36.0 / 72 | 24, 34.2 / 63 | 46, 42.1 / 103 |

## morning_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 50.8; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.7 ± 1.7 | -35.6% | [-18.94, -17.27] | 20/20 | 49% | better ✓ |
| nearest | 64.4 ± 15.6 | +26.7% | [+7.76, +21.09] | 1/20 | -37% | worse ✗ |
| zone | 40.0 ± 1.7 | -21.3% | [-11.66, -9.95] | 20/20 | 29% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 32.7 | -5.0% | [-2.83, -0.68] | 15/20 | - |
| nearest | look | 64.4 | -18.7% | [-25.28, -4.85] | 16/20 | better ✓ |
| round_robin | look | 50.8 | -8.7% | [-5.31, -4.36] | 20/20 | better ✓ |
| zone | look | 40.0 | -29.2% | [-17.39, -15.53] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.7 | 12.6 | 30.7 | 56.5 | 18.6 | 0.61 |
| cost | scan | 34.4 | 14.1 | 35.3 | 49.0 | 20.4 | 0.62 |
| nearest | look | 64.4 | 43.7 | 115.7 | 232.3 | 50.3 | 0.53 |
| nearest | scan | 79.1 | 58.2 | 161.8 | 251.7 | 65.1 | 0.54 |
| round_robin | look | 50.8 | 31.0 | 63.2 | 74.6 | 36.7 | 0.72 |
| round_robin | scan | 55.6 | 35.4 | 68.8 | 86.0 | 41.5 | 0.73 |
| zone | look | 40.0 | 21.4 | 58.6 | 119.7 | 25.9 | 0.54 |
| zone | scan | 56.4 | 36.9 | 72.4 | 181.1 | 42.3 | 0.68 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.6 | 6.0 | 11% / 25 | 11% | 9.9 / 4.2 | 88% | 7.4 | 1.71 | 0.10 | 0.0% |
| cost | scan | 14.1 | 6.3 | 8% / 29 | 11% | 10.9 / 4.5 | 86% | 7.3 | 1.73 | 0.10 | 0.0% |
| nearest | look | 43.7 | 6.6 | 45% / 67 | 5% | 4.7 / 4.7 | 82% | 7.3 | 1.68 | 0.24 | 16.8% |
| nearest | scan | 58.2 | 6.8 | 46% / 84 | 4% | 4.7 / 4.7 | 81% | 7.9 | 1.69 | 0.29 | 23.5% |
| round_robin | look | 31.0 | 5.7 | 50% / 46 | 1% | 12.1 / 4.5 | 98% | 8.7 | 1.61 | 0.01 | 0.2% |
| round_robin | scan | 35.4 | 6.1 | 53% / 51 | 1% | 13.0 / 4.4 | 98% | 8.8 | 1.64 | 0.01 | 0.3% |
| zone | look | 21.4 | 4.5 | 43% / 34 | 10% | 8.7 / 2.6 | 88% | 7.6 | 1.62 | 0.08 | 1.5% |
| zone | scan | 36.9 | 5.4 | 50% / 52 | 3% | 12.5 / 4.3 | 94% | 8.7 | 1.92 | 0.08 | 4.4% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 234, 12.7 / 30 | 24, 11.2 / 27 | 46, 13.1 / 33 |
| cost | scan | 234, 14.0 / 35 | 24, 13.2 / 33 | 46, 14.8 / 37 |
| nearest | look | 234, 47.5 / 120 | 24, 28.6 / 69 | 46, 31.1 / 85 |
| nearest | scan | 234, 65.4 / 170 | 24, 31.2 / 72 | 46, 35.7 / 93 |
| round_robin | look | 234, 30.5 / 63 | 24, 32.7 / 61 | 46, 32.8 / 62 |
| round_robin | scan | 234, 35.3 / 68 | 24, 35.1 / 67 | 46, 36.0 / 68 |
| zone | look | 234, 19.7 / 56 | 24, 22.1 / 53 | 46, 29.4 / 77 |
| zone | scan | 234, 36.1 / 72 | 24, 35.4 / 64 | 46, 42.1 / 97 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 50.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 33.7 ± 2.0 | -33.8% | [-18.14, -16.28] | 20/20 | 54% | better ✓ |
| nearest | 54.9 ± 7.6 | +7.8% | [+1.18, +7.51] | 6/20 | -12% | - |
| zone | 40.9 ± 1.8 | -19.7% | [-10.81, -9.18] | 20/20 | 31% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 33.7 | -2.1% | [-1.24, -0.22] | 13/20 | - |
| nearest | look | 54.9 | -8.8% | [-8.83, -1.42] | 15/20 | - |
| round_robin | look | 50.9 | -9.9% | [-6.47, -4.69] | 20/20 | better ✓ |
| zone | look | 40.9 | -27.0% | [-15.79, -14.37] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 33.7 | 14.8 | 32.7 | 38.6 | 14.8 | 0.68 |
| cost | scan | 34.4 | 15.5 | 33.5 | 56.2 | 15.5 | 0.67 |
| nearest | look | 54.9 | 35.9 | 88.8 | 174.4 | 35.9 | 0.52 |
| nearest | scan | 60.2 | 41.2 | 89.7 | 151.6 | 41.2 | 0.56 |
| round_robin | look | 50.9 | 32.0 | 65.6 | 75.2 | 32.0 | 0.72 |
| round_robin | scan | 56.5 | 37.5 | 73.2 | 77.0 | 37.5 | 0.73 |
| zone | look | 40.9 | 21.9 | 59.6 | 107.0 | 21.9 | 0.56 |
| zone | scan | 56.0 | 37.0 | 74.7 | 137.2 | 37.0 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.8 | 0.0 | 5% / 18 | 17% | 14.3 / 5.6 | 56% | 8.9 | 1.66 | 0.29 | 0.0% |
| cost | scan | 15.5 | 0.0 | 2% / 26 | 17% | 14.8 / 5.6 | 54% | 8.6 | 1.67 | 0.29 | 0.0% |
| nearest | look | 35.9 | 0.0 | 42% / 61 | 9% | 5.4 / 5.4 | 67% | 11.3 | 1.59 | 0.39 | 10.2% |
| nearest | scan | 41.2 | 0.0 | 43% / 72 | 7% | 4.8 / 4.8 | 75% | 12.7 | 1.60 | 0.37 | 8.8% |
| round_robin | look | 32.0 | 0.0 | 49% / 47 | 3% | 15.6 / 4.2 | 96% | 15.8 | 1.47 | 0.01 | 0.0% |
| round_robin | scan | 37.5 | 0.0 | 48% / 57 | 3% | 17.7 / 7.8 | 96% | 16.0 | 1.52 | 0.01 | 0.0% |
| zone | look | 21.9 | 0.0 | 42% / 37 | 20% | 11.0 / 2.5 | 76% | 12.6 | 1.47 | 0.16 | 0.5% |
| zone | scan | 37.0 | 0.0 | 45% / 59 | 11% | 15.8 / 4.0 | 85% | 14.3 | 1.72 | 0.16 | 1.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 16.4 / 33 | 22, 8.4 / 20 | 48, 9.0 / 25 |
| cost | scan | 249, 16.9 / 34 | 22, 9.6 / 24 | 48, 10.4 / 28 |
| nearest | look | 249, 38.8 / 95 | 22, 25.4 / 67 | 48, 25.7 / 75 |
| nearest | scan | 249, 43.8 / 91 | 22, 32.6 / 74 | 48, 31.6 / 81 |
| round_robin | look | 249, 31.9 / 66 | 22, 31.4 / 61 | 48, 32.6 / 64 |
| round_robin | scan | 249, 37.5 / 73 | 22, 37.4 / 70 | 48, 38.1 / 72 |
| zone | look | 249, 21.0 / 58 | 22, 17.6 / 46 | 48, 28.8 / 69 |
| zone | scan | 249, 36.1 / 75 | 22, 38.6 / 71 | 48, 41.3 / 84 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 50.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 33.6 ± 1.8 | -34.0% | [-18.12, -16.41] | 20/20 | 54% | better ✓ |
| nearest | 53.8 ± 6.1 | +5.6% | [+0.25, +5.83] | 9/20 | -9% | - |
| zone | 40.5 ± 1.4 | -20.4% | [-11.30, -9.51] | 20/20 | 33% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 33.6 | -0.5% | [-0.57, +0.26] | 13/20 | - |
| nearest | look | 53.8 | -11.8% | [-9.89, -4.32] | 19/20 | better ✓ |
| round_robin | look | 50.9 | -10.3% | [-6.49, -5.18] | 20/20 | better ✓ |
| zone | look | 40.5 | -27.0% | [-15.56, -14.24] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 33.6 | 14.7 | 32.6 | 39.0 | 14.7 | 0.68 |
| cost | scan | 33.8 | 14.8 | 32.5 | 39.1 | 14.8 | 0.68 |
| nearest | look | 53.8 | 34.8 | 87.4 | 147.2 | 34.8 | 0.53 |
| nearest | scan | 60.9 | 42.0 | 84.7 | 168.1 | 42.0 | 0.55 |
| round_robin | look | 50.9 | 32.0 | 65.2 | 75.9 | 32.0 | 0.72 |
| round_robin | scan | 56.8 | 37.8 | 73.3 | 77.0 | 37.8 | 0.74 |
| zone | look | 40.5 | 21.6 | 59.6 | 101.6 | 21.6 | 0.56 |
| zone | scan | 55.4 | 36.5 | 74.9 | 137.9 | 36.5 | 0.67 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.7 | 0.0 | 4% / 17 | 17% | 14.3 / 5.5 | 55% | 8.7 | 1.68 | 0.23 | 0.0% |
| cost | scan | 14.8 | 0.0 | 1% / 16 | 17% | 14.5 / 5.5 | 53% | 8.5 | 1.68 | 0.25 | 0.0% |
| nearest | look | 34.8 | 0.0 | 42% / 59 | 8% | 5.2 / 5.2 | 66% | 11.1 | 1.60 | 0.39 | 9.8% |
| nearest | scan | 42.0 | 0.0 | 43% / 72 | 6% | 4.9 / 4.9 | 73% | 12.3 | 1.62 | 0.42 | 9.2% |
| round_robin | look | 32.0 | 0.0 | 49% / 47 | 3% | 15.7 / 4.1 | 96% | 15.8 | 1.47 | 0.01 | 0.0% |
| round_robin | scan | 37.8 | 0.0 | 49% / 57 | 3% | 18.1 / 4.3 | 96% | 16.0 | 1.52 | 0.01 | 0.0% |
| zone | look | 21.6 | 0.0 | 39% / 37 | 20% | 11.1 / 2.6 | 76% | 12.5 | 1.47 | 0.16 | 0.4% |
| zone | scan | 36.5 | 0.0 | 44% / 58 | 11% | 16.0 / 3.8 | 86% | 14.3 | 1.72 | 0.16 | 1.3% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 16.5 / 33 | 22, 7.9 / 19 | 48, 8.4 / 24 |
| cost | scan | 249, 16.4 / 33 | 22, 7.8 / 19 | 48, 9.7 / 27 |
| nearest | look | 249, 37.9 / 90 | 22, 21.5 / 65 | 48, 23.9 / 74 |
| nearest | scan | 249, 44.7 / 88 | 22, 32.2 / 75 | 48, 31.5 / 82 |
| round_robin | look | 249, 31.8 / 65 | 22, 31.9 / 60 | 48, 33.1 / 64 |
| round_robin | scan | 249, 37.9 / 73 | 22, 38.7 / 71 | 48, 37.5 / 72 |
| zone | look | 249, 20.7 / 58 | 22, 18.6 / 52 | 48, 27.6 / 67 |
| zone | scan | 249, 35.4 / 75 | 22, 38.1 / 72 | 48, 41.8 / 87 |

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

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 56.0; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.5 ± 1.8 | -34.8% | [-20.53, -18.44] | 20/20 | 53% | better ✓ |
| nearest | 70.3 ± 20.4 | +25.5% | [+7.12, +24.63] | 2/20 | -38% | worse ✗ |
| zone | 44.3 ± 1.8 | -20.9% | [-12.54, -10.86] | 20/20 | 32% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 36.5 | -1.9% | [-1.21, -0.28] | 15/20 | - |
| nearest | look | 70.3 | -10.1% | [-12.89, -2.53] | 14/20 | - |
| round_robin | look | 56.0 | -9.8% | [-6.69, -5.54] | 20/20 | better ✓ |
| zone | look | 44.3 | -27.6% | [-18.34, -15.63] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 36.5 | 14.2 | 32.7 | 41.1 | 17.6 | 0.66 |
| cost | scan | 37.3 | 14.7 | 33.0 | 40.9 | 18.3 | 0.67 |
| nearest | look | 70.3 | 48.1 | 130.0 | 223.2 | 51.3 | 0.52 |
| nearest | scan | 78.2 | 55.9 | 139.5 | 252.2 | 59.3 | 0.54 |
| round_robin | look | 56.0 | 34.7 | 71.3 | 82.5 | 37.1 | 0.72 |
| round_robin | scan | 62.1 | 40.5 | 78.5 | 84.8 | 43.2 | 0.73 |
| zone | look | 44.3 | 23.4 | 65.3 | 117.8 | 25.4 | 0.55 |
| zone | scan | 61.2 | 39.8 | 79.7 | 171.2 | 42.3 | 0.66 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.2 | 3.4 | 4% / 21 | 16% | 13.3 / 5.0 | 64% | 9.1 | 1.69 | 0.21 | 0.0% |
| cost | scan | 14.7 | 3.6 | 1% / 19 | 16% | 13.7 / 5.0 | 60% | 8.5 | 1.70 | 0.18 | 0.0% |
| nearest | look | 48.1 | 3.3 | 44% / 77 | 7% | 5.2 / 5.2 | 67% | 10.6 | 1.62 | 0.42 | 15.4% |
| nearest | scan | 55.9 | 3.3 | 44% / 89 | 5% | 4.5 / 4.5 | 74% | 12.0 | 1.63 | 0.38 | 16.4% |
| round_robin | look | 34.7 | 2.4 | 49% / 52 | 3% | 15.9 / 4.1 | 96% | 14.6 | 1.50 | 0.01 | 0.0% |
| round_robin | scan | 40.5 | 2.7 | 49% / 61 | 2% | 17.8 / 4.1 | 96% | 14.9 | 1.55 | 0.01 | 0.0% |
| zone | look | 23.4 | 2.0 | 40% / 40 | 18% | 11.3 / 2.3 | 80% | 11.8 | 1.52 | 0.16 | 0.6% |
| zone | scan | 39.8 | 2.4 | 45% / 62 | 8% | 16.0 / 3.7 | 88% | 13.7 | 1.79 | 0.16 | 1.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 15.6 / 33 | 22, 8.3 / 20 | 48, 9.4 / 26 |
| cost | scan | 249, 16.0 / 33 | 22, 8.3 / 20 | 48, 10.7 / 28 |
| nearest | look | 249, 52.6 / 133 | 22, 28.3 / 78 | 48, 32.3 / 96 |
| nearest | scan | 249, 60.6 / 141 | 22, 36.0 / 83 | 48, 38.9 / 110 |
| round_robin | look | 249, 34.2 / 71 | 22, 35.8 / 68 | 48, 36.6 / 72 |
| round_robin | scan | 249, 40.3 / 78 | 22, 41.6 / 74 | 48, 41.3 / 78 |
| zone | look | 249, 22.0 / 62 | 22, 21.0 / 56 | 48, 31.7 / 81 |
| zone | scan | 249, 38.2 / 79 | 22, 41.5 / 77 | 48, 47.6 / 106 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 61.7; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 39.4 ± 1.6 | -36.2% | [-23.17, -21.55] | 20/20 | 52% | better ✓ |
| nearest | 79.6 ± 22.3 | +29.0% | [+10.07, +28.60] | 1/20 | -42% | worse ✗ |
| zone | 48.8 ± 2.4 | -20.9% | [-13.75, -12.08] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 39.4 | -4.8% | [-3.41, -0.97] | 18/20 | better ✓ |
| nearest | look | 79.6 | -17.1% | [-22.76, -11.08] | 18/20 | better ✓ |
| round_robin | look | 61.7 | -9.2% | [-6.89, -5.59] | 20/20 | better ✓ |
| zone | look | 48.8 | -29.1% | [-21.62, -18.59] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 39.4 | 14.3 | 34.2 | 45.5 | 20.5 | 0.63 |
| cost | scan | 41.4 | 15.9 | 38.8 | 67.5 | 22.4 | 0.60 |
| nearest | look | 79.6 | 54.1 | 145.4 | 269.6 | 60.7 | 0.51 |
| nearest | scan | 96.0 | 70.2 | 196.6 | 323.8 | 77.1 | 0.52 |
| round_robin | look | 61.7 | 37.6 | 78.2 | 90.8 | 42.8 | 0.70 |
| round_robin | scan | 68.0 | 43.3 | 85.2 | 94.5 | 49.0 | 0.72 |
| zone | look | 48.8 | 25.8 | 71.1 | 151.0 | 29.9 | 0.53 |
| zone | scan | 68.9 | 44.9 | 87.3 | 262.9 | 49.9 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.3 | 6.2 | 5% / 24 | 16% | 12.7 / 4.5 | 76% | 9.9 | 1.68 | 0.13 | 0.0% |
| cost | scan | 15.9 | 6.5 | 5% / 38 | 15% | 13.2 / 5.0 | 74% | 9.5 | 1.70 | 0.17 | 0.0% |
| nearest | look | 54.1 | 6.6 | 42% / 84 | 8% | 4.9 / 4.9 | 71% | 10.2 | 1.63 | 0.36 | 17.9% |
| nearest | scan | 70.2 | 6.9 | 43% / 109 | 6% | 5.0 / 5.0 | 72% | 11.2 | 1.64 | 0.37 | 21.7% |
| round_robin | look | 37.6 | 5.2 | 50% / 57 | 3% | 15.7 / 3.9 | 96% | 13.5 | 1.52 | 0.01 | 0.0% |
| round_robin | scan | 43.3 | 5.7 | 52% / 64 | 2% | 17.7 / 9.2 | 97% | 13.7 | 1.57 | 0.01 | 0.0% |
| zone | look | 25.8 | 4.1 | 41% / 44 | 16% | 11.1 / 2.2 | 82% | 11.1 | 1.56 | 0.16 | 1.0% |
| zone | scan | 44.9 | 5.0 | 48% / 67 | 7% | 16.1 / 3.9 | 90% | 13.0 | 1.83 | 0.16 | 2.8% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 14.9 / 34 | 22, 10.5 / 24 | 48, 12.4 / 34 |
| cost | scan | 249, 16.3 / 38 | 22, 12.7 / 32 | 48, 15.1 / 41 |
| nearest | look | 249, 58.6 / 149 | 22, 33.9 / 85 | 48, 38.4 / 115 |
| nearest | scan | 249, 77.1 / 198 | 22, 42.1 / 93 | 48, 45.0 / 127 |
| round_robin | look | 249, 36.7 / 77 | 22, 40.5 / 74 | 48, 40.9 / 79 |
| round_robin | scan | 249, 43.0 / 85 | 22, 44.1 / 84 | 48, 44.7 / 86 |
| zone | look | 249, 24.0 / 69 | 22, 22.9 / 59 | 48, 36.6 / 93 |
| zone | scan | 249, 43.1 / 86 | 22, 42.0 / 79 | 48, 55.9 / 133 |

## morning_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 61.8; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 39.6 ± 1.6 | -36.0% | [-23.16, -21.29] | 20/20 | 52% | better ✓ |
| nearest | 79.6 ± 20.5 | +28.7% | [+9.69, +27.73] | 3/20 | -41% | worse ✗ |
| zone | 48.5 ± 2.6 | -21.6% | [-14.37, -12.30] | 20/20 | 31% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 39.6 | -0.9% | [-0.89, +0.20] | 16/20 | - |
| nearest | look | 79.6 | -10.8% | [-17.72, -1.52] | 14/20 | - |
| round_robin | look | 61.8 | -9.7% | [-7.15, -6.11] | 20/20 | better ✓ |
| zone | look | 48.5 | -29.0% | [-21.28, -18.30] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 39.6 | 14.3 | 33.7 | 46.2 | 20.6 | 0.64 |
| cost | scan | 39.9 | 14.2 | 33.2 | 46.9 | 21.0 | 0.65 |
| nearest | look | 79.6 | 54.0 | 145.5 | 252.5 | 60.6 | 0.51 |
| nearest | scan | 89.2 | 63.3 | 163.8 | 287.5 | 70.2 | 0.56 |
| round_robin | look | 61.8 | 37.7 | 77.9 | 90.4 | 42.9 | 0.71 |
| round_robin | scan | 68.4 | 43.8 | 85.4 | 95.0 | 49.5 | 0.73 |
| zone | look | 48.5 | 25.4 | 69.9 | 149.4 | 29.5 | 0.53 |
| zone | scan | 68.2 | 44.3 | 89.2 | 244.8 | 49.3 | 0.64 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.3 | 6.3 | 4% / 23 | 16% | 12.9 / 4.5 | 75% | 9.7 | 1.69 | 0.12 | 0.1% |
| cost | scan | 14.2 | 6.8 | 1% / 21 | 15% | 12.8 / 4.5 | 71% | 9.0 | 1.71 | 0.15 | 0.0% |
| nearest | look | 54.0 | 6.7 | 42% / 83 | 7% | 4.6 / 4.6 | 70% | 10.1 | 1.65 | 0.37 | 18.0% |
| nearest | scan | 63.3 | 6.9 | 45% / 98 | 5% | 4.7 / 4.7 | 75% | 11.3 | 1.64 | 0.33 | 19.6% |
| round_robin | look | 37.7 | 5.2 | 49% / 57 | 2% | 16.0 / 3.9 | 96% | 13.6 | 1.53 | 0.01 | 0.0% |
| round_robin | scan | 43.8 | 5.7 | 51% / 64 | 2% | 17.7 / 4.1 | 97% | 13.9 | 1.57 | 0.01 | 0.0% |
| zone | look | 25.4 | 4.2 | 40% / 44 | 16% | 11.3 / 2.2 | 82% | 11.1 | 1.55 | 0.16 | 0.8% |
| zone | scan | 44.3 | 5.0 | 46% / 67 | 7% | 16.5 / 3.6 | 90% | 13.1 | 1.84 | 0.16 | 3.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 249, 15.1 / 34 | 22, 9.4 / 22 | 48, 12.3 / 34 |
| cost | scan | 249, 14.9 / 33 | 22, 10.0 / 23 | 48, 12.7 / 34 |
| nearest | look | 249, 59.6 / 150 | 22, 29.7 / 81 | 48, 33.9 / 102 |
| nearest | scan | 249, 69.4 / 171 | 22, 39.3 / 91 | 48, 42.1 / 121 |
| round_robin | look | 249, 37.0 / 77 | 22, 40.3 / 73 | 48, 40.0 / 79 |
| round_robin | scan | 249, 43.6 / 85 | 22, 44.5 / 82 | 48, 44.3 / 84 |
| zone | look | 249, 23.4 / 67 | 22, 23.6 / 62 | 48, 36.4 / 95 |
| zone | scan | 249, 42.5 / 87 | 22, 41.2 / 80 | 48, 55.1 / 134 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 37.2; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 21.1 ± 0.7 | -43.3% | [-16.65, -15.53] | 20/20 | 70% | better ✓ |
| nearest | 32.6 ± 1.5 | -12.2% | [-5.27, -3.70] | 20/20 | 20% | better ✓ |
| zone | 30.2 ± 1.1 | -18.6% | [-7.47, -6.34] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 21.1 | -7.3% | [-1.87, -1.44] | 20/20 | better ✓ |
| nearest | look | 32.6 | -17.1% | [-7.43, -5.97] | 20/20 | better ✓ |
| round_robin | look | 37.2 | -11.9% | [-5.63, -4.45] | 20/20 | better ✓ |
| zone | look | 30.2 | -28.6% | [-12.48, -11.69] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 21.1 | 7.0 | 19.1 | 30.7 | 7.0 | 0.56 |
| cost | scan | 22.7 | 8.7 | 24.9 | 43.5 | 8.7 | 0.53 |
| nearest | look | 32.6 | 18.6 | 52.1 | 57.2 | 18.6 | 0.50 |
| nearest | scan | 39.4 | 25.3 | 56.5 | 59.3 | 25.3 | 0.56 |
| round_robin | look | 37.2 | 23.1 | 47.9 | 55.7 | 23.1 | 0.71 |
| round_robin | scan | 42.2 | 28.1 | 54.1 | 57.0 | 28.1 | 0.74 |
| zone | look | 30.2 | 16.2 | 44.3 | 55.6 | 16.2 | 0.57 |
| zone | scan | 42.3 | 28.3 | 54.6 | 57.1 | 28.3 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.0 | 0.0 | 13% / 12 | 21% | 5.8 / 3.3 | 83% | 9.8 | 1.44 | 0.09 | 0.0% |
| cost | scan | 8.7 | 0.0 | 9% / 17 | 25% | 6.6 / 3.4 | 78% | 9.2 | 1.47 | 0.13 | 0.0% |
| nearest | look | 18.6 | 0.0 | 39% / 36 | 12% | 3.7 / 3.7 | 85% | 10.3 | 1.44 | 0.16 | 0.0% |
| nearest | scan | 25.3 | 0.0 | 42% / 46 | 7% | 3.8 / 3.8 | 89% | 11.0 | 1.51 | 0.15 | 0.1% |
| round_robin | look | 23.1 | 0.0 | 48% / 33 | 4% | 10.6 / 4.1 | 96% | 11.7 | 1.45 | 0.01 | 0.0% |
| round_robin | scan | 28.1 | 0.0 | 49% / 40 | 3% | 11.7 / 6.2 | 97% | 11.8 | 1.51 | 0.01 | 0.0% |
| zone | look | 16.2 | 0.0 | 41% / 27 | 18% | 7.8 / 3.4 | 80% | 9.6 | 1.42 | 0.09 | 0.0% |
| zone | scan | 28.3 | 0.0 | 48% / 40 | 7% | 10.9 / 4.5 | 91% | 11.1 | 1.65 | 0.09 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 6.4 / 18 | 120, 7.5 / 20 | 46, 7.2 / 18 |
| cost | scan | 114, 7.0 / 20 | 120, 10.2 / 28 | 46, 8.7 / 22 |
| nearest | look | 114, 17.2 / 52 | 120, 19.6 / 51 | 46, 19.3 / 51 |
| nearest | scan | 114, 24.9 / 57 | 120, 26.7 / 56 | 46, 22.5 / 56 |
| round_robin | look | 114, 22.4 / 47 | 120, 23.3 / 48 | 46, 24.1 / 47 |
| round_robin | scan | 114, 27.8 / 54 | 120, 28.4 / 54 | 46, 28.2 / 53 |
| zone | look | 114, 15.0 / 43 | 120, 15.7 / 43 | 46, 20.0 / 46 |
| zone | scan | 114, 27.2 / 54 | 120, 29.0 / 54 | 46, 28.9 / 54 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 36.9; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 20.9 ± 1.0 | -43.2% | [-16.58, -15.30] | 20/20 | 70% | better ✓ |
| nearest | 32.8 ± 1.8 | -11.0% | [-4.85, -3.25] | 20/20 | 18% | better ✓ |
| zone | 30.4 ± 1.1 | -17.6% | [-7.04, -5.92] | 20/20 | 28% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 20.9 | -6.2% | [-1.60, -1.19] | 20/20 | better ✓ |
| nearest | look | 32.8 | -16.7% | [-7.15, -6.05] | 20/20 | better ✓ |
| round_robin | look | 36.9 | -12.5% | [-5.74, -4.84] | 20/20 | better ✓ |
| zone | look | 30.4 | -27.8% | [-12.28, -11.13] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 20.9 | 6.9 | 18.9 | 29.7 | 6.9 | 0.56 |
| cost | scan | 22.3 | 8.3 | 22.9 | 36.4 | 8.3 | 0.55 |
| nearest | look | 32.8 | 18.8 | 51.8 | 58.1 | 18.8 | 0.50 |
| nearest | scan | 39.4 | 25.3 | 56.7 | 63.5 | 25.3 | 0.55 |
| round_robin | look | 36.9 | 22.8 | 48.1 | 55.9 | 22.8 | 0.71 |
| round_robin | scan | 42.2 | 28.1 | 54.4 | 57.0 | 28.1 | 0.74 |
| zone | look | 30.4 | 16.3 | 44.3 | 56.4 | 16.3 | 0.57 |
| zone | scan | 42.1 | 28.0 | 54.4 | 59.6 | 28.0 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.9 | 0.0 | 13% / 11 | 22% | 5.7 / 3.3 | 83% | 9.7 | 1.44 | 0.10 | 0.0% |
| cost | scan | 8.3 | 0.0 | 9% / 16 | 25% | 6.5 / 3.3 | 78% | 9.3 | 1.47 | 0.14 | 0.0% |
| nearest | look | 18.8 | 0.0 | 40% / 36 | 12% | 3.7 / 3.7 | 86% | 10.4 | 1.44 | 0.14 | 0.0% |
| nearest | scan | 25.3 | 0.0 | 42% / 46 | 6% | 3.6 / 3.6 | 89% | 11.0 | 1.51 | 0.14 | 0.1% |
| round_robin | look | 22.8 | 0.0 | 47% / 33 | 4% | 10.5 / 3.9 | 96% | 11.7 | 1.45 | 0.01 | 0.0% |
| round_robin | scan | 28.1 | 0.0 | 49% / 40 | 3% | 11.6 / 3.8 | 97% | 11.9 | 1.51 | 0.01 | 0.0% |
| zone | look | 16.3 | 0.0 | 41% / 27 | 18% | 7.7 / 3.3 | 80% | 9.6 | 1.41 | 0.09 | 0.0% |
| zone | scan | 28.0 | 0.0 | 47% / 41 | 7% | 10.8 / 3.8 | 91% | 11.1 | 1.64 | 0.09 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 6.3 / 18 | 120, 7.3 / 19 | 46, 7.1 / 18 |
| cost | scan | 114, 7.0 / 21 | 120, 9.3 / 25 | 46, 8.7 / 21 |
| nearest | look | 114, 18.1 / 52 | 120, 18.9 / 50 | 46, 19.8 / 52 |
| nearest | scan | 114, 25.9 / 57 | 120, 25.4 / 56 | 46, 23.8 / 56 |
| round_robin | look | 114, 22.5 / 48 | 120, 22.8 / 47 | 46, 23.4 / 46 |
| round_robin | scan | 114, 27.9 / 54 | 120, 28.4 / 54 | 46, 27.7 / 53 |
| zone | look | 114, 15.0 / 42 | 120, 16.1 / 43 | 46, 20.3 / 47 |
| zone | scan | 114, 26.7 / 54 | 120, 29.2 / 54 | 46, 28.4 / 54 |

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

## lunch · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 42.5; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.0 ± 1.0 | -41.1% | [-17.96, -16.85] | 20/20 | 61% | better ✓ |
| nearest | 37.9 ± 2.0 | -10.8% | [-5.31, -3.92] | 20/20 | 16% | better ✓ |
| zone | 34.0 ± 1.5 | -20.1% | [-9.09, -7.93] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 25.0 | -7.5% | [-2.63, -1.47] | 19/20 | better ✓ |
| nearest | look | 37.9 | -16.9% | [-8.61, -6.75] | 20/20 | better ✓ |
| round_robin | look | 42.5 | -10.2% | [-5.36, -4.25] | 20/20 | better ✓ |
| zone | look | 34.0 | -28.0% | [-13.83, -12.59] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.0 | 8.9 | 23.5 | 37.6 | 11.0 | 0.57 |
| cost | scan | 27.1 | 10.7 | 29.4 | 43.2 | 13.0 | 0.56 |
| nearest | look | 37.9 | 21.6 | 59.8 | 76.7 | 23.8 | 0.50 |
| nearest | scan | 45.5 | 29.0 | 64.5 | 86.8 | 31.5 | 0.56 |
| round_robin | look | 42.5 | 26.4 | 54.3 | 63.8 | 28.4 | 0.72 |
| round_robin | scan | 47.3 | 31.0 | 59.8 | 66.2 | 33.2 | 0.73 |
| zone | look | 34.0 | 18.0 | 49.4 | 65.0 | 19.9 | 0.57 |
| zone | scan | 47.2 | 30.9 | 60.0 | 71.0 | 33.1 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.9 | 2.0 | 15% / 16 | 14% | 6.4 / 3.5 | 90% | 9.3 | 1.52 | 0.09 | 0.0% |
| cost | scan | 10.7 | 2.3 | 11% / 22 | 18% | 7.3 / 3.6 | 86% | 8.9 | 1.54 | 0.11 | 0.0% |
| nearest | look | 21.6 | 2.2 | 39% / 41 | 9% | 3.7 / 3.7 | 88% | 9.5 | 1.50 | 0.13 | 0.3% |
| nearest | scan | 29.0 | 2.4 | 43% / 52 | 5% | 3.7 / 3.7 | 92% | 10.1 | 1.56 | 0.16 | 0.3% |
| round_robin | look | 26.4 | 2.0 | 47% / 38 | 3% | 10.7 / 3.9 | 97% | 10.6 | 1.50 | 0.01 | 0.0% |
| round_robin | scan | 31.0 | 2.2 | 48% / 44 | 2% | 11.6 / 3.7 | 97% | 10.7 | 1.54 | 0.01 | 0.0% |
| zone | look | 18.0 | 1.9 | 39% / 30 | 15% | 8.0 / 3.2 | 84% | 8.9 | 1.47 | 0.09 | 0.0% |
| zone | scan | 30.9 | 2.3 | 47% / 45 | 5% | 10.7 / 4.0 | 93% | 10.2 | 1.70 | 0.09 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 8.0 / 22 | 120, 9.5 / 24 | 46, 9.5 / 23 |
| cost | scan | 114, 8.7 / 26 | 120, 12.0 / 31 | 46, 11.9 / 29 |
| nearest | look | 114, 20.4 / 60 | 120, 22.8 / 59 | 46, 21.5 / 59 |
| nearest | scan | 114, 27.5 / 65 | 120, 30.8 / 65 | 46, 28.1 / 64 |
| round_robin | look | 114, 25.6 / 54 | 120, 26.7 / 53 | 46, 27.6 / 53 |
| round_robin | scan | 114, 30.4 / 59 | 120, 31.5 / 60 | 46, 31.5 / 59 |
| zone | look | 114, 16.5 / 47 | 120, 17.7 / 48 | 46, 22.4 / 52 |
| zone | scan | 114, 29.6 / 59 | 120, 31.9 / 60 | 46, 31.3 / 60 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 48.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 30.3 ± 1.8 | -37.4% | [-18.76, -17.36] | 20/20 | 53% | better ✓ |
| nearest | 45.2 ± 2.7 | -6.6% | [-4.33, -2.01] | 18/20 | 9% | better ✓ |
| zone | 38.7 ± 1.4 | -20.0% | [-10.35, -9.04] | 20/20 | 28% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 30.3 | -21.9% | [-11.42, -5.82] | 18/20 | better ✓ |
| nearest | look | 45.2 | -13.6% | [-8.27, -5.82] | 20/20 | better ✓ |
| round_robin | look | 48.4 | -9.5% | [-5.95, -4.24] | 20/20 | better ✓ |
| zone | look | 38.7 | -27.0% | [-15.00, -13.63] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 30.3 | 12.0 | 31.4 | 53.4 | 16.2 | 0.57 |
| cost | scan | 38.8 | 20.3 | 49.1 | 62.9 | 24.8 | 0.61 |
| nearest | look | 45.2 | 26.3 | 70.8 | 99.0 | 31.1 | 0.51 |
| nearest | scan | 52.3 | 32.8 | 77.3 | 116.6 | 38.2 | 0.55 |
| round_robin | look | 48.4 | 30.0 | 62.0 | 73.7 | 34.3 | 0.71 |
| round_robin | scan | 53.5 | 34.7 | 67.6 | 77.8 | 39.4 | 0.73 |
| zone | look | 38.7 | 20.7 | 57.3 | 84.7 | 24.6 | 0.56 |
| zone | scan | 53.0 | 34.2 | 66.6 | 89.1 | 38.9 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 12.0 | 4.2 | 17% / 23 | 8% | 7.2 / 3.9 | 95% | 8.8 | 1.59 | 0.08 | 0.0% |
| cost | scan | 20.3 | 4.4 | 25% / 35 | 7% | 9.6 / 5.8 | 94% | 9.0 | 1.67 | 0.09 | 0.0% |
| nearest | look | 26.3 | 4.9 | 40% / 49 | 7% | 3.9 / 3.9 | 90% | 8.6 | 1.55 | 0.15 | 0.4% |
| nearest | scan | 32.8 | 5.4 | 40% / 60 | 5% | 4.1 / 4.1 | 91% | 8.9 | 1.60 | 0.18 | 0.7% |
| round_robin | look | 30.0 | 4.3 | 46% / 44 | 2% | 10.6 / 4.0 | 97% | 9.4 | 1.54 | 0.01 | 0.0% |
| round_robin | scan | 34.7 | 4.7 | 47% / 50 | 2% | 11.7 / 6.7 | 98% | 9.5 | 1.58 | 0.01 | 0.0% |
| zone | look | 20.7 | 4.0 | 39% / 35 | 12% | 8.0 / 3.2 | 87% | 8.0 | 1.53 | 0.09 | 0.1% |
| zone | scan | 34.2 | 4.8 | 45% / 50 | 4% | 10.8 / 4.3 | 94% | 9.4 | 1.76 | 0.09 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 10.1 / 29 | 120, 13.0 / 32 | 46, 14.5 / 36 |
| cost | scan | 114, 17.6 / 45 | 120, 22.4 / 51 | 46, 21.5 / 49 |
| nearest | look | 114, 22.1 / 70 | 120, 29.8 / 71 | 46, 27.1 / 70 |
| nearest | scan | 114, 29.8 / 77 | 120, 35.6 / 78 | 46, 32.5 / 76 |
| round_robin | look | 114, 28.8 / 61 | 120, 31.0 / 62 | 46, 30.1 / 62 |
| round_robin | scan | 114, 34.4 / 67 | 120, 34.7 / 68 | 46, 35.4 / 67 |
| zone | look | 114, 18.5 / 55 | 120, 20.7 / 56 | 46, 25.6 / 57 |
| zone | scan | 114, 32.6 / 65 | 120, 35.0 / 67 | 46, 35.9 / 67 |

## lunch · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 48.4; B0 floor = 14.1)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.6 ± 2.2 | -38.7% | [-19.65, -17.75] | 20/20 | 55% | better ✓ |
| nearest | 44.1 ± 1.4 | -8.8% | [-5.29, -3.29] | 20/20 | 12% | better ✓ |
| zone | 38.7 ± 1.6 | -19.9% | [-10.23, -8.99] | 20/20 | 28% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.6 | -16.4% | [-7.84, -3.94] | 18/20 | better ✓ |
| nearest | look | 44.1 | -14.0% | [-8.71, -5.72] | 20/20 | better ✓ |
| round_robin | look | 48.4 | -9.4% | [-5.66, -4.35] | 20/20 | better ✓ |
| zone | look | 38.7 | -27.0% | [-15.11, -13.57] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.6 | 11.4 | 29.7 | 49.8 | 15.6 | 0.57 |
| cost | scan | 35.5 | 16.9 | 44.9 | 59.0 | 21.4 | 0.57 |
| nearest | look | 44.1 | 25.2 | 69.5 | 100.3 | 30.0 | 0.50 |
| nearest | scan | 51.3 | 31.9 | 76.3 | 112.5 | 37.2 | 0.54 |
| round_robin | look | 48.4 | 29.9 | 62.0 | 74.7 | 34.3 | 0.71 |
| round_robin | scan | 53.4 | 34.6 | 67.6 | 77.7 | 39.3 | 0.73 |
| zone | look | 38.7 | 20.7 | 56.7 | 79.7 | 24.7 | 0.57 |
| zone | scan | 53.0 | 34.2 | 66.9 | 91.8 | 39.0 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.4 | 4.2 | 16% / 21 | 9% | 7.0 / 3.7 | 94% | 8.7 | 1.59 | 0.08 | 0.0% |
| cost | scan | 16.9 | 4.5 | 19% / 32 | 10% | 8.5 / 4.7 | 92% | 8.8 | 1.63 | 0.10 | 0.0% |
| nearest | look | 25.2 | 4.8 | 39% / 48 | 6% | 3.6 / 3.6 | 91% | 8.7 | 1.55 | 0.13 | 0.3% |
| nearest | scan | 31.9 | 5.3 | 40% / 58 | 5% | 4.2 / 4.2 | 92% | 9.0 | 1.60 | 0.19 | 0.9% |
| round_robin | look | 29.9 | 4.3 | 45% / 44 | 2% | 10.7 / 3.9 | 97% | 9.4 | 1.54 | 0.01 | 0.0% |
| round_robin | scan | 34.6 | 4.7 | 47% / 50 | 2% | 11.5 / 3.8 | 98% | 9.5 | 1.57 | 0.01 | 0.0% |
| zone | look | 20.7 | 4.0 | 39% / 35 | 12% | 8.0 / 3.2 | 87% | 8.0 | 1.53 | 0.09 | 0.1% |
| zone | scan | 34.2 | 4.8 | 46% / 49 | 4% | 10.9 / 3.9 | 94% | 9.4 | 1.76 | 0.09 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 114, 9.5 / 27 | 120, 12.3 / 31 | 46, 13.6 / 32 |
| cost | scan | 114, 14.3 / 42 | 120, 19.1 / 47 | 46, 17.5 / 43 |
| nearest | look | 114, 21.7 / 69 | 120, 28.2 / 70 | 46, 26.0 / 67 |
| nearest | scan | 114, 30.0 / 76 | 120, 34.0 / 76 | 46, 31.1 / 82 |
| round_robin | look | 114, 28.6 / 61 | 120, 30.8 / 62 | 46, 30.9 / 61 |
| round_robin | scan | 114, 33.9 / 67 | 120, 35.4 / 68 | 46, 33.9 / 67 |
| zone | look | 114, 18.3 / 54 | 120, 20.6 / 56 | 46, 26.7 / 60 |
| zone | scan | 114, 32.9 / 66 | 120, 35.6 / 67 | 46, 34.0 / 67 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.3; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.2 ± 0.7 | -48.9% | [-24.71, -23.39] | 20/20 | 79% | better ✓ |
| nearest | 41.9 ± 2.4 | -14.9% | [-8.15, -6.49] | 20/20 | 24% | better ✓ |
| zone | 39.4 ± 1.5 | -20.0% | [-10.33, -9.34] | 20/20 | 32% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 25.2 | -6.1% | [-1.91, -1.38] | 20/20 | better ✓ |
| nearest | look | 41.9 | -18.8% | [-10.78, -8.76] | 20/20 | better ✓ |
| round_robin | look | 49.3 | -13.9% | [-8.79, -7.21] | 20/20 | better ✓ |
| zone | look | 39.4 | -29.9% | [-17.61, -16.13] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.2 | 6.5 | 18.8 | 36.2 | 6.5 | 0.51 |
| cost | scan | 26.8 | 8.1 | 23.7 | 60.4 | 8.1 | 0.46 |
| nearest | look | 41.9 | 23.2 | 70.6 | 81.2 | 23.2 | 0.46 |
| nearest | scan | 51.7 | 32.9 | 76.7 | 82.3 | 32.9 | 0.52 |
| round_robin | look | 49.3 | 30.5 | 64.2 | 75.2 | 30.5 | 0.71 |
| round_robin | scan | 57.2 | 38.5 | 73.8 | 77.0 | 38.5 | 0.74 |
| zone | look | 39.4 | 20.7 | 58.6 | 74.8 | 20.7 | 0.55 |
| zone | scan | 56.3 | 37.5 | 73.5 | 78.7 | 37.5 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.5 | 0.0 | 9% / 11 | 28% | 5.7 / 3.2 | 76% | 13.2 | 1.40 | 0.16 | 0.0% |
| cost | scan | 8.1 | 0.0 | 5% / 20 | 30% | 6.4 / 3.2 | 71% | 12.4 | 1.43 | 0.16 | 0.0% |
| nearest | look | 23.2 | 0.0 | 36% / 48 | 15% | 3.6 / 3.6 | 80% | 14.6 | 1.39 | 0.17 | 0.1% |
| nearest | scan | 32.9 | 0.0 | 39% / 64 | 9% | 3.5 / 3.5 | 85% | 15.7 | 1.47 | 0.23 | 0.1% |
| round_robin | look | 30.5 | 0.0 | 47% / 45 | 6% | 14.1 / 3.9 | 95% | 17.1 | 1.40 | 0.01 | 0.0% |
| round_robin | scan | 38.5 | 0.0 | 49% / 54 | 3% | 15.8 / 7.0 | 95% | 17.6 | 1.46 | 0.01 | 0.0% |
| zone | look | 20.7 | 0.0 | 39% / 36 | 23% | 10.3 / 3.2 | 74% | 13.4 | 1.38 | 0.16 | 0.0% |
| zone | scan | 37.5 | 0.0 | 45% / 55 | 11% | 14.6 / 3.8 | 87% | 15.9 | 1.61 | 0.16 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 5.8 / 18 | 116, 6.7 / 19 | 48, 7.4 / 19 |
| cost | scan | 124, 6.4 / 19 | 116, 9.8 / 29 | 48, 8.3 / 22 |
| nearest | look | 124, 20.7 / 71 | 116, 24.5 / 69 | 48, 26.4 / 69 |
| nearest | scan | 124, 32.2 / 77 | 116, 34.8 / 76 | 48, 30.6 / 76 |
| round_robin | look | 124, 29.8 / 64 | 116, 30.9 / 64 | 48, 31.7 / 62 |
| round_robin | scan | 124, 37.7 / 73 | 116, 39.6 / 74 | 48, 38.0 / 73 |
| zone | look | 124, 19.7 / 58 | 116, 19.3 / 55 | 48, 26.5 / 61 |
| zone | scan | 124, 35.9 / 73 | 116, 39.6 / 74 | 48, 36.9 / 72 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.3; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 25.0 ± 0.8 | -49.3% | [-25.03, -23.58] | 20/20 | 79% | better ✓ |
| nearest | 41.8 ± 2.0 | -15.3% | [-8.25, -6.91] | 20/20 | 25% | better ✓ |
| zone | 39.2 ± 1.3 | -20.5% | [-10.64, -9.62] | 20/20 | 33% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 25.0 | -4.2% | [-1.34, -0.82] | 19/20 | better ✓ |
| nearest | look | 41.8 | -19.4% | [-11.53, -8.68] | 20/20 | better ✓ |
| round_robin | look | 49.3 | -14.1% | [-8.90, -7.30] | 20/20 | better ✓ |
| zone | look | 39.2 | -30.3% | [-17.65, -16.43] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 25.0 | 6.3 | 18.1 | 31.4 | 6.3 | 0.53 |
| cost | scan | 26.1 | 7.4 | 21.3 | 35.0 | 7.4 | 0.53 |
| nearest | look | 41.8 | 23.1 | 70.5 | 76.5 | 23.1 | 0.45 |
| nearest | scan | 51.8 | 33.1 | 76.6 | 80.1 | 33.1 | 0.52 |
| round_robin | look | 49.3 | 30.6 | 65.0 | 75.7 | 30.6 | 0.70 |
| round_robin | scan | 57.4 | 38.7 | 73.6 | 77.0 | 38.7 | 0.74 |
| zone | look | 39.2 | 20.5 | 58.8 | 75.2 | 20.5 | 0.54 |
| zone | scan | 56.3 | 37.6 | 73.8 | 80.9 | 37.6 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 6.3 | 0.0 | 9% / 10 | 28% | 5.6 / 3.0 | 76% | 13.2 | 1.40 | 0.14 | 0.0% |
| cost | scan | 7.4 | 0.0 | 5% / 15 | 30% | 6.3 / 3.1 | 72% | 12.5 | 1.44 | 0.14 | 0.0% |
| nearest | look | 23.1 | 0.0 | 37% / 47 | 16% | 3.5 / 3.5 | 81% | 14.7 | 1.39 | 0.18 | 0.0% |
| nearest | scan | 33.1 | 0.0 | 40% / 63 | 9% | 3.5 / 3.5 | 86% | 15.9 | 1.48 | 0.17 | 0.1% |
| round_robin | look | 30.6 | 0.0 | 47% / 45 | 5% | 14.0 / 3.7 | 95% | 17.1 | 1.40 | 0.01 | 0.0% |
| round_robin | scan | 38.7 | 0.0 | 50% / 55 | 3% | 15.5 / 3.7 | 96% | 17.6 | 1.46 | 0.01 | 0.0% |
| zone | look | 20.5 | 0.0 | 39% / 36 | 23% | 10.2 / 3.1 | 74% | 13.4 | 1.38 | 0.16 | 0.0% |
| zone | scan | 37.6 | 0.0 | 45% / 55 | 11% | 14.5 / 3.7 | 87% | 15.9 | 1.60 | 0.16 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 6.0 / 18 | 116, 6.3 / 17 | 48, 7.2 / 18 |
| cost | scan | 124, 6.4 / 19 | 116, 8.3 / 23 | 48, 8.0 / 22 |
| nearest | look | 124, 21.3 / 71 | 116, 24.7 / 70 | 48, 23.6 / 68 |
| nearest | scan | 124, 32.8 / 77 | 116, 34.2 / 76 | 48, 31.4 / 76 |
| round_robin | look | 124, 30.2 / 66 | 116, 30.6 / 63 | 48, 31.6 / 64 |
| round_robin | scan | 124, 38.3 / 73 | 116, 38.8 / 73 | 48, 40.0 / 73 |
| zone | look | 124, 19.3 / 55 | 116, 19.6 / 57 | 48, 26.2 / 62 |
| zone | scan | 124, 35.9 / 73 | 116, 39.2 / 73 | 48, 37.9 / 72 |

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

## lunch · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 54.0; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.0 ± 1.0 | -48.1% | [-26.52, -25.40] | 20/20 | 74% | better ✓ |
| nearest | 46.4 ± 2.5 | -14.1% | [-8.56, -6.56] | 20/20 | 22% | better ✓ |
| zone | 42.8 ± 1.8 | -20.8% | [-12.10, -10.30] | 20/20 | 32% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.0 | -3.9% | [-1.52, -0.78] | 19/20 | better ✓ |
| nearest | look | 46.4 | -17.8% | [-11.56, -8.46] | 20/20 | better ✓ |
| round_robin | look | 54.0 | -11.6% | [-7.93, -6.29] | 20/20 | better ✓ |
| zone | look | 42.8 | -29.2% | [-18.72, -16.42] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.0 | 7.4 | 20.8 | 36.5 | 9.3 | 0.53 |
| cost | scan | 29.2 | 8.3 | 23.1 | 39.1 | 10.4 | 0.54 |
| nearest | look | 46.4 | 25.6 | 77.1 | 86.2 | 27.7 | 0.45 |
| nearest | scan | 56.4 | 35.4 | 84.0 | 93.7 | 37.7 | 0.51 |
| round_robin | look | 54.0 | 33.4 | 69.9 | 81.5 | 35.3 | 0.71 |
| round_robin | scan | 61.1 | 40.3 | 78.4 | 84.6 | 42.4 | 0.73 |
| zone | look | 42.8 | 22.3 | 63.1 | 82.2 | 24.1 | 0.55 |
| zone | scan | 60.4 | 39.6 | 78.1 | 92.2 | 41.7 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 7.4 | 2.0 | 9% / 13 | 24% | 6.0 / 3.1 | 82% | 12.9 | 1.45 | 0.13 | 0.0% |
| cost | scan | 8.3 | 2.1 | 5% / 18 | 26% | 6.6 / 3.1 | 79% | 12.5 | 1.47 | 0.12 | 0.0% |
| nearest | look | 25.6 | 2.1 | 37% / 53 | 13% | 3.5 / 3.5 | 83% | 13.8 | 1.43 | 0.18 | 0.2% |
| nearest | scan | 35.4 | 2.3 | 40% / 69 | 8% | 3.3 / 3.3 | 87% | 14.8 | 1.50 | 0.23 | 0.2% |
| round_robin | look | 33.4 | 1.9 | 47% / 49 | 4% | 14.3 / 3.6 | 95% | 16.0 | 1.43 | 0.01 | 0.0% |
| round_robin | scan | 40.3 | 2.1 | 48% / 58 | 3% | 15.7 / 3.6 | 96% | 16.4 | 1.48 | 0.01 | 0.0% |
| zone | look | 22.3 | 1.7 | 39% / 39 | 21% | 10.3 / 3.0 | 77% | 12.6 | 1.41 | 0.16 | 0.0% |
| zone | scan | 39.6 | 2.1 | 44% / 59 | 8% | 14.3 / 3.5 | 88% | 15.1 | 1.66 | 0.16 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 6.8 / 20 | 116, 7.6 / 20 | 48, 8.2 / 22 |
| cost | scan | 124, 6.9 / 20 | 116, 9.4 / 24 | 48, 9.4 / 25 |
| nearest | look | 124, 23.4 / 78 | 116, 27.7 / 77 | 48, 26.3 / 74 |
| nearest | scan | 124, 33.7 / 84 | 116, 38.5 / 84 | 48, 32.0 / 84 |
| round_robin | look | 124, 32.8 / 69 | 116, 33.6 / 69 | 48, 34.7 / 69 |
| round_robin | scan | 124, 39.7 / 78 | 116, 41.1 / 78 | 48, 40.2 / 77 |
| zone | look | 124, 20.8 / 61 | 116, 21.5 / 61 | 48, 28.2 / 65 |
| zone | scan | 124, 37.1 / 77 | 116, 41.2 / 77 | 48, 41.9 / 78 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 59.6; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.0 ± 1.6 | -46.4% | [-28.49, -26.82] | 20/20 | 68% | better ✓ |
| nearest | 51.6 ± 3.0 | -13.4% | [-9.16, -6.88] | 20/20 | 20% | better ✓ |
| zone | 46.6 ± 1.6 | -21.8% | [-13.70, -12.21] | 20/20 | 32% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 32.0 | -12.4% | [-7.62, -2.58] | 18/20 | better ✓ |
| nearest | look | 51.6 | -18.1% | [-13.06, -9.73] | 20/20 | better ✓ |
| round_robin | look | 59.6 | -10.6% | [-7.95, -6.24] | 20/20 | better ✓ |
| zone | look | 46.6 | -29.7% | [-20.57, -18.82] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.0 | 9.4 | 26.2 | 45.8 | 13.2 | 0.54 |
| cost | scan | 36.5 | 13.5 | 38.7 | 71.2 | 17.8 | 0.50 |
| nearest | look | 51.6 | 28.5 | 85.6 | 109.7 | 32.9 | 0.45 |
| nearest | scan | 63.1 | 39.3 | 95.5 | 147.7 | 44.3 | 0.51 |
| round_robin | look | 59.6 | 37.0 | 76.2 | 88.7 | 40.9 | 0.71 |
| round_robin | scan | 66.7 | 43.7 | 84.2 | 94.2 | 48.0 | 0.73 |
| zone | look | 46.6 | 24.3 | 68.0 | 95.0 | 27.9 | 0.55 |
| zone | scan | 66.4 | 43.2 | 84.5 | 99.5 | 47.6 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.4 | 3.9 | 11% / 18 | 18% | 6.8 / 3.5 | 88% | 12.8 | 1.50 | 0.11 | 0.0% |
| cost | scan | 13.5 | 4.3 | 10% / 30 | 19% | 8.4 / 4.0 | 85% | 12.4 | 1.53 | 0.12 | 0.0% |
| nearest | look | 28.5 | 4.4 | 36% / 59 | 12% | 3.5 / 3.5 | 84% | 12.8 | 1.47 | 0.18 | 0.2% |
| nearest | scan | 39.3 | 5.0 | 39% / 75 | 8% | 4.0 / 4.0 | 87% | 13.7 | 1.53 | 0.23 | 1.0% |
| round_robin | look | 37.0 | 3.9 | 47% / 54 | 3% | 14.4 / 3.8 | 96% | 14.9 | 1.46 | 0.01 | 0.0% |
| round_robin | scan | 43.7 | 4.3 | 48% / 62 | 3% | 15.7 / 7.8 | 96% | 15.1 | 1.51 | 0.01 | 0.0% |
| zone | look | 24.3 | 3.6 | 38% / 43 | 19% | 10.4 / 3.1 | 79% | 11.9 | 1.45 | 0.16 | 0.1% |
| zone | scan | 43.2 | 4.4 | 45% / 63 | 7% | 14.5 / 4.3 | 90% | 14.4 | 1.70 | 0.16 | 0.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 7.8 / 24 | 116, 10.4 / 28 | 48, 11.1 / 27 |
| cost | scan | 124, 10.6 / 33 | 116, 16.3 / 43 | 48, 14.2 / 35 |
| nearest | look | 124, 22.8 / 84 | 116, 33.7 / 86 | 48, 30.8 / 84 |
| nearest | scan | 124, 35.3 / 96 | 116, 43.2 / 94 | 48, 40.1 / 100 |
| round_robin | look | 124, 35.7 / 76 | 116, 37.8 / 76 | 48, 38.2 / 75 |
| round_robin | scan | 124, 42.1 / 83 | 116, 44.5 / 84 | 48, 45.7 / 85 |
| zone | look | 124, 22.3 / 65 | 116, 23.4 / 66 | 48, 32.0 / 71 |
| zone | scan | 124, 41.3 / 83 | 116, 44.9 / 85 | 48, 44.5 / 83 |

## lunch · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.36 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 59.5; B0 floor = 18.7)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 31.4 ± 1.5 | -47.3% | [-29.00, -27.36] | 20/20 | 69% | better ✓ |
| nearest | 52.1 ± 3.2 | -12.6% | [-8.47, -6.30] | 19/20 | 18% | better ✓ |
| zone | 46.4 ± 1.9 | -22.1% | [-13.99, -12.37] | 20/20 | 32% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 31.4 | -6.4% | [-2.84, -1.50] | 19/20 | better ✓ |
| nearest | look | 52.1 | -16.7% | [-11.99, -8.74] | 20/20 | better ✓ |
| round_robin | look | 59.5 | -10.0% | [-7.66, -5.49] | 20/20 | better ✓ |
| zone | look | 46.4 | -30.0% | [-21.06, -18.71] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 31.4 | 8.9 | 25.1 | 41.7 | 12.7 | 0.54 |
| cost | scan | 33.5 | 10.6 | 30.8 | 48.7 | 14.8 | 0.52 |
| nearest | look | 52.1 | 28.9 | 86.1 | 103.5 | 33.3 | 0.46 |
| nearest | scan | 62.5 | 38.8 | 94.7 | 123.9 | 43.7 | 0.52 |
| round_robin | look | 59.5 | 36.9 | 75.5 | 87.9 | 40.8 | 0.72 |
| round_robin | scan | 66.1 | 43.1 | 84.1 | 93.6 | 47.4 | 0.73 |
| zone | look | 46.4 | 24.0 | 69.3 | 91.0 | 27.7 | 0.54 |
| zone | scan | 66.3 | 43.1 | 84.4 | 100.5 | 47.6 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 8.9 | 3.8 | 10% / 17 | 18% | 6.5 / 3.2 | 88% | 12.8 | 1.50 | 0.11 | 0.0% |
| cost | scan | 10.6 | 4.3 | 7% / 24 | 20% | 7.4 / 3.3 | 84% | 12.2 | 1.52 | 0.12 | 0.0% |
| nearest | look | 28.9 | 4.4 | 37% / 59 | 11% | 3.5 / 3.5 | 85% | 13.0 | 1.47 | 0.19 | 0.1% |
| nearest | scan | 38.8 | 4.9 | 39% / 74 | 7% | 3.7 / 3.7 | 87% | 13.8 | 1.54 | 0.20 | 0.7% |
| round_robin | look | 36.9 | 3.9 | 46% / 53 | 3% | 14.5 / 3.5 | 96% | 14.9 | 1.46 | 0.01 | 0.0% |
| round_robin | scan | 43.1 | 4.3 | 47% / 62 | 2% | 15.6 / 3.4 | 96% | 15.2 | 1.51 | 0.01 | 0.0% |
| zone | look | 24.0 | 3.6 | 38% / 43 | 19% | 10.2 / 2.8 | 80% | 11.8 | 1.45 | 0.16 | 0.0% |
| zone | scan | 43.1 | 4.4 | 45% / 63 | 7% | 14.5 / 3.5 | 90% | 14.4 | 1.69 | 0.16 | 0.0% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 124, 7.5 / 23 | 116, 9.8 / 26 | 48, 10.0 / 25 |
| cost | scan | 124, 8.5 / 27 | 116, 12.1 / 33 | 48, 12.0 / 31 |
| nearest | look | 124, 25.0 / 86 | 116, 32.9 / 85 | 48, 29.1 / 82 |
| nearest | scan | 124, 37.5 / 95 | 116, 40.8 / 93 | 48, 37.1 / 93 |
| round_robin | look | 124, 35.5 / 75 | 116, 37.6 / 74 | 48, 38.7 / 76 |
| round_robin | scan | 124, 42.1 / 84 | 116, 43.8 / 84 | 48, 44.2 / 84 |
| zone | look | 124, 22.2 / 64 | 116, 23.3 / 67 | 48, 30.6 / 73 |
| zone | scan | 124, 41.1 / 83 | 116, 44.8 / 84 | 48, 44.1 / 84 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.4; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.8 ± 1.1 | -38.0% | [-15.06, -14.07] | 20/20 | 60% | better ✓ |
| nearest | 39.3 ± 4.5 | +2.2% | [-0.90, +2.92] | 12/20 | -3% | - |
| zone | 31.3 ± 1.6 | -18.5% | [-7.59, -6.66] | 20/20 | 29% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 23.8 | -25.6% | [-8.84, -7.61] | 20/20 | better ✓ |
| nearest | look | 39.3 | -9.0% | [-5.61, -1.91] | 16/20 | better ✓ |
| round_robin | look | 38.4 | -10.6% | [-5.17, -3.95] | 20/20 | better ✓ |
| zone | look | 31.3 | -29.8% | [-13.87, -12.73] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.8 | 9.6 | 26.5 | 42.1 | 9.6 | 0.57 |
| cost | scan | 32.0 | 17.8 | 41.7 | 54.1 | 17.8 | 0.64 |
| nearest | look | 39.3 | 25.0 | 71.8 | 187.7 | 25.0 | 0.44 |
| nearest | scan | 43.2 | 28.9 | 61.3 | 143.3 | 28.9 | 0.57 |
| round_robin | look | 38.4 | 24.2 | 48.8 | 56.0 | 24.2 | 0.73 |
| round_robin | scan | 43.0 | 28.7 | 54.5 | 62.2 | 28.7 | 0.75 |
| zone | look | 31.3 | 17.1 | 45.2 | 76.5 | 17.1 | 0.58 |
| zone | scan | 44.6 | 30.4 | 55.6 | 116.8 | 30.4 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.6 | 0.0 | 20% / 14 | 19% | 7.0 / 3.9 | 84% | 9.0 | 1.49 | 0.11 | 0.3% |
| cost | scan | 17.8 | 0.0 | 25% / 25 | 19% | 8.4 / 3.7 | 63% | 6.8 | 1.63 | 0.29 | 0.0% |
| nearest | look | 25.0 | 0.0 | 40% / 39 | 12% | 4.3 / 4.3 | 72% | 7.9 | 1.55 | 0.31 | 6.4% |
| nearest | scan | 28.9 | 0.0 | 43% / 44 | 6% | 3.1 / 3.1 | 88% | 9.8 | 1.60 | 0.16 | 2.6% |
| round_robin | look | 24.2 | 0.0 | 50% / 33 | 4% | 9.7 / 3.9 | 96% | 10.6 | 1.52 | 0.00 | 0.0% |
| round_robin | scan | 28.7 | 0.0 | 49% / 38 | 3% | 10.2 / 6.0 | 97% | 10.6 | 1.59 | 0.00 | 0.1% |
| zone | look | 17.1 | 0.0 | 42% / 27 | 16% | 7.8 / 4.5 | 82% | 8.9 | 1.52 | 0.10 | 0.5% |
| zone | scan | 30.4 | 0.0 | 47% / 40 | 5% | 9.8 / 4.2 | 93% | 10.2 | 1.84 | 0.10 | 1.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 3.5 / 14 | 242, 10.0 / 27 | 46, 10.1 / 26 |
| cost | scan | 23, 1.4 / 7 | 242, 20.6 / 43 | 46, 10.8 / 29 |
| nearest | look | 23, 4.9 / 26 | 242, 27.4 / 81 | 46, 21.9 / 55 |
| nearest | scan | 23, 20.6 / 55 | 242, 30.9 / 62 | 46, 22.3 / 56 |
| round_robin | look | 23, 22.6 / 46 | 242, 24.2 / 49 | 46, 25.0 / 48 |
| round_robin | scan | 23, 27.6 / 51 | 242, 28.9 / 55 | 46, 28.2 / 54 |
| zone | look | 23, 13.3 / 37 | 242, 16.6 / 44 | 46, 21.5 / 48 |
| zone | scan | 23, 26.6 / 52 | 242, 30.8 / 56 | 46, 29.8 / 54 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 38.3; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 23.6 ± 1.0 | -38.2% | [-15.11, -14.09] | 20/20 | 61% | better ✓ |
| nearest | 37.6 ± 5.1 | -1.7% | [-2.63, +2.18] | 15/20 | 3% | - |
| zone | 31.3 ± 1.4 | -18.2% | [-7.48, -6.51] | 20/20 | 29% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 23.6 | -24.1% | [-8.16, -6.93] | 20/20 | better ✓ |
| nearest | look | 37.6 | -11.1% | [-6.60, -2.07] | 18/20 | better ✓ |
| round_robin | look | 38.3 | -10.4% | [-5.00, -3.93] | 20/20 | better ✓ |
| zone | look | 31.3 | -28.9% | [-13.29, -12.24] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 23.6 | 9.4 | 26.2 | 40.4 | 9.4 | 0.56 |
| cost | scan | 31.2 | 16.9 | 40.5 | 54.5 | 16.9 | 0.62 |
| nearest | look | 37.6 | 23.3 | 70.0 | 159.2 | 23.3 | 0.46 |
| nearest | scan | 42.3 | 28.0 | 58.4 | 138.3 | 28.0 | 0.56 |
| round_robin | look | 38.3 | 24.0 | 48.5 | 58.6 | 24.0 | 0.73 |
| round_robin | scan | 42.7 | 28.5 | 54.6 | 58.2 | 28.5 | 0.74 |
| zone | look | 31.3 | 17.0 | 45.2 | 75.2 | 17.0 | 0.58 |
| zone | scan | 44.0 | 29.8 | 55.5 | 110.5 | 29.8 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.4 | 0.0 | 20% / 14 | 19% | 6.9 / 3.7 | 84% | 9.0 | 1.49 | 0.12 | 0.3% |
| cost | scan | 16.9 | 0.0 | 24% / 24 | 19% | 8.3 / 3.6 | 64% | 6.9 | 1.63 | 0.27 | 0.0% |
| nearest | look | 23.3 | 0.0 | 39% / 38 | 13% | 4.1 / 4.1 | 74% | 8.2 | 1.53 | 0.22 | 5.2% |
| nearest | scan | 28.0 | 0.0 | 42% / 44 | 6% | 3.0 / 3.0 | 88% | 9.8 | 1.61 | 0.15 | 2.4% |
| round_robin | look | 24.0 | 0.0 | 50% / 33 | 4% | 9.7 / 3.6 | 96% | 10.5 | 1.52 | 0.00 | 0.0% |
| round_robin | scan | 28.5 | 0.0 | 49% / 38 | 3% | 10.1 / 3.2 | 96% | 10.6 | 1.57 | 0.00 | 0.0% |
| zone | look | 17.0 | 0.0 | 43% / 26 | 16% | 7.8 / 4.4 | 82% | 8.9 | 1.52 | 0.10 | 0.4% |
| zone | scan | 29.8 | 0.0 | 46% / 40 | 6% | 9.6 / 3.4 | 92% | 10.2 | 1.84 | 0.10 | 1.6% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 3.5 / 13 | 242, 9.8 / 26 | 46, 10.1 / 26 |
| cost | scan | 23, 1.2 / 7 | 242, 19.5 / 42 | 46, 10.7 / 28 |
| nearest | look | 23, 5.6 / 29 | 242, 25.4 / 74 | 46, 21.0 / 53 |
| nearest | scan | 23, 18.6 / 55 | 242, 29.7 / 59 | 46, 23.7 / 56 |
| round_robin | look | 23, 22.4 / 46 | 242, 23.9 / 49 | 46, 25.2 / 47 |
| round_robin | scan | 23, 29.1 / 53 | 242, 28.4 / 55 | 46, 28.3 / 53 |
| zone | look | 23, 14.0 / 38 | 242, 16.5 / 44 | 46, 21.5 / 47 |
| zone | scan | 23, 26.1 / 52 | 242, 30.4 / 56 | 46, 28.3 / 54 |

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

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 44.6; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.3 ± 1.1 | -36.7% | [-16.82, -15.85] | 20/20 | 54% | better ✓ |
| nearest | 44.9 ± 5.9 | +0.7% | [-1.66, +3.03] | 12/20 | -1% | - |
| zone | 35.9 ± 1.7 | -19.5% | [-9.17, -8.23] | 20/20 | 29% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.3 | -21.3% | [-8.23, -7.08] | 20/20 | better ✓ |
| nearest | look | 44.9 | -14.2% | [-11.05, -3.74] | 18/20 | better ✓ |
| round_robin | look | 44.6 | -8.8% | [-4.88, -3.74] | 20/20 | better ✓ |
| zone | look | 35.9 | -29.2% | [-15.56, -14.05] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.3 | 11.6 | 30.5 | 50.4 | 14.0 | 0.58 |
| cost | scan | 35.9 | 18.2 | 44.0 | 62.9 | 21.6 | 0.62 |
| nearest | look | 44.9 | 27.8 | 76.0 | 211.9 | 30.7 | 0.46 |
| nearest | scan | 52.4 | 35.0 | 80.1 | 274.4 | 38.1 | 0.48 |
| round_robin | look | 44.6 | 27.7 | 55.7 | 68.3 | 30.4 | 0.73 |
| round_robin | scan | 48.9 | 31.7 | 61.1 | 82.3 | 34.7 | 0.73 |
| zone | look | 35.9 | 19.5 | 51.9 | 104.9 | 21.7 | 0.56 |
| zone | scan | 50.7 | 33.8 | 63.0 | 158.4 | 36.4 | 0.68 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.6 | 2.4 | 23% / 19 | 13% | 7.1 / 3.8 | 92% | 8.7 | 1.57 | 0.08 | 0.3% |
| cost | scan | 18.2 | 3.4 | 23% / 28 | 15% | 8.4 / 3.5 | 75% | 7.0 | 1.70 | 0.14 | 0.0% |
| nearest | look | 27.8 | 2.9 | 41% / 45 | 10% | 3.8 / 3.8 | 81% | 7.8 | 1.57 | 0.18 | 5.1% |
| nearest | scan | 35.0 | 3.1 | 43% / 54 | 5% | 3.2 / 3.2 | 90% | 9.0 | 1.67 | 0.19 | 4.7% |
| round_robin | look | 27.7 | 2.7 | 49% / 38 | 3% | 9.8 / 3.6 | 97% | 9.4 | 1.57 | 0.00 | 0.1% |
| round_robin | scan | 31.7 | 2.9 | 48% / 44 | 2% | 10.0 / 3.2 | 97% | 9.6 | 1.61 | 0.00 | 0.3% |
| zone | look | 19.5 | 2.2 | 41% / 30 | 13% | 7.6 / 4.2 | 85% | 8.1 | 1.59 | 0.10 | 0.9% |
| zone | scan | 33.8 | 2.7 | 46% / 45 | 4% | 9.3 / 3.3 | 93% | 9.4 | 1.92 | 0.10 | 2.9% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 5.9 / 19 | 242, 11.9 / 30 | 46, 13.1 / 32 |
| cost | scan | 23, 3.6 / 15 | 242, 20.7 / 46 | 46, 12.2 / 31 |
| nearest | look | 23, 8.1 / 37 | 242, 30.1 / 83 | 46, 25.2 / 65 |
| nearest | scan | 23, 25.3 / 64 | 242, 37.2 / 89 | 46, 27.9 / 65 |
| round_robin | look | 23, 25.1 / 52 | 242, 27.7 / 56 | 46, 28.4 / 53 |
| round_robin | scan | 23, 30.0 / 57 | 242, 31.6 / 61 | 46, 33.0 / 61 |
| zone | look | 23, 16.6 / 43 | 242, 18.9 / 51 | 46, 23.9 / 54 |
| zone | scan | 23, 28.8 / 56 | 242, 34.5 / 65 | 46, 32.3 / 60 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.0; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 34.4 ± 1.5 | -33.9% | [-18.47, -16.74] | 20/20 | 47% | better ✓ |
| nearest | 60.2 ± 8.9 | +15.9% | [+4.94, +12.27] | 3/20 | -22% | worse ✗ |
| zone | 41.7 ± 2.5 | -19.8% | [-11.32, -9.26] | 20/20 | 27% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 34.4 | -19.3% | [-9.82, -6.69] | 20/20 | better ✓ |
| nearest | look | 60.2 | -8.6% | [-9.79, -1.19] | 15/20 | - |
| round_robin | look | 52.0 | -9.0% | [-5.79, -4.43] | 20/20 | better ✓ |
| zone | look | 41.7 | -29.7% | [-19.10, -16.35] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 34.4 | 15.2 | 38.4 | 59.0 | 20.1 | 0.60 |
| cost | scan | 42.6 | 22.1 | 50.7 | 73.2 | 28.3 | 0.65 |
| nearest | look | 60.2 | 39.7 | 129.7 | 353.6 | 46.0 | 0.40 |
| nearest | scan | 65.9 | 45.1 | 127.2 | 362.4 | 51.6 | 0.45 |
| round_robin | look | 52.0 | 31.7 | 64.6 | 108.0 | 37.7 | 0.71 |
| round_robin | scan | 57.1 | 36.4 | 70.3 | 121.3 | 42.8 | 0.72 |
| zone | look | 41.7 | 22.9 | 60.8 | 149.1 | 27.4 | 0.53 |
| zone | scan | 59.3 | 39.6 | 81.4 | 228.6 | 45.0 | 0.63 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 15.2 | 4.9 | 27% / 25 | 6% | 7.8 / 4.1 | 96% | 8.1 | 1.69 | 0.06 | 0.6% |
| cost | scan | 22.1 | 6.2 | 26% / 34 | 8% | 9.2 / 4.4 | 88% | 7.4 | 1.82 | 0.06 | 0.1% |
| nearest | look | 39.7 | 6.2 | 40% / 61 | 8% | 4.1 / 4.1 | 83% | 6.9 | 1.66 | 0.24 | 10.0% |
| nearest | scan | 45.1 | 6.6 | 42% / 66 | 3% | 3.7 / 3.7 | 91% | 8.2 | 1.73 | 0.17 | 8.0% |
| round_robin | look | 31.7 | 6.0 | 46% / 45 | 2% | 9.9 / 3.9 | 97% | 8.4 | 1.63 | 0.00 | 0.5% |
| round_robin | scan | 36.4 | 6.4 | 46% / 51 | 1% | 10.2 / 5.7 | 97% | 8.5 | 1.66 | 0.00 | 1.1% |
| zone | look | 22.9 | 4.5 | 40% / 35 | 11% | 7.4 / 4.1 | 88% | 7.3 | 1.67 | 0.10 | 1.7% |
| zone | scan | 39.6 | 5.4 | 46% / 52 | 3% | 9.3 / 4.3 | 95% | 8.7 | 2.01 | 0.10 | 5.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 8.9 / 24 | 242, 15.6 / 38 | 46, 16.6 / 38 |
| cost | scan | 23, 10.1 / 32 | 242, 23.9 / 52 | 46, 18.4 / 45 |
| nearest | look | 23, 10.7 / 49 | 242, 43.7 / 149 | 46, 32.8 / 92 |
| nearest | scan | 23, 26.1 / 71 | 242, 48.8 / 147 | 46, 34.2 / 79 |
| round_robin | look | 23, 28.7 / 60 | 242, 32.0 / 65 | 46, 31.5 / 62 |
| round_robin | scan | 23, 33.0 / 63 | 242, 36.9 / 71 | 46, 35.2 / 67 |
| zone | look | 23, 18.1 / 51 | 242, 22.3 / 61 | 46, 27.9 / 63 |
| zone | scan | 23, 32.6 / 63 | 242, 40.6 / 86 | 46, 37.9 / 75 |

## evening_rush · 30 floors x 4 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 52.0; B0 floor = 14.3)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 33.8 ± 1.8 | -35.0% | [-18.92, -17.53] | 20/20 | 48% | better ✓ |
| nearest | 54.7 ± 5.3 | +5.1% | [+0.71, +5.04] | 5/20 | -7% | - |
| zone | 41.6 ± 2.8 | -20.0% | [-11.47, -9.33] | 20/20 | 28% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 33.8 | -16.6% | [-7.68, -5.74] | 20/20 | better ✓ |
| nearest | look | 54.7 | -15.8% | [-13.15, -7.57] | 19/20 | better ✓ |
| round_robin | look | 52.0 | -9.0% | [-5.75, -4.63] | 20/20 | better ✓ |
| zone | look | 41.6 | -29.6% | [-19.05, -16.24] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 33.8 | 14.6 | 37.2 | 59.1 | 19.5 | 0.60 |
| cost | scan | 40.5 | 19.8 | 47.3 | 68.8 | 26.3 | 0.64 |
| nearest | look | 54.7 | 34.3 | 93.2 | 276.1 | 40.4 | 0.44 |
| nearest | scan | 64.9 | 44.2 | 125.9 | 342.6 | 50.7 | 0.46 |
| round_robin | look | 52.0 | 31.8 | 65.0 | 99.8 | 37.8 | 0.71 |
| round_robin | scan | 57.2 | 36.6 | 70.0 | 127.2 | 42.9 | 0.72 |
| zone | look | 41.6 | 22.8 | 60.7 | 147.4 | 27.4 | 0.53 |
| zone | scan | 59.1 | 39.5 | 80.1 | 217.1 | 44.9 | 0.63 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 14.6 | 5.0 | 26% / 24 | 7% | 7.4 / 3.8 | 96% | 8.0 | 1.67 | 0.06 | 0.3% |
| cost | scan | 19.8 | 6.5 | 22% / 31 | 10% | 8.7 / 3.6 | 87% | 7.2 | 1.78 | 0.08 | 0.1% |
| nearest | look | 34.3 | 6.1 | 42% / 54 | 7% | 3.8 / 3.8 | 85% | 7.2 | 1.64 | 0.18 | 6.5% |
| nearest | scan | 44.2 | 6.5 | 43% / 65 | 4% | 3.4 / 3.4 | 91% | 8.2 | 1.72 | 0.18 | 7.4% |
| round_robin | look | 31.8 | 6.0 | 46% / 45 | 2% | 9.8 / 3.5 | 97% | 8.4 | 1.62 | 0.00 | 0.5% |
| round_robin | scan | 36.6 | 6.3 | 48% / 50 | 1% | 10.2 / 3.3 | 97% | 8.5 | 1.66 | 0.00 | 0.9% |
| zone | look | 22.8 | 4.6 | 41% / 36 | 11% | 7.3 / 4.0 | 88% | 7.3 | 1.66 | 0.10 | 1.7% |
| zone | scan | 39.5 | 5.4 | 45% / 52 | 3% | 9.2 / 3.5 | 95% | 8.7 | 2.00 | 0.10 | 5.2% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 23, 9.1 / 25 | 242, 14.8 / 37 | 46, 16.2 / 38 |
| cost | scan | 23, 7.4 / 26 | 242, 21.7 / 49 | 46, 15.9 / 39 |
| nearest | look | 23, 12.5 / 56 | 242, 37.3 / 106 | 46, 29.0 / 72 |
| nearest | scan | 23, 26.9 / 69 | 242, 47.7 / 145 | 46, 34.3 / 76 |
| round_robin | look | 23, 28.6 / 59 | 242, 31.9 / 65 | 46, 32.9 / 64 |
| round_robin | scan | 23, 33.6 / 64 | 242, 37.1 / 70 | 46, 35.0 / 68 |
| zone | look | 23, 17.9 / 49 | 242, 22.2 / 60 | 46, 28.2 / 65 |
| zone | scan | 23, 34.2 / 62 | 242, 40.4 / 85 | 46, 37.3 / 74 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.9; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 29.1 ± 0.8 | -41.7% | [-21.44, -20.17] | 20/20 | 67% | better ✓ |
| nearest | 51.7 ± 8.2 | +3.6% | [-1.02, +5.94] | 10/20 | -6% | - |
| zone | 40.4 ± 1.7 | -18.9% | [-10.14, -8.67] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 29.1 | -33.4% | [-15.97, -13.03] | 20/20 | better ✓ |
| nearest | look | 51.7 | -8.1% | [-7.65, -0.70] | 17/20 | better ✓ |
| round_robin | look | 49.9 | -12.6% | [-7.91, -6.48] | 20/20 | better ✓ |
| zone | look | 40.4 | -31.1% | [-19.13, -17.47] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 29.1 | 10.2 | 30.5 | 45.9 | 10.2 | 0.52 |
| cost | scan | 43.6 | 24.7 | 58.2 | 73.0 | 24.7 | 0.62 |
| nearest | look | 51.7 | 32.8 | 100.2 | 266.2 | 32.8 | 0.43 |
| nearest | scan | 56.3 | 37.4 | 77.2 | 198.4 | 37.4 | 0.54 |
| round_robin | look | 49.9 | 31.0 | 64.2 | 75.0 | 31.0 | 0.72 |
| round_robin | scan | 57.1 | 38.2 | 73.5 | 77.0 | 38.2 | 0.74 |
| zone | look | 40.4 | 21.6 | 58.9 | 79.3 | 21.6 | 0.58 |
| zone | scan | 58.7 | 39.9 | 74.1 | 112.8 | 39.9 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 10.2 | 0.0 | 12% / 12 | 28% | 8.3 / 4.2 | 73% | 12.1 | 1.42 | 0.19 | 0.1% |
| cost | scan | 24.7 | 0.0 | 26% / 36 | 20% | 10.4 / 4.2 | 53% | 8.8 | 1.59 | 0.49 | 0.0% |
| nearest | look | 32.8 | 0.0 | 38% / 54 | 15% | 4.6 / 4.6 | 63% | 10.8 | 1.48 | 0.43 | 6.0% |
| nearest | scan | 37.4 | 0.0 | 40% / 59 | 8% | 3.1 / 3.1 | 83% | 14.4 | 1.54 | 0.24 | 2.3% |
| round_robin | look | 31.0 | 0.0 | 48% / 42 | 6% | 13.3 / 3.8 | 95% | 16.0 | 1.44 | 0.01 | 0.0% |
| round_robin | scan | 38.2 | 0.0 | 48% / 52 | 4% | 13.5 / 6.6 | 96% | 16.5 | 1.51 | 0.01 | 0.0% |
| zone | look | 21.6 | 0.0 | 40% / 36 | 21% | 10.6 / 4.7 | 76% | 12.9 | 1.44 | 0.15 | 0.1% |
| zone | scan | 39.9 | 0.0 | 47% / 52 | 8% | 13.3 / 3.8 | 90% | 15.4 | 1.79 | 0.15 | 0.7% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 1.2 / 7 | 236, 11.0 / 31 | 48, 10.9 / 29 |
| cost | scan | 25, 0.3 / 1 | 236, 29.6 / 61 | 48, 12.8 / 38 |
| nearest | look | 25, 4.2 / 27 | 236, 36.7 / 110 | 48, 28.4 / 73 |
| nearest | scan | 25, 19.4 / 72 | 236, 40.7 / 81 | 48, 29.8 / 76 |
| round_robin | look | 25, 28.9 / 61 | 236, 31.1 / 64 | 48, 31.8 / 62 |
| round_robin | scan | 25, 35.6 / 70 | 236, 38.4 / 73 | 48, 38.4 / 73 |
| zone | look | 25, 20.5 / 53 | 236, 20.7 / 58 | 48, 26.8 / 60 |
| zone | scan | 25, 35.9 / 70 | 236, 40.9 / 74 | 48, 37.2 / 72 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 0 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 49.5; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 28.8 ± 0.7 | -41.9% | [-21.20, -20.24] | 20/20 | 68% | better ✓ |
| nearest | 47.3 ± 3.1 | -4.3% | [-3.59, -0.64] | 15/20 | 7% | - |
| zone | 40.1 ± 1.3 | -18.9% | [-9.81, -8.89] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 28.8 | -31.1% | [-14.24, -11.57] | 20/20 | better ✓ |
| nearest | look | 47.3 | -12.5% | [-8.25, -5.20] | 19/20 | better ✓ |
| round_robin | look | 49.5 | -13.7% | [-8.63, -7.10] | 20/20 | better ✓ |
| zone | look | 40.1 | -32.3% | [-19.74, -18.56] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 28.8 | 9.9 | 29.8 | 45.9 | 9.9 | 0.52 |
| cost | scan | 41.7 | 22.8 | 55.8 | 72.2 | 22.8 | 0.60 |
| nearest | look | 47.3 | 28.5 | 77.1 | 208.9 | 28.5 | 0.45 |
| nearest | scan | 54.1 | 35.2 | 76.9 | 143.2 | 35.2 | 0.56 |
| round_robin | look | 49.5 | 30.6 | 64.2 | 75.2 | 30.6 | 0.72 |
| round_robin | scan | 57.3 | 38.5 | 73.8 | 77.0 | 38.5 | 0.74 |
| zone | look | 40.1 | 21.3 | 58.4 | 83.8 | 21.3 | 0.57 |
| zone | scan | 59.3 | 40.4 | 74.3 | 112.5 | 40.4 | 0.74 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 9.9 | 0.0 | 12% / 12 | 29% | 8.0 / 4.0 | 73% | 12.1 | 1.41 | 0.19 | 0.1% |
| cost | scan | 22.8 | 0.0 | 24% / 35 | 21% | 10.1 / 3.9 | 53% | 8.9 | 1.57 | 0.45 | 0.0% |
| nearest | look | 28.5 | 0.0 | 38% / 49 | 16% | 4.1 / 4.1 | 66% | 11.2 | 1.46 | 0.33 | 3.8% |
| nearest | scan | 35.2 | 0.0 | 40% / 57 | 9% | 2.8 / 2.8 | 85% | 14.7 | 1.51 | 0.18 | 1.1% |
| round_robin | look | 30.6 | 0.0 | 47% / 42 | 6% | 13.1 / 3.4 | 94% | 16.0 | 1.44 | 0.01 | 0.0% |
| round_robin | scan | 38.5 | 0.0 | 49% / 52 | 4% | 13.4 / 3.1 | 95% | 16.4 | 1.51 | 0.01 | 0.0% |
| zone | look | 21.3 | 0.0 | 40% / 35 | 20% | 10.3 / 4.5 | 76% | 12.9 | 1.44 | 0.15 | 0.1% |
| zone | scan | 40.4 | 0.0 | 48% / 53 | 8% | 13.1 / 3.3 | 90% | 15.3 | 1.78 | 0.15 | 0.8% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 1.3 / 7 | 236, 10.6 / 30 | 48, 10.9 / 29 |
| cost | scan | 25, 0.4 / 2 | 236, 27.1 / 59 | 48, 12.6 / 37 |
| nearest | look | 25, 4.4 / 27 | 236, 31.3 / 80 | 48, 26.4 / 72 |
| nearest | scan | 25, 23.3 / 76 | 236, 37.7 / 77 | 48, 29.1 / 76 |
| round_robin | look | 25, 29.5 / 62 | 236, 30.7 / 64 | 48, 31.0 / 62 |
| round_robin | scan | 25, 37.5 / 71 | 236, 38.5 / 74 | 48, 38.5 / 72 |
| zone | look | 25, 19.2 / 54 | 236, 20.5 / 57 | 48, 26.4 / 61 |
| zone | scan | 25, 35.8 / 71 | 236, 41.1 / 75 | 48, 40.0 / 73 |

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

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 1 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 55.2; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 32.1 ± 0.8 | -41.9% | [-23.84, -22.32] | 20/20 | 64% | better ✓ |
| nearest | 56.0 ± 7.2 | +1.6% | [-1.72, +4.30] | 13/20 | -2% | - |
| zone | 44.3 ± 1.5 | -19.7% | [-11.63, -10.16] | 20/20 | 30% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 32.1 | -28.4% | [-13.94, -11.38] | 20/20 | better ✓ |
| nearest | look | 56.0 | -8.9% | [-8.11, -1.94] | 19/20 | better ✓ |
| round_robin | look | 55.2 | -11.9% | [-8.21, -6.76] | 20/20 | better ✓ |
| zone | look | 44.3 | -30.4% | [-19.89, -18.80] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 32.1 | 11.0 | 31.9 | 51.1 | 13.2 | 0.54 |
| cost | scan | 44.8 | 22.5 | 57.8 | 77.3 | 25.9 | 0.58 |
| nearest | look | 56.0 | 34.3 | 99.1 | 254.6 | 37.1 | 0.43 |
| nearest | scan | 61.5 | 39.7 | 85.1 | 213.7 | 42.6 | 0.53 |
| round_robin | look | 55.2 | 33.9 | 70.3 | 81.4 | 36.3 | 0.72 |
| round_robin | scan | 62.6 | 41.2 | 78.9 | 87.0 | 43.8 | 0.74 |
| zone | look | 44.3 | 23.5 | 63.5 | 95.5 | 25.4 | 0.57 |
| zone | scan | 63.6 | 42.3 | 79.3 | 142.4 | 44.7 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 11.0 | 2.2 | 14% / 16 | 25% | 8.1 / 3.7 | 83% | 12.3 | 1.44 | 0.11 | 0.0% |
| cost | scan | 22.5 | 3.4 | 24% / 37 | 19% | 10.2 / 3.8 | 63% | 9.2 | 1.61 | 0.30 | 0.0% |
| nearest | look | 34.3 | 2.8 | 39% / 57 | 13% | 3.6 / 3.6 | 72% | 11.2 | 1.49 | 0.31 | 4.5% |
| nearest | scan | 39.7 | 2.9 | 39% / 66 | 8% | 2.9 / 2.9 | 87% | 13.9 | 1.55 | 0.19 | 2.0% |
| round_robin | look | 33.9 | 2.4 | 47% / 47 | 5% | 13.3 / 3.3 | 95% | 14.9 | 1.48 | 0.01 | 0.0% |
| round_robin | scan | 41.2 | 2.6 | 48% / 56 | 3% | 13.7 / 3.0 | 96% | 15.1 | 1.53 | 0.01 | 0.1% |
| zone | look | 23.5 | 2.0 | 40% / 39 | 18% | 10.1 / 4.4 | 79% | 12.1 | 1.49 | 0.15 | 0.2% |
| zone | scan | 42.3 | 2.5 | 46% / 56 | 6% | 12.8 / 3.3 | 90% | 14.7 | 1.83 | 0.15 | 1.1% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 2.9 / 11 | 236, 11.5 / 32 | 48, 12.3 / 32 |
| cost | scan | 25, 1.1 / 6 | 236, 26.4 / 60 | 48, 14.1 / 40 |
| nearest | look | 25, 5.5 / 34 | 236, 38.1 / 105 | 48, 30.6 / 81 |
| nearest | scan | 25, 23.6 / 81 | 236, 42.8 / 87 | 48, 32.9 / 84 |
| round_robin | look | 25, 31.5 / 63 | 236, 33.9 / 71 | 48, 35.2 / 69 |
| round_robin | scan | 25, 38.3 / 75 | 236, 41.4 / 79 | 48, 41.4 / 78 |
| zone | look | 25, 22.1 / 58 | 236, 22.4 / 62 | 48, 29.4 / 65 |
| zone | scan | 25, 37.9 / 74 | 236, 43.0 / 79 | 48, 41.5 / 78 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · lobby · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 61.6; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.7 ± 1.5 | -40.5% | [-25.66, -24.21] | 20/20 | 58% | better ✓ |
| nearest | 68.4 ± 10.5 | +11.0% | [+2.66, +12.30] | 2/20 | -16% | worse ✗ |
| zone | 48.1 ± 1.8 | -21.9% | [-14.25, -12.66] | 20/20 | 32% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 36.7 | -24.5% | [-13.32, -10.49] | 20/20 | better ✓ |
| nearest | look | 68.4 | -7.9% | [-9.18, -2.18] | 16/20 | better ✓ |
| round_robin | look | 61.6 | -11.2% | [-8.99, -6.61] | 20/20 | better ✓ |
| zone | look | 48.1 | -31.2% | [-22.79, -20.97] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 36.7 | 13.5 | 37.1 | 58.5 | 17.8 | 0.56 |
| cost | scan | 48.6 | 23.3 | 58.9 | 82.8 | 29.7 | 0.59 |
| nearest | look | 68.4 | 43.5 | 136.3 | 373.7 | 49.5 | 0.41 |
| nearest | scan | 74.2 | 49.3 | 116.2 | 347.6 | 55.4 | 0.49 |
| round_robin | look | 61.6 | 37.7 | 78.0 | 89.4 | 42.7 | 0.72 |
| round_robin | scan | 69.4 | 45.0 | 85.1 | 100.5 | 50.5 | 0.75 |
| zone | look | 48.1 | 25.2 | 68.6 | 121.0 | 29.3 | 0.56 |
| zone | scan | 70.0 | 46.1 | 85.3 | 178.1 | 51.1 | 0.72 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.5 | 4.3 | 17% / 21 | 18% | 8.9 / 4.1 | 90% | 12.3 | 1.50 | 0.10 | 0.1% |
| cost | scan | 23.3 | 6.4 | 22% / 38 | 16% | 10.7 / 3.9 | 73% | 9.7 | 1.69 | 0.21 | 0.0% |
| nearest | look | 43.5 | 6.0 | 39% / 69 | 11% | 4.0 / 4.0 | 72% | 10.0 | 1.56 | 0.37 | 7.7% |
| nearest | scan | 49.3 | 6.1 | 40% / 77 | 6% | 3.4 / 3.4 | 86% | 12.8 | 1.61 | 0.22 | 4.6% |
| round_robin | look | 37.7 | 5.0 | 47% / 53 | 4% | 13.3 / 3.7 | 96% | 13.8 | 1.51 | 0.01 | 0.0% |
| round_robin | scan | 45.0 | 5.6 | 49% / 60 | 2% | 13.9 / 7.2 | 95% | 14.0 | 1.57 | 0.01 | 0.1% |
| zone | look | 25.2 | 4.1 | 39% / 42 | 17% | 10.0 / 4.4 | 82% | 11.4 | 1.53 | 0.15 | 0.4% |
| zone | scan | 46.1 | 5.1 | 46% / 61 | 5% | 12.8 / 4.3 | 91% | 13.9 | 1.88 | 0.15 | 1.8% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 5.5 / 21 | 236, 14.0 / 37 | 48, 15.2 / 37 |
| cost | scan | 25, 3.1 / 17 | 236, 26.6 / 61 | 48, 17.1 / 46 |
| nearest | look | 25, 7.7 / 47 | 236, 48.4 / 153 | 48, 37.0 / 95 |
| nearest | scan | 25, 23.8 / 89 | 236, 53.9 / 128 | 48, 39.4 / 94 |
| round_robin | look | 25, 35.0 / 74 | 236, 37.5 / 78 | 48, 40.1 / 77 |
| round_robin | scan | 25, 42.2 / 81 | 236, 45.3 / 85 | 48, 45.1 / 85 |
| zone | look | 25, 23.1 / 61 | 236, 24.1 / 67 | 48, 32.0 / 73 |
| zone | scan | 25, 41.9 / 80 | 236, 46.7 / 87 | 48, 45.2 / 84 |

## evening_rush · 40 floors x 6 cars · capacity 8 · door_time 2 · spread · load 1 (0.39 requests/tick) · 800 ticks

20 seeds.

**Dispatch axis** (LOOK motion; baseline `round_robin` = 61.5; B0 floor = 18.9)

| policy | total mean ± std | Δ | 95% CI of Δ | wins | gap closed | verdict |
|---|---:|---:|---|---:|---:|:---:|
| cost | 36.2 ± 1.4 | -41.0% | [-26.07, -24.39] | 20/20 | 59% | better ✓ |
| nearest | 61.6 ± 2.8 | +0.1% | [-1.43, +1.56] | 10/20 | -0% | - |
| zone | 48.2 ± 2.1 | -21.6% | [-14.24, -12.30] | 20/20 | 31% | better ✓ |

**Motion axis** (baseline `scan`)

| dispatch | motion | total mean | Δ | 95% CI of Δ | wins | verdict |
|---|---|---:|---:|---|---:|:---:|
| cost | look | 36.2 | -23.1% | [-12.13, -9.70] | 20/20 | better ✓ |
| nearest | look | 61.6 | -11.2% | [-9.48, -5.98] | 20/20 | better ✓ |
| round_robin | look | 61.5 | -10.5% | [-8.38, -6.02] | 20/20 | better ✓ |
| zone | look | 48.2 | -30.6% | [-22.14, -20.38] | 20/20 | better ✓ |

**All combinations** (means over seeds)

| dispatch | motion | total | wait | wait p95 | wait max | excess | Jain (wait) |
|---|---|---:|---:|---:|---:|---:|---:|
| cost | look | 36.2 | 13.1 | 36.2 | 61.5 | 17.4 | 0.55 |
| cost | scan | 47.1 | 21.9 | 56.8 | 78.8 | 28.3 | 0.58 |
| nearest | look | 61.6 | 36.9 | 98.2 | 265.6 | 42.7 | 0.43 |
| nearest | scan | 69.3 | 44.4 | 98.8 | 269.6 | 50.4 | 0.50 |
| round_robin | look | 61.5 | 37.6 | 77.4 | 91.4 | 42.6 | 0.72 |
| round_robin | scan | 68.7 | 44.3 | 85.9 | 97.2 | 49.8 | 0.74 |
| zone | look | 48.2 | 25.3 | 69.6 | 109.6 | 29.3 | 0.56 |
| zone | scan | 69.5 | 45.5 | 85.6 | 181.1 | 50.6 | 0.71 |

**Why: diagnostics** (means over seeds; *away* = assigned to a car moving away from the passenger; *idle* = assigned to an idle car; distance = floors from the chosen / nearest car at assignment; busy = share of car time not idle)

| dispatch | motion | wait | detour | away: share / wait | idle | distance chosen / nearest | busy | floors per passenger | riders per stop | load CV | full pass-bys |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cost | look | 13.1 | 4.2 | 18% / 21 | 18% | 8.6 / 3.7 | 90% | 12.2 | 1.50 | 0.10 | 0.0% |
| cost | scan | 21.9 | 6.4 | 21% / 37 | 17% | 10.3 / 3.7 | 72% | 9.6 | 1.67 | 0.21 | 0.0% |
| nearest | look | 36.9 | 5.8 | 39% / 64 | 12% | 3.7 / 3.7 | 76% | 10.6 | 1.53 | 0.25 | 5.1% |
| nearest | scan | 44.4 | 6.0 | 39% / 74 | 7% | 3.1 / 3.1 | 87% | 13.0 | 1.59 | 0.22 | 3.5% |
| round_robin | look | 37.6 | 5.0 | 47% / 53 | 4% | 13.3 / 3.3 | 96% | 13.8 | 1.51 | 0.01 | 0.0% |
| round_robin | scan | 44.3 | 5.5 | 47% / 61 | 2% | 13.7 / 3.1 | 95% | 14.1 | 1.56 | 0.01 | 0.0% |
| zone | look | 25.3 | 4.1 | 39% / 42 | 16% | 9.9 / 4.1 | 82% | 11.3 | 1.53 | 0.15 | 0.4% |
| zone | scan | 45.5 | 5.0 | 45% / 62 | 6% | 12.4 / 3.3 | 91% | 13.8 | 1.88 | 0.15 | 1.7% |

**By trip type** (means over seeds: passengers per run, mean / p95 wait in ticks; inbound = from the lobby, outbound = to the lobby)

| dispatch | motion | inbound: n, wait mean / p95 | outbound: n, wait mean / p95 | inter-floor: n, wait mean / p95 |
|---|---|---:|---:|---:|
| cost | look | 25, 5.6 / 20 | 236, 13.6 / 37 | 48, 14.8 / 37 |
| cost | scan | 25, 2.6 / 15 | 236, 24.9 / 59 | 48, 16.9 / 44 |
| nearest | look | 25, 9.5 / 55 | 236, 40.7 / 108 | 48, 32.1 / 88 |
| nearest | scan | 25, 25.7 / 90 | 236, 48.1 / 109 | 48, 35.2 / 93 |
| round_robin | look | 25, 34.8 / 72 | 236, 37.6 / 77 | 48, 38.8 / 76 |
| round_robin | scan | 25, 41.7 / 80 | 236, 44.8 / 86 | 48, 43.1 / 84 |
| zone | look | 25, 22.3 / 61 | 236, 24.3 / 68 | 48, 31.9 / 72 |
| zone | scan | 25, 39.0 / 77 | 236, 46.3 / 86 | 48, 45.2 / 86 |
