
-- ==========================================
-- NOVAMART BUSINESS ANALYTICS
-- Day 13: SQL Queries
-- ==========================================

-- 1. Total Revenue from Completed Orders
SELECT
    ROUND(
        SUM(oi.quantity * oi.unit_price - oi.discount),
        2
    ) AS total_revenue
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.order_status = 'Completed';


-- 2. Total Profit from Completed Orders
SELECT
    ROUND(
        SUM(
            (oi.quantity * oi.unit_price - oi.discount)
            - (oi.quantity * p.cost_price)
        ),
        2
    ) AS total_profit
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE o.order_status = 'Completed';


-- 3. Revenue by Region
SELECT
    r.region_name,
    ROUND(
        SUM(oi.quantity * oi.unit_price - oi.discount),
        2
    ) AS revenue
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN regions r
    ON o.region_id = r.region_id
WHERE o.order_status = 'Completed'
GROUP BY r.region_name
ORDER BY revenue DESC;



-- 4. Monthly Revenue
SELECT
    DATE_TRUNC('month', o.order_date)::DATE AS month,
    ROUND(
        SUM(oi.quantity * oi.unit_price - oi.discount),
        2
    ) AS monthly_revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'Completed'
GROUP BY DATE_TRUNC('month', o.order_date)
ORDER BY month;


-- 5. Top 10 Best-Selling Products by Revenue
SELECT
    p.product_name,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(oi.quantity * oi.unit_price - oi.discount),
        2
    ) AS revenue
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE o.order_status = 'Completed'
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC
LIMIT 10;


-- 6. Kerala Sales
SELECT
    r.region_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(
        SUM(oi.quantity * oi.unit_price - oi.discount),
        2
    ) AS revenue
FROM orders o
JOIN order_items oi
    ON oi.order_id = o.order_id
JOIN regions r
    ON o.region_id = r.region_id
WHERE o.order_status = 'Completed'
  AND r.region_name ILIKE '%Kerala%'
GROUP BY r.region_name;



-- 7. Overall Profit Margin
SELECT
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(
        100.0 * SUM(profit) / NULLIF(SUM(revenue), 0),
        2
    ) AS profit_margin_percentage
FROM (
    SELECT
        oi.quantity * oi.unit_price - oi.discount AS revenue,
        oi.quantity * oi.unit_price
            - oi.discount
            - oi.quantity * p.cost_price AS profit
    FROM order_items oi
    JOIN orders o
        ON oi.order_id = o.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    WHERE o.order_status = 'Completed'
) AS sales;


-- 8. Top 10 Customers by Revenue
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(
        SUM(oi.quantity * oi.unit_price - oi.discount),
        2
    ) AS total_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'Completed'
GROUP BY c.customer_id, c.customer_name
ORDER BY total_revenue DESC
LIMIT 10;


-- 9. Monthly Revenue Growth
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', o.order_date)::DATE AS month,
        SUM(oi.quantity * oi.unit_price - oi.discount) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    WHERE o.order_status = 'Completed'
    GROUP BY DATE_TRUNC('month', o.order_date)
),
revenue_with_previous_month AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) AS previous_month_revenue
    FROM monthly_revenue
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(previous_month_revenue, 2) AS previous_month_revenue,
    ROUND(
        100.0 * (revenue - previous_month_revenue)
        / NULLIF(previous_month_revenue, 0),
        2
    ) AS growth_percentage
FROM revenue_with_previous_month
ORDER BY month;



-- 10. Data Quality Checks

-- Check 1: Orders without a valid customer
SELECT COUNT(*) AS invalid_customer_orders
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;


-- Check 2: Order items without a valid order
SELECT COUNT(*) AS invalid_order_items
FROM order_items oi
LEFT JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;


-- Check 3: Order items without a valid product
SELECT COUNT(*) AS invalid_product_items
FROM order_items oi
LEFT JOIN products p
    ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;


-- Check 4: Invalid or non-positive order item values
SELECT COUNT(*) AS invalid_order_item_values
FROM order_items
WHERE quantity <= 0
   OR unit_price < 0
   OR discount < 0
   OR discount > quantity * unit_price;


-- Check 5: Expenses with invalid regions or amounts
SELECT COUNT(*) AS invalid_expenses
FROM expenses e
LEFT JOIN regions r
    ON e.region_id = r.region_id
WHERE r.region_id IS NULL
   OR e.amount <= 0;


-- Check 6: Duplicate monthly targets for a region
SELECT
    region_id,
    target_month,
    COUNT(*) AS duplicate_count
FROM targets
GROUP BY region_id, target_month
HAVING COUNT(*) > 1;
