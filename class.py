#working with polymorphism

#creating the parrent class this part we are implementiing the what we call the method overiding
class animal:
       def sound(self):
           pass




#creating a method to overide animal
class dog(animal):
    def sound(self):
        print('barks')


#this one is for a cat
class cat(animal):
    def sound(self):
        print('meous')


#creating an instance
animal = [dog(), cat()]

for i in animal:
    print(i.sound())
