#!/usr/bin/env python3
"""Plan a committee path backwards from a target meeting.

Usage:
  plan_path.py --target Board --date 2027-04-15 [--path TC,GAC,GEC,RCC,Board]
               [--calendar committee-calendar.xlsx|.csv] [--buffer 3] [--today 2026-11-11]

Uses the calendar when given (it overrides the rules, incl. moved/extra/ad hoc meetings);
otherwise computes meetings from the standard rhythm. Prints a markdown timeline.
"""
import argparse, csv, datetime as dt, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from committee_rules import ORDER, ordinary_meetings, minus_business_days, is_business_day

COLS = {"committee": ["committee"], "date": ["meeting date", "date"], "deadline": ["pre-read deadline", "deadline"],
        "type": ["type"], "booked": ["booked"]}


def to_date(v):
    if isinstance(v, dt.datetime): return v.date()
    if isinstance(v, dt.date): return v
    return dt.date.fromisoformat(str(v).strip()[:10]) if v else None


def load_calendar(path):
    if path.lower().endswith((".xlsx", ".xlsm")):
        import openpyxl
        ws = openpyxl.load_workbook(path, data_only=True).worksheets[0]
        rows = list(ws.iter_rows(values_only=True))
    else:
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.reader(f))
    head = [str(h or "").strip().lower() for h in rows[0]]
    idx = {k: next((head.index(a) for a in alts if a in head), None) for k, alts in COLS.items()}
    out = []
    for r in rows[1:]:
        if not r or idx["committee"] is None or not r[idx["committee"]]: continue
        get = lambda k: r[idx[k]] if idx[k] is not None and idx[k] < len(r) else None
        out.append({"committee": str(get("committee")).strip(), "date": to_date(get("date")),
                    "deadline": to_date(get("deadline")), "type": get("type") or "", "booked": get("booked") or ""})
    return out


def bdays_between(a, b):
    n, d = 0, a
    while d < b:
        d += dt.timedelta(1)
        if is_business_day(d): n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--path")
    ap.add_argument("--calendar")
    ap.add_argument("--buffer", type=int, default=3)
    ap.add_argument("--today", default=dt.date.today().isoformat())
    a = ap.parse_args()
    today, target_date = dt.date.fromisoformat(a.today), dt.date.fromisoformat(a.date)
    path = a.path.split(",") if a.path else ORDER[: ORDER.index(a.target) + 1]
    meetings = load_calendar(a.calendar) if a.calendar else ordinary_meetings(today, target_date)
    src = "calendar" if a.calendar else "standard rhythm (computed)"

    target = next((m for m in meetings if m["committee"] == path[-1] and m["date"] == target_date), None)
    if not target:
        sys.exit(f"No {path[-1]} meeting on {target_date} in the {src}.")
    plan = [target]
    for com in reversed(path[:-1]):
        latest = minus_business_days(plan[0]["deadline"], a.buffer)
        cands = [m for m in meetings if m["committee"] == com and today <= m["date"] <= latest]
        if not cands:
            plan.insert(0, {"committee": com, "date": None, "deadline": None, "type": "", "booked": ""})
            break
        plan.insert(0, max(cands, key=lambda m: m["date"]))

    first_dl = plan[0]["deadline"]
    rows = []
    if first_dl:
        mgr = minus_business_days(first_dl, 5)
        rows += [(minus_business_days(mgr, 3), "First draft ready", "–", "–", ""), (mgr, "Review with manager", "Manager", "–", "")]
    for m in plan:
        if m["date"] is None:
            rows.append((None, f"No feasible {m['committee']} meeting – path not feasible", m["committee"], "", "🔴"))
            continue
        tag = f" ({m['type']})" if m["type"] and m["type"] != "Ordinary" else ""
        rows.append((m["deadline"], "Pre-read deadline", m["committee"], m["booked"] or "No", ""))
        rows.append((m["date"], "Meeting" + tag, m["committee"], m["booked"] or "No", ""))

    print(f"Target: {path[-1]} {target_date} · path {' → '.join(path)} · buffer {a.buffer} business days · source: {src} · today {today}\n")
    print("| Date | What | Body | Booked | Flag |\n|---|---|---|---|---|")
    worst = "🟢"
    for d, what, body, booked, flag in rows:
        if not flag:
            if d < today or bdays_between(today, d) < 5: flag = "🔴"
            elif booked in ("No", "") and body not in ("–", "Manager") and "Meeting" in what: flag = "🟠"
            else: flag = "🟢"
        worst = "🔴" if "🔴" in (worst, flag) else ("🟠" if "🟠" in (worst, flag) else "🟢")
        print(f"| {d.isoformat() if d else '—'} | {what} | {body} | {booked} | {flag} |")
    print("\nVerdict:", {"🟢": "feasible", "🟠": "feasible – book the unbooked meetings", "🔴": "tight or not feasible – see red rows"}[worst])


if __name__ == "__main__":
    main()
