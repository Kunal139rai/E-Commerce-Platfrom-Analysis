# This file handles the generation of random data and populates the database.

# data_generation.py
import random
from datetime import datetime, timedelta

# Helper function to generate a random date
def random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    return start + timedelta(days=random.randint(0, (end - start).days))

# Generate random product data
def generate_products(cursor):
    product_names = ["T-shirt", "Jeans", "Laptop", "Smartphone", "Milk", "Bread", "Headphones", "Sneakers", "Watch", "Bag"]
    categories = ["Clothing", "Clothing", "Electronics", "Electronics", "Groceries", "Groceries", "Electronics", "Clothing", "Accessories", "Accessories"]

    for i in range(10):
        cursor.execute(
            "INSERT INTO Product (product_name, category, description, is_discontinued) VALUES (%s, %s, %s, %s)",
            (product_names[i], categories[i], f"Description of {product_names[i]}", random.choice([True, False]))
        )

# Generate random variant data
def generate_variants(cursor):
    variants = [("Red", "Green", "Blue"), ("32GB", "64GB"), ("1L", "2L")]

    for product_id in range(1, 11):
        num_variants = random.choice([1, 2, 3])
        product_variants = random.sample(variants, k=num_variants)

        for variant in product_variants:
            for name in variant:
                cursor.execute(
                    "INSERT INTO Variant (product_id, variant_name, price, is_discontinued) VALUES (%s, %s, %s, %s)",
                    (product_id, name, round(random.uniform(10, 500), 2), random.choice([True, False]))
                )

# Generate random price history data
def generate_price_history(cursor):
    cursor.execute("SELECT variant_id FROM Variant")
    variant_ids = cursor.fetchall()

    for variant_id in variant_ids:
        num_price_changes = random.randint(1, 3)
        price_start_date = datetime(2022, 1, 1)

        for _ in range(num_price_changes):
            price = round(random.uniform(10, 500), 2)
            price_end_date = random_date(price_start_date, datetime(2024, 7, 28))

            cursor.execute(
                "INSERT INTO PriceHistory (variant_id, price, start_date, end_date) VALUES (%s, %s, %s, %s)",
                (variant_id[0], price, price_start_date, price_end_date)
            )
            price_start_date = price_end_date + timedelta(days=1)

# Generate random customer data
def generate_customers(cursor):
    first_names = ["John", "Jane", "Jim", "Anna", "Sara", "Paul", "Nina", "Mike", "Emma", "Tom"]
    last_names = ["Doe", "Smith", "Beam", "Taylor", "Connor", "Walker", "Brown", "Davis", "Wilson", "Harris"]

    for i in range(10):
        cursor.execute(
            "INSERT INTO Customer (first_name, last_name, email, phone_number, address) VALUES (%s, %s, %s, %s, %s)",
            (first_names[i], last_names[i], f"user{i + 1}@example.com", f"555-01{i:04d}", f"Address {i + 1}")
        )

# Generate random order data
def generate_orders(cursor):
    for customer_id in range(1, 11):
        num_orders = random.randint(1, 5)

        for _ in range(num_orders):
            order_date = random_date(datetime(2022, 1, 1), datetime(2024, 7, 28))
            total_amount = round(random.uniform(20, 1000), 2)

            cursor.execute(
                "INSERT INTO OrderTable (customer_id, order_date, total_amount) VALUES (%s, %s, %s)",
                (customer_id, order_date, total_amount)
            )

# Generate random order item data
def generate_order_items(cursor):
    cursor.execute("SELECT order_id FROM OrderTable")
    order_ids = cursor.fetchall()

    for order_id in order_ids:
        num_items = random.randint(1, 3)

        cursor.execute("SELECT variant_id FROM Variant")
        variant_ids = cursor.fetchall()

        for _ in range(num_items):
            variant_id = random.choice(variant_ids)[0]
            cursor.execute("SELECT price FROM Variant WHERE variant_id = %s", (variant_id,))
            price = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO OrderItem (order_id, variant_id, quantity, price_at_purchase) VALUES (%s, %s, %s, %s)",
                (order_id[0], variant_id, random.randint(1, 3), price)
            )
