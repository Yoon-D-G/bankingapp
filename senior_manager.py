import employee_manager
import person

class SeniorManager:
    managers = []

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = float(salary)

    def promote(self, employee):
        employee_manager.Employee_manager(employee.firstname, employee.lastname, employee.salary * 2)
        if employee.manager:
            employee.manager.subordinates.remove(employee)
        del employee

    def allocate_employee_to_manager(self, employee_manager, employee):
        employee_manager.subordinates.append(employee)
        employee.manager = employee_manager

    def display_employee_managers(self):
        managers = ''
        for manager in SeniorManager.managers:
            managers += manager.__str__() + '\n'
        return managers

    def display_all_employees(self):
        employees = ''
        for employee in employee_manager.Employee_manager.employees:
            employees += employee.__str__() + '\n'
        return employees








