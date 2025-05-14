# Task 1: Setting Up SQLite Database
# This script creates store.db if it doesn't exist

import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('store.db')
conn.close()

# Expected output: store.db file is created in the current directory
