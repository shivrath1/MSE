from database import create_connection
import sqlite3

def add_customer(name, email, contact_number, kyc_status):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customer (full_name, email_id, contact_number, kyc_status ) VALUES (?, ?, ?, ?)", 
        (name, email, contact_number, kyc_status))
        customer_id = cursor.lastrowid
        account_number = f"ACC{customer_id}001"
        cursor.execute("""
            INSERT INTO account (
                customer_id,
                account_number,
                account_status,
                account_type,
                balance
            )
            VALUES (?, ?, ?, ?, ?)
        """, (customer_id, account_number, "ACTIVE", "SAVINGS", 1000))

        conn.commit()
        print(" Customer added and Account Created successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_customer(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer WHERE full_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_customer(customer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customer WHERE customer_id = ?", (customer_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
