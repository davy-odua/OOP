#Multiple inheritance = Where a child class inherits from more than one parent class.
#                      A(B, C)
#Multilevel inheritance = Where a child class inherits from a parent class which also inherits from another parent class.
#                         C(B) <- B(A) <- A

#Multiple Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

class Rabbit(Prey):
    pass



hawk = Hawk("Bird")
fish = Fish("Tilapia")
rabbit = Rabbit("Rabbit")

print(f"This is a {hawk.name}")
print(f"This is a {fish.name}")
print(f"This is a {rabbit.name}")

print(" ")

hawk.hunt()
fish.hunt()
fish.flee()
rabbit.flee()

print("")

hawk.sleep()
fish.sleep()
rabbit.sleep()



