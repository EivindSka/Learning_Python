
# // Functions And Scope //

# // Global Scope
name = 'Eivind Skårnes'

# // Functions to acsess global scope


def test1():
    print(f'My name is {name}')


test1()

# // Global Scope can not access function scope
x = 10                          # Global Scope
# Name Collision


def test2():
    x = 50                      # Func Scope
    print(f'Func scope {x}')


test2()
print(f'Global Scope {x}')


# // Global > Function > Statement //

x = 15
############################
print(f'Global x: {x}')


def test3():
    x = 0
    print(f'Function x: {x}')
    for i in range(3):
        x += 1
        y = x * i
        print(f'Statement x: {x}')
        print(f'Statement y: {y}')
    print(f'Function x: {x}')
    print(f'Function y: {y}')


test3()
print(f'Global {x}')


# // Func Do not share scope
def cats():
    z = 1


def dogs():
    z = 3

# // Func can share values


def numbers(steps):
    l = range(1, 20, steps)
    for i in l:
        print(i)
    return l


def lotto():
    z = numbers(3)
    for x in z:
        print(f'Lucky Number {x}')


lotto()
