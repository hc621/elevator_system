[← README](../README.md) · [all studies](../README.md#detailed-studies)

# Performance

`cost` projects every eligible car twice per new request (with and without the newcomer), so the
projection is the hot path (95% of the time in a profile). Two shortcuts make it about 5× faster
without changing any result:

- **The plan is cached.** A car's future without new passengers is fixed until its next
  assignment: the real car follows its projection tick for tick. So the "without" projection is
  kept and only trimmed to future events and current passengers; an assignment replaces it (with
  the "with" projection just computed for that passenger, when it matches).
- **Floors without work are skipped.** A moving car with closed doors passes floors where nobody
  gets off or waits without deciding anything, so the copy in a projection jumps straight to the
  next floor with work. The real simulation still steps every tick. Only motion policies that
  declare it safe (LOOK, SCAN) allow the jump.

| Run | Before | After |
|---|---:|---:|
| 10,170 requests, 60 floors, 10 cars, `cost`, door_time 1 | 41.9 s | 8.4 s (target ≤ 10 s) |
| Full test suite | 10.8 s | 5.9 s (before the property tests were added) |

How it was checked: all five committed studies were regenerated with the shortcuts and every value
is identical (git shows no change in any number); a property test compares the fast projection with
the exact step-by-step one at every tick of random runs, and fails when the skip is deliberately
broken by one floor.
