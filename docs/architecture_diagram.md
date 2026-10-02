# System Architecture Diagram

## Enterprise AI Business Intelligence Copilot

```text
┌───────────────────────────────┐
│            USER               │
│                               │
│  Business Executive           │
│  Business Analyst             │
│  Finance Manager              │
│  Administrator                │
└───────────────┬───────────────┘
                │
                │ Natural Language Question
                ▼
┌───────────────────────────────┐
│       STREAMLIT UI            │
│                               │
│ • AI Chat                     │
│ • KPI Dashboard               │
│ • Tables                      │
│ • Charts                      │
│ • Reports                     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      APPLICATION BACKEND      │
│                               │
│ • Request Handling            │
│ • Authentication              │
│ • Query Processing            │
│ • Result Processing           │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│          AI / LLM             │
│                               │
│ • Understand Question         │
│ • Identify Intent             │
│ • Generate SQL                │
│ • Explain Results             │
└───────────────┬───────────────┘
                │
                │ Generated SQL
                ▼
┌───────────────────────────────┐
│       SQL VALIDATION          │
│                               │
│ • Validate SQL                │
│ • Read-only Check             │
│ • Block Dangerous Queries     │
└───────────────┬───────────────┘
                │
                │ Approved SQL
                ▼
┌───────────────────────────────┐
│       POSTGRESQL DATABASE     │
│                               │
│ • Customers                   │
│ • Products                    │
│ • Orders                      │
│ • Sales                       │
│ • Employees                   │
│ • Expenses                    │
│ • Targets                     │
└───────────────┬───────────────┘
                │
                │ Query Results
                ▼
┌───────────────────────────────┐
│       ANALYTICS LAYER         │
│                               │
│ • Pandas                      │
│ • NumPy                       │
│ • KPI Calculations            │
│ • Trend Analysis              │ 
│ • Visualization               │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       RESULT / INSIGHT        │
│                               │
│ • KPI                         │
│ • Table                       │
│ • Chart                       │
│ • AI Explanation              │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│            USER               │
│                               │
│       Business Insight        │
└───────────────────────────────┘

Additional Components
Power BI

Power BI will connect to the business data for advanced dashboards.

Forecasting

The forecasting module will use historical sales data to estimate future sales.

Financial Report Analysis

The system will process uploaded financial reports and generate summaries.

Report Generation

The reporting module will generate PDF business reports.

Future Deployment

The application may be deployed using Docker and cloud infrastructure.


Save with **Ctrl + S**.

---

## What this diagram means

For example, the user asks:

> **"What were our total sales in Kerala?"**

The system will eventually work like this:

```text
Your Question
     ↓
Streamlit
     ↓
AI
     ↓
SQL
     ↓
SQL Validation
     ↓
PostgreSQL
     ↓
Sales Result
     ↓
Chart + AI Explanation
     ↓
Your Answer