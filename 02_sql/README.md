# Stage 2 — Model the data as a database (SQL)

Now you will load your cleaned data into a real database table and answer
questions with SQL.

> ⚠️ Do this stage **after** (or alongside) the Python cleaning in Stage 3, because
> the database should hold the *clean* data — `data/processed/online_orders_clean.csv`.
> If you haven't cleaned yet, you can load the raw file to practise, but redo it with
> the clean file before you submit.

## Easiest path: SQLite via Python (nothing to install)

You already have Python. SQLite is built in. From the project root:

```bash
# 1. Create the empty table from the schema
sqlite3 dukaonline.db < 02_sql/schema.sql      # if you have the sqlite3 command

# OR do everything in one short Python script (works everywhere):
python3 02_sql/load_data.py
```

A ready-to-run loader, `load_data.py`, is provided in this folder — it creates the
database, applies `schema.sql`, and imports `data/processed/online_orders_clean.csv`.

Then explore:
```bash
sqlite3 dukaonline.db        # opens an interactive SQL prompt
sqlite> .read 02_sql/queries.sql
sqlite> .quit
```

> Prefer **MySQL Workbench** or **pgAdmin**? That's fine too — create a database,
> run `schema.sql`, import the CSV, then run `queries.sql`. The SQL is standard.

## Your tasks
1. Create the `orders` table from [`schema.sql`](schema.sql).
2. Load the **cleaned** CSV into it.
3. Complete every query in [`queries.sql`](queries.sql) (Q2–Q6).
4. Below, paste each query's **result** (numbers or a screenshot) and explain in one
   sentence what it tells the business.

## My results & explanations
*(fill this in)*

**Q2 — Revenue by category:**
> result + one-sentence explanation

**Q3 — Top 5 counties:**
>

**Q4 — Payment methods:**
>

**Q5 — Average rating per category:**
>

**Q6 — Best-selling product:**
>
