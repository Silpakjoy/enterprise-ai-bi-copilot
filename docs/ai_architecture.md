# AI Architecture

## AI Pipeline

User Question
↓
Question Understanding
↓
Business Intent Detection
↓
Database Schema Context
↓
SQL Generation
↓
SQL Validation
↓
SQL Execution
↓
Result Analysis
↓
AI Explanation
↓
Final Answer

---

## AI Inputs

The AI receives:

- User question
- Database schema
- Table names
- Column names
- Relationships
- Business definitions
- Relevant examples

---

## AI Outputs

The AI can produce:

- SQL query
- Business explanation
- Summary
- Chart explanation
- Executive insight

---

## SQL Safety

Only approved read-only SQL should be executed.

### Blocked Operations

- INSERT
- UPDATE
- DELETE
- DROP
- ALTER
- TRUNCATE