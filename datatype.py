"this is all about the data types"
from operator import truediv
from tkinter.font import names

name: str
number: int
salary: float
isPythonIntresting: bool

name= "phinacius"
number=34
salary=20000
isPythonIntresting=True
print(name)
print(number)
print(salary)
print(isPythonIntresting)



"data structures"  #multiple value store in single variable
"list and dictionaries"

"list is ordered and changable"

cars=["toyota","nissani","bmw","mercedece"]

print(cars[0])

"data strucute called a tuple"


"taple are ordered and unchangebale"
fruit=("banana","mango","maize","wow")

print(fruit[0])

"set they are unordered and unchangeble"

countries={"kenya","china","uganda","tanzani"}
print(countries)


"dictionary"

student={
    "firstname":"jane",
    "lastname":"doe",
    "age":25,
    "course":"programming",
    "gender":"female"

}

"printing the dictionary"
print(student["gender"])



"dertermining a datatype"

print(type(student))

print(type(student["firstname"]))
print(type(student["lastname"]))



"type casting"

print(float(12))

