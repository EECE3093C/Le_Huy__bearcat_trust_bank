class Account:
    """A class representing a bank account."""
    
    def __init__(self, account_number, account_holder_name, balance):
        #account details
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        """Add the amount to the current balance of the account."""
        self.balance += amount
        
    def withdraw(self, amount):
        """Withdraw amount of money if it doesn't exceed the balance."""
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Your account does not have sufficient funds.")
     
    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def display(self):
        """Display the account information."""
        print(f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance}")


class SavingsAccount(Account):
    """A class representing a savings account."""

    def __init__(self, account_number, account_holder_name, balance, interest_rate = 0.0):
        super().__init__(account_number,account_holder_name,balance)
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        """Calculate and return the interest on the account balance."""
        return self.balance * (self.interest_rate / 100)

    def display(self):
        """Display the savings account information including the interest rate."""
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")


class CheckingAccount(Account):
    """A class representing a checking account."""

    def __init__(self, account_number, account_holder_name, balance, overdraft_limit = 0):
        super().__init__(account_number,account_holder_name,balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Withdraw the given amount from the account if it doesn't exceed the overdraft limit."""
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded.")

    def display(self):
        """Display the checking account information including the overdraft limit."""
        super().display()
        print(f"Overdraft Limit: ${self.overdraft_limit}")
