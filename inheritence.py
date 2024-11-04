#here is more about the inheritance
#class of animal
class animal:
    def __init__(self, name):
        self.name = name

    #here is the method for the animal that move
    def move(self):
        print('animal is moving')


#here is another class of the child class

class dog(animal):

    #this is more about polymorphism act
    def move(self):
        print('dog is moving')

    def bark(self):
        print('dog is barking')



#here is now creating the object

