"""Self-contained HTML report: one file, inline SVG and a little JavaScript, no dependencies.

Two kinds of input:

- a run journal (``run.jsonl``): KPI tiles, the time-space diagram (each car's floor per tick,
  with a crosshair), the wait distribution, the assigned-car-state split, per-car load,
  observations and the passenger table;
- a benchmark summary (``summary.json``): ``cost`` vs ``round_robin`` across experiments with
  confidence intervals, then per experiment (chosen in one selector above the charts) mean total
  time by policy against the B0 floor, the wait tail, the root-cause diagnostics and, when present,
  the fairness frontier.

Every chart has a table view, colours come from a validated palette with light and dark steps, and
all text is escaped. Charts are plain SVG strings built here, so they are testable without a
browser.
"""

from __future__ import annotations

import html
import json
import math
from collections import defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from elevator_sim.bench import building_families
from elevator_sim.events import CarState
from elevator_sim.journal import Journal
from elevator_sim.report import ASSIGNMENT_STATES, TRIP_KINDS, RunReport, aggregate

# ---------------------------------------------------------------- styling

SLOTS = 8  # categorical colours available (never cycled; extra series fall back to muted grey)
POLICY_ORDER = ("cost", "nearest", "zone", "round_robin")

CSS = """
:root {
  color-scheme: light;
  --page: #f9f9f7; --surface: #fcfcfb; --ink: #0b0b0b; --ink-2: #52514e; --muted: #898781;
  --grid: #e1e0d9; --axis: #c3c2b7; --ring: rgba(11,11,11,0.10);
  --s1: #2a78d6; --s2: #eb6834; --s3: #1baf7a; --s4: #eda100;
  --s5: #e87ba4; --s6: #008300; --s7: #6250d6; --s8: #e34948;
  --good: #006300; --bad: #d03b3b;
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) {
    color-scheme: dark;
    --page: #0d0d0d; --surface: #1a1a19; --ink: #f0efec; --ink-2: #c3c2b7; --muted: #898781;
    --grid: #2c2c2a; --axis: #383835; --ring: rgba(255,255,255,0.10);
    --s1: #3987e5; --s2: #d95926; --s3: #199e70; --s4: #c98500;
    --s5: #d55181; --s6: #0ca30c; --s7: #9085e9; --s8: #e66767;
    --good: #0ca30c; --bad: #e66767;
  }
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --page: #0d0d0d; --surface: #1a1a19; --ink: #f0efec; --ink-2: #c3c2b7; --muted: #898781;
  --grid: #2c2c2a; --axis: #383835; --ring: rgba(255,255,255,0.10);
  --s1: #3987e5; --s2: #d95926; --s3: #199e70; --s4: #c98500;
  --s5: #d55181; --s6: #0ca30c; --s7: #9085e9; --s8: #e66767;
  --good: #0ca30c; --bad: #e66767;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--page); color: var(--ink);
  font: 14px/1.45 system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width: 980px; margin: 0 auto; padding: 24px 16px 64px; }
h1 { font-size: 22px; margin: 0 0 4px; }
h2 { font-size: 17px; margin: 32px 0 4px; }
h3 { font-size: 14px; margin: 0 0 2px; }
p.sub, .note { color: var(--ink-2); margin: 0 0 12px; }
.card { background: var(--surface); border: 1px solid var(--ring); border-radius: 8px;
  padding: 16px; margin: 12px 0; }
.grid2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(380px, 100%), 1fr));
  gap: 12px; }
.grid2 > .card { margin: 0; }
.kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; }
.kpi { background: var(--surface); border: 1px solid var(--ring); border-radius: 8px;
  padding: 12px; }
.kpi .label { color: var(--ink-2); font-size: 13px; }
.kpi .value { font-size: 26px; font-weight: 600; }
.kpi .unit { color: var(--muted); font-size: 13px; margin-left: 2px; }
svg { width: 100%; height: auto; display: block; overflow: visible; }
svg text { fill: var(--ink-2); font-size: 11px; }
svg .axis-label { fill: var(--muted); }
svg .value-label { fill: var(--ink); }
.legend { display: flex; flex-wrap: wrap; gap: 4px 16px; color: var(--ink-2); font-size: 13px;
  margin: 4px 0 8px; }
.legend span { display: inline-flex; align-items: center; gap: 6px; }
.key-rect { width: 12px; height: 12px; border-radius: 3px; display: inline-block; }
.key-line { width: 16px; height: 2px; border-radius: 1px; display: inline-block; }
.key-dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
details { margin-top: 8px; }
summary { cursor: pointer; color: var(--ink-2); font-size: 13px; }
table { border-collapse: collapse; width: 100%; font-size: 13px; margin-top: 6px;
  font-variant-numeric: tabular-nums; }
th, td { text-align: right; padding: 3px 8px; border-bottom: 1px solid var(--grid); }
th:first-child, td:first-child { text-align: left; }
th { color: var(--ink-2); font-weight: 600; }
.scroll { max-height: 320px; overflow: auto; }
.filters { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin: 16px 0 4px; }
select { font: inherit; padding: 4px 8px; border-radius: 6px; border: 1px solid var(--axis);
  background: var(--surface); color: var(--ink); max-width: 100%; }
.good { color: var(--good); } .bad { color: var(--bad); }
ul.obs { padding-left: 18px; margin: 4px 0; } ul.obs li { margin: 2px 0; }
#tip { position: fixed; pointer-events: none; z-index: 10; background: var(--surface);
  color: var(--ink); border: 1px solid var(--ring); border-radius: 6px; padding: 6px 8px;
  font-size: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.12); display: none; max-width: 280px; }
#tip .row { display: flex; align-items: center; gap: 6px; white-space: nowrap; }
#tip .row b { font-weight: 600; }
#tip .head { color: var(--ink-2); margin-bottom: 2px; }
[data-tip] { cursor: default; }
[data-tip]:hover, [data-tip]:focus { opacity: 0.8; outline: none; }
.seg { display: flex; gap: 2px; height: 28px; margin: 8px 0 4px; }
.seg div { border-radius: 4px; color: #fff; font-size: 12px; line-height: 28px; padding-left: 6px;
  overflow: hidden; white-space: nowrap; }
"""

