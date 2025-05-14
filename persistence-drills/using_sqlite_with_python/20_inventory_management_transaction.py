import sqlite3
import datetime

def setup_inventory_tables():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Ensure products table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER DEFAULT 0
        )
    ''')

    # Create inventory_log table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            change_quantity INTEGER NOT NULL,
            change_date TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    ''')

    # Insert sample product if not already present
    cursor.execute('SELECT COUNT(*) FROM products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', ("Pen", 1.5, 100))

    conn.commit()
    conn.close()

def update_inventory(product_id, change_quantity):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        conn.execute('BEGIN')

        # Update stock
        cursor.execute('UPDATE products SET stock = stock + ? WHERE id = ?', (change_quantity, product_id))
        if cursor.rowcount == 0:
            raise Exception("Product not found")

        # Insert into inventory_log
        change_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO inventory_log (product_id, change_quantity, change_date)
            VALUES (?, ?, ?)
        ''', (product_id, change_quantity, change_date))

        conn.commit()
        print(f"Inventory updated for product {product_id}. Change: {change_quantity}")
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed: {e}")
    finally:
        conn.close()

# Setup and test
setup_inventory_tables()
update_inventory(1, -5)  # E.g., sold 5 units of product 1
