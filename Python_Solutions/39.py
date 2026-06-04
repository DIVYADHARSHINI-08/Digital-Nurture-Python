class Employee:
    def work(self):
        pass
class Manager(Employee):
    def work(self):
        print("Managing the team and overseeing projects.")
class Developer(Employee):
    def work(self):
        print("Writing code and developing software.")
list_employees = ["Manager","Developer"]
for employee in list_employees:
    if employee == "Manager":
        emp = Manager()
        emp.work()
    elif employee == "Developer":
        emp = Developer()
        emp.work()      
    else:
        print("Unknown employee type.")