JS = """
(() => {
  const tip = document.getElementById('tip');
  const show = (evt, head, rows) => {
    tip.replaceChildren();
    if (head) { const h = document.createElement('div'); h.className = 'head';
      h.textContent = head; tip.appendChild(h); }
    for (const [value, label, color] of rows) {
      const r = document.createElement('div'); r.className = 'row';
      if (color) { const k = document.createElement('span'); k.className = 'key-line';
        k.style.background = color; r.appendChild(k); }
      const b = document.createElement('b'); b.textContent = value; r.appendChild(b);
      const s = document.createElement('span'); s.textContent = label; r.appendChild(s);
      tip.appendChild(r);
    }
    tip.style.display = 'block';
    const x = Math.min(evt.clientX + 14, window.innerWidth - tip.offsetWidth - 8);
    const y = Math.min(evt.clientY + 14, window.innerHeight - tip.offsetHeight - 8);
    tip.style.left = x + 'px'; tip.style.top = y + 'px';
  };
  const hide = () => { tip.style.display = 'none'; };
  // Per-mark tooltips: data-tip = JSON [head, [[value, label], ...]]
  const markTip = (evt) => {
    const el = evt.target.closest('[data-tip]'); if (!el) return;
    const [head, rows] = JSON.parse(el.dataset.tip);
    const at = evt.clientX !== undefined && evt.clientX !== 0 ? evt
      : (() => { const r = el.getBoundingClientRect();
                 return {clientX: r.right, clientY: r.top}; })();
    show(at, head, rows);
  };
  document.addEventListener('pointerover', markTip);
  document.addEventListener('focusin', markTip);
  document.addEventListener('pointerout', (e) => { if (e.target.closest('[data-tip]')) hide(); });
  document.addEventListener('focusout', hide);
  // Crosshair charts: <svg data-xhair="id"> with a JSON payload script#id
  for (const svg of document.querySelectorAll('svg[data-xhair]')) {
    const data = JSON.parse(document.getElementById(svg.dataset.xhair).textContent);
    const line = svg.querySelector('.xhair');
    const toSvg = (evt) => { const p = svg.createSVGPoint(); p.x = evt.clientX; p.y = evt.clientY;
      return p.matrixTransform(svg.getScreenCTM().inverse()); };
    svg.addEventListener('pointermove', (evt) => {
      const p = toSvg(evt);
      const f = (p.x - data.x0) / (data.x1 - data.x0);
      if (f < 0 || f > 1) { line.setAttribute('visibility', 'hidden'); hide(); return; }
      const i = Math.round(f * (data.xs.length - 1));
      const x = data.x0 + (data.x1 - data.x0) * i / Math.max(1, data.xs.length - 1);
      line.setAttribute('x1', x); line.setAttribute('x2', x);
      line.setAttribute('visibility', 'visible');
      show(evt, data.xlabel + ' ' + data.xs[i],
        data.series.map(s => [s.values[i] + (s.extra ? s.extra[i] : ''), s.name, s.color]));
    });
    svg.addEventListener('pointerleave', () => {
      line.setAttribute('visibility', 'hidden'); hide(); });
  }
  // Experiment selector: shows one section[data-exp] at a time
  const sel = document.getElementById('exp');
  if (sel) {
    const apply = () => { for (const s of document.querySelectorAll('section[data-exp]'))
      s.hidden = s.dataset.exp !== sel.value; };
    sel.addEventListener('change', apply); apply();
  }
})();
"""


def _e(text: object) -> str:
    return html.escape(str(text), quote=True)


def _color(i: int) -> str:
    return f"var(--s{i + 1})" if i < SLOTS else "var(--muted)"


def _num(v: float, digits: int = 1) -> str:
    if isinstance(v, int) or float(v).is_integer():
        return f"{int(v):,}"
    return f"{v:,.{digits}f}"


def _tip(head: str, rows: Sequence[tuple[str, str]]) -> str:
    return _e(json.dumps([head, [list(r) for r in rows]]))


def nice_ticks(lo: float, hi: float, count: int = 5) -> list[float]:
    """Round tick values covering [lo, hi] (1, 2, 2.5 or 5 times a power of ten)."""
    if hi <= lo:
        hi = lo + 1
    raw = (hi - lo) / max(1, count)
    power = 10 ** math.floor(math.log10(raw))
    step = next(m * power for m in (1, 2, 2.5, 5, 10) if m * power >= raw)
    start = math.floor(lo / step) * step
    ticks = []
    t = start
    while t <= hi + step * 1e-9:
        ticks.append(round(t, 10))
        t += step
    if ticks[-1] < hi:
        ticks.append(round(t, 10))
    return ticks


@dataclass(frozen=True)
class Scale:
    lo: float
    hi: float
    a: float
    b: float

    def __call__(self, v: float) -> float:
        if self.hi == self.lo:
            return self.a
        return self.a + (v - self.lo) * (self.b - self.a) / (self.hi - self.lo)


def _svg(width: int, height: int, body: str, label: str, extra: str = "") -> str:
    return (
        f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{_e(label)}"{extra}>'
        f"<title>{_e(label)}</title>{body}</svg>"
    )


