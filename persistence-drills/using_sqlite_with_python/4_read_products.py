# Task 4: Fetch and print all records from products table

import sqlite3

def read_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Example usage
read_products()

# Expected output: List of all products in the table
# Example: (1, 'Pen', 1.5)
