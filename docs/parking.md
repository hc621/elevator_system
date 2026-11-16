[← README](../README.md) · [all studies](../README.md#detailed-studies)

# Parking idle cars

When a car has no passengers and no assignments, where should it wait? A **parking policy**
answers once, when the car goes idle; the car then drives there (a real move: it shows in the
positions log, floors travelled and car trips) and drops the target the moment it is assigned a
passenger. The decision is made at the end of the tick the car goes idle, so it leaves on the
next tick. A policy sees read-only car views, the floors other idle cars hold, and requests
already made, never future ones (a spy test checks this).

| Policy | Rule |
|---|---|
| `stay` (default) | wait where the last trip ended |
| `lobby` | go back to floor 1 |
| `spread` | car i waits at its own home floor, spaced evenly up the building |
| `demand` | wait at the floor where the most requests started in the last 100 ticks, skipping floors another idle car already holds |

```bash
uv run elevator-sim bench --suite standard --seeds 20 --parking stay,lobby,spread,demand \
    --dispatch cost,round_robin --motion look -o results/parking    # 1,280 runs, ~1 min
uv run elevator-sim rush.csv -f 30 -e 4 --parking lobby             # a single run
```

Each policy against `stay` on the same seeds and passengers (`cost` dispatch, LOOK; Δ mean total
time with verdict, and the change in floors travelled per passenger, the price of parking moves):

| scenario | building | `cost`, stay | `lobby`: Δ total, extra floors | `spread`: Δ total, extra floors | `demand`: Δ total, extra floors |
|---|---|---:|---:|---:|---:|
| quiet | 30 × 4 | 19.6 | +5.4% ✗, +30% | -5.5% ✓, +40% | -3.6% ✓, +25% |
| quiet | 40 × 6 | 23.2 | +9.8% ✗, +35% | -5.5% ✓, +54% | -3.4% ✓, +29% |
| morning_rush | 30 × 4 | 28.3 | -6.4% ✓, +24% | -5.0% ✓, +19% | -5.7% ✓, +19% |
| morning_rush | 40 × 6 | 36.8 | -17.1% ✓, +51% | -15.0% ✓, +33% | -13.5% ✓, +30% |
| lunch | 30 × 4 | 25.3 | -0.4% ?, +6% | -1.8% ?, +7% | -0.1% ?, +6% |
| lunch | 40 × 6 | 28.2 | +1.0% ?, +15% | +0.1% ?, +15% | -0.5% ?, +13% |
| evening_rush | 30 × 4 | 28.5 | +0.5% ?, +1% | -2.2% ?, +5% | -0.3% ?, +4% |
| evening_rush | 40 × 6 | 32.5 | -0.4% ?, +0% | -3.9% ✓, +13% | -3.0% ✓, +8% |

**What it shows**
- **`lobby` does its job**: it is the best policy in the morning rush (-6%, -17%), and it backfires
  when it's quiet (+5%, +10%), where the next passenger is rarely at the lobby.
- **`spread` is best when it's quiet** (-5.5% in both buildings, max wait 4.5-7 ticks shorter) and
  also helps the morning rush, at the highest travel cost (up to +54% floors per passenger).
- **`demand` is never significantly worse** and helps in 5 of the 8 experiments, with less extra
  travel than `spread`. In the morning rush most recent requests start at the lobby, so it parks
  there by itself; when it's quiet it scatters the cars much like `spread`.
- **At lunch and in the 30-floor evening rush nothing helps**: the cars are rarely idle.
- **Round-robin gains nothing from any parking policy** (all inconclusive, within ±2.5%): it
  never looks at where the cars are, so where they wait doesn't matter to it. Parking only pays
  for a dispatcher that uses car positions.
- **Parking costs travel**: up to +54% floors per passenger under `cost` (0-15% at lunch and in
  the evening rush, where cars are rarely idle).

**Decisions** (made before the results, revisited with them)
1. **Keep `demand`.** A recent request at a floor could mean that passenger has already gone, or
   that colleagues on the same floor of an office will leave around the same time; rather than
   assume, let the simulation decide. It did: `demand` is never worse, and in the morning rush the
   "colleagues follow" reading wins.
2. **`lobby` stays a simple rule** (every idle car goes to floor 1, no cap): it exists to handle the
   morning rush, and the results confirm it is best there and only there.
3. **`stay` remains the default.** A trip to a parking floor is itself a cost to the building
   (energy, wear), and the table shows that cost is real; the headline results use no parking.
   `demand` is the best all-round choice when that travel is acceptable; `lobby` before a known
   morning rush.
