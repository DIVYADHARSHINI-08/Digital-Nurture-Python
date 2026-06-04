import csv

employees = []

try:
    # Read CSV file
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        employees = [row for row in reader]

    for emp in employees:
        emp["Salary"] = int(emp["Salary"])

    high_salary_employees = [
        emp for emp in employees if emp["Salary"] > 50000
    ]

    total_salary = sum(emp["Salary"] for emp in employees)
    average_salary = total_salary / len(employees)

    print("----- Employee Data -----")
    for emp in employees:
        print(emp)

    print("\n----- Employees with Salary > 50000 -----")
    for emp in high_salary_employees:
        print(emp)

    print(f"\nAverage Salary: {average_salary}")

except FileNotFoundError:
    print("Error: employees.csv file not found.")

except Exception as e:
    print("Error:", e)