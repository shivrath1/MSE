"""Command-line menu for the login & signup system.

Run this file to use the program:  python main.py
"""

from database import init_db
from auth import sign_up, login, reset_password


def main():
    init_db()
    print("=== Login & Signup System ===")

    while True:
        print("\n1. Sign Up")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            full_name = input("Full Name: ").strip()
            email = input("Email: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            password = input("Password: ").strip()
            ok, message = sign_up(full_name, email, dob, password)
            print(message)

        elif choice == "2":
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            ok, user = login(email, password)
            if ok:
                print(f"Welcome back, {user['full_name']}!")
            else:
                print("Invalid email or password.")

        elif choice == "3":
            email = input("Email: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            new_password = input("New Password: ").strip()
            ok, message = reset_password(email, dob, new_password)
            print(message)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
