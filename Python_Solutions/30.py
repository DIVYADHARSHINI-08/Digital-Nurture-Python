def expection(num1,num2):
    try:
        div = num1/num2
        print(f"The result of {num1} divided by {num2} is: {div}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
expection(num1,num2)