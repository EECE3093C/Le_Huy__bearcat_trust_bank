# Account Class Modifications

Modify the `Account` class defined in the [account.py](/banking_system/account.py) file as follows:

1. Add **init** method: Define an initializer method called `init` that takes three arguments - `account_number`, `account_holder_name`, and `balance`. Assign these values to instance variables with the same names.
2. Add **deposit** method: Define a method called `deposit` that takes one argument, `amount`. Add the amount to the current balance of the account.
3. Add **withdraw** method: Define a method called `withdraw` that takes one argument, `amount`. Check if there are sufficient funds in the account before subtracting the amount from the balance. If there are insufficient funds, print a message to inform the user.

<br/>

Modify the `SavingsAccount` class defined in the [account.py](/banking_system/account.py) file as follows:

1. Add **init** method: Define an initializer method called `init` that takes four arguments - `account_number`, `account_holder_name`, `balance`, and `interest_rate` (with a default value of 0.0). Call the superclass (`Account`) initializer using the `super()` function and pass the `account_number`, `account_holder_name`, and `balance` as arguments. Assign the `interest_rate` argument to an instance variable with the same name.

<br/>

Modify the `CheckingAccount` class defined in the [account.py](/banking_system/account.py) file as follows:

1. Add **init** method: Define an initializer method called `init` that takes four arguments - `account_number`, `account_holder_name`, `balance`, and `overdraft_limit` (with a default value of 0). Call the superclass (`Account`) initializer using the `super()` function and pass the `account_number`, `account_holder_name`, and `balance` as arguments. Assign the `overdraft_limit` argument to an instance variable with the same name.
