import employee_manager
import employee
<<<<<<< HEAD
import customer_manager
import account

def main():
    account1 = account.Current_Account(1000, 0.02)
    account2 = account.Savings_Account(2000, 0.05)
    account3 = account.Current_Account(3000, 0.07)

    customer_dictionary = {}
    customer1 = customer_manager.Customer("Eric", "Clapton", account1)
    customer2 = customer_manager.Customer("Henry", "Rollins", account2)
    customer3 = customer_manager.Customer("James", "Bond", account3)
    customer1.get_account().deposit(2000)
=======
from enum import IntEnum, auto
import customer_manager

class Account_type(IntEnum):
    SAVINGS = auto()
    CURRENT = auto()

def main():
    customer1 = customer_manager.Customer("Eric", "Clapton", 100000, Account_type.CURRENT)
    customer2 = customer_manager.Customer("Henry", "Rollins", 25000, Account_type.SAVINGS)
    customer3 = customer_manager.Customer("James", "Bond", 10000, Account_type.CURRENT)

    customer1.set_new_overdraft_limit(1000)
    print(customer1)
    customer1.apply_interest()
    print(customer1)

    customer2.withdraw(1000)
    customer2.withdraw(1000)
    customer2.withdraw(1000)
    print(customer2)

    customer_list = []
    customer_list.append(customer1)
    customer_list.append(customer2)
    customer_list.append(customer3)

    customer_current = [x for x in customer_list if x.get_account_type() == Account_type.CURRENT]
    customer_toString = [customer.__str__() for customer in customer_list]
>>>>>>> 76b3ca6fd2ca7ddf2b740652394bfcc5e177adf2

    employee1 = employee.Employee('Steven', 'Morrissey', 27500)
    employee2 = employee.Employee('Ziggy', 'Stardust', 26000)
    employee3 = employee.Employee('Nick', 'Drake', 28000)
    employee4 = employee.Employee('Johnny', 'Marr', 32000)
    employee5 = employee.Employee('Samy', 'Kamkar', 41000)
    employee6 = employee.Employee('Joan', "D'Arc", 25000)

    employeeManager1 = employee_manager.Employee_manager('Simon', 'Lebon', 55000)
    employeeManager2 = employee_manager.Employee_manager('Jane', 'Seymour', 62000)

    employeeManager1.add_employee(employee1)
    employeeManager1.add_employee(employee2)
    employeeManager1.add_employee(employee3)
    employeeManager2.add_employee(employee4)
    employeeManager2.add_employee(employee5)
    employeeManager2.add_employee(employee6)


    senior_manager1 = employee_manager.Employee_manager('David', 'Bowie', 92000)
    senior_manager1.add_employee(employeeManager1)
    senior_manager1.add_employee(employeeManager2)

    senior_manager1.pay_employee()

if __name__ == '__main__':
    main()
