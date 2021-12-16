
foods = list()

while True:
    food = input('What foods do you like?: ')
    if food == 'quit':
        break
    foods.append(food)

# // Can be written like this vv //

foods = list()
while food := input('What food do you like? ') != 'quit':
    foods.append()
