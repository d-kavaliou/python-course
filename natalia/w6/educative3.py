# Challenge 1: Override a Method Using the Super Function

class Shape:
    sname = "Shape"

    def getName(self):
        return (self.sname) # ???


class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return (super().getName() + ", " + self.xsname)
    
square = XShape('Square')
print(square.getName()) 

circle = XShape('Circle')
print(circle.getName())


# Challenge 2: Implement an Animal Class

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def Animal_details():
        print('Name: ' + self.name)
        print('Sound: ' + self.sound)
        
class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def Animal_details():
        super().Animal_details()
        print('Family: ' + self.family)

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details():
        super().Animal_details()
        print('Color: ' + self.color)