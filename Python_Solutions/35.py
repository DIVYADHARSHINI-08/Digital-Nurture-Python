def validation(tuple1):
    if tuple1 == ():
        print("The tuple is empty.")
    for i in tuple1:
        if i < 0:
            print("Invalid value (negative number)")
    else:
        print("The Coordinates are valid.")
    
tuple1 = (10.5,20)
validation(tuple1)