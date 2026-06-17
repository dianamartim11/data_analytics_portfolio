"""
analyse.py  —  STARTER (you finish the TODOs)
---------------------------------------------
Merges the cleaned tables and answers the business questions, saving charts
to 03_python/figures/.

Run from the project root (after clean.py):
    python3 03_python/analyse.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

P = "data/processed"
FIG = "03_python/figures"

orders   = pd.read_csv(f"{P}/orders_clean.csv", parse_dates=["order_date"])
products = pd.read_csv(f"{P}/products_clean.csv")
customers= pd.read_csv(f"{P}/customers_clean.csv")
returns  = pd.read_csv(f"{P}/returns_clean.csv")

# --- build the analysis table: orders + product + customer info ------------
df = orders.merge(products, on="product_id", how="left") \
           .merge(customers[["customer_id","county","gender","age"]],
                  on="customer_id", how="left")
df["revenue"] = df["quantity"] * df["unit_price"]
df["profit"]  = (df["unit_price"] - df["cost_price"]) * df["quantity"]
df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

# --- headline numbers ------------------------------------------------------
print("Orders        :", len(df))
print("Total revenue : KES", round(df["revenue"].sum()))
print("Total profit  : KES", round(df["profit"].sum()))

# --- revenue & profit by category ------------------------------------------
by_cat = df.groupby("category").agg(revenue=("revenue","sum"),
                                    profit=("profit","sum")).sort_values("revenue", ascending=False)
print("\nBy category:\n", by_cat)

# TODO: revenue by county (merge already gives county) -> print top 5
# TODO: orders by channel and by payment_method -> print
# TODO: return rate = number of returned orders / total orders
#       (merge returns on order_id, count non-null return_id)

# --- Chart 1: revenue by category (bar) ------------------------------------
by_cat["revenue"].plot(kind="bar", title="Revenue by Category", ylabel="KES")
plt.tight_layout(); plt.savefig(f"{FIG}/revenue_by_category.png"); plt.close()

# --- Chart 2: revenue over time (line) -------------------------------------
monthly = df.groupby("order_month")["revenue"].sum()
monthly.plot(kind="line", marker="o", title="Revenue by Month", ylabel="KES")
plt.tight_layout(); plt.savefig(f"{FIG}/revenue_by_month.png"); plt.close()

# TODO Chart 3: histogram of order ratings  (df["rating"].plot(kind="hist"))
# TODO Chart 4: box plot of unit_price by category (shows outliers)
#       sns.boxplot(data=df, x="category", y="unit_price")
# TODO Chart 5: correlation heatmap of
#       df[["quantity","unit_price","discount","rating","revenue","age"]].corr()

print(f"\nCharts saved to {FIG}/. Deeper stats live in ../04_statistics/.")
