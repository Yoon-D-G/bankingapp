class Employee_manager:
    def __init__(self, firstname, lastname, employee_id, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.employee_id = employee_id
        self.salary = salary
        self.line_manager_group = []

    def pay_salary(self):
        return self.salary

    def pension_contribution(self, pension_contribution_percentage):
        return float(self.salary) * pension_contribution_percentage

    def add_to_line_manager(self, employee_object):
        self.line_manager_group.append(employee_object)

    def display_line_manager_group(self):
        list = ''
        for employee_manager in  self.line_manager_group:
            list += '{firstname} {lastname}, ID: {employee_id}, Salary: £{salary}\n'.format(firstname=employee_manager.firstname,
                              lastname=employee_manager.lastname,
                              employee_id=employee_manager.employee_id,
                              salary=employee_manager.salary)
        return list


