

class Organism:

    alive = True


class Animal(Organism):

    def eat(self):
        print('This animal is eating')


class Fish(Animal):

    def speak(self):
        print('This fish is making bubbles')


f = Fish()

f.speak()


# Fish has a parent that has a parent
