# import os

# import pandas as pd
# from dotenv import load_dotenv
# from sqlalchemy import create_engine, text


# # Load environment variables
# load_dotenv()


# # Read database settings
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")


# # Create PostgreSQL connection URL
# DATABASE_URL = (
#     f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )


# # Create database engine
# engine = create_engine(DATABASE_URL)


# def test_connection():
#     """Test the PostgreSQL connection."""
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT current_database();"))
#         database_name = result.scalar()

#         print("Connected to database:", database_name)


# def check_regions():
#     """Read existing regions from PostgreSQL."""
#     query = "SELECT region_id, region_name FROM regions ORDER BY region_id;"

#     df = pd.read_sql(query, engine)

#     print("\nExisting regions:")
#     print(df)


# if __name__ == "__main__":
#     test_connection()
#     check_regions()



import os

import pandas as pd
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine
from datetime import date, timedelta



# Load environment variables
load_dotenv()

# Database settings
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# PostgreSQL connection
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

# Faker
fake = Faker("en_IN")

# Make generated data reproducible
Faker.seed(42)


def generate_customers(count=10000):
    """Generate customer records."""

    # Indian locations
    locations = [
        ("Kozhikode", "Kerala"),
        ("Kochi", "Kerala"),
        ("Thiruvananthapuram", "Kerala"),
        ("Bengaluru", "Karnataka"),
        ("Mysuru", "Karnataka"),
        ("Chennai", "Tamil Nadu"),
        ("Coimbatore", "Tamil Nadu"),
        ("Hyderabad", "Telangana"),
        ("Mumbai", "Maharashtra"),
        ("Pune", "Maharashtra"),
        ("Delhi", "Delhi"),
        ("Jaipur", "Rajasthan"),
        ("Lucknow", "Uttar Pradesh"),
        ("Kolkata", "West Bengal"),
        ("Ahmedabad", "Gujarat"),
    ]

    segments = [
        "Premium",
        "Regular",
        "New",
        "Occasional",
    ]

    genders = [
        "Male",
        "Female",
        "Other",
    ]

    # Generate customer data
    customers = []

    for customer_id in range(1, count + 1):

        city, state = locations[(customer_id - 1) % len(locations)]

        customers.append({
            "customer_id": customer_id,
            "customer_name": fake.name(),
            "gender": genders[(customer_id - 1) % len(genders)],
            "age": fake.random_int(min=18, max=70),
            "city": city,
            "state": state,
            "region_id": ((customer_id - 1) % 5) + 1,
            "signup_date": fake.date_between(
    start_date="-1095d",
    end_date="today"
),
            "customer_segment": segments[
                (customer_id - 1) % len(segments)
            ],
        })

    df = pd.DataFrame(customers)

    print(f"\nGenerated customers: {len(df)}")

    print("\nFirst 5 customers:")
    print(df.head())

    return df


def load_customers(df):
    """Load customers into PostgreSQL."""

    df.to_sql(
        "customers",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000,
    )

    print(f"\nInserted {len(df)} customers into PostgreSQL.")

def generate_employees(count=150):
    """Generate employee records."""

    departments = [
        "Sales",
        "Finance",
        "Marketing",
        "Operations",
        "IT",
        "Human Resources",
        "Customer Support",
    ]

    designations = [
        "Executive",
        "Analyst",
        "Senior Executive",
        "Manager",
        "Senior Manager",
    ]

    employees = []

    for employee_id in range(1, count + 1):

        employees.append({
            "employee_id": employee_id,
            "employee_name": fake.name(),
            "department": departments[(employee_id - 1) % len(departments)],
            "designation": designations[(employee_id - 1) % len(designations)],
            "joining_date": fake.date_between(
                start_date="-1825d",
                end_date="today"
            ),
            "region_id": ((employee_id - 1) % 5) + 1,
        })

    df = pd.DataFrame(employees)

    print(f"\nGenerated employees: {len(df)}")

    print("\nFirst 5 employees:")
    print(df.head())

    return df


