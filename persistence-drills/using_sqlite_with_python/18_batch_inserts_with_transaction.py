import sqlite3

def batch_insert_products(products):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        conn.execute('BEGIN')  # Start a transaction

        for product in products:
            cursor.execute(
                "INSERT INTO products (name, price) VALUES (?, ?)",
                (product[0], product[1])
            )

        conn.commit()
        print("All products inserted successfully.")
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Transaction failed and rolled back: {e}")
    finally:
        conn.close()

# Sample product data: list of (name, price)
product_data = [
    ("Notebook", 3.5),
    ("Pencil", 0.5),
    ("Eraser", 0.75),
    # Uncomment the below line to trigger a rollback (invalid column count)
    # ("Faulty",) 
]

batch_insert_products(product_data)
