import sqlite3

# Open the database 
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()


# Task 1: Total price of the first 5 orders (Complex JOINs with Aggregation)
print("Task 1: Total price of the first 5 orders")
task1_query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products   AS p  ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
"""
cursor.execute(task1_query)
for row in cursor.fetchall():
    print(f"Order {row[0]}: ${row[1]:.2f}")

# Task 2: Average order total per customer
print("\nTask 2: Average order total per customer")
task2_query = """
    SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
    FROM customers AS c
    LEFT JOIN (
        SELECT o.customer_id AS customer_id_b,
               SUM(p.price * li.quantity) AS total_price
        FROM orders AS o
        JOIN line_items AS li ON o.order_id = li.order_id
        JOIN products   AS p  ON li.product_id = p.product_id
        GROUP BY o.order_id
    ) AS sub ON c.customer_id = sub.customer_id_b
    GROUP BY c.customer_id;
"""
cursor.execute(task2_query)
for row in cursor.fetchall():
    avg = row[1] if row[1] is not None else 0
    print(f"{row[0]}: ${avg:.2f}")
    
# Task 3: Insert transaction based on data — new order for Perez and Sons by Miranda Harris,
print("\nTask 3: New order for Perez and Sons")
try:
    # Look up customer_id
    cursor.execute(
        "SELECT customer_id FROM customers WHERE customer_name = ?",
        ("Perez and Sons",)
    )
    customer_id = cursor.fetchone()[0]

    # Look up employee_id
    cursor.execute(
        "SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?",
        ("Miranda", "Harris")
    )
    employee_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute(
        """INSERT INTO orders (customer_id, employee_id, date)
           VALUES (?, ?, date('now'))
           RETURNING order_id""",
        (customer_id, employee_id)
    )
    order_id = cursor.fetchone()[0]

    for pid in product_ids:
        cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, pid, 10)
        )

    # Commit the whole transaction atomically
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Transaction failed, rolled back: {e}")

# Print the line items of the new order (SELECT with JOIN per the assignment)
cursor.execute(
    """SELECT li.line_item_id, li.quantity, p.product_name
       FROM line_items AS li
       JOIN products   AS p ON li.product_id = p.product_id
       WHERE li.order_id = ?""",
    (order_id,)
)
for row in cursor.fetchall():
    print(f"Line item {row[0]}: {row[1]} x {row[2]}")



# Task 4: Employees with more than 5 orders
print("\nTask 4: Employees with more than 5 orders")
task4_query = """SELECT e.employee_id, e.first_name, e.last_name
                FROM employees AS e
                JOIN orders AS o ON e.employee_id = o.employee_id
                GROUP BY e.employee_id, e.first_name, e.last_name
                HAVING COUNT(o.order_id) > 5
"""
cursor.execute(task4_query)
for row in cursor.fetchall():
    print(f"Employee {row[0]}: {row[1]} {row[2]} orders")
                
# close connection
conn.close()sk 