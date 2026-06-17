# Stage 4 — Statistics & Modelling

This is where you go beyond "what happened" to "is it real?" and "what will
happen?". Each script is a starter with `# TODO`s. Run them from the project root
after Stage 3 cleaning, e.g. `python3 04_statistics/01_outliers_descriptives.py`.

Save any charts to `04_statistics/figures/` and paste key numbers into the
"Results" section at the bottom of this file.

## The scripts

### `01_outliers_descriptives.py` — describe the data & find outliers
- Descriptive stats: mean, median, mode, std, quartiles.
- **IQR rule** to flag outliers (e.g. those quantity = 100 orders): an outlier is
  below `Q1 - 1.5*IQR` or above `Q3 + 1.5*IQR`.
- Box plots to show them.

### `02_ab_test.py` — did the new marketing email work?
- Compare conversion rate of **variant A** (control) vs **variant B** (treatment).
- Build a **95% confidence interval** for each rate.
- Run a **hypothesis test** (two-proportion / chi-square) → p-value.
- State the conclusion in plain English: is B *significantly* better?

### `03_regression.py` — predict things
- **Linear regression**: predict `rating` from `unit_price` (and `discount`).
  Report slope, intercept, R², and what it means.
- **Logistic regression**: predict `converted` (0/1) from `variant` + `age`.
  Report accuracy and which factor matters most.

### `04_timeseries.py` — trends over time
- Monthly revenue line.
- **3-month moving average** to smooth the trend.
- **Month-over-month** and **year-over-year** growth %.
- Comment on seasonality (look at December).

### `05_rfm_segmentation.py` — who are our best customers?
- For each customer compute **Recency** (days since last order),
  **Frequency** (number of orders), **Monetary** (total spend).
- Score each 1–4 and combine into segments (e.g. "Champions", "At risk").
- Chart the segment sizes.

## Hand in
- The five completed scripts
- Charts in `04_statistics/figures/`
- The "Results" section below filled in (this is what proves the stats skills)

---

## Results
*(fill in with your numbers and one-line interpretations)*

- **Outliers found:** …
- **A/B test:** A = __% , B = __% , p = __ → conclusion: …
- **Linear regression:** rating = __·price + __, R² = __ → …
- **Logistic regression:** accuracy __ ; biggest driver of conversion = …
- **Time series:** trend is … ; December effect: …
- **RFM segments:** Champions = __ customers; At-risk = __ ; …
