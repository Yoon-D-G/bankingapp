
class AdditionalFunctions:
    def get_salary(self):
        return '{0:.2f}'.format(self.salary)

    def __str__(self):
        return 'Name: {firstname} {lastname}, Position: {position}, Salary: £{pay}\n'.format(
            firstname=self.firstname,
            lastname=self.lastname,
            position=self.__class__.__name__,
            pay=self.get_salary())