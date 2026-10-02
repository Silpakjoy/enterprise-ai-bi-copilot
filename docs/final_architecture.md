# Final System Architecture

```text
                     ┌───────────────┐
                     │     USER      │
                     └───────┬───────┘
                             │
                             ▼
                     ┌───────────────┐
                     │   STREAMLIT   │
                     │   FRONTEND    │
                     └───────┬───────┘
                             │
                             ▼
                     ┌───────────────┐
                     │    FASTAPI    │
                     │    BACKEND    │
                     └───────┬───────┘
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
         ┌─────────────────┐   ┌─────────────────┐
         │    AI COPILOT   │   │  ANALYTICS      │
         │                 │   │    ENGINE       │
         │ Natural Language│   │                 │
         │      → SQL      │   │ Pandas / NumPy  │
         └────────┬────────┘   └────────┬────────┘
                  │                     │
                  ▼                     │
         ┌─────────────────┐             │
         │ SQL VALIDATOR   │             │
         └────────┬────────┘             │
                  │                     │
                  ▼                     │
         ┌─────────────────┐             │
         │   POSTGRESQL    │◄────────────┘
         │    DATABASE     │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │    REPORTING    │
         │     ENGINE      │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │   DASHBOARD /   │
         │     REPORT      │
         └─────────────────┘
```

## Supporting Components

### Forecasting Engine

Historical Sales
↓
Forecast Model
↓
Future Sales Prediction

### Power BI

PostgreSQL / Analytics Data
↓
Power BI
↓
Advanced Dashboard