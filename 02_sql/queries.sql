-- Stage 2 — Analysis queries
-- Complete each query below. The first one is done for you as an example.
-- Run them against the `orders` table after loading your CLEANED data.

-- ------------------------------------------------------------------
-- Q1 (EXAMPLE - already done): Total revenue and number of orders
-- ------------------------------------------------------------------
SELECT
    COUNT(*)                       AS total_orders,
    SUM(quantity * unit_price)     AS total_revenue
FROM orders;


-- ------------------------------------------------------------------
-- Q2: Revenue by category, highest first
-- Hint: GROUP BY category, ORDER BY ... DESC
-- ------------------------------------------------------------------
-- YOUR QUERY HERE


-- ------------------------------------------------------------------
-- Q3: Top 5 counties by revenue
-- Hint: GROUP BY county, ORDER BY revenue DESC, LIMIT 5
-- ------------------------------------------------------------------
-- YOUR QUERY HERE


-- ------------------------------------------------------------------
-- Q4: Number of orders per payment method (which is most popular?)
-- Hint: GROUP BY payment_method, COUNT(*)
-- ------------------------------------------------------------------
-- YOUR QUERY HERE


-- ------------------------------------------------------------------
-- Q5: Average rating per category (ignore NULL ratings)
-- Hint: AVG(rating) ignores NULLs automatically
-- ------------------------------------------------------------------
-- YOUR QUERY HERE


-- ------------------------------------------------------------------
-- Q6 (CHALLENGE): The single best-selling product by revenue
-- ------------------------------------------------------------------
-- YOUR QUERY HERE
