import sqlite3

def setup_accounts():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS accounts')
    cursor.execute('''
        CREATE TABLE accounts (
            account_id INTEGER PRIMARY KEY,
            balance REAL NOT NULL
        )
    ''')
    cursor.executemany('INSERT INTO accounts (account_id, balance) VALUES (?, ?)', [
        (1, 1000.0),
        (2, 500.0)
    ])
    conn.commit()
    conn.close()

def transfer_funds(from_id, to_id, amount):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()
        conn.execute('BEGIN')

        # Check balance
        cursor.execute('SELECT balance FROM accounts WHERE account_id = ?', (from_id,))
        from_balance = cursor.fetchone()
        if not from_balance or from_balance[0] < amount:
            raise Exception("Insufficient funds")

        # Debit
        cursor.execute('UPDATE accounts SET balance = balance - ? WHERE account_id = ?', (amount, from_id))

        # Credit
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_id = ?', (amount, to_id))

        conn.commit()
        print(f"Transferred ₹{amount} from Account {from_id} to Account {to_id}")
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed: {e}")
    finally:
        conn.close()
        # Add this function to check balances
def show_balances():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts')
    for row in cursor.fetchall():
        print(row)
    conn.close()




# Setup and Test
setup_accounts()
transfer_funds(1, 2, 200.0)
show_balances()