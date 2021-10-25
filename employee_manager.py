import employee
import senior_manager
import additional_functions

class Employee_manager(additional_functions.AdditionalFunctions):
    employees = []

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = float(salary)
        self.subordinates = []
        senior_manager.SeniorManager.managers.append(self)

    def add_employee(self, employee: employee):
        Employee_manager.employees.append(employee)

    def remove_employee(self, employee: employee):
        Employee_manager.employees.remove(employee)

    def pay_employee(self):
        for employee in Employee_manager.employees:
            employee.pay()

    def display_subordinates(self):
        subordinates = 'The employees who report to {} {} are: \n'.format(self.firstname, self.lastname)
        for subordinate in self.subordinates:
            subordinates += '{}\n'.format(subordinate.__str__())
        return subordinates











