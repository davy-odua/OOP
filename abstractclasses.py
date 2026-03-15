#Abstract class = A class which cannot be INSTANTIATED on its own = It must be a parent class to child classes.
#                 Its methods are only used by its child classes but not it.
#                 Its methods are only used by the child classes.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod

    def go(self):
        pass

    @abstractmethod

    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You are driving a car")

    def stop(self):
        print("You stop the car.")


class Motorcycle(Vehicle):
    def go(self):
        print("You are riding a motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):
    def go(self):
        print("You are sailing a boat")

    def stop(self):
        print("You anchor the boat")

car = Car()
motorcycle = Motorcycle()
boat = Boat()

car.stop()
motorcycle.stop()
boat.stop()




