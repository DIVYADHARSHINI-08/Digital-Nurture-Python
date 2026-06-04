import math
def area_of_circle(radius):
    area = math.pi*math.pow(radius,2)
    return area
radius = float(input("Enter the radius of the circle: "))
if radius < 0:
    print("Radius cannot be negative.")
else:
    area = area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is: {area}")