def _bar(x0: float, x1: float, y: float, h: float, r: float = 4) -> str:
    """Horizontal bar from the baseline x0 to x1: rounded data end, square at the baseline."""
    w = abs(x1 - x0)
    r = min(r, w, h / 2)
    if w < 0.5:
        return ""
    if x1 >= x0:
        return (
            f"M{x0:.1f},{y:.1f}H{x1 - r:.1f}A{r},{r} 0 0 1 {x1:.1f},{y + r:.1f}"
            f"V{y + h - r:.1f}A{r},{r} 0 0 1 {x1 - r:.1f},{y + h:.1f}H{x0:.1f}Z"
        )
    return (
        f"M{x0:.1f},{y:.1f}H{x1 + r:.1f}A{r},{r} 0 0 0 {x1:.1f},{y + r:.1f}"
        f"V{y + h - r:.1f}A{r},{r} 0 0 0 {x1 + r:.1f},{y + h:.1f}H{x0:.1f}Z"
    )


def _legend(items: Sequence[tuple[str, str]], kind: str = "rect") -> str:
    spans = "".join(
        f'<span><i class="key-{kind}" style="background:{color}"></i>{_e(name)}</span>'
        for name, color in items
    )
    return f'<div class="legend">{spans}</div>'


def _table(header: Sequence[str], rows: Sequence[Sequence[object]], scroll: bool = False) -> str:
    head = "".join(f"<th>{_e(h)}</th>" for h in header)
    body = "".join("<tr>" + "".join(f"<td>{_e(c)}</td>" for c in r) + "</tr>" for r in rows)
    table = f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
    return f'<div class="scroll">{table}</div>' if scroll else table


def _table_view(
    header: Sequence[str], rows: Sequence[Sequence[object]], scroll: bool = False
) -> str:
    return f"<details><summary>Table view</summary>{_table(header, rows, scroll)}</details>"


def _card(title: str, sub: str, body: str) -> str:
    sub_html = f'<p class="sub">{_e(sub)}</p>' if sub else ""
    return f'<div class="card"><h3>{_e(title)}</h3>{sub_html}{body}</div>'


# ---------------------------------------------------------------- chart builders


def grouped_hbar(
    categories: Sequence[str],
    series: Sequence[tuple[str, str, Sequence[float | None]]],
    unit: str,
    label: str,
    reference: tuple[str, float] | None = None,
    digits: int = 1,
    width: int = 720,
) -> str:
    """Horizontal bars, one row per category, one bar per series; optional reference line.

    Use ``width`` ~420 for half-width cards so text renders at its nominal size.
    """
    left, right = (130, 60) if width >= 600 else (90, 40)
    bar_h, gap, row_gap = 14, 2, 12
    row_h = len(series) * (bar_h + gap) - gap + row_gap
    top = 22 if reference else 8
    height = top + len(categories) * row_h + 28
    values = [v for _, _, vs in series for v in vs if v is not None]
    hi = max([*values, reference[1] if reference else 0, 1e-9])
    ticks = nice_ticks(0, hi, 5)
    x = Scale(0, ticks[-1], left, width - right)
    parts = []
    for t in ticks:
        parts.append(
            f'<line x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top}" y2="{height - 22}" '
            f'stroke="var(--grid)" stroke-width="1"/>'
            f'<text x="{x(t):.1f}" y="{height - 8}" text-anchor="middle">{_num(t)}</text>'
        )
    for ci, cat in enumerate(categories):
        y0 = top + ci * row_h
        parts.append(
            f'<text x="{left - 8}" y="{y0 + (row_h - row_gap) / 2 + 4:.1f}" '
            f'text-anchor="end" class="value-label">{_e(cat)}</text>'
        )
        for si, (name, color, vs) in enumerate(series):
            v = vs[ci]
            if v is None:
                continue
            y = y0 + si * (bar_h + gap)
            tip = _tip(cat, [(f"{_num(v, digits)} {unit}", name)])
            parts.append(
                f'<path d="{_bar(x(0), x(v), y, bar_h)}" fill="{color}" tabindex="0" '
                f'data-tip="{tip}"/>'
                f'<text x="{x(v) + 4:.1f}" y="{y + bar_h - 3}" class="value-label">'
                f"{_num(v, digits)}</text>"
            )
    parts.append(
        f'<line x1="{x(0)}" x2="{x(0)}" y1="{top}" y2="{height - 22}" stroke="var(--axis)"/>'
    )
    if reference:
        name, v = reference
        parts.append(
            f'<line x1="{x(v):.1f}" x2="{x(v):.1f}" y1="{top}" y2="{height - 22}" '
            f'stroke="var(--ink-2)" stroke-width="1.5"/>'
            f'<text x="{x(v):.1f}" y="12" text-anchor="middle" class="value-label">'
            f"{_e(name)} {_num(v)}</text>"
        )
    return _svg(width, height, "".join(parts), label)


