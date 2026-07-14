# Checklist 1 — Excel Cleaning & Dashboard Feedback

Review of the `dukaonline` workbook (orders + customers cleaning and the revenue dashboard).

## What's working well — keep it
- Power Query import (UTF-8 / comma delimiter) ✓
- Price cleaning (`KES 950` → `950`, `2,200` → `2200`) ✓
- Revenue = quantity × unit_price (`=E2*K2`) ✓
- Channel standardized to App / Web / Store ✓
- Status logic (rating ≤3 = At Risk, ≥4 = Happy) — consistent ✓
- Customer name/county cleaning (proper case, standardized counties) ✓

## 🔴 Must fix (data is not trustworthy until these are done)
1. **Undo the Remove Duplicates step.** It deleted 938 rows (~46% of the data). That is
   too many — it looks like it ran on the `channel` column (only 3 values) instead of on
   the order ID.
2. **Fix the date column.** All the text-format dates (`Sep 24 2024`, `Apr 6 2025`) failed
   to convert and are blank — the time chart is missing those orders.

## 🟡 Should fix (dashboard accuracy)
3. **"c" bar** in *revenue by category* — a bad category value; find and correct it.
4. **"Total by channel" chart** — y-axis shows 3.5–3.7, so it is charting rating/count,
   not revenue. Point it at summed revenue.

## ⚪ Nice to clean up
5. Phone numbers show as `2.54E+11` → format as Text.
6. `gender` still mixed (F/M/Female/m/f) → standardize.
7. Delete leftover helper columns (`Column1`, `profit2`, duplicate `revenue`, `counts`).

---

## Exact steps for the two must-fixes

### Fix #1 — Re-do Remove Duplicates safely
1. Press **Ctrl+Z** repeatedly until the deleted rows come back (or reload the CSV via
   Power Query → Refresh).
2. Click any single cell **inside the table**.
3. **Data tab → Remove Duplicates.**
4. In the dialog, click **Unselect All**, then tick **only `order_id`** (the column that
   should be unique).
5. Click OK. You should now see very few — ideally zero — duplicates removed. If it still
   removes hundreds, the raw file genuinely has repeated order IDs and that is worth
   investigating, not deleting blindly.

### Fix #2 — Convert the text dates
1. Best option: do it in **Power Query** (where the import lives) so it re-applies on every
   refresh:
   - Right-click the `order_date` column → **Change Type → Using Locale…**
   - Data Type = **Date**, Locale = **English (United States)** → OK. Power Query parses
     `Sep 24 2024`, `Apr 6 2025`, etc.
2. Quick in-sheet alternative: in a new column use `=DATEVALUE(D2)` — but this fails on some
   formats, which is exactly why Power Query is the reliable route.
3. After converting, refresh the dashboard so the time chart picks up the recovered dates.
