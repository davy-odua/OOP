#super = A function which enables a child class to inherit the methods of a parent class(super)
#        It extends the functionality of the methods.
import math
pi = 3.14

class Shapes:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is a {self.color} and is {"filled" if self.filled else "not filled" } ")


class Circle(Shapes):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of { pi * self.radius * self.radius  }cm^2 ")
        super().describe()

class Triangle(Shapes):
    def __init__(self, color, filled, base, height):
        super().__init__(color, filled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {1/2 * self.base * self.height}cm^2 ")
        super().describe()




class Square(Shapes):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of { self.width * self.width}cm^2 ")
        super().describe()


circle = Circle("red", False, 5)
triangle = Triangle("yellow", False, 10, 15)
square = Square("orange", False, 20)



# circle.describe()
# print("")
# triangle.describe()
# print("")
# square.describe()






