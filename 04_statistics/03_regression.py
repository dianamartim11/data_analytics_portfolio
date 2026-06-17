"""
03_regression.py  —  STARTER
----------------------------
Two models:
  (A) Linear regression  — predict a NUMBER  (rating from price/discount)
  (B) Logistic regression — predict a YES/NO  (converted from variant + age)
Run from project root:  python3 04_statistics/03_regression.py
"""

import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression

# ===========================================================================
# (A) LINEAR REGRESSION: does price predict the rating?
# ===========================================================================
orders = pd.read_csv("data/processed/orders_clean.csv")
orders["unit_price"] = pd.to_numeric(orders["unit_price"], errors="coerce")
d = orders.dropna(subset=["rating", "unit_price"])

X = d[["unit_price"]]          # feature(s)
y = d["rating"]               # target (a number)
lin = LinearRegression().fit(X, y)
print("LINEAR REGRESSION (rating ~ unit_price)")
print(f"  rating = {lin.coef_[0]:.6f} * price + {lin.intercept_:.3f}")
print(f"  R^2 = {lin.score(X, y):.3f}")
print("  Interpretation: ", "higher price -> higher rating" if lin.coef_[0] > 0
      else "higher price -> lower rating")

# TODO: add 'discount' as a second feature: X = d[['unit_price','discount']]
#       Does R^2 improve? Write the answer in the README.

# ===========================================================================
# (B) LOGISTIC REGRESSION: who will convert in the campaign?
# ===========================================================================
ab = pd.read_csv("data/processed/ab_test_clean.csv")
cust = pd.read_csv("data/processed/customers_clean.csv")[["customer_id", "age"]]
m = ab.merge(cust, on="customer_id", how="left").dropna(subset=["age"])
m["is_B"] = (m["variant"] == "B").astype(int)   # turn variant into 0/1

Xc = m[["is_B", "age"]]
yc = m["converted"]
log = LogisticRegression().fit(Xc, yc)
print("\nLOGISTIC REGRESSION (converted ~ variant + age)")
print(f"  accuracy on training data: {log.score(Xc, yc):.3f}")
for name, coef in zip(Xc.columns, log.coef_[0]):
    print(f"  {name}: coefficient {coef:+.3f} "
          f"({'increases' if coef > 0 else 'decreases'} chance of converting)")

# TODO: based on the coefficients, which matters more for conversion —
#       being in group B, or the customer's age? Note it in the README.
