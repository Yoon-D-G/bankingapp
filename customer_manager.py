class Customer:
    id = 10000000

    def __init__(self, firstname, lastname, balance, account_type):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        self.account_type = account_type
        self.customer_id = self.customer_id()

    def customer_id(self):  # I'd like this to only be accessed within the constructor
        Customer.id += 1
        return Customer.id

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.update_balance(self.balance - amount)

    def deposit(self, amount):
        self.update_balance(self.balance + amount)

    def status(self):
        return 'Customer {firstname} {lastname} has £{balance} in their account'.format(
            firstname=self.firstname,
            lastname=self.lastname,
            balance=self.balance)

    def update_balance(self, new_balance):
        self.balance = new_balance