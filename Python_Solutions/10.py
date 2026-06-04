def convertion(age):
    age = int(age)
    if age < 0:
        print("Age cannot be negative.")
    else:
        print(f"Next year you will be :{age + 1}")

age = input("Enter your age:")
convertion(age)