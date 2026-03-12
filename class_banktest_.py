import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_deposit(self):

        akun = BankAccount("rodhi", 4000)
        akun.deposit(2000)

        self.assertEqual(akun.get_balance(), 6000)

    def test_depositerror(self):
        
        akun = BankAccount("rodhi", 3000)

        with self.assertRaises(ValueError):
            akun.deposit(-1000)


    def test_withdraw(self):

        akun = BankAccount("rodhi", 5000)
        akun.withdraw(2000)

        self.assertEqual(akun.get_balance(), 3000)

    def test_withdrawerror(self):

        akun = BankAccount("rodhi", 1000)

        with self.assertRaises(ValueError):
            akun.withdraw(-100)

    def test_get_balance(self):

        akun = BankAccount("rodhi", 3000)

        self.assertEqual(akun.get_balance(), 3000)





if __name__ =="__main__":
    unittest.main()