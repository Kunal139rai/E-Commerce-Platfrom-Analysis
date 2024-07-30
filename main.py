# This is the main script where we use the functions from the above modules.

# main.py
from db_connection import get_connection, close_connection
from data_generation import (
    generate_products,
    generate_variants,
    generate_price_history,
    generate_customers,
    generate_orders,
    generate_order_items
)
from queries import (
    top_customers,
    lower_order_value_this_year,
    cumulative_purchases_by_customer,
    top_selling_products
)

def main():
    # Establish a connection to the database
    connection = get_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        # Generate and insert random data
        generate_products(cursor)
        generate_variants(cursor)
        generate_price_history(cursor)
        generate_customers(cursor)
        generate_orders(cursor)
        generate_order_items(cursor)

        connection.commit()  # Commit the changes

        # Execute queries and print results
        print("Random data inserted successfully.")

        # 1. Retrieve the top 5 customers with the highest average order amounts in the last 6 months
        print("\nTop 5 Customers with Highest Average Order Amounts (Last 6 Months):")
        for row in top_customers(cursor):
            print(row)

        # 2. Retrieve the list of customers whose order value is lower this year compared to the previous year
        print("\nCustomers with Lower Order Value This Year Compared to Last Year:")
        for row in lower_order_value_this_year(cursor):
            print(row)

        # 3. Cumulative purchases by customer, broken down by product category
        print("\nCumulative Purchases by Customer (Broken Down by Product Category):")
        for row in cumulative_purchases_by_customer(cursor):
            print(row)

        # 4. Top 5 selling products, broken down by product variants
        print("\nTop 5 Selling Products (Broken Down by Product Variants):")
        for row in top_selling_products(cursor):
            print(row)

    except Exception as e:
        print("Error during data generation or querying:", e)
        connection.rollback()
    finally:
        # Close the database connection
        close_connection(connection, cursor)

if __name__ == "__main__":
    main()
