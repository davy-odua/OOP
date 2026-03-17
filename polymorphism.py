#polymorphism = Means to have many forms
#              Poly = Means many
#              Morphe = means form
from super import circle


#WAYS IN WHICH WE CAN ACHIEVE POLYMORPHISM
#1. Inheritance = A child class inheriting the attributes of a parent class
#2. Duck typing

from  abc import ABC, abstractmethod
import math

class Shapes:

    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(7), Square(5), Triangle(3, 2), Pizza("Pepperoni",7)]

for shape in shapes:
    print(f"The area is {shape.area()} cm^2")













