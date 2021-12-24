# Object Orientated Programming


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print('bark')

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog('Enzo', 12)
print(d.get_name())
d2 = Dog('Woofers', 23)
print(d2.name)
print(d2.get_age())

d.set_age(33)
print(d.get_age())
