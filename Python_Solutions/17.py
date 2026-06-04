def count(num):
    count = 0
    while num > 0:
        count +=1
        num -=1
    return count
loop_count = count(5)
print(f"Count from 1 to 5: {loop_count}")