def delta_chart(
    rows: Sequence[tuple[str, float, float, float, str]], label: str, unit: str = "ticks"
) -> str:
    """Δ vs a baseline per row (negative = better), bar plus 95% CI whisker, verdict on hover."""
    width, left, right = 720, 300, 70
    bar_h, row_h, top = 12, 22, 8
    height = top + len(rows) * row_h + 28
    lo = min([0.0, *(r[2] for r in rows)])
    hi = max([0.0, *(r[3] for r in rows)])
    pad = (hi - lo) * 0.18  # room for the value label beyond the longest whisker
    ticks = nice_ticks(lo - pad if lo < 0 else lo, hi + pad if hi > 0 else hi, 5)
    x = Scale(ticks[0], ticks[-1], left, width - right)
    parts = []
    for t in ticks:
        parts.append(
            f'<line x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top}" y2="{height - 22}" '
            f'stroke="var(--grid)"/>'
            f'<text x="{x(t):.1f}" y="{height - 8}" text-anchor="middle">{_num(t)}</text>'
        )
    for i, (name, delta, ci_lo, ci_hi, verdict) in enumerate(rows):
        y = top + i * row_h
        tip = _tip(
            name,
            [
                (f"{delta:+.1f} {unit}", "Δ vs baseline"),
                (f"[{ci_lo:+.1f}, {ci_hi:+.1f}]", "95% CI"),
                (verdict, "verdict"),
            ],
        )
        parts.append(
            f'<text x="{left - 8}" y="{y + bar_h - 1}" text-anchor="end" class="value-label">'
            f"{_e(name)}</text>"
            f'<path d="{_bar(x(0), x(delta), y, bar_h)}" fill="var(--s1)" tabindex="0" '
            f'data-tip="{tip}"/>'
            f'<line x1="{x(ci_lo):.1f}" x2="{x(ci_hi):.1f}" y1="{y + bar_h / 2}" '
            f'y2="{y + bar_h / 2}" stroke="var(--ink)" stroke-width="1.5"/>'
        )
        anchor_x = x(min(delta, ci_lo)) - 4 if delta < 0 else x(max(delta, ci_hi)) + 4
        anchor = "end" if delta < 0 else "start"
        parts.append(
            f'<text x="{anchor_x:.1f}" y="{y + bar_h - 1}" text-anchor="{anchor}">'
            f"{delta:+.1f}</text>"
        )
    parts.append(
        f'<line x1="{x(0):.1f}" x2="{x(0):.1f}" y1="{top}" y2="{height - 22}" '
        f'stroke="var(--axis)"/>'
    )
    return _svg(width, height, "".join(parts), label)


_XHAIR_IDS = iter(range(1, 10**6))


def line_chart(
    xs: Sequence[float],
    series: Sequence[tuple[str, str, Sequence[float], Sequence[str] | None]],
    x_label: str,
    y_label: str,
    label: str,
    height: int = 320,
    y_range: tuple[float, float] | None = None,
    step: bool = False,
    width: int = 720,
    markers: bool = False,
) -> str:
    """Multi-line chart over shared xs, with a crosshair that reads every series at that x."""
    left, right, top, bottom = 48, 16, 24, 36
    lo, hi = y_range or (
        min(v for _, _, vs, _ in series for v in vs),
        max(v for _, _, vs, _ in series for v in vs),
    )
    y_ticks = nice_ticks(lo, hi, 5)
    x_ticks = (
        list(xs)
        if markers and len(xs) <= 8
        else nice_ticks(xs[0], xs[-1], 8 if width >= 600 else 4)
    )
    x = Scale(x_ticks[0], x_ticks[-1], left, width - right)
    y = Scale(y_ticks[0], y_ticks[-1], height - bottom, top)
    parts = []
    for t in y_ticks:
        parts.append(
            f'<line x1="{left}" x2="{width - right}" y1="{y(t):.1f}" y2="{y(t):.1f}" '
            f'stroke="var(--grid)"/>'
            f'<text x="{left - 6}" y="{y(t) + 4:.1f}" text-anchor="end">{_num(t)}</text>'
        )
    for t in x_ticks:
        parts.append(
            f'<text x="{x(t):.1f}" y="{height - bottom + 16}" text-anchor="middle">{_num(t)}</text>'
        )
    parts.append(
        f'<line x1="{left}" x2="{width - right}" y1="{height - bottom}" y2="{height - bottom}" '
        f'stroke="var(--axis)"/>'
        f'<text x="{width - right}" y="{height - 4}" text-anchor="end" class="axis-label">'
        f"{_e(x_label)}</text>"
        f'<text x="0" y="12" class="axis-label">{_e(y_label)} ↑</text>'
    )
    for _, color, vs, _ in series:
        points: list[str] = []
        for i, (xv, yv) in enumerate(zip(xs, vs, strict=True)):
            if step and i:
                points.append(f"{x(xv):.1f},{y(vs[i - 1]):.1f}")
            points.append(f"{x(xv):.1f},{y(yv):.1f}")
        parts.append(
            f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" '
            f'stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>'
        )
        if markers:
            parts.extend(
                f'<circle cx="{x(xv):.1f}" cy="{y(yv):.1f}" r="4" fill="{color}" '
                f'stroke="var(--surface)" stroke-width="2"/>'
                for xv, yv in zip(xs, vs, strict=True)
            )
    parts.append(
        f'<line class="xhair" x1="0" x2="0" y1="{top}" y2="{height - bottom}" '
        f'stroke="var(--muted)" visibility="hidden"/>'
        f'<rect x="{left}" y="{top}" width="{width - left - right}" '
        f'height="{height - top - bottom}" fill="transparent"/>'
    )
    payload_id = f"xh{next(_XHAIR_IDS)}"
    payload = {
        "x0": x(xs[0]),
        "x1": x(xs[-1]),
        "xs": [_num(v) for v in xs],
        "xlabel": x_label,
        "series": [
            {"name": name, "color": color, "values": [_num(v) for v in vs], "extra": extra}
            for name, color, vs, extra in series
        ],
    }
    script = (
        f'<script type="application/json" id="{payload_id}">'
        f"{json.dumps(payload).replace('</', '<' + chr(92) + '/')}</script>"
    )
    return _svg(width, height, "".join(parts), label, f' data-xhair="{payload_id}"') + script


