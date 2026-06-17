"""
04_timeseries.py  —  STARTER
----------------------------
Trends over time: monthly revenue, moving average, growth rates, seasonality.
Run from project root:  python3 04_statistics/04_timeseries.py
"""

import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("data/processed/orders_clean.csv", parse_dates=["order_date"])
orders["unit_price"] = pd.to_numeric(orders["unit_price"], errors="coerce")
orders["revenue"] = orders["quantity"] * orders["unit_price"]

# --- monthly revenue -------------------------------------------------------
monthly = (orders
           .set_index("order_date")
           .resample("M")["revenue"].sum()
           .rename("revenue")
           .to_frame())

# --- 3-month moving average ------------------------------------------------
monthly["moving_avg_3m"] = monthly["revenue"].rolling(3).mean()

# --- month-over-month growth % ---------------------------------------------
monthly["mom_growth_%"] = monthly["revenue"].pct_change() * 100
print(monthly.round(0))

# TODO: compute YEAR-over-year growth: compare each 2025 month to the same 2024
#       month (hint: monthly['revenue'].pct_change(12)). Print it.
# TODO: look at December vs other months — is there a holiday spike? Note it.

# --- chart -----------------------------------------------------------------
monthly[["revenue", "moving_avg_3m"]].plot(marker="o", title="Monthly Revenue + 3-Month Moving Average")
plt.ylabel("KES")
plt.tight_layout()
plt.savefig("04_statistics/figures/revenue_timeseries.png")
plt.close()
print("\nSaved 04_statistics/figures/revenue_timeseries.png")
