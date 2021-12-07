
# for _ in range(5):          # Python makes its own variable
#     print("Hello")


# // Some Namestuff //
# def test_decorator(func):
#     print("before")
#     func()
#     print("after")


# @test_decorator
# def do_stuff():
#     print("Doing stuff")


# def makeBold(func):
#     def inner():
#         print("<b>")
#         func()
#         print("</b>")
#     return inner


# @makeBold       # Decoator
# def printName():
#     print("Eivind Skårnes")


# printName()


# // Number Division //

def numCheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print("Can not divide by zero")
                return False
            return True
        print(f'{o} is not a number')
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)
    return inner


@numCheck
def divide(x, y):
    print(x / y)


i1 = input('What two numbers do you wish to divide? example "10 , 5" ')
listIn = i1.split(',')
print(listIn[0], listIn[1])
x = int(listIn[0])
y = int(listIn[1])
divide(int(listIn[0]), int(listIn[1]))
# divide(x, y)        # Easier version of the one above


# // Some other stuff //

# x = False
# y = True
# print('Equal: {x == y}')      # Are they Equal?
# print('Not Equal: {x != y}')  # Are they Not Equal?


# def outline(func):
#     def inner(*args, **kwargs):
#         print('~'*20)
#         func(*args, **kwargs)
#         print('~'*20)
#     return inner


# def list_items(func):
#     def inner(*args, **kwargs):
#         func(*args, **kwargs)
#         print(f'args = {args}')
#         print(f'kwargs = {kwargs}')
#         for x in args:
#             print(f'arg = {x}')
#         for k, v in kwargs.items():
#             print(f'key={k}, value={v}')
#     return inner


# @outline
# @list_items
# def display(msg):
#     print(msg)


# display('Hello World')


# @outline
# @list_items
# def birthday(name='', age=0):
#     print(f'Happy birthday {name} you are {age} years old')


# birthday(name="Eivind", age=22)
