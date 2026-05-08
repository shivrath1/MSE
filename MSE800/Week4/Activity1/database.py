import sqlite3

def create_connection():
    conn = sqlite3.connect("money_exchange.db")
    conn.execute("PRAGMA foreign_keys = ON")
    print("Money Transfere DB Connected Sucessfully")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    #Customer
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email_id TEXT NOT NULL UNIQUE,
            contact_number TEXT NOT NULL UNIQUE,
            kyc_status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Account
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            account_number TEXT,
            balance REAL DEFAULT 0,
            account_type TEXT,
            account_status TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
        )
    ''')
    #Currency
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS currency (
            currency_code TEXT PRIMARY KEY,
            currency_name TEXT,
            country_code TEXT,
            symbol TEXT,
            is_active TEXT
        )
    ''')
    #Fee
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fee (
            fee_id INTEGER PRIMARY KEY,
            from_currency TEXT,
            to_currency TEXT,
            fee_value TEXT,
            fee_type TEXT,
            FOREIGN KEY (from_currency) REFERENCES currency(currency_code),
            FOREIGN KEY (to_currency) REFERENCES currency(currency_code)
        )
    ''')
    #Exchange Rate
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rate (
            rate_id INTEGER PRIMARY KEY,
            from_currency TEXT,
            to_currency TEXT,
            rate_value TEXT,
            exchange_date TEXT,
            FOREIGN KEY (from_currency) REFERENCES currency(currency_code),
            FOREIGN KEY (to_currency) REFERENCES currency(currency_code)
        )
    ''')
    #Transaction
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_account_id INTEGER,
            to_account_id INTEGER,
            rate_id INTEGER,
            fee_id INTEGER,
            amount_sent REAL,
            amount_received REAL,
            txn_status TEXT,
            txn_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (from_account_id) REFERENCES account(account_id),
            FOREIGN KEY (to_account_id) REFERENCES account(account_id),
            FOREIGN KEY (rate_id) REFERENCES rate(rate_id),
            FOREIGN KEY (fee_id) REFERENCES fee(fee_id)
        )
    ''')
    conn.commit()
    conn.close()
