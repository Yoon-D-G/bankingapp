import customer_manager
import employee_manager
import employee
import senior_manager


def main():
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

    senior_manager1 = senior_manager.SeniorManager('Christopher', 'Hitchens', 120000)

    senior_manager1.allocate_employee_to_manager(employeeManager1, employee1)
    senior_manager1.allocate_employee_to_manager(employeeManager1, employee2)
    senior_manager1.allocate_employee_to_manager(employeeManager1, employee3)
    senior_manager1.allocate_employee_to_manager(employeeManager2, employee4)
    senior_manager1.allocate_employee_to_manager(employeeManager2, employee5)
    senior_manager1.allocate_employee_to_manager(employeeManager2, employee6)

    print(employeeManager2.display_subordinates())

    employeeManager1.remove_employee(employee1)

    print(employeeManager1.display_subordinates())

    senior_manager1.promote(employee2)

    print(employeeManager1.display_subordinates())

    print(senior_manager1)

    print(senior_manager1.display_employee_managers())

if __name__ == '__main__':
    main()
