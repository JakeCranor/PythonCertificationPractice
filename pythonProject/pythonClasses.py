# class Vehicle:
#     def __init__(self, body_type, make):
#         self.vehicle_body = body_type
#         self.vehicle_make = make
#
# car1 = Vehicle("jeep", 'toyota')
# print(car1.vehicle_body)
#
# car2 = Vehicle("truck", 'mercedes')
# print(car2.vehicle_body)
# print(type(car2))

# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""


# Your Code Below:
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Animal constructor called')

    def eat(self):
        print('Animal eat')

    def move(self):
        raise NotImplemented('Child class should be implemented here')


class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def move(self):
        print('Dog moves')


class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Fish moves')


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print('Bird moves')


myAnimal = Animal('Animal Friend', 20)
myAnimal.eat()
myDog = Dog('Doggy', 12)
myDog.eat()
myDog.move()
myFish = Fish('Fishy', 2)
myFish.eat()
myDog.move()
myBird = Bird('Birdy', 5)
myBird.eat()
myBird.move()
