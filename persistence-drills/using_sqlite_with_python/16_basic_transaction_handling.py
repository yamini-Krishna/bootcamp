import sqlite3

def create_customers_table():
    """Creates the 'customers' table."""
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Create the customers table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT
    )''')

    conn.commit()
    conn.close()

def insert_customers():
    """Inserts multiple customer records within a transaction."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Start a transaction
        cursor.execute("BEGIN TRANSACTION")

        # Insert customer records (example data)
        customers = [
            ("John Doe", "john@example.com", "1234567890"),
            ("Jane Smith", "jane@example.com", "0987654321"),
            ("Alice Johnson", "alice@example.com", "1122334455"),
            ("Bob Brown", "bob@example.com", "5566778899")
        ]
        
        # Insert the customers into the customers table
        cursor.executemany("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", customers)

        # Commit the transaction
        conn.commit()
        print(f"{len(customers)} customers inserted successfully.")

    except sqlite3.Error as e:
        # In case of any error, rollback the transaction
        conn.rollback()
        print(f"Error occurred: {e}. Transaction rolled back.")

    finally:
        # Close the connection
        conn.close()

# Example usage
if __name__ == "__main__":
    # Create the customers table (if not exists)
    create_customers_table()

    # Insert multiple customers in a transaction
    insert_customers()
