# This file handles the SQL queries for insights.

# queries.py

def top_customers(cursor):
    # SQL Query 1: Top 5 customers with the highest average order amounts in the last 6 months
    query = """
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        AVG(o.total_amount) AS average_order_amount
    FROM 
        Customer c
    JOIN 
        OrderTable o ON c.customer_id = o.customer_id
    WHERE 
        o.order_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY 
        c.customer_id
    ORDER BY 
        average_order_amount DESC
    LIMIT 5;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def lower_order_value_this_year(cursor):
    # SQL Query 2: Customers whose order value is lower this year compared to the previous year
    query = """
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        COALESCE(SUM(CASE WHEN YEAR(o.order_date) = YEAR(CURDATE()) THEN o.total_amount ELSE 0 END), 0) AS total_this_year,
        COALESCE(SUM(CASE WHEN YEAR(o.order_date) = YEAR(CURDATE()) - 1 THEN o.total_amount ELSE 0 END), 0) AS total_last_year
    FROM 
        Customer c
    JOIN 
        OrderTable o ON c.customer_id = o.customer_id
    GROUP BY 
        c.customer_id
    HAVING 
        total_this_year < total_last_year;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def cumulative_purchases_by_customer(cursor):
    # SQL Query 3: Cumulative purchases by customer, broken down by product category
    query = """
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        p.category,
        SUM(oi.price_at_purchase * oi.quantity) AS total_spent
    FROM 
        Customer c
    JOIN 
        OrderTable o ON c.customer_id = o.customer_id
    JOIN 
        OrderItem oi ON o.order_id = oi.order_id
    JOIN 
        Variant v ON oi.variant_id = v.variant_id
    JOIN 
        Product p ON v.product_id = p.product_id
    GROUP BY 
        c.customer_id, p.category
    ORDER BY 
        c.customer_id, total_spent DESC;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def top_selling_products(cursor):
    # SQL Query 4: Top 5 selling products, broken down by product variants
    query = """
    SELECT 
        p.product_id,
        p.product_name,
        v.variant_id,
        v.variant_name,
        SUM(oi.quantity) AS total_quantity_sold
    FROM 
        Product p
    JOIN 
        Variant v ON p.product_id = v.product_id
    JOIN 
        OrderItem oi ON v.variant_id = oi.variant_id
    GROUP BY 
        p.product_id, v.variant_id
    ORDER BY 
        total_quantity_sold DESC
    LIMIT 5;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result
