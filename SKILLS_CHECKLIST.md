# 🎯 Skills Coverage Checklist

This is the **master map** of every data-analysis skill this project demonstrates,
where you do it, and **what to capture** (screenshot / table / chart) to prove it.

> For each row: do the work, then save the evidence into that stage's folder.
> Tick the box when the evidence is in the repo. By the end, every box is ticked
> and you have a complete portfolio.

Legend for "Capture": 📷 screenshot · 📊 chart image · 🔢 table/numbers · 💾 file

---

## A. Excel  → folder `01_excel/`
| # | Skill | Capture | Done |
|---|---|---|---|
| A1 | Import CSV, set data types | 📷 | ☐ |
| A2 | `TRIM`, `PROPER`, `UPPER`/`LOWER` text cleanup | 📷 | ☐ |
| A3 | Find & Replace to fix spellings | 📷 | ☐ |
| A4 | `IF`, `SUMIF`, `COUNTIF`, `AVERAGEIF` | 📷 | ☐ |
| A5 | `VLOOKUP` **or** `XLOOKUP` (join products onto orders) | 📷 | ☐ |
| A6 | `INDEX`/`MATCH` | 📷 | ☐ |
| A7 | Remove duplicates | 📷 | ☐ |
| A8 | Conditional formatting (highlight top/bottom) | 📷 | ☐ |
| A9 | Data validation (dropdown list) | 📷 | ☐ |
| A10 | PivotTable (revenue by category) | 📷🔢 | ☐ |
| A11 | PivotChart / chart | 📊 | ☐ |
| A12 | A small Excel dashboard sheet | 📷 | ☐ |

## B. SQL  → folder `02_sql/`
| # | Skill | Capture | Done |
|---|---|---|---|
| B1 | `CREATE TABLE` / load data | 🔢 | ☐ |
| B2 | `SELECT … WHERE … ORDER BY … LIMIT` | 🔢 | ☐ |
| B3 | Aggregates `SUM/COUNT/AVG/MIN/MAX` + `GROUP BY` | 🔢 | ☐ |
| B4 | `GROUP BY … HAVING` | 🔢 | ☐ |
| B5 | `INNER JOIN` (orders × products) | 🔢 | ☐ |
| B6 | `LEFT JOIN` (orders × returns — find non-returns) | 🔢 | ☐ |
| B7 | Multi-table join (orders × customers × products) | 🔢 | ☐ |
| B8 | `CASE WHEN` (bucket into tiers) | 🔢 | ☐ |
| B9 | Date functions (revenue by month/year) | 🔢 | ☐ |
| B10 | Subquery | 🔢 | ☐ |
| B11 | CTE (`WITH …`) | 🔢 | ☐ |
| B12 | Window function (`RANK`/`ROW_NUMBER`/running total) | 🔢 | ☐ |

## C. Python — cleaning & wrangling  → folder `03_python/`
| # | Skill | Capture | Done |
|---|---|---|---|
| C1 | Load CSVs with pandas, inspect `.info()/.describe()` | 🔢 | ☐ |
| C2 | Clean text (strip, title-case, fix spellings) | 💾 | ☐ |
| C3 | Parse mixed-format dates → datetime | 💾 | ☐ |
| C4 | Convert `KES 3,500` text → number | 💾 | ☐ |
| C5 | Normalise phone numbers (regex) | 💾 | ☐ |
| C6 | Drop duplicates, handle missing values | 💾 | ☐ |
| C7 | Merge/join tables in pandas (`.merge`) | 🔢 | ☐ |
| C8 | `groupby` + `pivot_table` aggregation | 🔢 | ☐ |
| C9 | Write cleaned tables to `data/processed/` | 💾 | ☐ |
| C10 | Do the whole analysis in a **Jupyter notebook** | 📷💾 | ☐ |

## D. Visualisation  → `03_python/figures/` (and Power BI)
| # | Skill | Capture | Done |
|---|---|---|---|
| D1 | Bar chart (revenue by category) | 📊 | ☐ |
| D2 | Line chart (revenue over time) | 📊 | ☐ |
| D3 | Histogram (rating or order value distribution) | 📊 | ☐ |
| D4 | Box plot (spot outliers) | 📊 | ☐ |
| D5 | Scatter plot (price vs rating) | 📊 | ☐ |
| D6 | Correlation heatmap | 📊 | ☐ |
| D7 | Grouped/stacked bar (channel × category) | 📊 | ☐ |

## E. Statistics & modelling  → folder `04_statistics/`
| # | Skill | Capture | Done |
|---|---|---|---|
| E1 | Descriptive stats (mean/median/mode/std) | 🔢 | ☐ |
| E2 | Outlier detection with the IQR rule | 🔢📊 | ☐ |
| E3 | Correlation analysis + interpretation | 🔢 | ☐ |
| E4 | Confidence interval (e.g. conversion rate) | 🔢 | ☐ |
| E5 | **A/B test** (variant A vs B conversion) | 🔢 | ☐ |
| E6 | Hypothesis test (t-test or chi-square) + p-value | 🔢 | ☐ |
| E7 | **Linear regression** (predict rating from price) | 🔢📊 | ☐ |
| E8 | **Logistic regression** (predict `converted`) | 🔢 | ☐ |
| E9 | **Time-series** trend + 3-month moving average | 📊 | ☐ |
| E10 | Month-over-month / YoY growth % | 🔢 | ☐ |
| E11 | **RFM customer segmentation** | 🔢📊 | ☐ |

## F. Power BI (BI / dashboarding)  → folder `05_powerbi/`
| # | Skill | Capture | Done |
|---|---|---|---|
| F1 | Get Data + set column types | 📷 | ☐ |
| F2 | **Power Query** transform step (clean in the query editor) | 📷 | ☐ |
| F3 | Model relationships between tables | 📷 | ☐ |
| F4 | **DAX measure** (e.g. Total Revenue, Profit Margin %) | 📷 | ☐ |
| F5 | KPI cards | 📷 | ☐ |
| F6 | 4+ visuals on one page | 📷 | ☐ |
| F7 | Slicers / filters (county, category, date) | 📷 | ☐ |
| F8 | Export dashboard screenshot | 📷 | ☐ |

## G. Communication & professionalism  → `reports/` + repo
| # | Skill | Capture | Done |
|---|---|---|---|
| G1 | Frame the business questions clearly | ✍️ | ☐ |
| G2 | Data-storytelling write-up with embedded charts | ✍️📊 | ☐ |
| G3 | 3 actionable recommendations | ✍️ | ☐ |
| G4 | **Data ethics / PII note** (names + phones!) | ✍️ | ☐ |
| G5 | Clean Git history (frequent, clear commits) | 📷 | ☐ |
| G6 | Polished top-level `README.md` portfolio page | ✍️ | ☐ |

---

### Save your evidence
Make a `screenshots/` subfolder inside each stage folder and drop your 📷 there.
Charts (📊) from Python go in `03_python/figures/` and `04_statistics/figures/`.
Numbers/tables (🔢) can be pasted into that stage's `README.md`.
