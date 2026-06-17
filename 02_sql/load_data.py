"""
load_data.py
------------
Builds dukaonline.db (SQLite), creates all five tables from schema.sql, and loads
your CLEANED data from data/processed/.

Run from the project root (AFTER you finish the Python cleaning in Stage 3):
    python3 02_sql/load_data.py

Then explore:
    sqlite3 dukaonline.db
    sqlite> .read 02_sql/queries.sql
    sqlite> .quit

Uses Python's built-in sqlite3 — nothing to install.
"""

import sqlite3
import csv
import os

DB = "dukaonline.db"
SCHEMA = "02_sql/schema.sql"

# table name -> (clean csv path, column order matching schema.sql)
TABLES = {
    "customers": ("data/processed/customers_clean.csv",
                  ["customer_id","name","phone","county","gender","age","signup_date"]),
    "products":  ("data/processed/products_clean.csv",
                  ["product_id","product_name","category","cost_price","list_price"]),
    "orders":    ("data/processed/orders_clean.csv",
                  ["order_id","customer_id","product_id","order_date","quantity",
                   "unit_price","discount","payment_method","channel","rating"]),
    "returns":   ("data/processed/returns_clean.csv",
                  ["return_id","order_id","return_date","reason"]),
    "ab_test":   ("data/processed/ab_test_clean.csv",
                  ["customer_id","variant","exposed_date","converted"]),
}

# columns that should load as numbers (everything else stays text)
NUMERIC = {"age","quantity","unit_price","discount","rating","cost_price",
           "list_price","converted"}

def cast(col, val):
    if val == "" or val is None:
        return None
    if col in NUMERIC:
        return float(val) if ("." in val) else int(val)
    return val

missing = [p for (p, _) in TABLES.values() if not os.path.exists(p)]
if missing:
    raise SystemExit(
        "These cleaned files don't exist yet:\n  " + "\n  ".join(missing) +
        "\n\nFinish the Python cleaning (Stage 3) first so data/processed/ is populated."
    )

conn = sqlite3.connect(DB)
cur = conn.cursor()
with open(SCHEMA) as f:
    cur.executescript(f.read())

for table, (path, cols) in TABLES.items():
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        rows = [tuple(cast(c, r.get(c, "")) for c in cols) for r in reader]
    placeholders = ",".join("?" * len(cols))
    cur.executemany(f"INSERT OR REPLACE INTO {table} VALUES ({placeholders})", rows)
    print(f"  {table:<10} {len(rows)} rows")

conn.commit()
print(f"\nLoaded everything into {DB}. Open it with:  sqlite3 dukaonline.db")
conn.close()
