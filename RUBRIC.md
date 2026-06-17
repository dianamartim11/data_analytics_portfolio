# ✅ Marking Rubric & Checklist

Total: **100 points.** Tick each box as you complete it. This is also your
"definition of done" — if every box is ticked, you have a complete portfolio piece.

---

## 1. Excel stage — 15 pts
- [ ] Raw CSV opened and explored with filters (3)
- [ ] Cleaning done with `TRIM`/`PROPER`/find-replace/remove-duplicates (4)
- [ ] At least one pivot table built (3)
- [ ] At least one chart built (2)
- [ ] `01_excel/notes.md` describes what was found and fixed (3)

## 2. SQL stage — 15 pts
- [ ] `orders` table created from `schema.sql` (3)
- [ ] Cleaned data loaded successfully (3)
- [ ] All queries in `queries.sql` completed and return correct results (6)
- [ ] Each query explained in plain English in `02_sql/README.md` (3)

## 3. Python cleaning — 20 pts
- [ ] Dates parsed to a real date type (3)
- [ ] Phone numbers normalised to one format, e.g. `+2547XXXXXXXX` (3)
- [ ] `unit_price` converted from text (`KES 3,500`) to a number (3)
- [ ] County / category / payment spellings standardised (4)
- [ ] Duplicate rows removed; missing values handled sensibly (4)
- [ ] Clean file written to `data/processed/online_orders_clean.csv` (3)

## 4. Python analysis — 15 pts
- [ ] Revenue column created (`quantity * unit_price`) (2)
- [ ] `groupby` / `pivot_table` answers the business questions (4)
- [ ] At least 3 saved charts in `03_python/figures/` (5)
- [ ] One t-test **or** regression done and interpreted in words (4)

## 5. Power BI dashboard — 15 pts
- [ ] Clean CSV imported correctly (types right, phone as text) (3)
- [ ] At least 4 visuals on one page (4)
- [ ] At least 2 slicers / filters (2)
- [ ] KPI cards for total revenue and total orders (3)
- [ ] `.pbix` saved **and** a screenshot exported to `04_powerbi/` (3)

## 6. Report & README — 15 pts
- [ ] `reports/findings.md` answers all 5 business questions clearly (6)
- [ ] Charts embedded in the report (2)
- [ ] "3 recommendations for DukaOnline" section (3)
- [ ] Top-level `README.md` is a clean portfolio landing page (4)

## 7. Professionalism — 5 pts (bonus-style, across the whole repo)
- [ ] Sensible, frequent git commits with clear messages (2)
- [ ] Code is commented and readable (2)
- [ ] Repository is tidy (no stray files, folders used correctly) (1)

---

### Grade bands
| Score | Meaning |
|---|---|
| 90–100 | Excellent — portfolio-ready, show this to employers |
| 75–89 | Strong — small gaps in polish or explanation |
| 60–74 | Good effort — core pipeline works, documentation thin |
| < 60 | Keep going — revisit the unchecked boxes above |
