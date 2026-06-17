# Stage 4 — Build a Power BI Dashboard

Turn your clean data into a one-page interactive dashboard a manager could use.

> Needs **Power BI Desktop** (free, Windows). Download from the Microsoft Store or
> powerbi.microsoft.com. (No Windows? You can build the same dashboard in
> **Looker Studio** (free, web) or **Tableau Public** and screenshot that instead —
> just note which tool you used.)

## Steps

1. **Import the clean data.**
   `Home → Get Data → Text/CSV` → `data/processed/online_orders_clean.csv`.
   - In the preview, set the **`phone`** column type to **Text** (so `+254…` is kept).
   - Check `unit_price`, `quantity`, `rating` came in as **numbers**, and
     `order_date` as a **date**.

2. **Add a revenue measure.** In the Data/Modelling view:
   `New column` →
   ```
   revenue = orders[quantity] * orders[unit_price]
   ```

3. **Build at least 4 visuals**, for example:
   - **KPI cards**: Total Revenue, Total Orders (use `Card` visuals)
   - **Bar chart**: Revenue by Category
   - **Map or bar**: Revenue by County
   - **Donut/pie**: Orders by Payment Method
   - **Line chart**: Revenue over time (by `order_date` month)

4. **Add at least 2 slicers** (filters the viewer can click):
   - a `county` slicer and a `category` slicer.

5. **Tidy it up.** Add a title ("DukaOnline — Sales Overview"), align the visuals,
   and pick a simple colour theme.

6. **Save & export.**
   - Save the file as `04_powerbi/dukaonline_dashboard.pbix`.
   - Export a screenshot: `File → Export → ...` or just take a screen capture, and
     save it as `04_powerbi/dashboard.png` (the README preview links to this name).

## What to hand in
- `04_powerbi/dukaonline_dashboard.pbix`
- `04_powerbi/dashboard.png` (screenshot of the finished dashboard)

## Notes about my dashboard
*(2–3 sentences: what does the dashboard let someone explore?)*
