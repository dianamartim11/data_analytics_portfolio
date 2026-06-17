# Stage 2 — SQL: query a real (multi-table) database

This stage proves you can write SQL — the #1 skill employers test data analysts on.
You will load the five cleaned tables into a database and answer questions that
require **joins, grouping, dates, subqueries, CTEs, and window functions**.

> ⚠️ Do this **after** the Python cleaning (Stage 3) so the database holds clean
> data. The loader expects the cleaned files in `data/processed/`.

## Easiest path — SQLite via Python (nothing to install)

From the project root:
```bash
python3 02_sql/load_data.py      # builds dukaonline.db with all 5 tables
sqlite3 dukaonline.db            # opens an interactive SQL prompt
sqlite> .headers on
sqlite> .mode column
sqlite> .read 02_sql/queries.sql # runs all your queries
sqlite> .quit
```
> No `sqlite3` command? Install it (`sudo apt install sqlite3`, or on Windows
> download from sqlite.org), **or** run queries straight from Python with
> `pandas.read_sql(query, sqlite3.connect("dukaonline.db"))`.
>
> Prefer **MySQL Workbench** / **pgAdmin**? Also fine — create a database, run
> `schema.sql`, import the cleaned CSVs, then run `queries.sql`. The SQL is standard
> (except `substr(...)` for months — use `DATE_FORMAT`/`TO_CHAR` there instead).

## Your tasks
Open [`queries.sql`](queries.sql) and complete **Q2, Q4, Q6–Q15**.
They are grouped by difficulty:
1. **Basics** — SELECT / WHERE / ORDER BY
2. **Grouping** — GROUP BY / HAVING / aggregates
3. **Joins** — INNER and LEFT joins across tables
4. **CASE / dates / subqueries / CTEs**
5. **Window functions** — RANK, running totals, LAG

## What to hand in
- A completed `queries.sql`
- The **result** of each query pasted below (numbers or a 📷 screenshot)
- One sentence per query on what it tells the business

## My results
*(fill in — one block per query)*

**Q2 — Top 10 orders by value:** …
**Q4 — Avg rating per channel (≥50 orders):** …
**Q5 — Revenue by category:** …
**Q6 — Profit by category:** …
**Q7 — Revenue by county:** …
**Q8 — Returned vs not returned:** …
**Q9 — Orders per price tier:** …
**Q10 — Revenue by month:** …
**Q11 — Above-average customers:** …
**Q12 — Top product per category (CTE):** …
**Q13 — Product rank within category (window):** …
**Q14 — Running monthly revenue (window):** …
**Q15 — Month-over-month change (LAG):** …
