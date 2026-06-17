"""
clean.py  —  STARTER (you finish the TODOs)
-------------------------------------------
Reads the messy raw orders and writes a clean version that every later stage
(SQL, Power BI, the report) will use.

Run from the project root:
    python3 03_python/clean.py

When you are done it should create:
    data/processed/online_orders_clean.csv

Look back at these class scripts for help — you have done all of this before:
  - fixamountandparse.py                  (currency text -> number, date parsing)
  - normalisephonedropduplicatesandsave.py (phone formats, drop_duplicates)
  - standardisetheservice.py              (fix inconsistent category spellings)
  - prepare_for_powerbi.py                (the whole pipeline as one example)
"""

import pandas as pd

RAW = "data/raw/online_orders_messy.csv"
OUT = "data/processed/online_orders_clean.csv"

# 1. Load -------------------------------------------------------------------
df = pd.read_csv(RAW)
print("Loaded:", df.shape)
print(df.head())

# 2. Trim spaces and fix capitalisation in text columns ----------------------
df["customer_name"] = df["customer_name"].str.strip().str.title()
# TODO: do the same kind of cleanup for county, category, payment_method
#       (strip spaces first, then fix capitalisation/spelling below)

# 3. Fix county spellings ----------------------------------------------------
# TODO: map nairobi/NAIROBI/' Nairobi' -> 'Nairobi', Mombassa -> 'Mombasa', etc.
# Hint:
# county_fixes = {"nairobi": "Nairobi", "mombassa": "Mombasa", ...}
# df["county"] = df["county"].str.strip().str.title().replace(county_fixes)

# 4. Fix category spellings ---------------------------------------------------
# TODO: 'Electronic' -> 'Electronics', trailing spaces -> none, etc.

# 5. Standardise payment_method ----------------------------------------------
# TODO: 'mpesa'/'Mpesa' -> 'M-Pesa', 'card' -> 'Card', 'cash' -> 'Cash'

# 6. Convert unit_price text -> number ---------------------------------------
# Values look like '3500', 'KES 3500', or '3,500'. Remove letters/commas/spaces.
# TODO:
# df["unit_price"] = (
#     df["unit_price"].astype(str)
#       .str.replace("KES", "", case=False)
#       .str.replace(",", "")
#       .str.strip()
# )
# df["unit_price"] = pd.to_numeric(df["unit_price"])

# 7. Parse the date (3 formats) ----------------------------------------------
# pandas is smart: pd.to_datetime can usually handle mixed formats.
# TODO:
# df["order_date"] = pd.to_datetime(df["order_date"], format="mixed", dayfirst=True)
# df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

# 8. Normalise phone numbers to +2547XXXXXXXX --------------------------------
# Formats seen: 07XXXXXXXX, +2547XXXXXXXX, 2547XXXXXXXX, 7XXXXXXXX
# TODO: write a small function that returns one consistent format.
# def fix_phone(p):
#     digits = "".join(ch for ch in str(p) if ch.isdigit())
#     if digits.startswith("0"):    digits = "254" + digits[1:]
#     elif digits.startswith("7"):  digits = "254" + digits
#     return "+" + digits
# df["phone"] = df["phone"].apply(fix_phone)

# 9. Remove duplicate rows ----------------------------------------------------
# TODO: df = df.drop_duplicates()

# 10. Handle missing values ---------------------------------------------------
# Decide and EXPLAIN in a comment: do you drop rows with blank county? Leave
# blank ratings as missing? (Average rating should ignore missing, not treat as 0.)
# TODO

# 11. Save -------------------------------------------------------------------
df.to_csv(OUT, index=False)
print("\nSaved clean data to:", OUT)
print("Final shape:", df.shape)
