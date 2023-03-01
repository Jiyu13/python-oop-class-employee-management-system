class Employee:

    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.name = emp_name
        self.id = emp_id
        self.salary = emp_salary
        self.department = emp_department

    def calculate_salary(self, salary, hour_worked):
        overtime = 0
        if hour_worked > 50:
            overtime = hour_worked - 50
        self.salary += overtime * (salary / 50)
        return self.salary

    def assign_department(self, new_department):
        self.department = new_department
        return self.department

    def print_employee_details(self):
        print(f"Name: {self.name}; Salary: {self.salary}; Department: {self.department}")
        print("----------------------")


employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

# Change the departments of employee1 and employee4
employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")


# Now calculate the overtime of the employees who are eligible:
employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)


print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()