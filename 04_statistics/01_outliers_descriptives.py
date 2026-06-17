"""
01_outliers_descriptives.py  —  STARTER
----------------------------------------
Descriptive statistics + outlier detection with the IQR rule.
Run from project root:  python3 04_statistics/01_outliers_descriptives.py
"""

import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("data/processed/orders_clean.csv")
orders["unit_price"] = pd.to_numeric(orders["unit_price"], errors="coerce")
orders["order_value"] = orders["quantity"] * orders["unit_price"]

# --- descriptive stats -----------------------------------------------------
print("Quantity stats:")
print("  mean  :", round(orders["quantity"].mean(), 2))
print("  median:", orders["quantity"].median())
print("  mode  :", orders["quantity"].mode().tolist())
print("  std   :", round(orders["quantity"].std(), 2))
print(orders["order_value"].describe())

# --- IQR outlier rule ------------------------------------------------------
def iqr_outliers(series):
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return series[(series < low) | (series > high)], low, high

out, low, high = iqr_outliers(orders["quantity"])
print(f"\nQuantity outliers (outside {low:.1f}..{high:.1f}): {len(out)} rows")
print(sorted(out.unique()))

# TODO: do the same IQR check on 'order_value' and report how many outliers.
# TODO: decide what to do with them — cap them? remove them? Explain in README.

# --- box plot --------------------------------------------------------------
orders.boxplot(column="quantity")
plt.title("Order quantity — box plot (dots above the whisker are outliers)")
plt.tight_layout()
plt.savefig("04_statistics/figures/quantity_boxplot.png")
plt.close()
print("\nSaved 04_statistics/figures/quantity_boxplot.png")
