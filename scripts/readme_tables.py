"""Print the README's result tables from results/*/summary.json.

    uv run python scripts/readme_tables.py            # all tables
    uv run python scripts/readme_tables.py fairness   # one table

Run the bench commands in the README first; this only formats what they wrote.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"
ORDER = ("quiet", "morning_rush", "lunch", "evening_rush")
MARK = {"better": "✓", "worse": "✗", "inconclusive": "?"}
LETTER = {"cost": "C", "nearest": "N", "zone": "Z", "round_robin": "R"}


def load(name: str) -> list[dict]:
    path = RESULTS / name / "summary.json"
    experiments = json.loads(path.read_text())["experiments"]
    return sorted(
        experiments,
        key=lambda e: (e["key"]["load"], ORDER.index(e["key"]["scenario"]), e["key"]["floors"]),
    )


def building(k: dict) -> str:
    return f"{k['floors']} × {k['cars']}"


def headline() -> str:
    rows = [
        "| scenario | building | requests / tick | round_robin | cost | Δ | 95% CI | wins "
        "| gap closed | B0 floor |",
        "|---|---|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    for e in load("standard"):
        k, c = e["key"], next(c for c in e["dispatch_axis"] if c["policy"] == "cost")
        rows.append(
            f"| {k['scenario']} | {building(k)} | {k['rate']:g} | {c['baseline_mean']:.1f} "
            f"| {c['mean']:.1f} | {c['delta_pct']:+.1%} | [{c['ci95'][0]:+.1f}, "
            f"{c['ci95'][1]:+.1f}] | {c['wins']} | {c['gap_closed']:.0%} "
            f"| {e['b0']['total_mean']:.1f} |"
        )
    return "\n".join(rows)


def policies() -> str:
    rows = [
        "| scenario | building | `nearest` vs RR | `zone` vs RR | LOOK vs SCAN (`cost`) "
        "| LOOK vs SCAN (RR) | ranking |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for e in load("standard"):
        k = e["key"]
        d = {c["policy"]: c for c in e["dispatch_axis"]}
        m = {c["dispatch"]: c for c in e["motion_axis"]}
        look = sorted(
            (c for c in e["combos"] if c["motion"] == "look"), key=lambda c: c["total_mean"]
        )

        def cell(c: dict) -> str:
            return f"{c['delta_pct']:+.0%} {MARK[c['verdict']]}"

        rows.append(
            f"| {k['scenario']} | {building(k)} | {cell(d['nearest'])} | {cell(d['zone'])} "
            f"| {cell(m['cost'])} | {cell(m['round_robin'])} "
            f"| {''.join(LETTER[c['dispatch']] for c in look)} |"
        )
    return "\n".join(rows)


def root_cause() -> str:
    rows = [
        "| scenario | building | wait RR → cost | detour RR → cost | assigned a car moving away "
        "RR → cost | chosen car distance RR → cost (nearest) | cars busy RR → cost |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for e in load("standard"):
        k = e["key"]
        c = {(x["dispatch"], x["motion"]): x for x in e["combos"]}
        rr, co = c[("round_robin", "look")], c[("cost", "look")]
        rows.append(
            f"| {k['scenario']} | {building(k)} | {rr['wait_mean']:.1f} → {co['wait_mean']:.1f} "
            f"| {rr['detour_mean']:.1f} → {co['detour_mean']:.1f} "
            f"| {rr['away_share']:.0%} (wait {rr['away_wait']:.0f}) → {co['away_share']:.0%} "
            f"(wait {co['away_wait']:.0f}) | {rr['chosen_distance']:.1f} → "
            f"{co['chosen_distance']:.1f} ({rr['nearest_distance']:.1f}) "
            f"| {rr['busy_share']:.0%} → {co['busy_share']:.0%} |"
        )
    return "\n".join(rows)


def capacity() -> str:
    rows = [
        "| scenario | building | passed by a full car: RR / nearest / cost | max wait: RR / "
        "nearest / cost | load CV: RR / nearest / zone / cost |",
        "|---|---|---:|---:|---:|",
    ]
    for e in load("standard"):
        k = e["key"]
        c = {x["dispatch"]: x for x in e["combos"] if x["motion"] == "look"}
        rr, ne, zo, co = c["round_robin"], c["nearest"], c["zone"], c["cost"]
        rows.append(
            f"| {k['scenario']} | {building(k)} | {rr['full_passby_share']:.1%} / "
            f"{ne['full_passby_share']:.1%} / {co['full_passby_share']:.1%} "
            f"| {rr['wait_max']:.0f} / {ne['wait_max']:.0f} / {co['wait_max']:.0f} "
            f"| {rr['load_cv']:.2f} / {ne['load_cv']:.2f} / {zo['load_cv']:.2f} / "
            f"{co['load_cv']:.2f} |"
        )
    return "\n".join(rows)


def sensitivity() -> str:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for e in load("sensitivity"):
        k = e["key"]
        groups[(k["scenario"], k["floors"], k["cars"])].append(e)

    def span(values: list[float]) -> str:
        lo, hi = min(values), max(values)
        return f"{lo:+.0%}" if round(lo, 2) == round(hi, 2) else f"{lo:+.0%} to {hi:+.0%}"

    def counts(verdicts: list[str]) -> str:
        n = Counter(verdicts)
        return " / ".join(f"{n[v]}{MARK[v]}" for v in ("better", "inconclusive", "worse") if n[v])

    rows = [
        "| scenario | building | `cost` vs RR | `nearest` vs RR | `zone` vs RR "
        "| LOOK vs SCAN (`cost`) | ranking at door 0 / 1 / 2 (lobby) |",
        "|---|---|---|---|---|---|---|",
    ]
    for (scenario, floors, cars), es in groups.items():

        def axis(policy: str, es: list[dict] = es) -> str:
            cs = [next(c for c in e["dispatch_axis"] if c["policy"] == policy) for e in es]
            return f"{span([c['delta_pct'] for c in cs])} ({counts([c['verdict'] for c in cs])})"

        ms = [next(c for c in e["motion_axis"] if c["dispatch"] == "cost") for e in es]
        ranks = []
        for e in sorted((e for e in es if e["key"]["placement"] == "lobby"),
                        key=lambda e: e["key"]["door_time"]):  # fmt: skip
            look = sorted(
                (c for c in e["combos"] if c["motion"] == "look"), key=lambda c: c["total_mean"]
            )
            ranks.append("".join(LETTER[c["dispatch"]] for c in look))
        rows.append(
            f"| {scenario} | {floors} × {cars} | {axis('cost')} | {axis('nearest')} "
            f"| {axis('zone')} | {span([c['delta_pct'] for c in ms])} "
            f"({counts([c['verdict'] for c in ms])}) | {' / '.join(ranks)} |"
        )
    return "\n".join(rows)


def fairness() -> str:
    rows = [
        "| scenario | building | load | `cost`: total / p95 wait / max wait "
        "| α = 0.2: Δ total | Δ wait p95 | Δ wait max |",
        "|---|---|---|---|---:|---:|---:|",
    ]
    for e in load("fairness"):
        k = e["key"]
        f = {x["policy"]: x for x in e["fairness"]}
        base, a = f["cost"], f["cost:0.2"]
        t, p, m = a["total_mean_vs_cost"], a["wait_p95_vs_cost"], a["wait_max_vs_cost"]
        rows.append(
            f"| {k['scenario']} | {building(k)} | {k['load']:g} ({k['rate']:g}/tick) "
            f"| {base['total_mean']:.1f} / {base['wait_p95']:.0f} / {base['wait_max']:.0f} "
            f"| {t['delta_pct']:+.1%} {MARK[t['verdict']]} "
            f"| {p['delta']:+.1f} {MARK[p['verdict']]} "
            f"| {m['delta']:+.1f} {MARK[m['verdict']]} |"
        )
    return "\n".join(rows)


def trips() -> str:
    """Per scenario: passengers per run by trip type and their mean wait, round_robin vs cost."""
    kinds = (("inbound", "inbound"), ("outbound", "outbound"), ("inter_floor", "inter-floor"))
    rows = [
        "| scenario | building | "
        + " | ".join(f"{label}: n, wait RR → cost" for _, label in kinds)
        + " |",
        "|---|---|" + "---:|" * len(kinds),
    ]
    for e in load("standard"):
        k = e["key"]
        c = {(x["dispatch"], x["motion"]): x for x in e["combos"]}
        rr, co = c[("round_robin", "look")], c[("cost", "look")]
        cells = [
            f"{co[kind + '_count']:.0f}, {rr[kind + '_wait_mean']:.1f} → "
            f"{co[kind + '_wait_mean']:.1f}"
            for kind, _ in kinds
        ]
        rows.append(f"| {k['scenario']} | {building(k)} | " + " | ".join(cells) + " |")
    return "\n".join(rows)


def buildings() -> str:
    """One-at-a-time building sweep: round_robin → cost mean total and ranking per setting."""
    experiments = load("buildings")
    base = {"floors": 30, "cars": 4, "capacity": 8}
    out = []
    for factor in ("floors", "cars", "capacity"):
        others = [f for f in base if f != factor]
        members = [e for e in experiments if all(e["key"][o] == base[o] for o in others)]
        values = sorted({e["key"][factor] for e in members})
        rows = [
            f"**Varying {factor}** ("
            + ", ".join(f"{o} {base[o]}" for o in others)
            + (", demand scales with floors" if factor == "floors" else "")
            + "): mean total, round_robin → cost (Δ), ranking",
            "",
            "| scenario | " + " | ".join(f"{factor} {v}" for v in values) + " |",
            "|---|" + "---:|" * len(values),
        ]
        for scenario in ORDER:
            cells = []
            for v in values:
                e = next(
                    x for x in members if x["key"]["scenario"] == scenario and x["key"][factor] == v
                )
                c = next(c for c in e["dispatch_axis"] if c["policy"] == "cost")
                look = sorted(
                    (x for x in e["combos"] if x["motion"] == "look"), key=lambda x: x["total_mean"]
                )
                rank = "".join(LETTER[x["dispatch"]] for x in look)
                cells.append(
                    f"{c['baseline_mean']:.0f} → {c['mean']:.0f} ({c['delta_pct']:+.0%}"
                    f"{'' if c['verdict'] == 'better' else ' ' + MARK[c['verdict']]}) {rank}"
                )
            rows.append(f"| {scenario} | " + " | ".join(cells) + " |")
        out.append("\n".join(rows))
    return "\n\n".join(out)


TABLES = {
    "headline": headline,
    "policies": policies,
    "root_cause": root_cause,
    "capacity": capacity,
    "sensitivity": sensitivity,
    "fairness": fairness,
    "trips": trips,
    "buildings": buildings,
}

if __name__ == "__main__":
    for name in sys.argv[1:] or TABLES:
        print(f"<!-- {name} -->\n{TABLES[name]()}\n")
