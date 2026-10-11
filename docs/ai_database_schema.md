
# AI Database Schema and Safety Rules

## 1. Purpose

This document defines how the AI Business Intelligence Copilot should understand and query the NovaMart PostgreSQL database.

## 2. Approved Database Objects

### Core Tables

- regions
- customers
- employees
- products
- orders
- order_items
- expenses
- targets

### Analytics Views

- analytics.sales_summary
- analytics.monthly_sales

## 3. Business Metric Definitions

### Revenue

Revenue is calculated as:

quantity × unit_price − discount

Use completed orders when calculating completed sales revenue.

### Cost

Cost is calculated as:

quantity × product cost_price

### Profit

Profit is calculated as:

revenue − cost

### Profit Margin

Profit margin is calculated as:

(profit ÷ revenue) × 100

Use NULLIF to prevent division-by-zero errors.

## 4. AI SQL Safety Rules

1. Generate SELECT statements only.
2. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, or TRUNCATE statements.
3. Use only approved database tables and views.
4. Use schema-qualified names for analytics views.
5. Apply a reasonable LIMIT when returning detailed records.
6. Avoid SELECT * when specific columns are sufficient.
7. Validate generated SQL before execution.
8. Never expose database passwords, connection strings, or other secrets.
9. Do not execute SQL that modifies database structures or data.
10. If a question is ambiguous, ask the user to clarify it.
11. Use parameterized queries for user-provided filter values.
12. Report when the database does not contain enough information to answer a question.

## 5. Query Validation Checklist

Before executing AI-generated SQL, verify:

- The query is a read-only SELECT statement.
- All referenced tables and columns exist.
- Only approved tables and views are used.
- Joins use appropriate relationships.
- Aggregations match the requested business metric.
- Division-by-zero cases are handled.
- The query has appropriate result limits.
- The query does not contain multiple statements.

## 6. Example Business Questions

The AI assistant should support questions such as:

- What is the total completed-sales revenue?
- Which region has the highest revenue?
- What was the monthly profit?
- Which products generated the most revenue?
- What is the overall profit margin?
- How did sales change from the previous month?

## 7. Important Limitation

These rules document the intended behavior of the AI assistant. They do not enforce database security by themselves. Read-only database permissions and server-side SQL validation must also be implemented.
