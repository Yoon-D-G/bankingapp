import person
class Employee(person.Person):

    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = float(salary)
        self.manager = None

    def pay(self):
        print('{} got paid'.format(self.firstname))

    def pension_contribution(self, pension_contribution_percentage):
        return float(self.salary) * pension_contribution_percentage

    def __str__(self):
        return super().__str__() + ', Salary=£{salary:,.2f}'.format(salary=self.salary)

