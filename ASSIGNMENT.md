# 📊 Capstone Portfolio Project — End-to-End Data Analysis

**Goal:** Take a realistic, messy, multi-table business dataset and carry it through
the **complete data-analyst workflow** — Excel, SQL, Python, statistics & modelling,
and Power BI — then communicate your findings like a professional.

When you finish, this repository is a portfolio piece that proves you can do the
job. You will share your **outcomes and screenshots** (tables, charts, dashboards)
as evidence of each skill.

> 📋 Two companion files drive this project:
> - **[`SKILLS_CHECKLIST.md`](SKILLS_CHECKLIST.md)** — every skill to demonstrate + what to capture
> - **[`RUBRIC.md`](RUBRIC.md)** — how it is marked
> - **[`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md)** — the tables, columns, and how they link

---

## The scenario

You are the first data analyst at **DukaOnline**, a Kenyan online store. All the
data already exists in `data/raw/` — five linked tables (customers, products,
orders, returns, and a marketing experiment). It is messy on purpose. Management
wants you to clean it, analyse it, and answer real business questions.

### Business questions you must answer
1. **Revenue** — Which categories, products, counties, and channels make the most money?
2. **Profit** — Which categories are most *profitable* (not just highest revenue)? *(needs the cost vs list price join)*
3. **Trends** — How are sales changing month over month? Is there seasonality?
4. **Customers** — Who are our best customers? Can we segment them (RFM)?
5. **Quality** — What gets returned most, and why?
6. **Experiment** — Did the new marketing email (variant B) convert better than the old one (A)? Is the difference *statistically significant*?
7. **Prediction** — Can we predict which customers will convert?

---

## The dataset (already provided)

Five CSVs in [`data/raw/`](data/raw/). Read **[`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md)**
for full details and the table-relationship diagram.

| File | Rows | What |
|---|---|---|
| `customers_raw.csv` | 300 | Customers (messy) |
| `products.csv` | 20 | Product catalogue (clean reference) |
| `orders_raw.csv` | 2,000+ | Orders, Jan-2024 → Jun-2025 (messy, has duplicates) |
| `returns.csv` | ~160 | Returned orders |
| `ab_test.csv` | 240 | Marketing experiment (variant A/B, converted yes/no) |

> Everything you need is here. You do **not** need to find external data (though you
> may add some if you want — e.g. pull live data from an API for bonus credit).

---

## The five stages (work the numbered folders in order)

Each folder has its own `README.md` with detailed, step-by-step instructions.

| Stage | Folder | You will demonstrate |
|---|---|---|
| 1️⃣ | [`01_excel/`](01_excel/) | Excel: formulas, `VLOOKUP`/`XLOOKUP`, pivots, conditional formatting, a dashboard |
| 2️⃣ | [`02_sql/`](02_sql/) | SQL: joins, `GROUP BY`/`HAVING`, `CASE`, dates, CTEs, **window functions** |
| 3️⃣ | [`03_python/`](03_python/) | Python/pandas: cleaning all 5 tables, merging, EDA, charts, a **Jupyter notebook** |
| 4️⃣ | [`04_statistics/`](04_statistics/) | Stats: outliers (IQR), confidence intervals, **A/B test**, linear & **logistic regression**, **time series**, **RFM segmentation** |
| 5️⃣ | [`05_powerbi/`](05_powerbi/) | Power BI: Power Query, relationships, **DAX measures**, an interactive dashboard |
| 🏁 | [`reports/`](reports/) + `README.md` | Storytelling, recommendations, **data-ethics note**, polished portfolio page |

---

## How to work & submit

1. **Set up Python** once (see `03_python/README.md`).
2. **Go stage by stage.** Don't skip — later stages use the cleaned data from Stage 3.
3. **Capture evidence as you go** — screenshots, exported charts, query results.
   The `SKILLS_CHECKLIST.md` tells you exactly what to capture for each skill.
4. **Commit often** with clear messages, and push to GitHub.
5. **Finish the top-level `README.md`** — it is your portfolio's front page.

> ⏱️ This is a *big* project — that's the point. Treat it like a real job: do a
> little each day, document everything, and don't aim for perfect cleaning in
> Excel (that's what Python is for). Quality of explanation matters as much as
> quality of code.

Make something you're proud to show an employer. 🚀
