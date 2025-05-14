import sqlite3

# Create the tables if they don't exist
def create_tables():
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Create 'orders' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                order_date TEXT,
                status TEXT
            )
        ''')

        # Create 'order_details' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_details (
                order_detail_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id)
            )
        ''')

        conn.commit()
        print("Tables created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()

# Insert sample data into orders and order_details
def insert_sample_data():
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Insert sample data into 'orders'
        cursor.execute("INSERT INTO orders (customer_id, order_date, status) VALUES (1, '2025-05-12', 'Pending')")

        # Insert sample data into 'order_details'
        cursor.execute("INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (1, 1, 2, 15.0)")

        conn.commit()
        print("Sample data inserted successfully!")
    except sqlite3.Error as e:
        print(f"Error inserting sample data: {e}")
    finally:
        conn.close()

# Function for performing the update transaction across multiple tables
def update_multiple_tables_transaction():
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Start transaction
        conn.isolation_level = None  # Disable autocommit to handle transaction explicitly
        cursor.execute('BEGIN TRANSACTION')

        # Update 'orders' table
        cursor.execute("UPDATE orders SET status = 'Shipped' WHERE order_id = 1")

        # Update 'order_details' table
        cursor.execute("UPDATE order_details SET price = 18.0 WHERE order_id = 1")

        # Commit the transaction
        conn.commit()
        print("Transaction successful: Both tables updated.")
    except sqlite3.Error as e:
        print(f"Transaction failed: {e}")
        conn.rollback()  # Rollback the transaction in case of any error
    finally:
        conn.close()

# Create the tables and insert sample data
create_tables()
insert_sample_data()

# Perform the update operation
update_multiple_tables_transaction()
