-- Stage 2 — Database schema
-- Creates the table that will hold your CLEANED orders.
--
-- Easiest way to run this (no install needed if you have Python):
--   See 02_sql/README.md for the exact commands.

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id        TEXT PRIMARY KEY,
    order_date      TEXT,        -- store as 'YYYY-MM-DD'
    customer_name   TEXT,
    phone           TEXT,        -- keep as TEXT so the leading + / 0 is preserved
    county          TEXT,
    product         TEXT,
    category        TEXT,
    quantity        INTEGER,
    unit_price      REAL,        -- a number, NOT 'KES 3,500'
    payment_method  TEXT,
    rating          INTEGER      -- 1..5, may be NULL if the customer didn't rate
);
