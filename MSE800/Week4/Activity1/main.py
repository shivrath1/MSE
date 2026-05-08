from database import create_table
from user_manager import add_customer, view_customers, search_customer, delete_customer

def menu():
    print("\n==== Customer Manager ====")
    print("1. Register Customer")
    print("2. Send Money")
    print("3. View Transaction History")
    print("4. Set Exchange Rate(Admin)")
    print("5. View Customers (Admin)")
    print("6. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter full name: ")
            email = input("Enter email: ")
            phone_number = input("Enter Phone number: ")
            kyc_status = True

            add_customer(name, email, phone_number, kyc_status)
        elif choice == '2':
            users = view_customers()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter full name to search: ")
            users = search_customer(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter customer ID to delete: "))
            delete_customer(user_id)
            add_customer(name, email, phone_number, kyc_status)
        elif choice == '5':
            users = view_customers()
            for user in users:
                print(user)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
