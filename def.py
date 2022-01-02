

def greet(name, age=-1):
    print(f'Hello {name} how are you?')
    if age >= 0:
        print(f'I know your age = {age}\n')


greet('Alex', 22)
greet('Ørjan', 22)
