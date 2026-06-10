import sqlite3
import pandas as pd

# Task 5: Read data into a DataFrame
conn = sqlite3.connect('../db/lesson.db')

df = pd.read_sql_query("""
    SELECT line_items.line_item_id, line_items.quantity, products.product_id,
           products.product_name, products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
""", conn)

conn.close()
df['total'] = df['quantity'] * df['price']

print(df.head())


grouped = df.groupby('product_id').agg(
    line_item_id=('line_item_id', 'count'),
    total=('total', 'sum'),
    product_name=('product_name', 'first')
)

print(grouped.head())

grouped = grouped.sort_values('product_name')

grouped.to_csv('order_summary.csv')
print("order_summary.csv written.")