#polymorphism = Means to have many forms
#              Poly = Means many
#              Morphe = means form

#WAYS IN WHICH WE CAN ACHIEVE POLYMORPHISM
#1. Inheritance = A child class inheriting the attributes of a parent class
#2. Duck typing

from abc import ABC, abstractmethod  # abstract method = A method which can only be used by children classes.

class Shapes:
    @abstractmethod
    def __init__(self):

    def area(self):




class Circle(Shapes):
    pass

class Triangle(Shapes):
    pass

class Square(Shapes):
    pass