def frontier_chart(points: Sequence[tuple[str, float, float]], label: str) -> str:
    """Mean total (x) against max wait (y) per fairness weight, joined in alpha order."""
    width, height, left, right, top, bottom = 720, 300, 52, 24, 26, 40
    xs = [p[1] for p in points]
    ys = [p[2] for p in points]
    pad_x = max(0.5, (max(xs) - min(xs)) * 0.25)
    pad_y = max(1.0, (max(ys) - min(ys)) * 0.25)
    x_ticks = nice_ticks(min(xs) - pad_x, max(xs) + pad_x, 5)
    y_ticks = nice_ticks(min(ys) - pad_y, max(ys) + pad_y, 5)
    x = Scale(x_ticks[0], x_ticks[-1], left, width - right)
    y = Scale(y_ticks[0], y_ticks[-1], height - bottom, top)
    parts = []
    for t in y_ticks:
        parts.append(
            f'<line x1="{left}" x2="{width - right}" y1="{y(t):.1f}" y2="{y(t):.1f}" '
            f'stroke="var(--grid)"/>'
            f'<text x="{left - 6}" y="{y(t) + 4:.1f}" text-anchor="end">{_num(t)}</text>'
        )
    for t in x_ticks:
        parts.append(
            f'<text x="{x(t):.1f}" y="{height - bottom + 16}" text-anchor="middle">{_num(t)}</text>'
        )
    parts.append(
        f'<line x1="{left}" x2="{width - right}" y1="{height - bottom}" y2="{height - bottom}" '
        f'stroke="var(--axis)"/>'
        f'<text x="{width - right}" y="{height - 6}" text-anchor="end" class="axis-label">'
        f"mean total time per passenger (ticks) →</text>"
        f'<text x="0" y="12" class="axis-label">max wait (ticks) ↑</text>'
    )
    path = " ".join(f"{x(px):.1f},{y(py):.1f}" for _, px, py in points)
    parts.append(f'<polyline points="{path}" fill="none" stroke="var(--s1)" stroke-width="2"/>')
    for name, px, py in points:
        tip = _tip(name, [(f"{py:.1f} ticks", "max wait"), (f"{px:.1f} ticks", "mean total")])
        parts.append(
            f'<circle cx="{x(px):.1f}" cy="{y(py):.1f}" r="12" fill="transparent" tabindex="0" '
            f'data-tip="{tip}"/>'
            f'<circle cx="{x(px):.1f}" cy="{y(py):.1f}" r="5" fill="var(--s1)" '
            f'stroke="var(--surface)" stroke-width="2" pointer-events="none"/>'
            f'<text x="{x(px) + 8:.1f}" y="{y(py) - 8:.1f}" class="value-label">{_e(name)}</text>'
        )
    return _svg(width, height, "".join(parts), label)


def segmented_bar(parts: Sequence[tuple[str, float, str]], label: str) -> str:
    """One whole split into parts (tall segmented bar), share printed where it fits, + legend."""
    total = sum(v for _, v, _ in parts) or 1
    blocks = []
    for name, v, color in parts:
        if v <= 0:
            continue
        share = v / total
        text = f"{share:.0%}" if share >= 0.07 else ""
        ink = "#0b0b0b" if color == "var(--s4)" else "#fff"
        tip = _tip(name, [(f"{share:.0%}", "of passengers")])
        blocks.append(
            f'<div style="flex:{share:.4f};background:{color};color:{ink}" tabindex="0" '
            f'data-tip="{tip}">{text}</div>'
        )
    legend = _legend([(name, color) for name, _, color in parts])
    return f'<div class="seg" role="img" aria-label="{_e(label)}">{"".join(blocks)}</div>{legend}'


# ---------------------------------------------------------------- page shell


def _page(title: str, subtitle: str, body: str) -> str:
    return (
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f"<title>{_e(title)}</title><style>{CSS}</style></head><body><main>"
        f'<h1>{_e(title)}</h1><p class="sub">{_e(subtitle)}</p>{body}'
        f'</main><div id="tip" role="tooltip"></div><script>{JS}</script></body></html>\n'
    )


def _kpis(items: Sequence[tuple[str, str, str]]) -> str:
    tiles = "".join(
        f'<div class="kpi"><div class="label">{_e(label)}</div>'
        f'<div class="value">{_e(value)}<span class="unit">{_e(unit)}</span></div></div>'
        for label, value, unit in items
    )
    return f'<div class="kpis">{tiles}</div>'


# ---------------------------------------------------------------- run report

TRIP_LABELS = {"inbound": "inbound", "outbound": "outbound", "inter_floor": "inter-floor"}

STATE_LABELS = {
    "idle": "idle",
    "on_the_way": "on the way",
    "ahead_opposite": "ahead, going the other way",
    "moving_away": "moving away",
}


