[← README](../README.md) · [all studies](../README.md#detailed-studies)

# Fairness vs efficiency

The brief's third bonus: the trade-off between serving everyone quickly (fairness) and optimising
for the majority (efficiency). The `cost` policy takes a fairness weight α:

```
cost(car) = increase in Σ total time  +  α · increase in Σ wait²     (over that car's passengers)
```

Squaring the projected waits makes one passenger waiting 40 ticks cost as much as sixteen waiting
10, and makes delaying someone who already waits long expensive (pushing a 30-tick wait to 33 adds
189 to Σ wait²; pushing a 3-tick wait to 6 adds 27), so the policy stops trading one long wait for
a few short ones. α = 0 is the plain policy. Fairness is judged on p95 and max wait, not the Jain
index (see [Metrics](metrics.md#metrics-what-we-measure-and-why)).

```bash
uv run elevator-sim bench --suite standard --seeds 20 --loads 1,1.5 --dispatch round_robin \
    --fairness 0,0.05,0.2,1 --motion look -o results/fairness   # 1,600 runs, ~4 min
uv run elevator-sim rush.csv -f 30 -e 4 --fairness 0.2          # a single run with α = 0.2
```

The sweep covers α = 0, 0.05, 0.2 and 1 at the standard load and at 1.5 × (the heavy rushes reach
0.585 requests per tick). Per-α frontier tables are in `results/fairness/summary.md`; α = 0.2
against plain `cost`, paired by seed:

| scenario | building | load | `cost`: total / p95 wait / max wait | α = 0.2: Δ total | Δ wait p95 | Δ wait max |
|---|---|---|---|---:|---:|---:|
| quiet | 30 × 4 | 1 (0.12/tick) | 19.6 / 18 / 26 | -0.4% ? | -0.6 ? | -0.7 ? |
| quiet | 40 × 6 | 1 (0.12/tick) | 23.2 / 18 / 30 | -0.1% ? | -0.5 ? | -0.5 ? |
| morning_rush | 30 × 4 | 1 (0.39/tick) | 28.3 / 26 / 38 | +0.0% ? | -1.0 ? | -5.2 ? |
| morning_rush | 40 × 6 | 1 (0.39/tick) | 36.8 / 33 / 43 | +0.4% ? | -0.5 ? | -3.6 ? |
| lunch | 30 × 4 | 1 (0.36/tick) | 25.3 / 24 / 37 | -1.9% ? | -2.0 ? | -3.5 ? |
| lunch | 40 × 6 | 1 (0.36/tick) | 28.2 / 21 / 38 | -0.5% ? | -0.3 ? | -1.6 ? |
| evening_rush | 30 × 4 | 1 (0.39/tick) | 28.5 / 31 / 50 | -0.8% ? | -1.9 ? | -4.9 ✓ |
| evening_rush | 40 × 6 | 1 (0.39/tick) | 32.5 / 33 / 51 | -0.6% ? | -1.5 ✓ | -5.0 ? |
| quiet | 30 × 4 | 1.5 (0.18/tick) | 20.5 / 19 / 27 | -0.4% ? | -0.3 ? | -0.7 ? |
| quiet | 40 × 6 | 1.5 (0.18/tick) | 24.1 / 19 / 33 | -0.2% ? | -0.6 ? | -1.4 ? |
| morning_rush | 30 × 4 | 1.5 (0.585/tick) | 36.5 / 40 / 62 | +1.7% ? | -1.8 ? | -10.3 ✓ |
| morning_rush | 40 × 6 | 1.5 (0.585/tick) | 40.7 / 36 / 52 | +0.9% ? | -1.2 ? | -7.0 ✓ |
| lunch | 30 × 4 | 1.5 (0.54/tick) | 28.9 / 30 / 51 | -1.6% ? | -0.7 ? | -2.5 ? |
| lunch | 40 × 6 | 1.5 (0.54/tick) | 30.9 / 26 / 44 | -2.9% ? | -3.3 ✓ | -5.6 ? |
| evening_rush | 30 × 4 | 1.5 (0.585/tick) | 31.7 / 36 / 64 | -0.9% ? | -2.1 ? | -8.2 ✓ |
| evening_rush | 40 × 6 | 1.5 (0.585/tick) | 34.2 / 34 / 60 | -0.9% ? | -1.8 ? | -7.4 ? |

✓ better, ? inconclusive, ✗ worse (claim rule as above; the max is noisy, so few results clear
the 80%-of-seeds bar).

**What we found**
- **When it's quiet there is nothing to trade.** Plain `cost`'s worst wait is already short
  (26-33 ticks); the fairness term changes it by under 1.5 ticks.
- **In the rushes it trims the worst waits**, and more so under heavy load: at load 1.5, max wait
  falls by 7-10 ticks in both rushes (significant in the morning rush in both buildings and the
  30-floor evening rush); at load 1, by 3.6-5.2 ticks.
- **We found no efficiency price.** Mean total time is never significantly worse at any α tested
  (changes between -2.9% and +1.7%, all inconclusive). The only hint of a cost is the heavy
  morning rush (+0.9%, +1.7%).
  A likely reason: plain `cost` is greedy, so leaving one passenger waiting long is not even good
  for the total; the penalty corrects some of those greedy choices.
- **No guarantee per input.** On a small starvation-prone case (20 floors, 3 cars, 120 requests in
  200 ticks), α = 1 lowers the max wait in 20 of 30 seeds but raises it in 7
  (`tests/test_fairness.py`).
- So, within `cost`, fairness and efficiency did not conflict in our settings. The visible
  trade-off is between policies: round-robin gives the most *equal* waits (highest Jain index)
  but the longest ones. The default stays α = 0 so the headline results are the plain policy;
  α = 0.2 is a reasonable setting for heavy rushes.
