employees = [
("John", "IT", 50000),
("Jane", "HR", 45000),
 ("Mike", "IT", 60000),
 ("Sara", "Finance", 70000)
]

def unpack_employee_tuple(employees):
    name,department,salary = employees
    return not department == "IT"
    
employees_without_IT_department = list(filter(unpack_employee_tuple,employees))

print(employees_without_IT_department)

def employee_with_over_55000_earning(employees):
    name,department,salary = employees
    return salary > 55000
    
employee_with_over_55000_earning_list = list(filter(employee_with_over_55000_earning,employees))

print(employee_with_over_55000_earning_list)

