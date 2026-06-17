"""
clean.py  —  STARTER (you finish the TODOs)
-------------------------------------------
Cleans ALL FIVE raw tables and writes tidy versions to data/processed/.
Every later stage (SQL, statistics, Power BI, the report) uses these clean files.

Run from the project root:
    python3 03_python/clean.py

Produces:
    data/processed/customers_clean.csv
    data/processed/products_clean.csv
    data/processed/orders_clean.csv
    data/processed/returns_clean.csv
    data/processed/ab_test_clean.csv

You have done every technique below in the class repo — reuse those ideas
(fixamountandparse.py, normalisephonedropduplicatesandsave.py, standardisetheservice.py).
"""

import re
import pandas as pd

RAW = "data/raw"
OUT = "data/processed"

# --------------------------------------------------------------------------
# small reusable helpers
# --------------------------------------------------------------------------
def fix_phone(p):
    """Return a phone in one consistent format: +2547XXXXXXXX."""
    digits = re.sub(r"\D", "", str(p))          # keep digits only
    if digits.startswith("0"):
        digits = "254" + digits[1:]
    elif digits.startswith("7"):
        digits = "254" + digits
    return "+" + digits

def to_number(series):
    """'KES 3,500' / '3,500' -> 3500.0"""
    return pd.to_numeric(
        series.astype(str)
              .str.replace("KES", "", case=False)
              .str.replace(",", "")
              .str.strip(),
        errors="coerce",
    )

def parse_date(series):
    """Handle the 3 date formats and return 'YYYY-MM-DD' strings."""
    return pd.to_datetime(series, format="mixed", dayfirst=True, errors="coerce").dt.strftime("%Y-%m-%d")

# ==========================================================================
# 1. CUSTOMERS
# ==========================================================================
cust = pd.read_csv(f"{RAW}/customers_raw.csv")
cust["name"] = cust["name"].str.strip().str.title()
cust["phone"] = cust["phone"].apply(fix_phone)
# TODO: fix county spellings -> Title case, map 'Mombassa'->'Mombasa'
# TODO: standardise gender -> 'M'/'F' (map 'Male'->'M','female'->'F', etc.)
cust["signup_date"] = parse_date(cust["signup_date"])
# TODO: age has impossible values (0, 150, 200). Set ages outside 10..100 to NaN.
cust.to_csv(f"{OUT}/customers_clean.csv", index=False)
print("customers ->", cust.shape)

# ==========================================================================
# 2. PRODUCTS  (already clean — just copy through, maybe verify types)
# ==========================================================================
prod = pd.read_csv(f"{RAW}/products.csv")
prod.to_csv(f"{OUT}/products_clean.csv", index=False)
print("products  ->", prod.shape)

# ==========================================================================
# 3. ORDERS  (the big messy one)
# ==========================================================================
orders = pd.read_csv(f"{RAW}/orders_raw.csv")
orders["unit_price"] = to_number(orders["unit_price"])
orders["order_date"] = parse_date(orders["order_date"])
# TODO: standardise payment_method ('mpesa'/'Mpesa'->'M-Pesa', 'card'->'Card', ...)
# TODO: standardise channel ('web'->'Web','app'->'App','store'->'Store')
# TODO: drop exact duplicate rows  -> orders = orders.drop_duplicates()
# NOTE: leave blank ratings as missing (NaN) — do NOT fill with 0.
# NOTE: extreme quantities (e.g. 100) are handled in the STATS stage (outliers),
#       so keep them here but be aware of them.
orders.to_csv(f"{OUT}/orders_clean.csv", index=False)
print("orders    ->", orders.shape)

# ==========================================================================
# 4. RETURNS
# ==========================================================================
returns = pd.read_csv(f"{RAW}/returns.csv")
returns["return_date"] = parse_date(returns["return_date"])
# TODO: standardise 'reason' capitalisation (Title case)
returns.to_csv(f"{OUT}/returns_clean.csv", index=False)
print("returns   ->", returns.shape)

# ==========================================================================
# 5. AB_TEST
# ==========================================================================
ab = pd.read_csv(f"{RAW}/ab_test.csv")
ab["exposed_date"] = parse_date(ab["exposed_date"])
ab.to_csv(f"{OUT}/ab_test_clean.csv", index=False)
print("ab_test   ->", ab.shape)

print("\nAll cleaned files written to", OUT)
