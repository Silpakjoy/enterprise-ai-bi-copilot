# MVP Architecture

## 1. MVP Objective

The MVP will demonstrate the complete core workflow of the Enterprise AI Business Intelligence Copilot.

A user should be able to ask a business question in natural language and receive a database-backed answer.

---

# 2. MVP Technology Stack

## Frontend

Streamlit

## Backend

Python

FastAPI will be added as the application backend as the project develops.

## Database

PostgreSQL

## AI

Large Language Model (LLM)

## Data Processing

Pandas

NumPy

## Visualization

Plotly

## Machine Learning

Scikit-learn

---

# 3. MVP Components

The MVP contains:

1. Streamlit interface
2. PostgreSQL database
3. NovaMart business data
4. Database connection
5. Natural Language to SQL
6. SQL validation
7. SQL execution
8. Query results
9. Data visualization
10. AI business explanation
11. KPI dashboard

---

# 4. MVP Architecture

```text
                    USER
                      │
                      ▼
            ┌─────────────────┐
            │   STREAMLIT UI  │
            │                 │
            │ • AI Chat       │
            │ • Dashboard     │
            │ • Charts        │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  PYTHON BACKEND │
            │                 │
            │ Request Handler │
            │ Query Processor │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │    AI / LLM     │
            │                 │
            │ Question → SQL  │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │ SQL VALIDATOR   │
            │                 │
            │ Safety Checks   │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │   POSTGRESQL    │
            │                 │
            │ Customers       │
            │ Products        │
            │ Orders          │
            │ Sales           │
            │ Employees       │
            │ Expenses        │
            │ Targets         │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  QUERY RESULT   │
            │                 │
            │ Pandas DataFrame│
            └────────┬────────┘
                     │
             ┌───────┴────────┐
             ▼                ▼
      ┌─────────────┐   ┌─────────────┐
      │ VISUALIZATION│   │ AI EXPLAINER │
      │             │   │              │
      │ Charts      │   │ Business     │
      │ Tables      │   │ Explanation  │
      └──────┬──────┘   └──────┬───────┘
             │                 │
             └────────┬────────┘
                      ▼
                FINAL ANSWER
5. MVP User Flow
Step 1

User opens the Streamlit application.

Step 2

User enters a business question.

Example:

"What are our total sales in Kerala?"

Step 3

The application sends the question to the AI model.

Step 4

The AI generates SQL.

Step 5

The SQL validator checks the query.

Step 6

The approved SQL is executed against PostgreSQL.

Step 7

The database returns the result.

Step 8

Pandas processes the result.

Step 9

The application creates an appropriate visualization.

Step 10

The AI generates a business explanation.

Step 11

The user sees the final result.

6. MVP Success Criteria

The MVP will be considered successful when the following workflow works:

Natural Language Question
        ↓
AI-generated SQL
        ↓
SQL Validation
        ↓
PostgreSQL Query
        ↓
Correct Result
        ↓
Visualization
        ↓
AI Explanation
7. Example MVP Questions

The MVP should eventually support questions such as:

What is our total sales?
What is our total profit?
What are our monthly sales?
Which state has the highest sales?
Which products generate the highest profit?
Who are our top customers?
Compare Kerala and Karnataka sales.
What were our sales last month?
What are our sales by region?
8. Features After MVP

The following features will be developed after the core MVP works:

Advanced Analytics
Sales forecasting
Customer analytics
Advanced product analytics
Financial Intelligence
Financial PDF analysis
Financial report summaries
Reporting
Automated PDF reports
Executive reports
AI Features
Voice input
Chart explanation
Advanced AI executive summaries
Business Intelligence
Power BI integration
Application Architecture
FastAPI production backend
Authentication
Role-based access control
Deployment
Docker
Cloud deployment

Save with **Ctrl + S**.

---

## 🎯 After this step

Your **Day 2 design work will be complete**.

You'll have:

```text
docs
│
├── architecture.md
├── architecture_diagram.md
├── ai_sql_workflow.md
├── business_questions.md
├── business_scenario.md
├── dashboard_design.md
├── database_design.md
├── er_diagram.md
├── features.md
├── kpis.md
├── mvp.md
├── mvp_architecture.md      ← NEW
├── project_requirements.md
└── users.md