# Task 9: Search products by name fragment

import sqlite3

def search_products(name_fragment):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name_fragment + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

# Example usage
print(search_products("Pen"))

# Expected output: List of products with 'Pen' in their name
