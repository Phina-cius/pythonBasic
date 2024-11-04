#this is we call the method overloarding


#representation in many forms
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def shape(self):
        print('draw a rectangle')



#here is another class for the rhombus
class rhombus:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def shape(self):
        print('draw a rhombus')


#here is the class for the parallologram
class parallelogram:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def shape(self):
        print('draw a parallelogram')



