#a simple program to return the largest number
from operators import numbertwo

def largest(num1, num2, num3):
    large=int
    if(num1<num2):
        large=num2
    elif(large<num3):
        large=num3
    return large



numberone=int(input("Enter the first number:"))
numbertwo=int(input("Enter the second number:"))
numberThree=int(input("Enter the third number:"))

largestNumber=largest(numberone, numbertwo, numberThree)
print(largestNumber)
