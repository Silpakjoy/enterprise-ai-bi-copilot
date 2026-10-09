import os
import random
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

random.seed(42)


def generate_expenses(count=5000):

    expenses = []

    categories = [
        "Rent",
        "Salaries",
        "Marketing",
        "Transport",
        "Utilities",
        "Maintenance",
        "Technology",
        "Office Supplies",
        "Travel",
        "Other"
    ]

    start_id = 2

    for expense_id in range(start_id, start_id + count):

        region_id = random.randint(1, 5)

        expense_date = (
            pd.Timestamp("2024-01-01")
            + pd.Timedelta(days=random.randint(0, 1095))
        )

        category = random.choice(categories)

        amount = round(random.uniform(500, 50000), 2)

        expenses.append({
            "expense_id": expense_id,
            "region_id": region_id,
            "expense_date": expense_date,
            "expense_category": category,
            "amount": amount
        })

    return pd.DataFrame(expenses)


def load_expenses(df):

    print("Loading expenses into PostgreSQL...")

    df.to_sql(
        "expenses",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=500
    )

    print("Expenses inserted successfully.")


if __name__ == "__main__":

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT COUNT(*) FROM expenses")
        )

        existing = result.scalar()

    print(f"Existing expenses: {existing}")

remaining = 5000 - existing

if remaining <= 0:

    print("Expenses already contain 5000 records.")

else:

    expenses_df = generate_expenses(remaining)

    print(
        f"Generated expenses: {len(expenses_df)}"
    )

    load_expenses(expenses_df)

    print(
        "\nExpense generation completed successfully."
    )