#!/usr/bin/env python3
"""Builds the FICTIONAL sample committee calendar (xlsx + csv) from the standard rhythm,
with a few moved, extra and ad hoc meetings and some booked items."""
import csv, datetime as dt, os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "skills", "memo-assistent", "scripts"))
from committee_rules import ordinary_meetings, deadline, prev_business_day, ORDER
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

D = dt.date
rows = ordinary_meetings(D(2026, 12, 1), D(2027, 12, 31))
# A moved Board meeting, an extra GAC and an ad hoc committee
for r in rows:
    if r["committee"] == "Board" and r["date"] == D(2027, 6, 17):
        r.update(date=D(2027, 6, 10), deadline=deadline("Board", D(2027, 6, 10)), type="Moved", comment="Moved from 17 June")
rows.append({"committee": "GAC", "date": D(2027, 3, 4), "deadline": D(2027, 3, 1), "type": "Extra", "comment": "Extra meeting – ICAAP"})
rows.append({"committee": "Basel Steering Group", "date": D(2027, 1, 20), "deadline": D(2027, 1, 15), "type": "Ad hoc", "comment": "Ad hoc – CRR3 implementation"})
booked = {
    ("TC", D(2026, 12, 3)): ("FX hedging programme 2027", "A. Example", "Approved with conditions", "Report hedge effectiveness quarterly"),
    ("GAC", D(2026, 12, 15)): ("FX hedging programme 2027", "A. Example", "Paper submitted", ""),
    ("TC", D(2027, 2, 11)): ("Revised IRRBB limit framework", "A. Example", "Planned", ""),
    ("GAC", D(2027, 2, 23)): ("Revised IRRBB limit framework", "A. Example", "Planned", "Pre-alignment with CFO pending"),
    ("Board", D(2027, 2, 18)): ("Annual funding plan 2027", "B. Sample", "Planned", ""),
}
rows.sort(key=lambda r: (r["date"], ORDER.index(r["committee"]) if r["committee"] in ORDER else 99))
hdr = ["Committee", "Meeting date", "Pre-read deadline", "Type", "Booked", "Item", "Owner", "Status", "Comment"]
table = []
for r in rows:
    b = booked.get((r["committee"], r["date"]))
    item, owner, status, comment = b if b else ("", "", "", r.get("comment", ""))
    table.append([r["committee"], r["date"], r["deadline"], r["type"], "Yes" if b else "No", item, owner, status, comment or r.get("comment", "")])

wb = Workbook(); ws = wb.active; ws.title = "Committee calendar"
ws.append(hdr)
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1F3864")
for t in table: ws.append(t)
for r in ws.iter_rows(min_row=2): r[1].number_format = r[2].number_format = "yyyy-mm-dd"
n = ws.max_row
for col, opts in (("D", "Ordinary,Moved,Extra,Ad hoc"), ("E", "Yes,No,Proposed"),
                  ("H", "Planned,Paper submitted,Presented,Approved,Approved with conditions,Returned,Noted")):
    dv = DataValidation(type="list", formula1=f'"{opts}"'); ws.add_data_validation(dv); dv.add(f"{col}2:{col}{n}")
for col, w in zip("ABCDEFGHI", [22, 14, 17, 10, 9, 32, 12, 24, 40]): ws.column_dimensions[col].width = w
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
info = wb.create_sheet("About")
for line in ["FICTIONAL sample data. Rhythm: TC Thu (deadline Mon), GAC Tue (deadline Thu week before),",
             "GEC Mon (deadline Fri week before), RCC Wed 3rd week (deadline 9 days before), Board 3rd Thu (deadline 9 days before).",
             "Meetings on Swedish public holidays are dropped. Type: Ordinary / Moved / Extra / Ad hoc."]:
    info.append([line])
info.column_dimensions["A"].width = 110
wb.save(os.path.join(here, "committee-calendar.xlsx"))
with open(os.path.join(here, "committee-calendar.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(hdr)
    for t in table: w.writerow([x.isoformat() if isinstance(x, dt.date) else x for x in t])
print(len(table), "meetings")
