
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # represent class obj in string
        return 'How you doin {}?'.format(self.name)


i1 = input('Whats your name? ')

user = User(i1)
print(user)