def load_employees(df):
    """Load employees into PostgreSQL."""

    df.to_sql(
        "employees",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=500,
    )

    print(f"\nInserted {len(df)} employees into PostgreSQL.")


def generate_products(count=200):
    """Generate product records."""

    product_templates = [
        ("Laptop", "Electronics", "Dell", 45000, 90000),
        ("Smartphone", "Electronics", "Samsung", 12000, 80000),
        ("Tablet", "Electronics", "Lenovo", 15000, 50000),
        ("Monitor", "Electronics", "LG", 8000, 45000),
        ("Keyboard", "Accessories", "Logitech", 500, 5000),
        ("Mouse", "Accessories", "HP", 300, 3000),
        ("Headphones", "Accessories", "Sony", 1000, 15000),
        ("Printer", "Electronics", "HP", 6000, 30000),
        ("Office Chair", "Furniture", "GreenSoul", 5000, 25000),
        ("Desk", "Furniture", "IKEA", 5000, 30000),
        ("Backpack", "Bags", "Wildcraft", 800, 5000),
        ("Power Bank", "Accessories", "MI", 800, 4000),
        ("Smart Watch", "Wearables", "Noise", 1500, 10000),
        ("Bluetooth Speaker", "Audio", "JBL", 1500, 12000),
        ("USB Cable", "Accessories", "Portronics", 150, 1500),
    ]

    products = []

    for product_id in range(1, count + 1):

        base_name, category, brand, min_price, max_price = (
            product_templates[(product_id - 1) % len(product_templates)]
        )

        unit_price = fake.random_int(
            min=min_price,
            max=max_price
        )

        # Cost price is 50%–85% of selling price
        cost_price = round(
            unit_price * fake.pyfloat(
                left_digits=1,
                right_digits=2,
                min_value=0.50,
                max_value=0.85
            ),
            2
        )

        products.append({
            "product_id": product_id,
            "product_name": f"{base_name} {product_id}",
            "category": category,
            "brand": brand,
            "unit_price": unit_price,
            "cost_price": cost_price,
            "launch_date": fake.date_between(
                start_date="-1825d",
                end_date="today"
            ),
        })

    df = pd.DataFrame(products)

    print(f"\nGenerated products: {len(df)}")

    print("\nFirst 5 products:")
    print(df.head())

    return df


def load_products(df):
    """Load products into PostgreSQL."""

    df.to_sql(
        "products",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=500,
    )

    print(f"\nInserted {len(df)} products into PostgreSQL.")



def generate_orders(count=50000):
    """Generate order records."""

    payment_methods = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Cash on Delivery",
    ]

    order_statuses = [
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Pending",
        "Cancelled",
        "Returned",
    ]

    start_date = date(2024, 1, 1)
    end_date = date(2026, 12, 31)
    date_range = (end_date - start_date).days

    orders = []

    for order_id in range(1, count + 1):

        orders.append({
            "order_id": order_id,
            "customer_id": fake.random_int(
                min=1,
                max=10000
            ),
            "region_id": fake.random_int(
                min=1,
                max=5
            ),
            "order_date": start_date + timedelta(
                days=fake.random_int(
                    min=0,
                    max=date_range
                )
            ),
            "payment_method": fake.random_element(
                payment_methods
            ),
            "order_status": fake.random_element(
                order_statuses
            ),
        })

    df = pd.DataFrame(orders)

    print(f"\nGenerated orders: {len(df)}")

    print("\nFirst 5 orders:")
    print(df.head())

    return df


def load_orders(df):
    """Load orders into PostgreSQL."""

    df.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=2000,
    )

    print(f"\nInserted {len(df)} orders into PostgreSQL.")


if __name__ == "__main__":
    orders_df = generate_orders(50000)

    load_orders(orders_df)

    print("\nOrder generation completed successfully.")