# Data Dictionary

## 1. Customers

| Column           | Type         | Key | Description       |
|------------------|--------------|-----|-------------------|
| customer_id      | INTEGER      | PK  | Unique customer   |
| customer_name    | VARCHAR(150) |     | Customer name     |
| gender           | VARCHAR(20)  |     | Customer gender   |
| age              | INTEGER      |     | Customer age      |
| city             | VARCHAR(100) |     | Customer city     |
| state            | VARCHAR(100) |     | Customer state    |
| region_id        | INTEGER      | FK  | Customer region   |
| signup_date      | DATE         |     | Registration date |
| customer_segment | VARCHAR(50)  |     | Customer segment  |

---

## 2. Products

| Column       | Type          | Key | Description      |
|--------------|---------------|-----|------------------|
| product_id   | INTEGER       | PK  | Unique product   |
| product_name | VARCHAR(150)  |     | Product name     |
| category_id  | INTEGER       | FK  | Product category |
| brand        | VARCHAR(100)  |     | Product brand    |
| unit_price   | DECIMAL(10,2) |     | Selling price    |
| cost_price   | DECIMAL(10,2) |     | Product cost     |

---

## 3. Categories

| Column        | Type         | Key | Description     |
|---------------|--------------|-----|-----------------|
| category_id   | INTEGER      | PK  | Unique category |
| category_name | VARCHAR(100) |     | Category name   |

---

## 4. Orders

| Column         | Type        | Key | Description                   |
|----------------|-------------|-----|-------------------------------|
| order_id       | INTEGER     | PK  | Unique order                  |
| customer_id    | INTEGER     | FK  | Customer who placed the order |
| store_id       | INTEGER     | FK  | Store where order was placed  |
| order_date     | DATE        |     | Order date                    |
| payment_method | VARCHAR(50) |     | Payment method                |
| order_status   | VARCHAR(50) |     | Order status                  |

---

## 5. Order Items

| Column        | Type          | Key | Description        |
|---------------|---------------|-----|--------------------|
| order_item_id | INTEGER       | PK  | Unique order item  |
| order_id      | INTEGER       | FK  | Related order      |
| product_id    | INTEGER       | FK  | Purchased product  |
| quantity      | INTEGER       |     | Quantity purchased |
| unit_price    | DECIMAL(10,2) |     | Selling price      |
| discount      | DECIMAL(10,2) |     | Discount amount    |

---

## 6. Stores

| Column    | Type         | Key | Description  |
|-----------|--------------|-----|--------------|
| store_id  | INTEGER      | PK  | Unique store |
| store_name| VARCHAR(150) |     | Store name   |
| city      | VARCHAR(100) |     | Store city   |
| state     | VARCHAR(100) |     | Store state  |
| region_id | INTEGER      | FK  | Store region |

---

## 7. Regions

| Column      | Type         | Key | Description   |
|-------------|--------------|-----|---------------|
| region_id   | INTEGER      | PK  | Unique region |
| region_name | VARCHAR(100) |     | Region name   |

---

## 8. Employees

| Column       | Type         | Key | Description          |
|--------------|--------------|-----|----------------------|
| employee_id  | INTEGER      | PK  | Unique employee      |
| employee_name| VARCHAR(150) |     | Employee name        |
| department   | VARCHAR(100) |     | Employee department  |
| designation  | VARCHAR(100) |     | Employee designation |
| store_id     | INTEGER      | FK  | Employee store       |
| joining_date | DATE         |     | Employee joining date|

---

## 9. Targets

| Column        | Type          | Key | Description   |
|---------------|---------------|-----|---------------|
| target_id     | INTEGER       | PK  | Unique target |
| store_id      | INTEGER       | FK  | Target store  |
| target_month  | DATE          |     | Target month  |
| sales_target  | DECIMAL(12,2) |     | Sales target  |
| profit_target | DECIMAL(12,2) |     | Profit target |

---

## 10. Expenses

| Column           | Type          | Key | Description      |
|------------------|---------------|-----|------------------|
| expense_id       | INTEGER       | PK  | Unique expense   |
| store_id         | INTEGER       | FK  | Expense store    |
| expense_date     | DATE          |     | Expense date     |
| expense_category | VARCHAR(100)  |     | Expense category |
| amount           | DECIMAL(12,2) |     | Expense amount   |