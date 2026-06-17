# 📊 Capstone Portfolio Project — Build a Full Data Analysis Pipeline

**Your goal:** Take one messy, real-world-style dataset and carry it all the way
from raw mess → clean data → a database → Python analysis → a Power BI dashboard →
a short written report of what you found.

This is the project that ties together **everything** you have learned. When you
finish, this repository becomes a portfolio piece you can show to an employer.

---

## The story

You have been hired (pretend!) as the first data analyst for **DukaOnline**, a small
Kenyan online store. The operations team has been dumping every order into one
spreadsheet, and it is a mess: dates are typed three different ways, phone numbers
have no standard format, county names are misspelled, prices have "KES" stuck on the
front, some rows are duplicated, and some values are missing.

Management wants answers:

1. **Which product categories and products bring in the most revenue?**
2. **Which counties are our best markets?**
3. **Which payment method is most popular?**
4. **Are customers who pay more leaving better ratings, or worse?**
5. **Do ratings differ between our two biggest markets (Nairobi vs Mombasa)?**

Your job is to clean the data and answer these questions with evidence.

---

## The dataset

📁 `data/raw/online_orders_messy.csv` — **220+ online orders** (already provided).

| Column | What it is | The mess to fix |
|---|---|---|
| `order_id` | Unique order code | (clean) |
| `order_date` | Date of the order | 3 formats: `2025-01-05`, `05/01/2025`, `Jan 6 2025` |
| `customer_name` | Buyer's name | Extra spaces, ALL CAPS / lowercase |
| `phone` | Buyer's phone | 4 formats: `07..`, `+2547..`, `2547..`, `7..` |
| `county` | Delivery county | Misspelled: `nairobi`, `NAIROBI`, `Mombassa`; some blank |
| `product` | Item bought | (clean) |
| `category` | Product category | Trailing spaces, `Electronic` vs `Electronics` |
| `quantity` | Units bought | (clean) |
| `unit_price` | Price per unit (KES) | Sometimes `KES 3500` or `3,500` (text, not number!) |
| `payment_method` | How they paid | `M-Pesa` / `Mpesa` / `mpesa`, `Card` / `card`, `Cash` |
| `rating` | Star rating 1–5 | Some blank |

> You may use a **different dataset of your own** if you prefer (e.g. from
> [Kaggle](https://www.kaggle.com/datasets) or your own work) — as long as it is
> messy enough to need cleaning and big enough (100+ rows) to analyse. If you do,
> update the questions above to fit your data.

---

## What to build (5 stages)

Work through the numbered folders in order. Each folder has its own `README.md`
with detailed steps.

### 1️⃣ `01_excel/` — Explore & clean in Excel
- Open the raw CSV in Excel.
- Use filters, `TRIM`, `PROPER`, find-and-replace, and remove duplicates to get a
  feel for the problems.
- Build **one pivot table** (e.g. revenue by category) and **one chart**.
- Save your cleaned workbook as `01_excel/dukaonline_clean.xlsx` and write a few
  notes in `01_excel/notes.md` about what you found and fixed.

### 2️⃣ `02_sql/` — Model it as a database
- Use the provided `schema.sql` to create an `orders` table (SQLite is easiest).
- Load the cleaned data into it.
- Complete the queries in `queries.sql` (revenue by category, top counties, etc.).
- Save the results / screenshots and explain each query in `02_sql/README.md`.

### 3️⃣ `03_python/` — Clean & analyse with Python (the heart of the project)
- Write a cleaning script that fixes **every** problem in the table above and writes
  `data/processed/online_orders_clean.csv`.
- Compute the business answers with `pandas` (`groupby`, `pivot_table`, `.corr()`).
- Make at least **3 charts** with `matplotlib`/`seaborn` and save them to
  `03_python/figures/`.
- Do **one** statistical test or model (your choice):
  - a **t-test** comparing Nairobi vs Mombasa ratings, **or**
  - a **linear regression** predicting `rating` from `unit_price`.

### 4️⃣ `04_powerbi/` — Build a dashboard
- Import `data/processed/online_orders_clean.csv` into Power BI Desktop.
- Build a one-page dashboard with at least **4 visuals** and **2 slicers**
  (e.g. county and category filters) + KPI cards for total revenue and total orders.
- Save the `.pbix` file and **export a screenshot** (PNG) into the folder.

### 5️⃣ `reports/findings.md` — Tell the story
- Write a 1-page report answering the 5 business questions, in plain English,
  with your charts embedded and a final **"3 recommendations for DukaOnline"** section.

### 🏁 Finally — `README.md`
- Turn the top-level `README.md` into a proper portfolio landing page: what the
  project is, the tools you used, your key findings, and links to each stage.

---

## How to submit

1. Do your work in this repository.
2. Commit often with clear messages (`git commit -m "Clean phone numbers in Python"`).
3. Push to GitHub when each stage is done.
4. Make sure the top-level `README.md` looks good — that is the first thing anyone sees.

See **`RUBRIC.md`** for exactly how this is marked. **Take your time and document as
you go.** A portfolio is judged as much on clear explanation as on correct code.

Good luck — make it something you are proud to show off! 🚀
