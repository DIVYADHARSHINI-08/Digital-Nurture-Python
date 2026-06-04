def maximum(salary):
    max_salary = max(salary)
    return max_salary

def minimum(salary):
    min_salary = min(salary)
    return min_salary

salary =  [50000, 75000, 62000, 95000]
highest_salary = maximum(salary)
lowest_salary = minimum(salary)
print(f"Highest Salary: {highest_salary}")
print(f"Lowest Salary: {lowest_salary}")