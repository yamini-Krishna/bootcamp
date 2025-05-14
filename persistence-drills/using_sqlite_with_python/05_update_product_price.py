# Task 5: Update the price of a product using its id

import sqlite3

def update_price(product_id, new_price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()

# Example usage
update_price(1, 2.5)

# Expected output: Updates product with id=1 to price=2.0
