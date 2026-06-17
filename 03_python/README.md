# Stage 3 — Python: clean, merge & explore (the engine room)

This is the heart of the project. Here you build a **repeatable** cleaning pipeline
for all five tables, merge them, and explore the data. Unlike Excel, your cleaning
here is code anyone can re-run.

## Setup (once)
From the project root:
```bash
python3 -m venv .venv
# Windows:   .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## What to do
1. **`clean.py`** — finish the `# TODO`s so it cleans every problem listed in
   [`data/DATA_DICTIONARY.md`](../data/DATA_DICTIONARY.md) and writes the five
   `*_clean.csv` files to `data/processed/`:
   - text cleanup (spaces, capitalisation, spellings)
   - mixed-format dates → `YYYY-MM-DD`
   - `KES 3,500` → number
   - phone → `+2547XXXXXXXX` (regex)
   - standardise `gender`, `payment_method`, `channel`, `reason`
   - drop duplicates; set impossible ages to missing; keep blank ratings as missing
2. **`analyse.py`** — finish the `# TODO`s: **merge** orders↔products↔customers,
   add `revenue` and `profit`, answer the revenue/profit/county/channel/return-rate
   questions, and save the charts.
3. **`notebook/analysis.ipynb`** — open it in Jupyter / VS Code and tell the story
   with code + narrative together (this is how analysts actually present work):
   ```bash
   pip install jupyter        # if not already
   jupyter notebook 03_python/notebook/analysis.ipynb
   ```

## Run it
```bash
python3 03_python/clean.py      # writes data/processed/*_clean.csv
python3 03_python/analyse.py    # prints answers, saves charts to figures/
```

## Charts to produce (save to `figures/`)
Bar (revenue by category), line (revenue by month), histogram (ratings),
box plot (price by category — shows outliers), correlation heatmap.
*(Scatter and grouped bars are nice extras.)*

## Hand in
- Completed `clean.py`, `analyse.py`, and `notebook/analysis.ipynb`
- `data/processed/*_clean.csv` (generated — these feed SQL, stats & Power BI)
- 4+ charts in `03_python/figures/`

> 🔁 The cleaning here is the same toolbox as the class `prepare_for_powerbi.py`,
> just applied to five tables instead of one.
