# UML Sequence Diagram

UML Sequence Diagram includes the following interactions:
* Creating a Savings account
* Creating a Checking account
* Depositing to a Checking account
* Withdrawing from a Savings account

```mermaid

sequenceDiagram
    participant User as User
    participant Bank as Bank
    participant Savings Account as SavingsAccount
    participant Checking Account as CheckingAccount
    participant Account as Account

    User ->> Bank: create Savings account
    Bank ->> Bank: create_account("SavingsAccount",...)
    Bank ->> SavingsAccount: __init__(account_number, account_holder_name, balance, interest_rate)
    SavingsAccount ->> Account: __init__(account_number, account_holder_name, balance)
    Bank ->> Bank: accounts.append(savings_account)

    User ->> Bank: create Checking account
    Bank ->> Bank: create_account("CheckingAccount",...)
    Bank ->> CheckingAccount: __init__(account_number, account_holder_name, balance, overdraft_limit)
    CheckingAccount ->> Account: __init__(account_number, account_holder_name, balance)
    Bank ->> Bank: accounts.append(checking_account)

    User ->> Bank: find account: account_number)
    Bank ->> Bank: find_account(account_number)
    Bank -->> User: Account
    
    User ->> Bank: deposit (amount)
    Bank ->> Account: deposit(amount)
    Account ->> SavingsAccount: deposit(amount)
    SavingsAccount ->> SavingsAccount: calculate_interest()

    User ->> Bank: delete_account(account_number)
    Bank ->> Bank: accounts.remove(account)
    
    User ->> Bank: withdraw (amount)
    Bank ->> Account: withdraw (amount)
    Account ->> CheckingAccount: withdraw(amount)
    CheckingAccount ->> Bank: withdraw(amount)


```
