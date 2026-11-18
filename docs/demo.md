[← README](../README.md)

# Demo walkthrough

A five-minute tour on any machine with Python 3.10+. Every command takes under a second, and the
expected output is shown so you can tell at a glance that it worked.

## Setup on a fresh machine

```bash
git clone https://github.com/hc621/elevator_system.git && cd elevator_system
```

Then one of:

| You have | Run |
|---|---|
| uv, or permission to install it | `./scripts/install.sh` then `source .venv/bin/activate` |
| only Python 3.10+ (no uv) | `python3 -m venv .venv && source .venv/bin/activate && pip install -e .` |
| Windows | `py -m venv .venv`, `.venv\Scripts\activate`, `pip install -e .` |

The package has no runtime dependencies, so `pip install -e .` is enough to run everything below.
With the environment activated, the command is `elevator-sim` (`python -m elevator_sim` is the same).
To run the tests too: `uv sync` with uv, or `pip install pytest pytest-cov hypothesis` without it,
then `pytest -q` (expect 255 passed).

`open` below is macOS; on Windows use `start`, on Linux `xdg-open`, or open the file in a browser.

**No Python on the machine?** The benchmark reports are committed as `results/<study>/report.html`.
Download one from GitHub (open the file, then "Download raw file") and open it in a browser: each is
a single self-contained page that works offline. Steps 4 and 5 below show the same reports.

## 1. The brief's example: the two required outputs

```bash
elevator-sim examples/brief.csv --elevators 3 --floors 60 --capacity 8 --html -o out/demo/brief
open out/demo/brief/report.html
```

Expect `3 passengers delivered`, `last drop-off at t=51`, wait min / mean / max = 0 / 6.3 / 19.
Written to `out/demo/brief/`:
- `positions.jsonl` and `positions.csv`: the positions log, one row per tick from t = 0
- `passengers.json`: each passenger's times
- `report.json`: the statistics (also printed)
- `report.html`: the report

## 2. The same run as a function

```bash
python -c "
from elevator_sim import run_requests
r = run_requests([(0,'passenger1',1,51),(0,'passenger2',1,37),(10,'passenger3',20,1)],
                 elevators=3, floors=60, capacity=8)
print(r.positions[0], r.report.wait.max, r.report.total.mean)"
```

Expect `[1, 1, 1] 19 42.333...`.

## 3. Realistic traffic: two policies on identical passengers

```bash
elevator-sim generate morning_rush -f 30 -s 1 -o out/demo/rush.csv
elevator-sim out/demo/rush.csv -f 30 -e 4 --html -q -o out/demo/rush_cost
elevator-sim out/demo/rush.csv -f 30 -e 4 --algorithm round_robin --html -q -o out/demo/rush_rr
open out/demo/rush_cost/report.html out/demo/rush_rr/report.html
```

Expect `Wrote 327 requests ... (247 inbound, 30 outbound, 50 inter-floor)`. In the reports, `cost`
gives a mean wait of **10.9** ticks (p95 26.7, max 35) against round-robin's **27.6** (p95 56, max 65).
Worth looking at: the time-space diagram (hover for every car's floor and load) and "Why: the
assigned car's state", where round-robin hands far more passengers a car that is moving away.

## 4. The benchmark, small

```bash
elevator-sim bench --suite quick --seeds 5 --dispatch cost,round_robin --motion look -o out/demo/bench
elevator-sim report out/demo/bench -o out/demo/bench.html && open out/demo/bench.html
```

Runs in under a second: `cost` vs `round_robin` on identical passengers with 95% confidence
intervals. The full studies use the same harness with 20 seeds (the standard suite takes about
40 seconds, the building sweep a few minutes; the results are committed, so there is no need to
re-run them).

## 5. The committed studies, as reports

```bash
elevator-sim report results/standard  -o out/demo/standard.html  && open out/demo/standard.html
elevator-sim report results/buildings -o out/demo/buildings.html && open out/demo/buildings.html
elevator-sim report results/parking   -o out/demo/parking.html   && open out/demo/parking.html
```

- **standard:** `cost` vs round-robin across all scenarios, then per experiment.
- **buildings:** "Varying floors", morning rush: `zone` (green) crosses below `cost` (blue) once the
  building is overloaded.
- **parking:** each parking policy against `stay`.

## Try a variation

| To see | Add to a run |
|---|---|
| another dispatch policy | `--algorithm nearest` (or `zone`, `round_robin`, `cost`) |
| another motion rule | `--motion scan` |
| parked idle cars | `--parking lobby` (or `spread`, `demand`) |
| a fairness weight | `--fairness 0.2` (cost only) |
| more cars, floors, capacity | `-e 6`, `-f 40`, `-c 4` |
| stops that cost nothing | `--door-time 0` |
| cars starting spread out | `--placement spread` |
| the event log, rebuilt later | `--journal out/demo/run.jsonl`, then `elevator-sim summarize out/demo/run.jsonl` |
| a heavier rush | `elevator-sim generate morning_rush -f 30 --load 1.5 -o out/demo/heavy.csv` |
| every option | `elevator-sim run --help` (also `bench --help`, `generate --help`) |

Bad input is reported, not guessed at: for example a request to floor 99 in a 60-floor building
prints `error: ...` and exits with code 2.
