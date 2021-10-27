import person
from main import Account_type
class Customer(person.Person):

    def __init__(self, firstname, lastname, balance, account_type: Account_type):
        super().__init__(firstname, lastname)
        self.balance = balance
        self.account_type = account_type

    def get_account_type(self):
        return self.account_type

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.update_balance(self.balance - amount)

    def deposit(self, amount):
        self.update_balance(self.balance + amount)

    def __str__(self):
        return super().__str__() + \
               '{balance} {account_type}'.format(balance=self.balance, account_type=self.account_type)

    def update_balance(self, new_balance):
        self.balance = new_balance

    def apply_interest(self, interest_amount):
        self.update_balance(self.balance * (1 + interest_amount))
