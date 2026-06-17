"""
02_ab_test.py  —  STARTER
-------------------------
Did marketing variant B convert better than variant A?
Covers: conversion rates, 95% confidence intervals, a significance test.
Run from project root:  python3 04_statistics/02_ab_test.py
"""

import pandas as pd
from scipy import stats
import math

ab = pd.read_csv("data/processed/ab_test_clean.csv")

# --- conversion rate per variant -------------------------------------------
summary = ab.groupby("variant")["converted"].agg(["sum", "count", "mean"])
summary.columns = ["conversions", "exposed", "rate"]
print(summary)

# --- 95% confidence interval for each rate ---------------------------------
def conf_interval(conversions, n):
    p = conversions / n
    se = math.sqrt(p * (1 - p) / n)        # standard error of a proportion
    return p - 1.96 * se, p + 1.96 * se    # 95% CI

for v in summary.index:
    c, n = summary.loc[v, "conversions"], summary.loc[v, "exposed"]
    lo, hi = conf_interval(c, n)
    print(f"Variant {v}: rate {c/n:.1%}  95% CI [{lo:.1%}, {hi:.1%}]")

# --- significance test: is B really better than A? -------------------------
# A 2x2 table of converted vs not, by variant, tested with chi-square.
table = pd.crosstab(ab["variant"], ab["converted"])
chi2, p, dof, _ = stats.chi2_contingency(table)
print(f"\nChi-square test: chi2 = {chi2:.3f}, p = {p:.4f}")
print("Result:", "B is SIGNIFICANTLY different from A (p<0.05)" if p < 0.05
      else "no significant difference (p>=0.05)")

# TODO: in one sentence in the README, recommend whether DukaOnline should roll
#       out variant B to everyone, and why (use the rates + the p-value).
