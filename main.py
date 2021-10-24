import customer_manager
import employee_manager

def main():
    customer1 = customer_manager.Customer('Ewen', 'Garrod', 1000, 123456, 'current')
    print(customer1.status())
    customer1.withdraw(100)
    print(customer1.status())
    employee1 = employee_manager.Employee_manager("Jon", "Bonham", 654321, 35000)
    employee2 = employee_manager.Employee_manager("Jimmy", "Page", 654322, 27000)
    employee3 = employee_manager.Employee_manager("Robert", "Plant", 654323, 27000)
    employee4 = employee_manager.Employee_manager("John-Paul", "Jones", 654324, 27000)
    print(employee1.pay_salary())
    print(employee1.pension_contribution(0.03))
    employee1.add_to_line_manager(employee2)
    employee1.add_to_line_manager(employee3)
    employee1.add_to_line_manager(employee4)
    print(employee1.display_line_manager_group())

if __name__ == '__main__':
    main()
