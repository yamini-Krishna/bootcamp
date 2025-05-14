import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def batch_insert(self, products):
        """
        Inserts multiple products in one transaction.
        :param products: List of tuples (name, price)
        """
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Begin a transaction
            cursor.execute("BEGIN TRANSACTION")

            # Insert each product
            cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

            # Commit the transaction
            conn.commit()
            print(f"{len(products)} products inserted successfully.")

        except sqlite3.Error as e:
            # In case of an error, roll back the transaction
            conn.rollback()
            print(f"Error: {e}")

        finally:
            # Close the connection
            conn.close()

# Example usage
if __name__ == "__main__":
    product = Product()

    # List of products to be inserted
    products_to_insert = [
        ("Pencil", 0.5),
        ("Eraser", 0.2),
        ("Ruler", 1.0),
        ("Sharpener", 0.3),
        ("Notebook", 1.5)
    ]

    product.batch_insert(products_to_insert)
