# Presentation outline (about 10 minutes + demo)

Numbers are from `results/` (20 paired seeds); the README has the tables and the method.

## 1. The problem and the model (1 min)

- Destination dispatch: a passenger gives origin and destination, the controller assigns one car
  at once, the assignment is final. Time moves one tick (one floor) at a time; nothing looks ahead.
- Outputs the brief asks for: the positions log (every car's floor per tick from t = 0) and the
  passenger statistics (min / max / average wait and total time, plus observations).
- My assumptions on top: a stop holds the car `door_time + 1` ticks (default door_time 1), a car
  stops only for its own passengers, capacity is a hard limit.

## 2. How it is built (1.5 min)

- Two separate decisions: **dispatch** (which car, once per passenger) and **motion** (how a car
  moves, every tick). Four dispatch policies (`cost`, `nearest`, `zone`, `round_robin`), two
  motion rules (LOOK, SCAN).
- `cost` simulates each car's future with and without the new passenger (`project()`, the car's
  own rules on a copy, capacity included) and picks the car where everyone's total time grows
  least.
- One-way data flow: feed → clock → dispatcher → cars → journal → report. Every output is computed
  from the journal, so a run can be re-analysed without re-simulating.
- Capacity: the car decides on arrival from its actual load (like a load sensor); looking ahead is
  the dispatcher's job.

## 3. Realistic traffic (1 min)

- An office building: three Poisson streams (inbound from the lobby, outbound to it, inter-floor
  at a steady rate). Scenarios: quiet, morning rush (heavy inbound), lunch (two-way), evening rush
  (heavy outbound). Each seed's streams are generated once and shared, so scenarios differ only in
  the rush stream.

## 4. How I measure (1 min)

- Paired runs: every policy sees the same passengers. Baselines: the theoretical floor (B0),
  round-robin, SCAN. A claim needs a 95% bootstrap CI excluding 0 *and* 80% of seeds agreeing.

## 5. Results (2.5 min)

- `cost` beats round-robin by 31-47% in every scenario and seed, closing 52-73% of the gap to the
  floor.
- **Why**: round-robin gives 46-50% of busy-period passengers a car moving away from them; the
  empty travel keeps its cars 95-98% busy. All the difference is waiting, not riding.
- `nearest` backfires in the rushes (piles onto the car near the lobby; 6-12% passed by a full
  car). `zone` is strong in rushes and even beats `cost` when a morning rush overloads the
  building: an honest limit of the greedy policy.
- Robust: `cost` is best in all 48 door-time / start-position settings.
- Parking idle cars: back to the lobby before the morning rush (up to 17% better), spread out when
  it's quiet; a demand-following policy is never worse. Round-robin gains nothing from parking
  (it ignores where cars are). Default stays "don't move": parking trips cost the building.

## 6. Fairness vs efficiency (1 min)

- A weight on squared waits trims the worst rush-hour waits by 7-10 ticks under heavy load, with
  no significant cost in mean total time; no per-passenger guarantee. The visible trade-off is
  across policies: round-robin has the most equal waits but the longest.

## 7. Limits and next steps (1 min)

- Fixed assignments (stale projections), no hard wait bound, sectoring for saturated up-peak,
  express banks, a full-day timeline calibrated from accumulated daily data.
- Quality: 249 tests incl. property-based ones; projections made 5x faster with byte-identical
  results (10k requests, 60 floors, 10 cars in 8.4 s).

## Demo (as time allows)

```bash
uv run elevator-sim examples/brief.csv -e 3 -f 60 --html -o out/brief && open out/brief/report.html
uv run elevator-sim generate morning_rush -f 30 -s 1 -o out/rush.csv
uv run elevator-sim out/rush.csv -f 30 -e 4 --html -o out/rush && open out/rush/report.html
uv run elevator-sim report results/standard -o out/standard.html && open out/standard.html
uv run elevator-sim report results/buildings -o out/buildings.html && open out/buildings.html
```

Show: the time-space diagram (hover the crosshair), wait by trip type, "assigned to a car moving
away", the building trend lines (zone crossing below cost in the overloaded morning rush).
