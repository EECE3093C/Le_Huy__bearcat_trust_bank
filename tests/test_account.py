import unittest
from banking_system import SavingsAccount, CheckingAccount


class TestAccount(unittest.TestCase):
    """Test cases for the Account class and its subclasses."""

    def test_savings_account(self):
        """Test the functionality of the SavingsAccount class."""
        savings_account = SavingsAccount("12345", "John Doe", 1000, 3)
        self.assertEqual(savings_account.get_balance(), 1000)
        self.assertEqual(savings_account.calculate_interest(), 30)
        savings_account.deposit(500)
        self.assertEqual(savings_account.get_balance(), 1500)
        savings_account.withdraw(200)
        self.assertEqual(savings_account.get_balance(), 1300)

    def test_checking_account(self):
        """Test the functionality of the CheckingAccount class."""
        checking_account = CheckingAccount("67890", "Jane Doe", 1000, 500)
        self.assertEqual(checking_account.get_balance(), 1000)
        checking_account.deposit(500)
        self.assertEqual(checking_account.get_balance(), 1500)
        checking_account.withdraw(2000)
        self.assertEqual(checking_account.get_balance(), -500)
        checking_account.withdraw(100)
        self.assertEqual(checking_account.get_balance(), -500)
        checking_account.deposit(500)
        self.assertEqual(checking_account.get_balance(), 0)
