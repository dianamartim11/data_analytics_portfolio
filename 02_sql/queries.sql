-- Stage 2 — Analysis queries (basics → window functions)
-- Complete each query. Q1, Q3 and Q5 are done as worked examples; the rest are
-- yours. Run them against your CLEANED data (see load_data.py).
-- Paste each result (numbers or a screenshot) into 02_sql/README.md.

-- ==================================================================
-- LEVEL 1 — Basics
-- ==================================================================

-- Q1 (EXAMPLE): total orders and total revenue
SELECT COUNT(*) AS total_orders,
       SUM(quantity * unit_price) AS total_revenue
FROM orders;

-- Q2: the 10 highest-value single orders (quantity * unit_price), highest first
--     Skills: SELECT, computed column, ORDER BY, LIMIT
-- YOUR QUERY HERE


-- ==================================================================
-- LEVEL 2 — Grouping & aggregation
-- ==================================================================

-- Q3 (EXAMPLE): revenue by payment method
SELECT payment_method,
       COUNT(*)                    AS orders,
       SUM(quantity * unit_price)  AS revenue
FROM orders
GROUP BY payment_method
ORDER BY revenue DESC;

-- Q4: average rating per channel, but ONLY channels with at least 50 orders
--     Skills: GROUP BY ... HAVING
-- YOUR QUERY HERE


-- ==================================================================
-- LEVEL 3 — Joins (this is what makes the tables worth having)
-- ==================================================================

-- Q5 (EXAMPLE): revenue by product CATEGORY  (orders must join to products)
SELECT p.category,
       SUM(o.quantity * o.unit_price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- Q6: total PROFIT by category.  profit per line = (unit_price - cost_price) * quantity
--     Skills: INNER JOIN + arithmetic across tables
-- YOUR QUERY HERE

-- Q7: which COUNTIES spend the most?  (orders -> customers)
--     Skills: JOIN to customers, GROUP BY county
-- YOUR QUERY HERE

-- Q8: how many orders were RETURNED vs not returned?
--     Skills: LEFT JOIN orders -> returns, then count where return_id IS NULL / NOT NULL
-- YOUR QUERY HERE


-- ==================================================================
-- LEVEL 4 — CASE, dates, subqueries, CTEs
-- ==================================================================

-- Q9: bucket every order into a price tier and count them:
--     'Low' (< 1000), 'Medium' (1000-2999), 'High' (>= 3000) by unit_price
--     Skills: CASE WHEN
-- YOUR QUERY HERE

-- Q10: revenue by month.  In SQLite use substr(order_date,1,7) to get 'YYYY-MM'.
--      Skills: date handling, GROUP BY month, ORDER BY month
-- YOUR QUERY HERE

-- Q11: customers who spent MORE than the average customer.
--      Skills: subquery (compare each customer's spend to the overall average)
-- YOUR QUERY HERE

-- Q12: use a CTE (WITH) to first compute revenue per product, then return the
--      single top product in EACH category.
--      Skills: WITH ... AS (...), then filter
-- YOUR QUERY HERE


-- ==================================================================
-- LEVEL 5 — Window functions (the "senior" skill)
-- ==================================================================

-- Q13: rank products by revenue WITHIN their category (1 = best in category).
--      Skills: RANK() OVER (PARTITION BY category ORDER BY revenue DESC)
-- YOUR QUERY HERE

-- Q14: running (cumulative) total of monthly revenue across the 18 months.
--      Skills: SUM(...) OVER (ORDER BY month) on top of a monthly-revenue CTE
-- YOUR QUERY HERE

-- Q15 (CHALLENGE): month-over-month revenue change using LAG().
--      Skills: LAG(revenue) OVER (ORDER BY month), then revenue - previous
-- YOUR QUERY HERE
