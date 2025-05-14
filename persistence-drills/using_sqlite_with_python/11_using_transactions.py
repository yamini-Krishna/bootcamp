# Task 11: Using Transactions - Wrap database operations in transactions to ensure data integrity
import sqlite3

class Product:
    @staticmethod
    def insert_product_with_transaction(name, price):
        try:
            conn = sqlite3.connect('store.db')
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            conn.commit()
            print(f"Product '{name}' inserted with price {price}")
        except sqlite3.Error as e:
            conn.rollback()
            print("Transaction failed, rolled back:", e)
        finally:
            conn.close()

# Example usage
Product.insert_product_with_transaction("Product A", 5.0)
Product.insert_product_with_transaction("Product B", 7.5)

# Expected output: Products inserted into the database using transactions.
