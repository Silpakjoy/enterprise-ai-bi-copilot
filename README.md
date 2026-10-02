# Enterprise AI Business Intelligence Copilot

An AI-powered Business Intelligence platform that allows business users to interact with enterprise data using natural language.

## Project Overview

The Enterprise AI Business Intelligence Copilot combines Business Intelligence, Artificial Intelligence, SQL analytics, forecasting, and automated reporting into one platform.

Users can ask business questions in natural language, and the system can generate SQL queries, retrieve data from PostgreSQL, analyze the results, and present insights through dashboards and reports.

## Key Features

- Natural language business queries
- AI-generated SQL
- PostgreSQL database integration
- KPI dashboards
- Sales and business analytics
- AI-generated business insights
- Financial report analysis
- Sales forecasting
- Automated executive summaries
- PDF report generation
- Interactive data visualization

## Technology Stack

### Programming & Data
- Python
- SQL
- Pandas
- NumPy
- Scikit-learn

### Database
- PostgreSQL
- SQLAlchemy

### AI
- Large Language Models
- LangChain
- AI-powered Text-to-SQL

### Backend
- FastAPI

### Frontend
- Streamlit

### Business Intelligence
- Power BI
- Tableau

### Deployment
- Docker
- GitHub

## Project Architecture

The main system flow is:

User  
↓  
Streamlit Interface  
↓  
FastAPI Backend  
↓  
AI / LLM Layer  
↓  
SQL Validation  
↓  
PostgreSQL  
↓  
Analytics  
↓  
Visualization / Reports

## Database

The project uses a relational enterprise database containing:

- Customers
- Products
- Categories
- Orders
- Order Items
- Stores
- Regions
- Employees
- Targets
- Expenses

## Example Business Question

> Show Q2 sales in Kerala.

The system processes the question, generates an appropriate SQL query, retrieves the required data from PostgreSQL, calculates the relevant metrics, and presents the result to the user.

## Project Documentation

Detailed project documentation is available in the `docs/` directory.

Important documentation includes:

- System Architecture
- Data Flow
- API Architecture
- AI Architecture
- Security Architecture
- Database Architecture
- Data Dictionary
- Database Relationships
- ER Diagram
- Analytics Architecture
- Forecasting Architecture
- Reporting Architecture

## Project Status

Current phase:

**Foundation and Architecture**

Completed:

- Project requirements
- Business scenario
- User definitions
- Feature definitions
- Business questions
- KPI definitions
- System architecture
- Data flow
- Database architecture
- Database design
- ER diagram
- GitHub repository

Next phase:

- Development environment
- PostgreSQL implementation
- Backend development
- AI SQL generation
- Analytics
- Forecasting
- Dashboard development
- Reporting

## Author

Silpa

BCA Graduate | Aspiring Data Analyst

## License

MIT License