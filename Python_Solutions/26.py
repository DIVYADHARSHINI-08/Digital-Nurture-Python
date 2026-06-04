def area_of_rectangle(length,width):
    area = length*width
    return area
length = 5
width = 3
if length < 0 or width < 0:
    print("Length and width cannot be negative.")
else:
    area = area_of_rectangle(length,width)
    print(f"The area of the rectangle with length {length} and width {width} is: {area}")