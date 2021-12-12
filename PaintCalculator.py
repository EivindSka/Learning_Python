
print("Paint Calculator")
print('Enter a wall size as width, height in feet or press enter to stop')
print('Example 12,2')

# Variables

walls = []  # List of walls
litres = 1 / 6  # One litre covers 6sq metre of walls
total = 0

# Get input

while True:
    s = input('Enter a wall size: ')
    if len(s) == 0:
        break

    # Verify input
    m3 = s.split(',')
    if len(m3) < 2:
        print("Invalid Format!")
        break

    # Convert str to int
    w = int(m3[0])
    h = int(m3[1])
    item = [w, h]
    walls.append(item)
    print(f'Adding wall: {item}')

# Calculate the numbers
print(f'You entered {walls}')
for m in walls:
    w = m[0]
    h = m[1]
    c = w * h
    v = c * litres
    total += v

print(
    f'You need to buy {round(total,2)} litres of paint for the first layer\n and another {round(total,2)} for the second layer')
