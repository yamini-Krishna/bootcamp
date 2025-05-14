import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE products ADD COLUMN stock INTEGER DEFAULT 0")
    conn.commit()
    print("Column 'stock' added successfully.")
except Exception as e:
    print("Error:", e)

conn.close()
