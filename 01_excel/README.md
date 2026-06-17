# Stage 1 — Excel: explore, formulas, lookups & a dashboard

Excel is where analysts do quick exploration and where many businesses still live.
Here you prove the core Excel skills. Work in **`01_excel/dukaonline.xlsx`** (create
it) with one sheet per raw CSV you import.

> Save screenshots of each step into `01_excel/screenshots/` — they are your
> evidence for skills A1–A12 in `SKILLS_CHECKLIST.md`.

## 1. Import & inspect
- `Data → Get Data → From Text/CSV` → import `orders_raw.csv`, `customers_raw.csv`
  and `products.csv` onto separate sheets.
- Set sensible data types. Keep `phone` as **Text**.

## 2. Clean with formulas (on a copy)
| Goal | Formula |
|---|---|
| Trim stray spaces | `=TRIM(B2)` |
| Fix capitalisation | `=PROPER(TRIM(B2))` |
| Strip `KES`/commas from price | `=NUMBERVALUE(SUBSTITUTE(SUBSTITUTE(I2,"KES",""),",",""))` |
| Fix county spellings | Find & Replace (`Ctrl+H`): `Mombassa`→`Mombasa`, etc. |

## 3. Calculations with `IF` family
- Add a `revenue` column: `=quantity*unit_price`.
- `=SUMIF(category_range,"Electronics",revenue_range)` → revenue for one category.
- `=COUNTIF(county_range,"Nairobi")` → orders from Nairobi.
- `=AVERAGEIF(channel_range,"Web",rating_range)` → average rating on the Web channel.
- `=IF(rating>=4,"Happy","At risk")` → a simple flag column.

## 4. **Lookups — join products onto orders**
On the orders sheet, pull each product's `category` and `cost_price` from the
products sheet (this is a "join" in Excel):
- **XLOOKUP** (modern): `=XLOOKUP(product_id, products!A:A, products!C:C)`
- or **VLOOKUP**: `=VLOOKUP(product_id, products!A:E, 3, FALSE)`
- or **INDEX/MATCH**: `=INDEX(products!C:C, MATCH(product_id, products!A:A, 0))`
- Then compute **profit**: `=(unit_price - cost_price) * quantity`.

## 5. Remove duplicates
`Data → Remove Duplicates` on the orders sheet (there are duplicate rows on purpose).

## 6. Conditional formatting
Highlight the top 10 orders by revenue (`Home → Conditional Formatting → Top/Bottom`),
and colour-scale the rating column.

## 7. Data validation
Add a dropdown (`Data → Data Validation → List`) so `county` can only be one of the
six valid counties — shows you can prevent bad data entry.

## 8. PivotTables & PivotCharts
Build at least these, each on its own pivot:
- Revenue **by category** (PivotChart: bar)
- Orders **by month** (group the date field by month → line chart)
- Average rating **by channel**

## 9. A one-page dashboard
On a new "Dashboard" sheet, arrange 3–4 of your pivot charts + a couple of KPI cells
(Total Revenue, Total Orders) into a tidy summary. Add slicers if you can.

## Hand in
- `01_excel/dukaonline.xlsx` (with all the above)
- `01_excel/screenshots/` (your evidence)
- `01_excel/notes.md` (filled in)

> 💡 Excel cleaning doesn't need to be perfect — the *repeatable* cleaning happens
> in Python (Stage 3). Excel is for exploring and for proving Excel skills.
