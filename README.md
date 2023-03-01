### 1. Write a Python class Employee with attributes and methods
    emp_id, emp_name, 
    emp_salary, 
    emp_department,
    calculate_salary(),
    assign_department(),
    print_employee_details().

### 2. Sample Employee Data:
    "ADAMS", "E7876", 50000, "ACCOUNTING"
    "JONES", "E7499", 45000, "RESEARCH"
    "MARTIN", "E7900", 50000, "SALES"
    "SMITH", "E7698", 55000, "OPERATIONS"

### 3. Use 'assign_department' method to change the department of an employee.
### 4. Use 'print_employee_details' method to print the details of an employee.
### 5. Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
    overtime = hours_worked – 50
    Overtime amount = (overtime * (salary / 50))