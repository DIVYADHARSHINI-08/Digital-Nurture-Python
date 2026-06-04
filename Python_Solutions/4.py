def NetSalary(salary, tax):
    net_salary = salary * (1 - tax)
    return net_salary

salary = float(input("Enter your gross salary: "))
tax = float(input("Enter the tax rate (as a decimal): "))
net_salary = NetSalary(salary,tax)
print(f"Net Salary: {net_salary} ") 