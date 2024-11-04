#area is l*w
from variables import length


def areaOfRectangle(width, height):
    area = width * height
    return area

length=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))

#calling the area

print(areaOfRectangle(length,width))