def render_run(journal: Journal, report: RunReport | None = None) -> str:
    """The report for one simulation run."""
    report = report or aggregate(journal)
    cfg = report.config
    floors: dict[int, dict[int, int]] = defaultdict(dict)
    loads: dict[int, dict[int, int]] = defaultdict(dict)
    for e in journal.events(CarState):
        floors[e.car][e.tick] = e.floor
        loads[e.car][e.tick] = e.load
    ticks = sorted({t for rows in floors.values() for t in rows})
    cars = sorted(floors)

    kpis = _kpis(
        [
            ("Passengers delivered", f"{len(report.passengers):,}", ""),
            ("Mean wait", _num(report.wait.mean), " ticks"),
            ("p95 wait", _num(report.wait.p95), " ticks"),
            ("Max wait", _num(report.wait.max), " ticks"),
            ("Mean total time", _num(report.total.mean), " ticks"),
            ("Last drop-off", f"t={report.makespan}", ""),
        ]
    )

    body = [kpis]
    if ticks:
        series = [
            (
                f"car {c}",
                _color(i),
                [floors[c][t] for t in ticks],
                [f" (load {loads[c][t]})" for t in ticks],
            )
            for i, c in enumerate(cars)
        ]
        chart = line_chart(
            ticks,
            series,
            "tick",
            "floor",
            "Each car's floor at every tick",
            height=360,
            y_range=(1, cfg.floors),
        )
        legend = _legend([(f"car {c}", _color(i)) for i, c in enumerate(cars)], "line")
        table = _table_view(
            ["tick", *(f"car {c}" for c in cars)],
            [[t, *(floors[c][t] for c in cars)] for t in ticks],
            scroll=True,
        )
        body.append(
            _card(
                "Time-space diagram",
                "Each car's floor at every tick (the positions log). Flat steps are stops; "
                "hover for every car's floor and load at that tick.",
                legend + chart + table,
            )
        )

    waits = sorted(r.wait for r in report.passengers)
    if waits:
        n = len(waits)
        cdf = [(i + 1) / n * 100 for i in range(n)]
        chart = line_chart(
            waits,
            [("passengers who waited at most this long", "var(--s1)", cdf, None)],
            "wait (ticks)",
            "% of passengers",
            "Wait time distribution",
            height=260,
            y_range=(0, 100),
            step=True,
        )
        table = _table_view(
            ["statistic", "wait (ticks)"],
            [
                ["min", _num(report.wait.min)],
                ["p50", _num(report.wait.p50)],
                ["p90", _num(report.wait.p90)],
                ["p95", _num(report.wait.p95)],
                ["max", _num(report.wait.max)],
            ],
        )
        body.append(
            _card(
                "Wait time distribution",
                f"Share of passengers picked up within a given wait. p50 {_num(report.wait.p50)}"
                f", p95 {_num(report.wait.p95)}, max {_num(report.wait.max)} ticks.",
                chart + table,
            )
        )

    kinds = [k for k in TRIP_KINDS if report.by_trip[k].count]
    if kinds:
        trips = grouped_hbar(
            [TRIP_LABELS[k] for k in kinds],
            [
                ("mean wait", _color(0), [report.by_trip[k].wait.mean for k in kinds]),
                ("p95 wait", _color(1), [report.by_trip[k].wait.p95 for k in kinds]),
            ],
            "ticks",
            "Wait by trip type",
        )
        trip_table = _table_view(
            ["trip type", "passengers", "wait mean", "wait p95", "wait max", "total mean"],
            [
                [
                    TRIP_LABELS[k],
                    report.by_trip[k].count,
                    _num(report.by_trip[k].wait.mean),
                    _num(report.by_trip[k].wait.p95),
                    _num(report.by_trip[k].wait.max),
                    _num(report.by_trip[k].total.mean),
                ]
                for k in kinds
            ],
        )
        counts = ", ".join(f"{report.by_trip[k].count} {TRIP_LABELS[k]}" for k in kinds)
        body.append(
            _card(
                "Wait by trip type",
                f"Inbound = from the lobby, outbound = to the lobby. Passengers: {counts}.",
                _legend([("mean wait", _color(0)), ("p95 wait", _color(1))]) + trips + trip_table,
            )
        )

    d = report.diagnostics
    seg = segmented_bar(
        [
            (STATE_LABELS[name], d.assignment[name].count, _color(i))
            for i, name in enumerate(ASSIGNMENT_STATES)
        ],
        "State of the assigned car when each passenger was assigned",
    )
    state_table = _table_view(
        ["assigned car was", "share", "mean wait (ticks)"],
        [
            [STATE_LABELS[n], f"{d.assignment[n].share:.0%}", _num(d.assignment[n].mean_wait)]
            for n in ASSIGNMENT_STATES
        ],
    )
    diag_note = (
        f"Detour {_num(d.detour.mean)} ticks vs {_num(report.wait.mean)} of waiting; chosen car "
        f"{_num(d.chosen_distance)} floors away (nearest {_num(d.nearest_distance)}); cars busy "
        f"{d.busy_share:.0%}; {_num(d.distance_per_passenger)} floors per passenger; "
        f"{d.full_passby_share:.1%} passed by a full car."
    )
    per_car = list(report.per_car.values())
    car_chart = grouped_hbar(
        [f"car {c.car}" for c in per_car],
        [("passengers", "var(--s1)", [c.passengers for c in per_car])],
        "passengers",
        "Passengers delivered per car",
        digits=0,
        width=420,
    )
    car_table = _table_view(
        ["car", "passengers", "trips", "floors travelled", "stops", "peak load"],
        [
            [c.car, c.passengers, c.trips, c.distance, c.stops, f"{c.peak_load}/{c.capacity}"]
            for c in per_car
        ],
    )
    body.append(
        '<div class="grid2">'
        + _card("Why: the assigned car's state", diag_note, seg + state_table)
        + _card("Load per car", "Passengers delivered by each car.", car_chart + car_table)
        + "</div>"
    )
    obs = "".join(f"<li>{_e(o)}</li>" for o in report.observations)
    body.append(_card("Observations", "", f'<ul class="obs">{obs}</ul>'))
    body.append(
        _card(
            "Passengers",
            "",
            _table_view(
                ["id", "car", "from", "to", "requested", "boarded", "alighted", "wait", "total"],
                [
                    [
                        r.id,
                        r.car,
                        r.source,
                        r.dest,
                        r.requested,
                        r.boarded,
                        r.alighted,
                        r.wait,
                        r.total,
                    ]
                    for r in report.passengers
                ],
                scroll=True,
            ),
        )
    )
    capacities = "/".join(sorted({str(c.capacity) for c in cfg.cars}))
    subtitle = (
        f"{cfg.floors} floors, {len(cfg.cars)} cars, capacity {capacities}, door_time "
        f"{cfg.door_time} · dispatch {report.dispatch}, motion {report.motion}"
    )
    return _page("Elevator simulation run", subtitle, "".join(body))


