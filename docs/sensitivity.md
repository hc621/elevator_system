[← README](../README.md) · [all studies](../README.md#detailed-studies)

# Sensitivity: stop time and start position

```bash
uv run elevator-sim bench --suite standard --seeds 20 --door-times 0,1,2 --placements lobby,spread \
    -o results/sensitivity                       # 48 experiments, 7,680 runs, ~4 min on 10 cores
```

The brief doesn't model doors, so `door_time` (extra ticks a stop holds the car) is our assumption,
and so is starting every car at the lobby. This study checks whether either one drives the
conclusions: the standard suite again at door_time 0, 1 and 2, with cars starting at the lobby or
spread evenly up the building. Full pivot tables are in `results/sensitivity/summary.md`; the
summary across the 6 settings per row:

| scenario | building | `cost` vs RR | `nearest` vs RR | `zone` vs RR | LOOK vs SCAN (`cost`) | ranking at door 0 / 1 / 2 (lobby) |
|---|---|---|---|---|---|---|
| quiet | 30 × 4 | -33% to -31% (6✓) | -14% to -8% (6✓) | -2% to +2% (6?) | -15% to -11% (6✓) | CNZR / CNZR / CNRZ |
| quiet | 40 × 6 | -37% to -33% (6✓) | -19% to -11% (6✓) | -1% to +4% (5? / 1✗) | -13% to -9% (6✓) | CNRZ / CNRZ / CNRZ |
| morning_rush | 30 × 4 | -36% to -34% (6✓) | -1% to +27% (2? / 4✗) | -21% to -19% (6✓) | -18% to +0% (2✓ / 4?) | CZNR / CZRN / CZRN |
| morning_rush | 40 × 6 | -36% to -34% (6✓) | +6% to +29% (2? / 4✗) | -22% to -20% (6✓) | -5% to -0% (1✓ / 5?) | CZRN / CZRN / CZRN |
| lunch | 30 × 4 | -43% to -37% (6✓) | -12% to -7% (6✓) | -20% to -18% (6✓) | -22% to -6% (6✓) | CZNR / CZNR / CZNR |
| lunch | 40 × 6 | -49% to -46% (6✓) | -15% to -13% (6✓) | -22% to -20% (6✓) | -12% to -4% (6✓) | CZNR / CZNR / CZNR |
| evening_rush | 30 × 4 | -38% to -34% (6✓) | -2% to +16% (5? / 1✗) | -20% to -18% (6✓) | -26% to -17% (6✓) | CZRN / CZRN / CZRN |
| evening_rush | 40 × 6 | -42% to -40% (6✓) | -4% to +11% (5? / 1✗) | -22% to -19% (6✓) | -33% to -23% (6✓) | CZRN / CZRN / CZRN |

✓ better, ? inconclusive, ✗ worse (counts out of 6 settings). Ranking letters: C `cost`,
N `nearest`, Z `zone`, R `round_robin`, best first.

**Conclusions that hold in every setting**
- `cost` is the best policy in all 48 experiments, 31-49% better than round-robin; its advantage
  moves by at most 6 points across stop times and start positions.
- `zone` is 18-22% better than round-robin in both rushes and at lunch at every stop time, and
  no better in the quiet scenario (once significantly worse, +4%).
- LOOK beats SCAN under `cost` at lunch, in the evening rush and in the quiet scenario in every
  setting; in the morning rush the difference is small and mostly inconclusive.

**Conclusions that depend on the stop time**
- **`nearest` gets worse as stops get longer.** It stays better than round-robin when it's quiet
  or at lunch, but in the rushes it is significantly worse in 10 of the 24 settings (up to +29%)
  and comes last in all 16 rush settings with door_time ≥ 1. It piles passengers onto a few cars,
  and every extra stop now costs more: from door_time 0 to 2 in the 30-floor rushes, its full-car
  pass-bys rise from 5% to 16% (morning) and its worst wait from 188 to 354 ticks (evening).
- **Longer stops hurt round-robin more than `cost`** in every pair: from door_time 0 to 2,
  round-robin's mean total grows by 3.4-13.5 ticks, `cost`'s by 3.0-10.5. `cost` also spreads
  passengers more evenly as stops get dearer (its load CV falls from door_time 0 to 2 in all 8
  pairs, e.g. 0.15 → 0.08 in the 30-floor morning rush), consistent with its projection pricing
  every stop.
- Headroom shrinks: at door_time 2, `cost`'s cars are busy up to 96% (30-floor evening rush).

**Start position barely matters.** Lobby vs spread changes `cost`'s and `zone`'s result by at
most 2 points (`nearest`: up to 11). Over an 800-tick run the cars leave their starting floors
within the first few dozen ticks, so the start only affects the earliest passengers. Where idle
cars wait *during* a run is a different question (parking, not built).

**Caveats**
- "Gap closed" falls as door_time grows (e.g. 60% → 52%, quiet 30 × 4) partly because the B0
  floor is the direct ride with no stops: with longer stops, more of the excess time is
  unavoidable. Compare gap closed within one door_time, not across them.
- Verdicts on `nearest` depend on the stop time, so claims about it name the door_time (the
  standard suite uses 1).
