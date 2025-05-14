import sqlite3

def insert_product(name, price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

# Example usage with different product names and prices
insert_product("Pen", 1.5)
insert_product("Notebook", 2.5)
insert_product("Eraser", 0.5)
insert_product("Pencil", 0.75)
insert_product("Sharpener", 1.0)
insert_product("Ruler", 1.25)

# Expected output: Products with different names and prices are inserted into the products table.