# ---------------------------------------------------------------- benchmark report


def _policy_sort(name: str) -> tuple[int, str]:
    base = name.partition(":")[0]
    return (POLICY_ORDER.index(base) if base in POLICY_ORDER else len(POLICY_ORDER), name)


def _short_title(key: Mapping[str, Any]) -> str:
    load = f"load {key['load']:.3g}" if "load" in key else f"{key['rate']}/tick"
    return (
        f"{key['scenario']} · {key['floors']}×{key['cars']} · cap {key['capacity']} · "
        f"door {key['door_time']} · {key['placement']} · {load}"
    )


def render_bench(summary: Mapping[str, Any]) -> str:
    """The report for a benchmark summary (``summary.json``)."""
    experiments: list[Mapping[str, Any]] = summary["experiments"]
    body: list[str] = []

    headline = []
    for e in experiments:
        c = next((c for c in e["dispatch_axis"] if c["policy"] == "cost"), None)
        if c:
            headline.append((_short_title(e["key"]), c))
    if headline:
        rows = [(t, c["delta"], c["ci95"][0], c["ci95"][1], c["verdict"]) for t, c in headline]
        chart = delta_chart(rows, "cost vs round_robin, mean total time per passenger")
        table = _table_view(
            ["experiment", "round_robin", "cost", "Δ", "95% CI", "wins", "gap closed", "verdict"],
            [
                [
                    t,
                    _num(c["baseline_mean"]),
                    _num(c["mean"]),
                    f"{c['delta_pct']:+.1%}",
                    f"[{c['ci95'][0]:+.2f}, {c['ci95'][1]:+.2f}]",
                    c["wins"],
                    "n/a" if c["gap_closed"] is None else f"{c['gap_closed']:.0%}",
                    c["verdict"],
                ]
                for t, c in headline
            ],
        )
        body.append(
            _card(
                "cost vs round_robin across experiments",
                "Change in mean total time per passenger (ticks; left is better), with the "
                "paired 95% bootstrap interval. LOOK motion.",
                chart + table,
            )
        )

    body.extend(_building_cards(experiments))

    options = "".join(
        f'<option value="{i}">{_e(_short_title(e["key"]))}</option>'
        for i, e in enumerate(experiments)
    )
    body.append(
        '<div class="filters"><label for="exp">Experiment</label>'
        f'<select id="exp">{options}</select></div>'
    )
    for i, e in enumerate(experiments):
        body.append(f'<section data-exp="{i}">' + _experiment_section(e) + "</section>")
    claim = summary.get("claim_rule", "")
    return _page(
        "Elevator benchmark",
        f"{len(experiments)} experiments · claim rule: {claim} · "
        f"{summary.get('resamples', '')} bootstrap resamples",
        "".join(body),
    )


POLICY_COLORS = {"cost": 0, "nearest": 1, "zone": 2, "round_robin": 3}


def _building_cards(experiments: Sequence[Mapping[str, Any]]) -> list[str]:
    """One-at-a-time building sweep: mean total time vs each setting, one chart per scenario."""
    cards = []
    for factor, members in building_families(experiments).items():
        values = sorted({e["key"][factor] for e in members})
        charts = []
        policies: list[str] = []
        for scenario in dict.fromkeys(e["key"]["scenario"] for e in members):
            by_value = {
                e["key"][factor]: {
                    c["dispatch"]: c["total_mean"] for c in e["combos"] if c["motion"] == "look"
                }
                for e in members
                if e["key"]["scenario"] == scenario
            }
            policies = sorted(
                {d for row in by_value.values() for d in row if d in POLICY_COLORS},
                key=_policy_sort,
            )
            series = [
                (d, _color(POLICY_COLORS[d]), [by_value[v][d] for v in values], None)
                for d in policies
                if all(d in by_value.get(v, {}) for v in values)
            ]
            if not series:
                continue
            chart = line_chart(
                values, series, factor, "mean total (ticks)",
                f"{scenario}: mean total time vs {factor}", height=240, width=420, markers=True,
            )  # fmt: skip
            charts.append(_card(scenario, "", chart))
        legend = _legend([(d, _color(POLICY_COLORS[d])) for d in policies], "line")
        base = {k: v for k, v in members[0]["key"].items() if k in ("floors", "cars", "capacity")}
        fixed = ", ".join(f"{k} {v}" for k, v in base.items() if k != factor)
        note = " Demand scales with floors (same people per floor)." if factor == "floors" else ""
        cards.append(
            f'<h2>Varying {_e(factor)}</h2><p class="sub">Mean total time per passenger (LOOK) '
            f"as {_e(factor)} changes; {_e(fixed)} fixed.{_e(note)}</p>{legend}"
            f'<div class="grid2">{"".join(charts)}</div>'
        )
    return cards


