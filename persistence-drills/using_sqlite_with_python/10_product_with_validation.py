# Task 10: Add data validation before inserting/updating

import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()

    def add_product(self, name, price):
        if isinstance(name, str) and isinstance(price, (int, float)) and price > 0:
            self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            self.conn.commit()
        else:
            print("Invalid data: name must be string, price must be positive number")

    def close(self):
        self.conn.close()

# Example usage
p = Product()
p.add_product("Eraser", 0.8)
p.add_product("Invalid", -5)  # This will be rejected
p.close()

# Expected output: Eraser added, second entry rejected with validation error
