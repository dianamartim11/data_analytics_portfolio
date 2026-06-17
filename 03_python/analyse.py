"""
analyse.py  —  STARTER (you finish the TODOs)
---------------------------------------------
Answers the business questions from the CLEANED data and saves charts.

Run from the project root (after clean.py):
    python3 03_python/analyse.py

Saves charts into: 03_python/figures/
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CLEAN = "data/processed/online_orders_clean.csv"
FIG = "03_python/figures"

df = pd.read_csv(CLEAN)

# Revenue per order ----------------------------------------------------------
df["revenue"] = df["quantity"] * df["unit_price"]

# Q1: headline numbers -------------------------------------------------------
print("Total orders :", len(df))
print("Total revenue: KES", round(df["revenue"].sum(), 2))

# Q2: revenue by category ----------------------------------------------------
by_cat = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by category:\n", by_cat)

# TODO Q3: revenue by county (groupby 'county') -> print top 5
# TODO Q4: orders per payment_method (value_counts or groupby size) -> print

# Chart 1: revenue by category (bar) -----------------------------------------
by_cat.plot(kind="bar", title="Revenue by Category", ylabel="Revenue (KES)")
plt.tight_layout()
plt.savefig(f"{FIG}/revenue_by_category.png")
plt.close()
print(f"\nSaved {FIG}/revenue_by_category.png")

# TODO Chart 2: a histogram of ratings OR a line of revenue over time
# TODO Chart 3: a correlation heatmap
#   corr = df[["unit_price", "quantity", "rating", "revenue"]].corr()
#   sns.heatmap(corr, annot=True, cmap="coolwarm")
#   plt.savefig(f"{FIG}/correlation_heatmap.png")

# ---------------------------------------------------------------------------
# Pick ONE statistical step and complete it:
# ---------------------------------------------------------------------------

# OPTION A — t-test: do Nairobi and Mombasa rate differently?
# from scipy import stats
# nbo = df[df["county"] == "Nairobi"]["rating"].dropna()
# msa = df[df["county"] == "Mombasa"]["rating"].dropna()
# t, p = stats.ttest_ind(nbo, msa)
# print(f"\nt-test Nairobi vs Mombasa ratings: p = {p:.4f}")
# print("Difference is", "significant" if p < 0.05 else "NOT significant", "(p<0.05?)")

# OPTION B — regression: does price predict rating?
# from sklearn.linear_model import LinearRegression
# d = df.dropna(subset=["rating"])
# X = d[["unit_price"]]; y = d["rating"]
# model = LinearRegression().fit(X, y)
# print(f"\nRegression: rating = {model.coef_[0]:.5f} * price + {model.intercept_:.2f}")
# print("R^2 =", round(model.score(X, y), 3))

print("\nDone. Now write up what these numbers mean in reports/findings.md")
