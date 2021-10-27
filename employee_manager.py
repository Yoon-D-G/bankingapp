import employee
import senior_manager
import person

class Employee_manager(employee.Employee):

    def __init__(self, firstname, lastname, salary):
        super().__init__(lastname=lastname, salary=salary, firstname=firstname)
        self.subordinates = []
        senior_manager.SeniorManager.managers.append(self)

    def add_employee(self, employee: employee):
        self.subordinates.append(employee)

    def remove_employee(self, employee: employee):
        self.subordinates.remove(employee)

    def pay_employee(self):
        for employee in self.subordinates:
            employee.pay()

    def __str__(self):
        return super().__str__() + 'Num subordinates = {num}'.format(num=len(self.subordinates))











