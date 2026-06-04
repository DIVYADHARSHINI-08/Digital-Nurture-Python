def length_of_string(string):
    if string == "":
        print("The string is empty.")
    else:
        length = len(string)
    return length
string = input("Enter a string: ")
length = length_of_string(string)
print(f"The length of the string is: {length}")