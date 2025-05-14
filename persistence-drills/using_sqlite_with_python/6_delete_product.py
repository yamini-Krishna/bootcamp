# Task 6: Delete a product from the table using its id

import sqlite3

def delete_product(product_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

# Example usage
delete_product(10)
delete_product(11)

# Expected output: Deletes product with id=1 from the table
