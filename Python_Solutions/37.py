class Employee:
    def __init__(self,name,age,department):
        self.name= name
        self.age=age
        self.department=department
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

emp1 = Employee("Divi", 20, "IT")
emp1.display()
emp2 = Employee("Ravi", 25, "HR")
emp2.display()
emp3 = Employee("Priya", 30, "Finance")
emp3.display()