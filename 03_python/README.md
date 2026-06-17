# Stage 3 — Clean & Analyse with Python

This is the **most important** stage. Here you build a *repeatable* cleaning
pipeline (unlike Excel, where you cleaned by hand) and answer the business
questions with code.

## Setup (once)
From the project root:
```bash
python3 -m venv .venv
# Windows:  .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## The two scripts

### `clean.py` — fix every problem and save a clean file
A starter version is provided with `# TODO` markers. Your job is to fill them in
so it fixes **all** of these and writes `data/processed/online_orders_clean.csv`:

- [ ] Standardise column text (strip spaces, fix capitalisation)
- [ ] Parse `order_date` (all 3 formats) into a real date → save as `YYYY-MM-DD`
- [ ] Convert `unit_price` from `KES 3,500` / `3,500` text into a number
- [ ] Normalise `phone` to one format (e.g. `+2547XXXXXXXX`)
- [ ] Fix `county` spellings (`nairobi`/`NAIROBI` → `Nairobi`, `Mombassa` → `Mombasa`)
- [ ] Fix `category` (`Electronic` → `Electronics`, trailing spaces)
- [ ] Standardise `payment_method` (`mpesa`/`Mpesa` → `M-Pesa`, `card` → `Card`)
- [ ] Drop duplicate rows
- [ ] Decide what to do with blank `county` / `rating` (drop? fill? — explain why)

> 🧠 You already practised every one of these in the class repo
> (`normalisephonedropduplicatesandsave.py`, `fixamountandparse.py`,
> `standardisetheservice.py`, `prepare_for_powerbi.py`). Reuse those ideas!

### `analyse.py` — answer the business questions
A starter version is provided. Make it:
- [ ] Add a `revenue = quantity * unit_price` column
- [ ] Print revenue by **category** and by **county** (`groupby`)
- [ ] Print orders per **payment_method**
- [ ] Build a correlation table (`unit_price`, `quantity`, `rating`, `revenue`)
- [ ] Save **at least 3 charts** to `figures/` (bar, line/hist, and a heatmap)
- [ ] Do **one** of:
  - **t-test**: do Nairobi and Mombasa have different average ratings?
    (`scipy.stats.ttest_ind`) — print the p-value and say what it means.
  - **regression**: predict `rating` from `unit_price`
    (`sklearn.linear_model.LinearRegression`) — print slope, intercept, R².

## Run it
```bash
python3 03_python/clean.py      # writes data/processed/online_orders_clean.csv
python3 03_python/analyse.py    # prints answers, saves charts to figures/
```

## What to hand in
- `clean.py` and `analyse.py` (completed)
- `data/processed/online_orders_clean.csv` (generated)
- 3+ PNG charts in `03_python/figures/`
