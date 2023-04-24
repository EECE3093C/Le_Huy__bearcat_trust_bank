from banking_system import Bank
from utils import generate_synthetic_data


def display_menu():
    """Display the main menu with available options."""
    print("Welcome to the Simple Banking System")
    print("Please choose an option:")
    print("1. Create a new account")
    print("2. Delete an account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Check balance")
    print("6. Display account information")
    print("7. List all accounts")
    print("8. Load synthetic data")
    print("9. Exit")


def main():
    """Execute the main program loop."""
    bank = Bank()

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        print("\n")

        if choice == '1':
            account_type = input("Enter account type (SavingsAccount or CheckingAccount): ")
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))

            if account_type == "SavingsAccount":
                interest_rate = float(input("Enter interest rate (in %): "))
                bank.create_account(account_type, account_number, account_holder_name, balance, interest_rate=interest_rate)
            elif account_type == "CheckingAccount":
                overdraft_limit = float(input("Enter overdraft limit: "))
                bank.create_account(account_type, account_number, account_holder_name, balance, overdraft_limit=overdraft_limit)
            else:
                print("Invalid account type.")

            print("Account created successfully.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            bank.delete_account(account_number)
            print("Account deleted successfully.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.find_account(account_number)
            if account:
                account.deposit(amount)
                print("Money deposited successfully.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.find_account(account_number)
            if account:
                account.withdraw(amount)
                print("Money withdrawn successfully.")

        elif choice == '5':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(f"Current balance: ${account.get_balance()}")

        elif choice == '6':
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                account.display()

        elif choice == '7':
            bank.list_accounts()

        elif choice == '8':
            num_accounts = int(input("Enter the number of synthetic accounts to generate: "))
            synthetic_data = generate_synthetic_data(num_accounts)
            for account in synthetic_data:
                account_type = account['account_type']
                account_number = account['account_number']
                account_holder_name = account['account_holder_name']
                balance = account['balance']

                if account_type == "SavingsAccount":
                    interest_rate = account['interest_rate']
                    bank.create_account(account_type, account_number, account_holder_name, balance, interest_rate=interest_rate)
                elif account_type == "CheckingAccount":
                    overdraft_limit = account['overdraft_limit']
                    bank.create_account(account_type, account_number, account_holder_name, balance, overdraft_limit=overdraft_limit)

            print(f"{num_accounts} synthetic accounts loaded successfully.")

        elif choice == '9':
            print("Thank you for using the Simple Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    main()