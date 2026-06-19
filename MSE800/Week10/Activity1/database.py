"""Database setup: creates the users table and gives us a connection."""

import sqlite3

DB_NAME = "users.db"


def get_connection():
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn


def init_db():
    """Create the users table the first time the app runs."""
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email     TEXT NOT NULL UNIQUE,
            dob       TEXT NOT NULL,
            password  TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()
