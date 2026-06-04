from math import *
def func(num):
    squareroot = sqrt(num)
    power = pow(num,2)
    PI = pi
    return squareroot, power, PI
num = float(input("Enter a number: "))
if num < 0:
    print("Cannot calculate square root of a negative number.") 
else:
    squareroot, power, PI = func(num)
    print(f"Square root of {num} is: {squareroot}")
    print(f"{num} raised to the power of 2 is: {power}")
    print(f"The value of PI is: {PI}")