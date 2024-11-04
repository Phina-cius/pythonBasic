from contextlib import redirect_stderr

from operators import numberone

roomTemp=25

currentTemp=int(input("please enter the temperature"))

if currentTemp<roomTemp:
    print("too cold")
elif currentTemp>roomTemp:
    print("too hot")
else:
    print("okay")


def smallestNumber(num1, num2, num3):
    rst = num1  # Start by assuming num1 is the smallest
    if num2 < rst:
        rst = num2  # Update rst if num2 is smaller
    if num3 < rst:
        rst = num3  # Update rst if num3 is smaller
    return rst

numberone = int(input("Enter a number: "))
numbertwo = int(input("Enter a number: "))
numberthree = int(input("Enter a number: "))
small = smallestNumber(numberone, numbertwo, numberthree)

print(f"The smallest number is: {small}")

