"""All the account logic: sign up, login, and reset password.

Passwords are never stored as plain text. Each password is hashed with a
random salt so two users with the same password get different stored values.
"""

import hashlib
import os

from database import get_connection


def hash_password(password, salt=None):
    """Hash a password with a salt. Returns 'salt$hash'."""
    if salt is None:
        salt = os.urandom(16).hex()
    digest = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}${digest}"


def check_password(password, stored):
    """Check a typed password against the stored 'salt$hash' value."""
    salt = stored.split("$")[0]
    return hash_password(password, salt) == stored


def sign_up(full_name, email, dob, password):
    """Create a new account. Returns (success, message)."""
    if not full_name or not email or not dob or not password:
        return False, "All fields are required."

    conn = get_connection()
    existing = conn.execute(
        "SELECT id FROM users WHERE email = ?", (email,)
    ).fetchone()
    if existing:
        conn.close()
        return False, "That email is already registered."

    conn.execute(
        "INSERT INTO users (full_name, email, dob, password) VALUES (?, ?, ?, ?)",
        (full_name, email, dob, hash_password(password)),
    )
    conn.commit()
    conn.close()
    return True, "Account created successfully."


def login(email, password):
    """Check login details. Returns (success, user_row_or_None)."""
    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()
    conn.close()

    if user and check_password(password, user["password"]):
        return True, user
    return False, None


def reset_password(email, dob, new_password):
    """Forgot password: verify identity with email + date of birth,
    then set a new password. Returns (success, message)."""
    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE email = ? AND dob = ?", (email, dob)
    ).fetchone()

    if not user:
        conn.close()
        return False, "Email and date of birth do not match our records."

    conn.execute(
        "UPDATE users SET password = ? WHERE email = ?",
        (hash_password(new_password), email),
    )
    conn.commit()
    conn.close()
    return True, "Password updated successfully."
