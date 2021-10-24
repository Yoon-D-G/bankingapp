class Customer:
    def __init__(self, firstname, lastname, balance, customer_id, account_type):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        self.customer_id = customer_id
        self.account_type = account_type

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.update_balance(self.balance - amount)

    def deposit(self, amount):
        self.update_balance(self.balance + amount)

    def status(self):
        return 'Customer {firstname} {lastname} has £{balance} in their account'.format(firstname=self.firstname, lastname=self.lastname, balance=self.balance)

    def update_balance(self, new_balance):
        self.balance = new_balance