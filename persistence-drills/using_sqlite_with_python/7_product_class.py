# Task 7: Create Product class with add, update, delete, list methods

import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def add_product(self, name, price):
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def update_product(self, product_id, price):
        self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()

    def list_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Example usage
p = Product()
p.add_product("Book", 12.5)
print(p.list_products())
p.close()

# Expected output: Adds "Book" and lists all products
