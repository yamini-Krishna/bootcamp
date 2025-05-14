# 12_insert_sample_data.py

import sqlite3

def insert_sample_data():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Insert categories
    cursor.execute("INSERT INTO categories (name) VALUES ('Stationery')")
    cursor.execute("INSERT INTO categories (name) VALUES ('Electronics')")
    cursor.execute("INSERT INTO categories (name) VALUES ('Books')")

    # Insert products with category_id (assuming 1, 2, and 3 are valid category IDs)
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES ('Pen', 1.5, 1)")
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES ('Laptop', 800, 2)")
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES ('Python Book', 30, 3)")

    conn.commit()
    conn.close()

# Run this to insert sample data
insert_sample_data()
