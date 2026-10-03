from app.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

print("Database configuration test")

print("DB_HOST:", DB_HOST)
print("DB_PORT:", DB_PORT)
print("DB_NAME:", DB_NAME)
print("DB_USER:", DB_USER)

if DB_PASSWORD:
    print("DB_PASSWORD: Loaded successfully")
else:
    print("DB_PASSWORD: Not loaded")