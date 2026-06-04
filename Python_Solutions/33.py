def updation(dict1,dict2):
    dict1.update(dict2)
    
dict1 = {"name" : "Divi", "age" : "20" }
dict2 = {"citu" : "Chennai", "Salary" : 1000000}
print("Dictionary before update:", dict1)
updation(dict1,dict2)
print("Dictionary after update:", dict1)