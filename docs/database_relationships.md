# Database Relationships

## 1. Regions → Customers

One region can have many customers.

```text
regions 1 ──────── many customers



2. Regions → Stores
One region can have many stores.
regions 1 ──────── many stores

Foreign Key:
stores.region_id
        ↓
regions.region_id

3. Categories → Products
One category can contain many products.
categories 1 ──────── many products

Foreign Key:
products.category_id
        ↓
categories.category_id

4. Customers → Orders
One customer can place many orders.
customers 1 ──────── many orders

Foreign Key:
orders.customer_id
        ↓
customers.customer_id

5. Stores → Orders
One store can have many orders.
stores 1 ──────── many orders

Foreign Key:
orders.store_id
        ↓
stores.store_id

6. Orders → Order Items
One order can contain many order items.
orders 1 ──────── many order_items

Foreign Key:
order_items.order_id
        ↓
orders.order_id

7. Products → Order Items
One product can appear in many order items.
products 1 ──────── many order_items

Foreign Key:
order_items.product_id
        ↓
products.product_id

8. Stores → Employees
One store can have many employees.
stores 1 ──────── many employees

Foreign Key:
employees.store_id
        ↓
stores.store_id

9. Stores → Targets
One store can have many targets over different months.
stores 1 ──────── many targets

Foreign Key:
targets.store_id
        ↓
stores.store_id

10. Stores → Expenses
One store can have many expenses.
stores 1 ──────── many expenses

Foreign Key:
expenses.store_id
        ↓
stores.store_id

Complete Relationship Summary
REGIONS
   │
   ├──────────────→ CUSTOMERS
   │
   └──────────────→ STORES
                         │
                         ├────────→ ORDERS
                         │             │
                         │             ↓
                         │        ORDER_ITEMS
                         │             │
                         │             ↓
                         │         PRODUCTS
                         │             │
                         │             ↓
                         │         CATEGORIES
                         │
                         ├────────→ EMPLOYEES
                         │
                         ├────────→ TARGETS
                         │
                         └────────→ EXPENSES

CUSTOMERS ─────────────→ ORDERS


---

## 3. Save

Press:

```text
Ctrl + S 