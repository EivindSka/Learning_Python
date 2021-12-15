

# # prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class that contains one or more abstract methods
# abstract class = a method that has a declaration but does not have a implementation

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod     # will prevent it
    def go(self):       # and forces subclasses to define "go"
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print('You drive to the car')

    def stop(self):
        print('This car is stopped')


class Motorcycle(Vehicle):
    def go(self):
        print('You ride the motorcycle')

    def stop(self):
        print('This motorcycle is stopped')


car = Car()
motorcycle = Motorcycle()

motorcycle.go()
car.go()
motorcycle.stop()
car.stop()
