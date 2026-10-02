# Minimum Viable Product (MVP)

## Version 1 — Core MVP

The first version of the Enterprise AI Business Intelligence Copilot will focus on the core AI + database workflow.

### MVP Components

1. PostgreSQL database
2. NovaMart business dataset
3. Database tables
4. SQL queries
5. Natural Language to SQL
6. SQL validation
7. Safe SQL execution
8. Query results
9. Streamlit user interface
10. Basic KPI dashboard
11. AI-generated result explanation

## Core Workflow

User Question
        ↓
Natural Language Processing
        ↓
AI / LLM
        ↓
SQL Generation
        ↓
SQL Validation
        ↓
PostgreSQL
        ↓
Query Result
        ↓
Visualization
        ↓
AI Explanation

## Version 2 — Advanced Features

After the MVP is working, the following features will be added:

- Power BI integration
- Sales forecasting
- Financial PDF analysis
- AI executive summaries
- PDF report generation
- Voice input
- Chart explanation
- FastAPI backend
- Docker deployment

## MVP Goal

The MVP is complete when a user can ask a business question in natural language and receive a correct database result with a useful explanation.

Example:

User:

"What were our total sales in Kerala?"

System:

1. Understands the question.
2. Generates SQL.
3. Validates the SQL.
4. Executes the query.
5. Displays the result.
6. Explains the result.