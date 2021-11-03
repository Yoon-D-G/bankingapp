import person
import account

class Customer(person.Person):

    def __init__(self, firstname, lastname, account: account.Account):
        super().__init__(firstname, lastname)
        self.account = account

    def get_account(self):
        return self.account

    def __str__(self):
        return person.Person.__str__(self) + \
               ', Balance={balance}, ' \
               'Account Type={account_type}'.format(balance=self.account.get_balance(),
                                                    account_type=self.account.account_type())


