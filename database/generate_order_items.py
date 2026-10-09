import os
import numpy as np
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

rng = np.random.default_rng(42)


def generate_order_items(count=100000):

    print("Reading existing orders...")

    orders = pd.read_sql(
        text("SELECT order_id FROM orders ORDER BY order_id"),
        engine
    )

    print("Reading existing products...")

    products = pd.read_sql(
        text("""
            SELECT product_id, unit_price
            FROM products
            ORDER BY product_id
        """),
        engine
    )

    print(f"Existing orders: {len(orders)}")
    print(f"Existing products: {len(products)}")

    if len(orders) == 0:
        raise ValueError("No orders found.")

    if len(products) == 0:
        raise ValueError("No products found.")

    # Select existing order IDs
    order_ids = rng.choice(
        orders["order_id"].to_numpy(),
        size=count,
        replace=True
    )

    # Select existing product IDs
    product_ids = rng.choice(
        products["product_id"].to_numpy(),
        size=count,
        replace=True
    )

    # Get prices for selected products
    price_lookup = products.set_index("product_id")["unit_price"]

    unit_prices = price_lookup.loc[product_ids].to_numpy()

    # Quantity between 1 and 5
    quantities = rng.integers(
        1,
        6,
        size=count
    )

    # Calculate subtotal
    subtotals = quantities * unit_prices

    # Random discount between 0% and 15%
    discounts = np.round(
        subtotals * rng.uniform(
            0,
            0.15,
            size=count
        ),
        2
    )

    order_items = pd.DataFrame({
        "order_id": order_ids.astype(int),
        "product_id": product_ids.astype(int),
        "quantity": quantities.astype(int),
        "unit_price": np.round(unit_prices, 2),
        "discount": discounts
    })

    return order_items


def load_order_items(df):

    print("Loading order items into PostgreSQL...")

    df.to_sql(
        "order_items",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=5000
    )

    print("Order items inserted successfully.")


if __name__ == "__main__":

    # Check existing rows first
    existing = pd.read_sql(
        text("SELECT COUNT(*) AS count FROM order_items"),
        engine
    ).iloc[0]["count"]

    print(f"Existing order_items: {existing}")

    if existing > 0:
        print(
            "order_items already contains data. "
            "Generation stopped to prevent duplicates."
        )

    else:
        order_items_df = generate_order_items(100000)

        print(
            f"Generated order items: {len(order_items_df)}"
        )

        load_order_items(order_items_df)

        print("\nOrder item generation completed successfully.")