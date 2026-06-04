def count(num):
    if num < 0:
        print("Please enter a non-negative number.")    
    count =  0
    for i in range(1,num+1):
        print(i,end=" ")
loop_count = count(5)

