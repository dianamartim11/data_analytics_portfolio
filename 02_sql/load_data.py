"""
load_data.py
------------
Creates a SQLite database (dukaonline.db), builds the `orders` table from
schema.sql, and loads your CLEANED data into it.

Run from the project root:
    python3 02_sql/load_data.py

Then explore with:
    sqlite3 dukaonline.db
    sqlite> .read 02_sql/queries.sql

This uses Python's built-in sqlite3 module — nothing to install.
"""

import sqlite3
import csv
import os

DB = "dukaonline.db"
SCHEMA = "02_sql/schema.sql"
DATA = "data/processed/online_orders_clean.csv"

if not os.path.exists(DATA):
    raise SystemExit(
        f"Could not find {DATA}.\n"
        "Run your Python cleaning script (Stage 3) first so the clean file exists."
    )

conn = sqlite3.connect(DB)
cur = conn.cursor()

# 1. Build the table from schema.sql
with open(SCHEMA) as f:
    cur.executescript(f.read())

# 2. Load the cleaned CSV
with open(DATA, newline="") as f:
    reader = csv.DictReader(f)
    rows = [
        (
            r["order_id"], r["order_date"], r["customer_name"], r["phone"],
            r["county"], r["product"], r["category"],
            int(r["quantity"]) if r["quantity"] else None,
            float(r["unit_price"]) if r["unit_price"] else None,
            r["payment_method"],
            int(r["rating"]) if r["rating"] else None,
        )
        for r in reader
    ]

cur.executemany(
    "INSERT OR REPLACE INTO orders VALUES (?,?,?,?,?,?,?,?,?,?,?)", rows
)
conn.commit()

count = cur.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
print(f"Loaded {count} rows into {DB} (table: orders).")
print("Open it with:  sqlite3 dukaonline.db")
conn.close()
