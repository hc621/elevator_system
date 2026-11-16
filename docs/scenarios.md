[← README](../README.md) · [all studies](../README.md#detailed-studies)

# Traffic scenarios: a business building

The simulation models an **office building**: people arrive in the morning, leave in the evening,
go out and come back at lunch, and move between floors all day. Requests come from three
independent streams, each a **Poisson process** (the number of new requests in a tick is
Poisson-distributed, so arrivals are random and bursty, not evenly spaced):

1. **inbound**: lobby (floor 1) → a random upper floor
2. **outbound**: a random upper floor → lobby
3. **inter-floor**: a random upper floor → a different upper floor, up or down

Inter-floor traffic runs at the same steady rate in every scenario; the scenarios differ in the
inbound and outbound rates (requests per tick):

| scenario | inbound | outbound | inter-floor | total | what it is |
|---|---:|---:|---:|---:|---|
| `quiet` | 0.03 | 0.03 | 0.06 | 0.12 | mid-morning / mid-afternoon: mostly people moving between floors |
| `morning_rush` | **0.30** | 0.03 | 0.06 | 0.39 | arrivals: heavy inbound (up-peak) |
| `lunch` | 0.15 | 0.15 | 0.06 | 0.36 | going out and coming back (two-way) |
| `evening_rush` | 0.03 | **0.30** | 0.06 | 0.39 | departures: heavy outbound (down-peak) |

- **Generated once, shared by every scenario.** For a seed, each stream is drawn once at a cap
  rate and every candidate request gets a random number u; a scenario keeps a candidate when
  u < its rate / cap. Thinning a Poisson process this way gives a Poisson process at the lower
  rate, so for one seed the inter-floor passengers are *identical* in every scenario and the
  morning rush's inbound passengers include the quiet scenario's: the only difference between
  scenarios is the rush stream. Ids name the stream (`in17`, `out3`, `fl8`), so the same
  passenger has the same id across scenarios.
- **Load.** `--load` / `--loads` multiplies every rate (the fairness study uses 1.5).
- The rates were calibrated so the rushes are heavy but stable: at load 1 `cost`, `zone` and
  round-robin finish within 120 ticks of the arrival window closing (`nearest`, which piles up in
  the rushes, within 260), and the rushes are busy enough that a full car passing someone happens
  (under `nearest`, 6-12% of passengers).
- **Other buildings differ.** A residential building reverses the rushes (outbound in the
  morning, inbound in the evening) and a hotel has its own peaks; only the business pattern is
  modelled. With the streams separated, another building type is a different rate table.

```bash
uv run elevator-sim generate morning_rush --floors 30 --duration 800 --seed 1 -o rush.csv
uv run elevator-sim generate lunch --floors 30 --load 1.5 -o lunch_heavy.csv
```
