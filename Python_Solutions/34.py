def nested_dict(dict):
    for emp_id, details in dict.items():
        if details["name"] == "":
            print(emp_id, "-> Invalid Name")
        elif details["Department"] == "":
            print(emp_id, "-> Invalid Department")
        elif details["Salary"] <= 0:
            print(emp_id, "-> Invalid Salary")
        else:
            print(emp_id, "-> Valid Employee")
    
    for key,value in dict.items():
        print(f"{dict[key]['name']} :{dict[key]['Salary']}")
        
dict = {"emp1" : {"name" : "Divi", "Department" : "IT", "Salary" : 1000000}, 
        "emp2" : {"name" : "Ravi", "Department" : "HR", "Salary" : 800000}}
nested_dict(dict)