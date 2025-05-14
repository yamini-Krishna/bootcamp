# 12_product_class.py

import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def fetch_products_with_categories(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Execute a JOIN query to fetch products along with their categories
        cursor.execute('''SELECT p.name AS product_name, p.price, c.name AS category_name
                          FROM products p
                          JOIN categories c ON p.category_id = c.id''')
        
        rows = cursor.fetchall()
        for row in rows:
            print(f"Product: {row[0]}, Price: {row[1]}, Category: {row[2]}")
        
        conn.close()

# Example usage
product = Product()
product.fetch_products_with_categories()
