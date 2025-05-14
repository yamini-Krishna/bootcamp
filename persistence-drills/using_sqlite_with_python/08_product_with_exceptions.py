# Task 8: Add exception handling to Product class

import sqlite3

class Product:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('store.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Connection error:", e)

    def add_product(self, name, price):
        try:
            self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Insert error:", e)

    def close(self):
        self.conn.close()

# Example usage
p = Product()
p.add_product("Pencil", 0.75)
p.close()

# Expected output: "Pencil" is added or error message is shown
