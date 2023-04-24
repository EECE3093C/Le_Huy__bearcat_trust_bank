import unittest
from banking_system import Bank, SavingsAccount, CheckingAccount


class TestBank(unittest.TestCase):
    """A class to test the Bank class."""

    def setUp(self):
        """Set up a Bank object with sample accounts before each test."""
        self.bank = Bank()
        self.bank.create_account("SavingsAccount", "12345", "John Doe", 1000, interest_rate=1.0)
        self.bank.create_account("CheckingAccount", "67890", "Jane Doe", 1000, overdraft_limit=200)

    def test_create_account(self):
        """Test the creation of accounts."""
        self.assertEqual(len(self.bank.accounts), 2)

    def test_find_account(self):
        """Test finding accounts by account number."""
        account = self.bank.find_account("12345")
        self.assertIsInstance(account, SavingsAccount)
        self.assertEqual(account.account_number, "12345")
        self.assertEqual(account.account_holder_name, "John Doe")

        account = self.bank.find_account("67890")
        self.assertIsInstance(account, CheckingAccount)
        self.assertEqual(account.account_number, "67890")
        self.assertEqual(account.account_holder_name, "Jane Doe")

        account = self.bank.find_account("99999")
        self.assertIsNone(account)

    def test_delete_account(self):
        """Test deleting accounts by account number."""
        self.bank.delete_account("12345")
        self.assertEqual(len(self.bank.accounts), 1)
        self.bank.delete_account("99999")
        self.assertEqual(len(self.bank.accounts), 1)


if __name__ == '__main__':
    unittest.main()
