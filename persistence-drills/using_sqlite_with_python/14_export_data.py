import sqlite3
import csv

def export_data_to_csv():
    # Connect to the SQLite database
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Execute a query to fetch all products
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Define the CSV file path
    csv_file = "products_data.csv"

    # Open the CSV file in write mode
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header (column names)
        writer.writerow(['id', 'name', 'price'])

        # Write the data (product records)
        writer.writerows(products)

    # Close the database connection
    conn.close()

    print(f"Data has been exported to {csv_file}")

# Example usage
export_data_to_csv()
