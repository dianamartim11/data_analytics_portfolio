-- Stage 2 — Database schema (all five tables)
-- Creates the tables that hold your CLEANED data, with the keys that link them.
-- See 02_sql/README.md for how to run this (SQLite, one command).

DROP TABLE IF EXISTS returns;
DROP TABLE IF EXISTS ab_test;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;

CREATE TABLE customers (
    customer_id   TEXT PRIMARY KEY,
    name          TEXT,
    phone         TEXT,           -- TEXT so '+254..' is preserved
    county        TEXT,
    gender        TEXT,
    age           INTEGER,
    signup_date   TEXT            -- 'YYYY-MM-DD'
);

CREATE TABLE products (
    product_id    TEXT PRIMARY KEY,
    product_name  TEXT,
    category      TEXT,
    cost_price    REAL,
    list_price    REAL
);

CREATE TABLE orders (
    order_id        TEXT PRIMARY KEY,
    customer_id     TEXT REFERENCES customers(customer_id),
    product_id      TEXT REFERENCES products(product_id),
    order_date      TEXT,         -- 'YYYY-MM-DD'
    quantity        INTEGER,
    unit_price      REAL,         -- a number, NOT 'KES 3,500'
    discount        REAL,
    payment_method  TEXT,
    channel         TEXT,
    rating          INTEGER       -- 1..5, may be NULL
);

CREATE TABLE returns (
    return_id     TEXT PRIMARY KEY,
    order_id      TEXT REFERENCES orders(order_id),
    return_date   TEXT,
    reason        TEXT
);

CREATE TABLE ab_test (
    customer_id   TEXT REFERENCES customers(customer_id),
    variant       TEXT,           -- 'A' control, 'B' treatment
    exposed_date  TEXT,
    converted     INTEGER         -- 1 / 0
);
