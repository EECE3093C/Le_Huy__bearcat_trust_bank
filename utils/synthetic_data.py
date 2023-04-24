import random
import string
import names


def random_account_number():
    """Generate a random 10-digit account number."""
    return ''.join(random.choice(string.digits) for _ in range(10))


def generate_synthetic_data(num_accounts=10):
    """Generate synthetic bank account data.

    Args:
        num_accounts (int, optional): Number of synthetic accounts to generate. Defaults to 10.

    Returns:
        list: A list of dictionaries containing synthetic bank account data.
    """
    account_data = []
    for _ in range(num_accounts):
        account_type = random.choice(['SavingsAccount', 'CheckingAccount'])
        account_holder_name = names.get_full_name()
        balance = round(random.uniform(1000, 10000), 2)
        if account_type == 'SavingsAccount':
            interest_rate = round(random.uniform(0.5, 3), 2)
            account_data.append({
                'account_type': account_type,
                'account_number': random_account_number(),
                'account_holder_name': account_holder_name,
                'balance': balance,
                'interest_rate': interest_rate
            })
        else:  # CheckingAccount
            overdraft_limit = random.choice([50, 100, 150, 200, 300])
            account_data.append({
                'account_type': account_type,
                'account_number': random_account_number(),
                'account_holder_name': account_holder_name,
                'balance': balance,
                'overdraft_limit': overdraft_limit
            })
    return account_data
