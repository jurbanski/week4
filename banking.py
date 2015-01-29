""" Banking class module """
# 2015-01-29
# Joseph Urbanski
# MPCS 50101

class BankAccount():
    """ Bank Account class contains only an account balance."""
    balance = None

    def __init__(self):
        """ When instantiating, set the account balance to zero. """
        self.balance = 0.0

    def deposit(self, amount):
        """ Deposits money into balance """
        self.balance += amount

    def withdraw(self, amount):
        """ Withdraws money from account balance while providing overdraft
            protection.
        """
        if amount <= self.balance:
            self.balance -= amount

    def transfer(self, amount, target):
        """ Transfers money from one account to another """
        self.withdraw(amount)
        target.deposit(amount)
