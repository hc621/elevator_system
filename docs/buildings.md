[← README](../README.md) · [all studies](../README.md#detailed-studies)

# Building sweep: floors, cars and capacity

```bash
uv run elevator-sim bench --suite buildings --seeds 20 -o results/buildings   # 3,520 runs, ~6 min
```

The brief makes floors, elevators and capacity configurable, and the standard suite's two
buildings differ in floors *and* cars at once. This sweep varies one setting at a time around
30 floors × 4 cars × capacity 8 (LOOK motion, all four dispatch policies, 20 seeds): floors
15 / 30 / 45 / 60, cars 2 / 3 / 4 / 6 / 8, capacity 4 / 6 / 8 / 12. **Demand scales with floors**
(same people per floor: rates × (floors − 1) / 29), so a 60-floor office has about twice the
requests of a 30-floor one; the car and capacity sweeps keep the 30-floor demand. All Δ below are
significant (✓) unless marked; the HTML report (`report results/buildings`) draws each row as a
trend line.

**Varying floors** (cars 4, capacity 8, demand scales with floors): mean total, round_robin → cost (Δ), ranking

| scenario | floors 15 | floors 30 | floors 45 | floors 60 |
|---|---:|---:|---:|---:|
| quiet | 13 → 10 (-23%) CNZR | 28 → 20 (-31%) CNZR | 57 → 32 (-43%) CNZR | 84 → 49 (-42%) CZNR |
| morning_rush | 16 → 14 (-15%) CZRN | 44 → 28 (-35%) CZRN | 169 → 142 (-16%) ZCRN | 483 → 443 (-8%) ZCRN |
| lunch | 15 → 11 (-25%) CNZR | 42 → 25 (-40%) CZNR | 74 → 46 (-38%) CZRN | 192 → 120 (-38%) CZRN |
| evening_rush | 16 → 13 (-16%) CRZN | 45 → 29 (-36%) CZRN | 155 → 63 (-60%) CZRN | 396 → 230 (-42%) CZRN |

**Varying cars** (floors 30, capacity 8): mean total, round_robin → cost (Δ), ranking

| scenario | cars 2 | cars 3 | cars 4 | cars 6 | cars 8 |
|---|---:|---:|---:|---:|---:|
| quiet | 38 → 28 (-26%) CZNR | 32 → 22 (-31%) CNZR | 28 → 20 (-31%) CNZR | 25 → 18 (-30%) CNRZ | 25 → 17 (-31%) CNRZ |
| morning_rush | 113 → 99 (-13%) ZCRN | 48 → 34 (-29%) CZRN | 44 → 28 (-35%) CZRN | 39 → 26 (-34%) CZRN | 36 → 26 (-29%) CZRN |
| lunch | 51 → 41 (-19%) CZRN | 46 → 31 (-33%) CZNR | 42 → 25 (-40%) CZNR | 38 → 21 (-45%) CZNR | 34 → 19 (-44%) CNZR |
| evening_rush | 116 → 59 (-49%) CZRN | 50 → 34 (-32%) CZRN | 45 → 29 (-36%) CZRN | 40 → 25 (-38%) CZRN | 36 → 24 (-33%) CZRN |

**Varying capacity** (floors 30, cars 4): mean total, round_robin → cost (Δ), ranking

| scenario | capacity 4 | capacity 6 | capacity 8 | capacity 12 |
|---|---:|---:|---:|---:|
| quiet | 28 → 20 (-31%) CNRZ | 28 → 20 (-31%) CNZR | 28 → 20 (-31%) CNZR | 28 → 20 (-31%) CNZR |
| morning_rush | 72 → 50 (-30%) CZRN | 45 → 31 (-31%) CZRN | 44 → 28 (-35%) CZRN | 44 → 28 (-37%) CZNR |
| lunch | 43 → 26 (-41%) CZNR | 42 → 25 (-40%) CZNR | 42 → 25 (-40%) CZNR | 42 → 25 (-40%) CZNR |
| evening_rush | 75 → 33 (-56%) CZRN | 46 → 29 (-37%) CZRN | 45 → 29 (-36%) CZRN | 45 → 28 (-36%) CZNR |

**What it shows**
- **Four cars can't serve a 45- or 60-floor office at rush hour.** Mean total times run to
  hundreds of ticks and up to 70% of passengers see a full car pass; a taller building needs more
  cars, and the sweep shows where the bank runs out.
- **In an overloaded morning rush, `zone` beats `cost`** (45 floors: 126 vs 142 ticks, `zone`
  better in 18 of 20 seeds; 60 floors: 327 vs 443, 20 of 20). Banding cars by destination is how
  real buildings handle up-peak: each car serves a short band, so its round trip is shorter, and
  fewer passengers are passed by a full car (32% vs 55% at 45 floors). `cost` is greedy and can't
  see that. In the overloaded evening rush `cost` still wins clearly (230 vs 299 ticks, 20 of 20).
  A known improvement: switch to destination sectoring when the up-peak saturates.
- **More cars help, with diminishing returns.** Going from 2 to 3 cars rescues the rushes (round-
  robin 113 → 48 ticks in the morning); beyond 6 cars `cost`'s mean total barely moves. `cost`
  stays 29-45% better than round-robin from 3 to 8 cars.
- **Capacity only matters when it binds**: in the quiet scenario and at lunch every capacity from 4
  to 12 gives the same result to within a tick. At capacity 4 in the rushes it binds hard, and
  `cost`'s capacity-aware projection pays off most: passengers passed by a full car 7-21% under
  `cost` vs 20-39% under round-robin and 35-54% under `nearest`, and p95 wait 40-71 ticks vs
  122-232 (round-robin). Above capacity 6 the rushes barely change.
