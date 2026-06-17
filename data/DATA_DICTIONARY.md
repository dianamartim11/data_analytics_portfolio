# Data Dictionary — DukaOnline

This project uses **five linked tables** (a small "data warehouse"). Understanding
how they connect is the first analyst skill — you JOIN them to answer questions.

## How the tables connect (relationships)

```
            ┌─────────────────┐         ┌──────────────────┐
            │   customers     │         │     products     │
            │  customer_id PK │         │   product_id PK  │
            └────────┬────────┘         └────────┬─────────┘
                     │ 1                       1 │
                     │                           │
                     │  *                      * │
            ┌────────┴───────────────────────────┴────────┐
            │                  orders                      │
            │  order_id PK                                 │
            │  customer_id FK ──> customers.customer_id    │
            │  product_id  FK ──> products.product_id      │
            └────────┬─────────────────────────────────────┘
                     │ 1
                     │ * (≈8% of orders)
            ┌────────┴────────┐        ┌─────────────────────┐
            │    returns      │        │      ab_test        │
            │  return_id PK   │        │  customer_id FK ──> customers
            │  order_id FK    │        │  variant, converted │
            └─────────────────┘        └─────────────────────┘
```
*PK = primary key (unique id).  FK = foreign key (points to another table's PK).*

- One **customer** can have many **orders**.
- One **product** can appear in many **orders**.
- One **order** may have zero or one **return**.
- Each exposed **customer** has one **ab_test** row (the marketing experiment).

---

## Tables & columns

### `customers_raw.csv` — one row per customer *(messy — needs cleaning)*
| Column | Type | Notes / mess to fix |
|---|---|---|
| `customer_id` | text (PK) | `C0001` … clean |
| `name` | text | Extra spaces, mixed CAPS/lowercase |
| `phone` | text | 4 formats: `07..`, `+2547..`, `2547..`, `7..` |
| `county` | text | Misspellings (`nairobi`, `Mombassa`); some blank |
| `gender` | text | `M`/`F`/`Male`/`Female`/`m`/`f`; some blank |
| `age` | number | A few impossible values (0, 150, 200) — outliers |
| `signup_date` | date | 3 date formats |

### `products.csv` — reference list of products *(already clean)*
| Column | Type | Notes |
|---|---|---|
| `product_id` | text (PK) | `P01` … |
| `product_name` | text | |
| `category` | text | Electronics / Clothing / Stationery / Home |
| `cost_price` | number | What DukaOnline pays per unit (KES) |
| `list_price` | number | The normal selling price (KES) — use for profit margin |

### `orders_raw.csv` — one row per order line *(messy — needs cleaning)*
| Column | Type | Notes / mess to fix |
|---|---|---|
| `order_id` | text (PK) | `ORD10000` … |
| `customer_id` | text (FK) | → `customers.customer_id` |
| `product_id` | text (FK) | → `products.product_id` |
| `order_date` | date | 3 date formats; spans Jan-2024 → Jun-2025 |
| `quantity` | number | A few extreme values (40/60/100) — outliers |
| `unit_price` | number | Text: `KES 3,500` / `3,500` — convert to number |
| `discount` | number | 0, 0.05, 0.10, 0.15 (fraction off list price) |
| `payment_method` | text | `M-Pesa`/`Mpesa`/`mpesa`, `Card`/`card`, `Cash` |
| `channel` | text | `Web`/`App`/`Store` (casing varies) |
| `rating` | number | 1–5 stars; some blank (customer didn't rate) |
| *(duplicates)* | — | Some whole rows are duplicated on purpose |

### `returns.csv` — orders that were returned *(lightly messy)*
| Column | Type | Notes |
|---|---|---|
| `return_id` | text (PK) | `RET500` … |
| `order_id` | text (FK) | → `orders.order_id` |
| `return_date` | date | 3 date formats |
| `reason` | text | `Damaged`/`Wrong item`/`Changed mind`/`Late delivery`/`Faulty` (casing varies) |

### `ab_test.csv` — marketing experiment *(lightly messy)*
| Column | Type | Notes |
|---|---|---|
| `customer_id` | text (FK) | → `customers.customer_id` |
| `variant` | text | `A` = control (old email), `B` = treatment (new email) |
| `exposed_date` | date | When they got the campaign |
| `converted` | number | 1 = bought after seeing it, 0 = did not |

---

## Derived fields you will create
| Field | Formula | Used for |
|---|---|---|
| `revenue` | `quantity * unit_price` | Sales analysis |
| `profit` | `(unit_price - cost_price) * quantity` | Margin analysis (needs join to products) |
| `order_month` | month of `order_date` | Time-series trends |
| RFM (`recency`,`frequency`,`monetary`) | per customer from orders | Customer segmentation |
