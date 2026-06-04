def multiple(x,y):
    if(x<0 or y<0):
        print("Please enter positive values.")
    else:
        print(x)
        print(y)
x,y = map(int,input("Enter the values :").split())
multiple(x,y)