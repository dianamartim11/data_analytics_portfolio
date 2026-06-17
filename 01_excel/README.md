# Stage 1 — Explore & Clean in Excel

The goal here is to get *familiar* with the data by hand before you automate
anything in Python. Excel is great for "eyeballing" problems.

## Steps

1. **Open the raw file.** In Excel: `File → Open` →
   `data/raw/online_orders_messy.csv`.
   (Or `Data → Get Data → From Text/CSV` to control the import.)

2. **Look for the mess.** Turn on filters (`Data → Filter`) and click the dropdown
   on each column. You will quickly see things like `nairobi`, `NAIROBI`,
   `Mombassa`, and `KES 3500` mixed with `3,500`.

3. **Clean a copy.** Work on a *copy* of the sheet so the raw data stays untouched.
   Useful tools:
   | Problem | Excel tool |
   |---|---|
   | Extra spaces in names | `=TRIM(A2)` |
   | Inconsistent capitalisation | `=PROPER(A2)` |
   | `nairobi` / `NAIROBI` → `Nairobi` | Find & Replace (`Ctrl+H`), or `PROPER` |
   | `KES 3,500` → number | `=NUMBERVALUE(SUBSTITUTE(SUBSTITUTE(I2,"KES",""),",",""))` |
   | Duplicate rows | `Data → Remove Duplicates` |

4. **One pivot table.** `Insert → PivotTable`. Try **revenue by category**:
   first add a `revenue` column (`= quantity * unit_price`), then drag `category`
   to Rows and `revenue` to Values (Sum).

5. **One chart.** Select your pivot table → `Insert → Recommended Charts`.
   A bar chart of revenue by category works well.

6. **Save your work** as `01_excel/dukaonline_clean.xlsx`.

## What to hand in
- `01_excel/dukaonline_clean.xlsx` — your cleaned workbook with the pivot + chart
- `01_excel/notes.md` — fill in the template already in this folder

> 💡 Don't worry about cleaning *perfectly* here. Excel is for exploring. The
> thorough, repeatable cleaning happens in Python (Stage 3).
