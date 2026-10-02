

```text
User Question
      ↓
AI understands question
      ↓
AI generates SQL
      ↓
SQL Validator checks SQL
      ↓
Approved SQL
      ↓
PostgreSQL
      ↓
Query Result
      ↓
AI explains result
      ↓
User sees answer + chart
```

### Step 5.1 — Create the AI workflow document

Inside:

```text
docs
```

create a new file:

```text
ai_sql_workflow.md
```

Paste this:

````markdown
# AI to SQL Workflow

## 1. User Question

The user enters a natural language business question.

Example:

"What were our total sales in Kerala?"

---

## 2. Question Processing

The application receives the user's question.

The system sends the question to the AI model together with relevant database information.

The database information may include:

- Table names
- Column names
- Relationships
- Data types
- Business definitions

---

## 3. AI Understanding

The AI identifies:

- Business intent
- Required tables
- Required columns
- Filters
- Aggregations
- Sorting
- Time period

For example:

Question:

"What were our total sales in Kerala?"

The AI identifies:

Intent:
Calculate total sales.

Required data:
Sales information.

Filter:
State = Kerala.

Aggregation:
SUM(sales_amount)

---

## 4. SQL Generation

The AI generates an SQL query.

Example:

```sql
SELECT SUM(s.sales_amount) AS total_sales
FROM sales s
JOIN orders o
    ON s.order_id = o.order_id
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.state = 'Kerala';
````

---

## 5. SQL Validation

Before execution, the application validates the generated SQL.

The validator checks:

* Is the SQL syntactically valid?
* Does the query use valid tables?
* Does the query use valid columns?
* Is the query read-only?
* Does the query contain dangerous operations?

The MVP should allow:

* SELECT
* JOIN
* WHERE
* GROUP BY
* ORDER BY
* HAVING
* LIMIT
* Aggregate functions

The MVP should block operations such as:

* INSERT
* UPDATE
* DELETE
* DROP
* ALTER
* TRUNCATE

---

## 6. SQL Execution

After validation, the approved SQL query is sent to PostgreSQL.

PostgreSQL executes the query.

The database returns the result.

---

## 7. Result Processing

The application receives the database result.

The result may be:

* A single number
* A table
* Multiple rows
* Aggregated data
* Time-series data

Pandas can be used to process the result.

---

## 8. Visualization

The system determines whether the result should be visualized.

Possible visualizations:

* KPI Card
* Bar Chart
* Line Chart
* Pie Chart
* Table

Example:

Monthly sales → Line chart

Sales by state → Bar chart

Total sales → KPI card

---

## 9. AI Business Explanation

The result can be sent back to the AI.

The AI generates a simple business explanation.

Example:

"NovaMart generated ₹12.5 lakh in sales from Kerala during the selected period."

---

## 10. Final User Response

The user receives:

1. Original question
2. Answer
3. KPI or table
4. Chart when appropriate
5. AI explanation

---

# Complete Workflow

```text
┌──────────────────────────┐
│       USER QUESTION      │
│                          │
│ "Sales in Kerala?"       │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│     QUESTION PROCESSING  │
│                          │
│ Identify intent          │
│ Identify entities        │
│ Identify filters         │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│          AI / LLM        │
│                          │
│ Generate SQL             │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│      SQL VALIDATOR       │
│                          │
│ Check safety             │
│ Check tables             │
│ Check columns            │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│       POSTGRESQL         │
│                          │
│ Execute approved query   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│      QUERY RESULT        │
│                          │
│ DataFrame / Result       │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│      VISUALIZATION       │
│                          │
│ KPI / Table / Chart      │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│     AI EXPLANATION       │
│                          │
│ Business insight         │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│       FINAL ANSWER       │
└──────────────────────────┘
```

# Example 2

User:

"Which product generated the highest profit?"

AI identifies:

* Table: sales
* Table: products
* Metric: profit
* Aggregation: SUM
* Grouping: product
* Sorting: descending
* Limit: 1

Possible SQL:

```sql
SELECT
    p.product_name,
    SUM(s.profit) AS total_profit
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_profit DESC
LIMIT 1;
```

The system then displays the product and profit and provides a business explanation.

# Example 3

User:

"Compare Kerala and Karnataka sales."

The AI identifies:

* Required table: sales
* Required geographic information: state
* States: Kerala and Karnataka
* Metric: sales
* Aggregation: SUM
* Grouping: state

The result can be displayed as a comparison bar chart.

````

Save with **Ctrl + S**.

### Why this step matters

This document defines the **core intelligence loop** of your project.

Later, we'll actually implement:

```text
User → LLM → SQL → Validator → PostgreSQL → Result → AI
````
