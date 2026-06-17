# Stage 5 — Power BI: model, DAX & an interactive dashboard

Turn your clean data into a dashboard a manager could actually use — and show the
BI skills employers pay for: **Power Query** (transform), **relationships** (model),
and **DAX** (measures).

> Needs **Power BI Desktop** (free, Windows). No Windows? Build the same thing in
> **Looker Studio** (free, web) or **Tableau Public** and screenshot that — just
> say which tool you used. Save all screenshots to `05_powerbi/screenshots/`.

## 1. Get Data (import all the tables)
`Home → Get Data → Text/CSV` and import from `data/processed/`:
`orders_clean.csv`, `products_clean.csv`, `customers_clean.csv`, `returns_clean.csv`.
- Set `phone` to **Text**; check numbers/dates imported correctly.

## 2. Power Query (transform step) — skill F2
Open `Transform Data`. Do at least one transform in the query editor itself
(e.g. trim a text column, change a type, or add a column). This shows you can
clean inside Power BI, not only in Python. Screenshot the Applied Steps.

## 3. Model the relationships — skill F3
In `Model` view, connect the tables (drag the keys):
- `orders[customer_id]` → `customers[customer_id]`
- `orders[product_id]` → `products[product_id]`
- `returns[order_id]` → `orders[order_id]`
Screenshot the relationship diagram.

## 4. DAX measures — skill F4 (the important one)
In `Modeling → New measure`, create at least three:
```DAX
Total Revenue = SUMX(orders, orders[quantity] * orders[unit_price])

Total Profit  = SUMX(orders, (orders[unit_price] - RELATED(products[cost_price])) * orders[quantity])

Profit Margin % = DIVIDE([Total Profit], [Total Revenue])

Total Orders = DISTINCTCOUNT(orders[order_id])
```
> A **measure** (calculated on the fly when you filter) is different from a
> calculated column — using measures is the skill being tested.

## 5. Build the dashboard (one page) — skills F5–F7
- **KPI cards**: Total Revenue, Total Profit, Profit Margin %, Total Orders
- **Bar**: Revenue by Category
- **Map or bar**: Revenue by County
- **Line**: Revenue by month (uses `order_date`)
- **Donut**: Orders by Channel or Payment Method
- **Slicers**: County, Category, and a Date range
Give it a title and a clean colour theme.

## 6. Export — skill F8
- Save as `05_powerbi/dukaonline_dashboard.pbix`
- Export a screenshot to `05_powerbi/dashboard.png` (the README preview uses this name).

## Hand in
- `dukaonline_dashboard.pbix`
- `dashboard.png` + the `screenshots/` evidence (Power Query, model, DAX)

## Notes about my dashboard
*(2–3 sentences: what can a viewer explore, and what's the headline insight?)*
