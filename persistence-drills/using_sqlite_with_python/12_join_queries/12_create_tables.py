# 12_create_tables.py

import sqlite3

def create_tables():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Drop the tables if they exist to reset the database (Optional: If you want a fresh start)
    cursor.execute('DROP TABLE IF EXISTS products')
    cursor.execute('DROP TABLE IF EXISTS categories')

    # Create categories table
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                    )''')

    # Create products table with a foreign key to categories
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        category_id INTEGER,
                        FOREIGN KEY (category_id) REFERENCES categories (id)
                    )''')

    conn.commit()
    conn.close()

# Run this to create the tables
create_tables()
