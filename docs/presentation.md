[← README](../README.md)

# Presentation outline (10 minutes + demo)

One model, one design decision, one result with its root cause, one honest limit, and why it
matters for a risk platform. Numbers are from `results/` (20 paired seeds).

## 1. The model (1.5 min)

- Destination dispatch: a passenger gives origin and destination, a car is assigned at once. Time
  moves one tick (one floor) at a time; nothing looks ahead.
- Two separate decisions: **dispatch** (which car, once per passenger) and **motion** (how a car
  moves, every tick). The car enforces the rules; policies only answer questions.
- Traffic is an office building: three Poisson streams (inbound, outbound, inter-floor), generated
  once per seed, so morning rush, lunch, evening rush and quiet differ only in the rush stream.
- Outputs the brief asks for: the positions log and min / max / average wait and total time.

## 2. One design decision: capacity along the route (2 min)

- The car decides whether to pick someone up **when it arrives**, from its actual load (like a load
  sensor): full at floor 1, two get off at 6, two board at 8. It never relies on a prediction.
- Looking ahead is the **dispatcher's** job: `cost` simulates each car's future with and without
  the newcomer, with the same capacity rule, so a car that would arrive full shows up as a late
  pickup. At capacity 4 in a rush: 7-21% of passengers passed by a full car under `cost`, 20-39%
  under round-robin, 35-54% under `nearest`.
- Pinned by tests that walk the timeline tick by tick (`test_capacity_scenarios.py`).

## 3. One result and its root cause (2.5 min)

- `cost` beats round-robin by 31-47% in every scenario and every seed, closing 52-73% of the gap to
  the theoretical floor; it stays best in all 48 door-time / start-position settings.
- **Why**: round-robin hands 46-50% of busy-period passengers a car that is moving away from them;
  the empty travel keeps its cars 95-98% busy, at saturation. All of the difference is waiting, not
  riding. These diagnostics are in every report, not a one-off analysis.

## 4. One honest limit (1.5 min)

- Serving everyone: 0 unserved in 15,360 runs (4.0 million passengers), but no per-passenger bound
  is proved; the first improvement is re-assigning a passenger whose wait passes a limit.
- `cost` is not always best: when a morning rush overloads the building (45-60 floors on 4 cars),
  `zone` beats it in 18-20 of 20 seeds. Destination sectoring shortens round trips; a greedy cost
  can't see that.

## 5. Why this matters for a risk platform (1.5 min)

- **Tails, not means**: fairness is judged on p95 and max wait; the Jain index was rejected because
  it rewards uniformly bad waits.
- **Paired scenarios on identical inputs**: every policy runs on the same passengers, so a
  difference is the policy, not the draw. The same discipline as scenario analysis.
- **An audit trail and deterministic replay**: every output is computed from an append-only event
  journal; a saved run rebuilds its report exactly; runs are byte-identical.
- **No result without significance**: a claim needs the 95% CI to exclude 0 and 80% of seeds to
  agree; anything else is reported as inconclusive.
- **AI with controls**: tests owned by people, numbers generated from data, every claim checked; the
  README lists where the AI was wrong and what caught it.

## Demo (as time allows)

```bash
uv run elevator-sim generate morning_rush -f 30 -s 1 -o out/rush.csv
uv run elevator-sim out/rush.csv -f 30 -e 4 --html -o out/rush && open out/rush/report.html
uv run elevator-sim report results/standard -o out/standard.html && open out/standard.html
uv run elevator-sim report results/buildings -o out/buildings.html && open out/buildings.html
```

Show: the time-space diagram (hover the crosshair), "assigned to a car moving away", and the
building trend lines where `zone` crosses below `cost` in the overloaded morning rush.

## If asked

Parking (back to the lobby before the morning rush, up to 17% better; round-robin gains nothing
because it ignores car positions); the fairness weight (trims the worst rush waits by 7-10 ticks at
no measurable cost); performance (5× faster projections, results byte-identical).
