#object oriented programming
class person:

    #variable/properties/attribute
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #behavour or method or function
    def study(self):
        print("student is studying")


    def registration(self):
        print("student is registered")




#creating an object
student1=person("phinaacius",20,"male")
student1.study()
student1.registration()
print(student1.name)
print(student1.age)
print(student1.gender)


