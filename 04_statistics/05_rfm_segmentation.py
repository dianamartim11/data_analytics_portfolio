"""
05_rfm_segmentation.py  —  STARTER
----------------------------------
RFM customer segmentation: rank customers by how Recently, how Frequently, and
how much (Monetary) they buy — the classic way analysts find "best customers".
Run from project root:  python3 04_statistics/05_rfm_segmentation.py
"""

import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("data/processed/orders_clean.csv", parse_dates=["order_date"])
orders["unit_price"] = pd.to_numeric(orders["unit_price"], errors="coerce")
orders["revenue"] = orders["quantity"] * orders["unit_price"]

# "today" = the day after the last order in the data
snapshot = orders["order_date"].max() + pd.Timedelta(days=1)

# --- compute R, F, M per customer ------------------------------------------
rfm = orders.groupby("customer_id").agg(
    recency=("order_date", lambda s: (snapshot - s.max()).days),  # days since last order
    frequency=("order_id", "count"),                              # number of orders
    monetary=("revenue", "sum"),                                  # total spend
)
print(rfm.describe().round(1))

# --- score each dimension 1..4 (quartiles) ---------------------------------
# Recency: fewer days = better, so reverse the labels.
rfm["R"] = pd.qcut(rfm["recency"], 4, labels=[4, 3, 2, 1]).astype(int)
rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
rfm["M"] = pd.qcut(rfm["monetary"], 4, labels=[1, 2, 3, 4]).astype(int)
rfm["RFM_score"] = rfm["R"] + rfm["F"] + rfm["M"]

# --- simple segment labels -------------------------------------------------
def segment(score):
    if score >= 10: return "Champions"
    if score >= 7:  return "Loyal"
    if score >= 5:  return "Potential"
    return "At risk"

rfm["segment"] = rfm["RFM_score"].apply(segment)
print("\nCustomers per segment:")
print(rfm["segment"].value_counts())

# TODO: who are the top 10 customers by monetary value? Print their ids + spend.
# TODO: write one recommendation per segment in the README
#       (e.g. "reward Champions, win back At-risk").

# --- chart -----------------------------------------------------------------
rfm["segment"].value_counts().plot(kind="bar", title="Customers by RFM Segment")
plt.tight_layout()
plt.savefig("04_statistics/figures/rfm_segments.png")
plt.close()
print("\nSaved 04_statistics/figures/rfm_segments.png")
