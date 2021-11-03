import person
import account

class Customer(person.Person):

<<<<<<< HEAD
    def __init__(self, firstname, lastname, account: account.Account):
        super().__init__(firstname, lastname)
        self.account = account
=======
    def __init__(self, firstname, lastname, balance, account_type, overdraft_limit=0):
        super().__init__(firstname, lastname)
        self.balance = balance
        self.account_type = account_type
        self.overdraft_limit = overdraft_limit
        self.interest = self.set_interest()
        self.number_of_withdrawals = 0

    def set_new_overdraft_limit(self, overdraft_limit):
        assert self.account_type == Account_type.CURRENT, 'No overdraft available for Savings accounts'
        self.overdraft_limit = overdraft_limit

    def get_account_type(self):
        return self.account_type

    def withdrawal_checker2(self):
        if self.account_type == Account_type.CURRENT:
            assert self.number_of_withdrawals <= 6
        else:
            assert self.number_of_withdrawals <= 2

    def withdrawal_checker(self):
        try:
            self.withdrawal_checker2()
            return True
        except AssertionError:
            print('Maximum Number Of Withdrawals Reached')
            return False

    def withdraw(self, amount):
        self.number_of_withdrawals += 1
        if self.withdrawal_checker():
            if self.balance - amount >= 0 - self.overdraft_limit:
                self.update_balance(self.balance - amount)
>>>>>>> 76b3ca6fd2ca7ddf2b740652394bfcc5e177adf2

    def get_account(self):
        return self.account

    def convert_account_type(self):
        if self.account_type == 2:
            return 'Current'
        else:
            return 'Savings'

    def __str__(self):
        return person.Person.__str__(self) + \
               ', Balance={balance}, ' \
<<<<<<< HEAD
               'Account Type={account_type}'.format(balance=self.account.get_balance(),
                                                    account_type=self.account.account_type())
=======
               'Account Type={account_type}'.format(balance=self.balance,
                                                    account_type=self.convert_account_type())
>>>>>>> 76b3ca6fd2ca7ddf2b740652394bfcc5e177adf2


<<<<<<< HEAD
=======
    def set_interest(self):
        if self.account_type == Account_type.CURRENT:
            return 0.02
        else:
            return 0.07

    def apply_interest(self):
        self.update_balance(self.balance * (1 + self.interest))
>>>>>>> 76b3ca6fd2ca7ddf2b740652394bfcc5e177adf2
