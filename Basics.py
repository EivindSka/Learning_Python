from time import sleep
# x = True
# if x:
#     print('I am Running!')
# else:
#     print('I am Stopping!')


# x = 100
# y = 99
# if y == x:
#     print("They're Equal")
# if y != x:
#     print("They're not Equal")
# if y < x:
#     print("less than")
# if y > x:
#     print("larger than")
# if y <= x:
#     print("is equal to or greater")
# if y >= x:
#     print("is equal to or greater")


# x = 10
# if x == 25:
#     print("x = 25")
# elif x == 50:
#     print("x = 50")
# elif x == 75:
#     print("x = 75")
# elif x == 100:
#     print("x = 100")
# else:
#     print("This value is unknown!")


# x = 82
# if x > 50:
#     print("Over 50")
#     if x > 60:
#         print("Over 60")
#         if x > 70:
#             print("Over 70")
#             if x > 80:
#                 print("Over 80")
#                 if x > 90:
#                     print("Over 90")
#                     if x >= 100:
#                         print("Complete")

# // WHILE LOOP //

# x = 0
# while x < 10:
#     x += 1
#     print(f'x = {x}')
# sleep(1)
# print('Test 1 is done')

# Pass

# x = 0
# while x < 10:
#     pass
# print("Test 2 is done")

x = 0
while True:
    x += 1
    if x < 5:
        print(f'X < 5 {x}')
        continue
    print(f'Do something {x}')

    if x == 10:
        print(f'Exiting X = {x}')
        break

print('Complete')


# // For Loop and
# Range //

l = [1, 2, 3, 4]  # List
t = (1, 2, 3, 4)  # Tuple
s = {1, 2, 3, 4}  # Set

for i in s:
    print(f'i = {i}')


x = dict(Eivind=22, Ørjan=23, Ottar=65)
print(x)

for k in x.keys():
    print(f'Keys: {k} = {x[k]}')

for k, v in x.items():
    print(f'Items: {k} = {v}')

# // Range //
x = range(5)
print(x)
for i in x:
    print(f'Range: {i}')

# // Range start, stop and step //
x = range(5, 20, 3)

# while x < 20

print(x)
for i in x:
    print(f'Stepped: {i}')
