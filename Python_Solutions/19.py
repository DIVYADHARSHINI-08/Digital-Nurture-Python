def OddCount(num):
    count = 0
    for i in range(1,num+1):
        if i%2==0:
            continue
        else:
            count +=1
    return count
num = 10
odd_count = OddCount(num)
print(f"The count of odd numbers from 1 to {num} is: {odd_count}")