# Final Database Blueprint

## Database Technology

PostgreSQL

---

## Overall Database Architecture

```text
                         POSTGRESQL
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
        MASTER DATA     TRANSACTIONS      ANALYTICS
             │                │                │
             ▼                ▼                ▼
        customers          orders          KPI Views
        products           order_items     Aggregations
        categories
        stores
        regions
        employees
             │
             │
             ▼
       BUSINESS PLANNING
             │
        ┌────┴────┐
        ▼         ▼
     targets   expenses
```

---

# Master Data

## Customers

Stores customer information.

## Products

Stores product information.

## Categories

Stores product categories.

## Stores

Stores store information.

## Regions

Stores business region information.

## Employees

Stores employee information.

---

# Transactional Data

## Orders

Stores customer order information.

## Order Items

Stores the individual products included in each order.

---

# Business Planning

## Targets

Stores sales and profit targets.

## Expenses

Stores business expenses.

---

# Analytics

The analytics layer will provide:

- KPI views
- Aggregations
- Business metrics
- Revenue analysis
- Profit analysis
- Profit margin analysis
- Sales analysis
- Customer analysis
- Product analysis
- Regional analysis

---

# Primary Keys

- customers → customer_id
- products → product_id
- categories → category_id
- orders → order_id
- order_items → order_item_id
- stores → store_id
- regions → region_id
- employees → employee_id
- targets → target_id
- expenses → expense_id

---

# Main Foreign Keys

- customers.region_id → regions.region_id
- products.category_id → categories.category_id
- orders.customer_id → customers.customer_id
- orders.store_id → stores.store_id
- order_items.order_id → orders.order_id
- order_items.product_id → products.product_id
- stores.region_id → regions.region_id
- employees.store_id → stores.store_id
- targets.store_id → stores.store_id
- expenses.store_id → stores.store_id

---

# Core Business Metrics

## Revenue

Revenue =
(quantity × unit_price) - discount

## Cost

Cost =
quantity × product.cost_price

## Profit

Profit =
Revenue - Cost

## Profit Margin

Profit Margin =
(Profit / Revenue) × 100

---

# Example Business Question

Question:

"Show Q2 sales in Kerala."

Database path:

Question
↓
orders
↓
order_items
↓
products
↓
stores
↓
Kerala filter
↓
Q2 date filter
↓
Sales calculation
↓
Result