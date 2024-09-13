"""Operator	Method
+	__add__ (self, other)
-	__sub__ (self, other)
/	__truediv__ (self, other)
*	__mul__ (self, other)
<	__lt__ (self, other)
>	__gt__ (self, other)
==	__eq__ (self, other)"""
"""class Shape():
    sname = 'SHAPE'
    def getName(self):
        return self.sname

class XShape(Shape):
    def __init__(self,name):
        self.xsname = name

    def getName(self):  # overriden method
        return (super().getName()+ self.xsname)


a = Shape()
print(a.getName())
b = XShape('asa')
print(b.getName())"""
class Animal:
    def __init__(self, name ,sound):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print("Name:",self.name)
        print("Sound:",self.sound)

class Dog(Animal):
    def __init__(self, name, family, sound ='Wof-Wof'):
        super().__init__(name,sound='Wof-Wof')
        self.family = family
    def Animal_details(self):
        super().Animal_details()
        print("Family:",self.family)

class Sheep(Animal):
    def __init__(self, name, color, sound ='Ba-Ba'):
        super().__init__(name,sound='Ba-ba')
        self.color = color
    def Animal_details(self):
        super().Animal_details()
        print("Color:",self.color)

d = Dog("Pongo", "Husky")
d.Animal_details()
print(" ")
s = Sheep("Billy", "White")
s.Animal_details()
