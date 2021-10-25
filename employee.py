import additional_functions
class Employee(additional_functions.AdditionalFunctions):
    id = 100000

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.employee_id = self.employee_id()
        self.salary = float(salary)
        self.manager = None

    def employee_id(self):  # I'd like this to only be accessed from within the constructor
        Employee.id += 1
        return Employee.id

    def pay(self):
        return '{} got paid'.format(self.firstname)

    def pension_contribution(self, pension_contribution_percentage):
        return float(self.salary) * pension_contribution_percentage

    def __str__(self):
        return 'Employee ID: {id}, Name: {firstname} {lastname}, Salary: £{pay}'.format(
            firstname=self.firstname,
            lastname=self.lastname,
            id=self.employee_id,
            pay=self.get_salary())

