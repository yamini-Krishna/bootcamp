# 13_aggregation_queries.py

import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name
    
    # Method to calculate the total value of all products
    def total_value_of_products(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Query to sum the price of all products
            cursor.execute("SELECT SUM(price) FROM products")
            total_value = cursor.fetchone()[0]

            conn.close()

            return total_value if total_value is not None else 0  # Return 0 if no products exist
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
            return None


# Example usage
if __name__ == '__main__':
    product = Product()
    total_value = product.total_value_of_products()

    print(f"Total value of all products in stock: {total_value}")
    # Expected output: Total value of all products in stock: <calculated_value>
