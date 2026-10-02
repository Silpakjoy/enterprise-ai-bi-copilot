# Database Architecture

## Database Technology

PostgreSQL

---

## Database Layers

### 1. Master Data

- customers
- products
- categories
- stores
- regions
- employees

---

### 2. Transactional Data

- orders
- order_items

---

### 3. Business Planning

- targets
- expenses

---

### 4. Analytics

- KPI views
- Aggregations
- Business metrics



# Database Tables

## Initial Database Tables

01. customers
02. products
03. categories
04. orders
05. order_items
06. stores
07. regions
08. employees
09. targets
10. expenses


# Business Metrics

## 1. Revenue

Revenue represents the total sales value after discount.

Formula:

Revenue =
(quantity × unit_price) - discount

---

## 2. Cost

Cost represents the total product cost.

Formula:

Cost =
quantity × product.cost_price

---

## 3. Profit

Profit represents the difference between revenue and cost.

Formula:

Profit =
Revenue - Cost

---

## 4. Profit Margin

Profit Margin represents profit as a percentage of revenue.

Formula:

Profit Margin =
(Profit / Revenue) × 100



# Primary Keys

The primary key uniquely identifies each record in a table.

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

# Foreign Keys

Foreign keys connect related tables.

## Customer → Region

customers.region_id
↓
regions.region_id

---

## Product → Category

products.category_id
↓
categories.category_id

---

## Order → Customer

orders.customer_id
↓
customers.customer_id

---

## Order → Store

orders.store_id
↓
stores.store_id

---

## Order Item → Order

order_items.order_id
↓
orders.order_id

---

## Order Item → Product

order_items.product_id
↓
products.product_id

---

## Store → Region

stores.region_id
↓
regions.region_id

---

## Employee → Store

employees.store_id
↓
stores.store_id

---

## Target → Store

targets.store_id
↓
stores.store_id

---

## Expense → Store

expenses.store_id
↓
stores.store_id



# Business Question → Database Flow

## Example Question

"Show Q2 sales in Kerala."

---

## Database Flow

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
Filter stores.state = Kerala
↓
Filter order_date = Q2
↓
Calculate Sales
↓
Sales Result

---

## Calculation

Sales =
SUM((quantity × unit_price) - discount)

---

## Required Tables

The question requires:

- orders
- order_items
- products
- stores

---

## Business Logic

1. Identify orders placed during Q2.
2. Connect orders with order_items.
3. Connect order_items with products.
4. Connect orders with stores.
5. Filter stores located in Kerala.
6. Calculate sales using quantity, unit price, and discount.
7. Return the sales result.



