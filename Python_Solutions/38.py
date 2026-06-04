class Employee:
    def __init__(self,name):
        self.name = name
        self.salary = 0
    def set_salary(self,salary):
        if salary < 0:
            print("Salary increase cannot be negative.")
        self.salary += salary
        return self
    def raise_salary(self,raise_amount):
        if raise_amount < 0:
            print("Salary raise cannot be negative.")
        self.salary += raise_amount
        return self
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

emp1 = Employee("Divi")
emp1.set_salary(50000).raise_salary(5000).display()