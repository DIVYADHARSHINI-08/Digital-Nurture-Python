import json
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary
        }

employees = {}
employees[101] = Employee(101, "Divya", "AI", 50000)
employees[102] = Employee(102, "Rahul", "HR", 45000)
employees[103] = Employee(103, "Sneha", "Development", 60000)
data = {}
for emp_id, emp in employees.items():
    data[emp_id] = emp.to_dict()

with open("emps.json", "w") as file:
    json.dump(data, file, indent=4)

print("Employee data saved to emps.json\n")

with open("emps.json", "r") as file:
    loaded_data = json.load(file)

loaded_employees = {}

for emp_id, emp_data in loaded_data.items():
    loaded_employees[emp_id] = Employee(
        emp_data["emp_id"],
        emp_data["name"],
        emp_data["department"],
        emp_data["salary"]
    )

print("Employee Details:\n")

for emp in loaded_employees.values():
    print(emp)

