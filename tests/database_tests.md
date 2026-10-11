
# NovaMart Database Tests

## 1. Objective

Verify database relationships, data quality, analytics views, and business metric calculations.

## 2. Database Connection

- [ ] Python connects to PostgreSQL successfully.
- [ ] Database name is `novamart`.
- [ ] Required database tables exist.

## 3. Data Integrity Tests

- [ ] Orders reference valid customers.
- [ ] Orders reference valid regions.
- [ ] Order items reference valid orders.
- [ ] Order items reference valid products.
- [ ] Expenses reference valid regions.
- [ ] Expense amounts are positive.
- [ ] Order item quantities are positive.
- [ ] Discounts do not exceed item subtotals.
- [ ] Regional monthly targets contain no duplicates.

## 4. Analytics View Tests

### sales_summary

```sql
SELECT *
FROM analytics.sales_summary
LIMIT 10;
```

Expected: Completed-order items with revenue, cost, and profit.

### monthly_sales

```sql
SELECT *
FROM analytics.monthly_sales
ORDER BY month
LIMIT 12;
```

Expected: Monthly revenue, cost, profit, and units sold.

## 5. Business Metric Validation

- [ ] Total revenue is calculated from completed orders.
- [ ] Total cost uses product cost prices.
- [ ] Profit equals revenue minus cost.
- [ ] Profit margin handles zero revenue safely.
- [ ] Monthly revenue is aggregated by month.
- [ ] Top products are ranked by revenue.

## 6. AI Safety Tests

- [ ] Read-only SELECT queries are allowed.
- [ ] INSERT queries are rejected.
- [ ] UPDATE queries are rejected.
- [ ] DELETE queries are rejected.
- [ ] DROP and ALTER queries are rejected.
- [ ] Queries referencing unapproved objects are rejected.
- [ ] Detailed result queries use appropriate limits.

Note: AI safety tests remain pending until SQL validation is implemented in the application.

## 7. Test Results

Record the actual execution date, query, expected result, actual result, and pass/fail status when running each test.

Do not mark a test as passed until it has been executed successfully.
