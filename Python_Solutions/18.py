def first_even_num(start,end):
    for i in range(start , end+1):
        if i%2==0:
            return i
            break
start = int(input("Enter the starting number:"))
end = int(input("Enter the ending number:"))
result = first_even_num(start,end)
print(f"The first even number between {start} and {end} is: {result}")