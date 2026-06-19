# Login & Signup System

A simple command-line login and signup system built in Python with SQLite.
It supports creating an account, logging in, and resetting a forgotten
password. Passwords are stored securely using salted hashing — never as
plain text.

## Features

- **Sign Up** with full name, email, date of birth, and password
- **Login** with email and password
- **Forgot Password** — reset password by verifying email + date of birth
- password hashing (SHA-256)
- Data saved in a local SQLite database

## Files

| File | Purpose |
|------|---------|
| `main.py` | Command-line menu |
| `auth.py` | Sign up, login, and reset-password logic |
| `database.py` | Database connection and table setup |

## How to Run

```bash
python main.py
```

## How to Use / Test

When you run `python main.py` you get a menu:

```
1. Sign Up
2. Login
3. Forgot Password
4. Exit
```

Test sequence:

1. Choose **1** and create an account
2. Choose **2** and log in with that email and password, logins successfully
3. Choose **3**, enter the same email and date of birth, and set a new password
4. Choose **2** and log in with the **new** password, logins successfully
5. Choose **2** and try the **old** password, login is rejected