def _experiment_section(e: Mapping[str, Any]) -> str:
    combos = e["combos"]
    dispatches = sorted({c["dispatch"] for c in combos}, key=_policy_sort)
    motions = [m for m in ("look", "scan") if any(c["motion"] == m for c in combos)]
    by = {(c["dispatch"], c["motion"]): c for c in combos}
    out = [f'<h2>{_e(e["title"])}</h2><p class="sub">{e["seeds"]} seeds, paired.</p>']

    series = [
        (m.upper(), _color(i), [by.get((d, m), {}).get("total_mean") for d in dispatches])
        for i, m in enumerate(motions)
    ]
    chart = grouped_hbar(
        dispatches,
        series,
        "ticks",
        "Mean total time per passenger by policy",
        reference=("B0 floor", e["b0"]["total_mean"]),
    )
    table = _table_view(
        ["dispatch", "motion", "total", "wait", "wait p95", "wait max", "excess"],
        [
            [
                c["dispatch"],
                c["motion"],
                _num(c["total_mean"]),
                _num(c["wait_mean"]),
                _num(c["wait_p95"]),
                _num(c["wait_max"]),
                _num(c["excess_mean"]),
            ]
            for c in sorted(combos, key=lambda c: (_policy_sort(c["dispatch"]), c["motion"]))
        ],
    )
    out.append(
        _card(
            "Mean total time per passenger",
            "Lower is better. The B0 line is the theoretical floor (picked up at once, direct "
            "ride); nothing can beat it.",
            _legend([(m.upper(), _color(i)) for i, m in enumerate(motions)]) + chart + table,
        )
    )

    if "look" in motions:
        look = [by[(d, "look")] for d in dispatches if (d, "look") in by]
        names = [c["dispatch"] for c in look]
        tail_series = [
            ("mean", _color(0), [c["wait_mean"] for c in look]),
            ("p95", _color(1), [c["wait_p95"] for c in look]),
            ("max", _color(2), [c["wait_max"] for c in look]),
        ]
        tail = grouped_hbar(names, tail_series, "ticks", "Wait: mean, p95 and max (LOOK)")
        out.append(
            _card(
                "Wait time: average and tail (LOOK)",
                "Fairness is judged on the tail: p95 and max wait (means over seeds).",
                _legend([(n, c) for n, c, _ in tail_series]) + tail,
            )
        )
        if all("inbound_wait_mean" in c for c in look):
            kinds = [k for k in TRIP_KINDS if any(c[f"{k}_count"] for c in look)]
            trip_series = [
                (TRIP_LABELS[k], _color(i), [c[f"{k}_wait_mean"] for c in look])
                for i, k in enumerate(kinds)
            ]
            counts = ", ".join(f"{look[0][k + '_count']:.0f} {TRIP_LABELS[k]}" for k in kinds)
            trip_chart = grouped_hbar(names, trip_series, "ticks", "Mean wait by trip type (LOOK)")
            trip_table = _table_view(
                ["dispatch", *(f"{TRIP_LABELS[k]} wait mean / p95" for k in kinds)],
                [
                    [
                        c["dispatch"],
                        *(
                            f"{_num(c[k + '_wait_mean'])} / {_num(c[k + '_wait_p95'])}"
                            for k in kinds
                        ),
                    ]
                    for c in look
                ],
            )
            out.append(
                _card(
                    "Wait by trip type (LOOK)",
                    f"Mean wait per trip type; inbound = from the lobby, outbound = to the lobby. "
                    f"Passengers per run (mean): {counts}.",
                    _legend([(n, c) for n, c, _ in trip_series]) + trip_chart + trip_table,
                )
            )
        if all("away_share" in c for c in look):
            away = grouped_hbar(
                names,
                [("moving away", "var(--s1)", [c["away_share"] * 100 for c in look])],
                "% of passengers",
                "Share of passengers assigned to a car moving away from them",
                digits=0,
                width=420,
            )
            busy = grouped_hbar(
                names,
                [("busy", "var(--s1)", [c["busy_share"] * 100 for c in look])],
                "% of car time",
                "Share of car time spent busy",
                digits=0,
                width=420,
            )
            diag_table = _table_view(
                [
                    "dispatch",
                    "away share",
                    "away wait",
                    "idle picks",
                    "chosen / nearest dist",
                    "busy",
                    "floors / passenger",
                    "riders / stop",
                    "full pass-bys",
                ],
                [
                    [
                        c["dispatch"],
                        f"{c['away_share']:.0%}",
                        _num(c["away_wait"]),
                        f"{c['idle_pick_share']:.0%}",
                        f"{_num(c['chosen_distance'])} / {_num(c['nearest_distance'])}",
                        f"{c['busy_share']:.0%}",
                        _num(c["distance_per_passenger"]),
                        _num(c["riders_per_stop"], 2),
                        f"{c['full_passby_share']:.1%}",
                    ]
                    for c in look
                ],
            )
            out.append(
                '<div class="grid2">'
                + _card(
                    "Why: assigned to a car moving away",
                    "% of passengers whose car was heading away from them when assigned.",
                    away,
                )
                + _card(
                    "Why: how busy the cars were",
                    "% of car time not idle; near 100% means every request queues.",
                    busy + diag_table,
                )
                + "</div>"
            )

    if e.get("fairness"):
        points = [(f"α = {f['fairness']:g}", f["total_mean"], f["wait_max"]) for f in e["fairness"]]
        chart = frontier_chart(points, "Fairness frontier: mean total vs max wait per α")
        rows = []
        for f in e["fairness"]:
            deltas = [
                f"{f[m]['delta']:+.1f} ({f[m]['verdict']})" if m in f else "baseline"
                for m in ("total_mean_vs_cost", "wait_p95_vs_cost", "wait_max_vs_cost")
            ]
            rows.append(
                [
                    f"{f['fairness']:g}",
                    _num(f["total_mean"]),
                    _num(f["wait_p95"]),
                    _num(f["wait_max"]),
                    *deltas,
                ]
            )
        table = _table_view(
            ["α", "total", "wait p95", "wait max", "Δ total", "Δ p95", "Δ max"], rows
        )
        out.append(
            _card(
                "Fairness frontier",
                "Each point is the cost policy with fairness weight α (means over seeds). "
                "Down is fairer (shorter worst wait), left is more efficient.",
                chart + table,
            )
        )
    return "".join(out)
