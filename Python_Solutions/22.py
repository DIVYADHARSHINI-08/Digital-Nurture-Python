def Salary(base, bonus): #Function to calculate total salary
    total_salary = base + bonus #Calculate total salary by adding base and bonus
    return total_salary #Return the total salary
base = float(input("Enter the base salary: "))  #Get the base salary from user input and convert it to a float
bonus = float(input("Enter the bonus amount: ")) #Get the bonus amount from user input and convert it to a float
total_salary = Salary(base,bonus) #Call the Salary function with the base and bonus values and store the result in total_salary
print(f"Total Salary: {total_salary}")  #Print the total salary using an f-string for formatting