
class Person:
    id = 100000
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Person.id += 1
        self.person_id = Person.id

    def __str__(self):
        return 'Name={firstname} {lastname}, id={id}'.format(
            firstname=self.firstname,
            lastname=self.lastname,
            id=self.person_id)
<<<<<<< HEAD

    def get_id(self):
        return self.person_id
=======
>>>>>>> 76b3ca6fd2ca7ddf2b740652394bfcc5e177adf2
