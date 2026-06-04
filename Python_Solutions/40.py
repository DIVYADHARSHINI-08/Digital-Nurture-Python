class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    @classmethod
    def from_string(cls,string):
        name , salary = string.split(",")
        return cls(name,int(salary))
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
string =  "Shubh,75000"
emp = Employee.from_string(string)
emp.display()