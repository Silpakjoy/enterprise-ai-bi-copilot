# API Architecture

## Backend

FastAPI

---

## Main API Endpoints

### 1. Health Check

GET /api/health

Purpose:

Check whether the backend is running.

---

### 2. AI Query

POST /api/query

Purpose:

Receive a natural language business question.

Example:

"What were our sales in Kerala?"

---

### 3. SQL Generation

POST /api/generate-sql

Purpose:

Convert a natural language question into SQL.

---

### 4. SQL Execution

POST /api/execute-sql

Purpose:

Execute a validated read-only SQL query.

---

### 5. Dashboard KPIs

GET /api/kpis

Purpose:

Return important business KPIs.

---

### 6. Sales Analysis

GET /api/sales

Purpose:

Return sales analytics.

---

### 7. Forecast

POST /api/forecast

Purpose:

Generate sales forecasts.

---

### 8. Report

POST /api/report

Purpose:

Generate a business report.