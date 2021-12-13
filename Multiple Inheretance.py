

class Prey:

    def flee(self):
        print('This animal is fleeing')


class Predator:

    def hunt(self):
        print('This animal is hunting')


class Lion(Predator):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


l = Lion()
h = Hawk()
f = Fish()

f.flee()
f.hunt()
h.hunt()
l.hunt()
