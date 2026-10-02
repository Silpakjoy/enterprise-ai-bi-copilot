# Security Architecture

## Database Security

- Database credentials must not be hard-coded.
- Credentials will be stored in environment variables.
- Database access will use a restricted application user.

---

## SQL Security

AI-generated SQL must be validated before execution.

Only read-only queries will be permitted by the MVP.

### Blocked Operations

- INSERT
- UPDATE
- DELETE
- DROP
- ALTER
- TRUNCATE

---

## Application Security

The application should eventually include:

- Authentication
- Authorization
- Role-based access
- Input validation
- Error handling
- Activity logging

---

## Secret Management

Sensitive information should be stored in:

.env

The `.env` file must not be uploaded to GitHub.