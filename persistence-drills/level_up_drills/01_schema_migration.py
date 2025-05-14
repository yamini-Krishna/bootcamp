import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Step 1: Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
''')

# Step 2: Simulate adding a 'created_at' column via migration
try:
    cursor.execute('ALTER TABLE users ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
    print("Migration applied successfully: 'created_at' column added.")
except sqlite3.OperationalError as e:
    print(f"Error applying migration: {e}")

# Step 3: Insert some data into the table (optional)
cursor.execute('INSERT INTO users (name) VALUES ("Alice")')
cursor.execute('INSERT INTO users (name) VALUES ("Bob")')

# Step 4: Verify the changes (show users with created_at)
cursor.execute('SELECT id, name, created_at FROM users')
rows = cursor.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

# Commit and close the connection
conn.commit()
conn.close()
