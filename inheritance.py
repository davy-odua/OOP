#inheritance = Where a child class obtains attributes(variables) and methods (functions) from a parent class.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Boss", 3)
cat = Cat("Mickey", 4 )
mouse = Mouse("Jerry", 5)

print(f"{dog.name} is {dog.age} years old ")
print(f"{cat.name} is {cat.age} years old")
print(f"{mouse.name} is {mouse.age} years old ")
print("")
dog.sleep()
cat.sleep()
mouse.sleep()

