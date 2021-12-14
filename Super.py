

# // How Super() method works //

class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width


class Square(Rectangle):

    def __init__(self, lenght, width):
        super().__init__(lenght, width)
# super method will take the __init__ from parent class

    def area(self):
        return self.lenght * self.width


class Cube(Rectangle):

    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height
# super method will take the __init__ from parent class
# but we add self.height because the parent class does not have it

    def volume(self):
        return self.height * self.width * self.height


square = Square(3, 3)
cube = Cube(4, 5, 6)

print(square.area())
print(cube.volume())
