

# number = 0

# # for i in range(number):
# #     print(i*2)

# while number <= 10:
#     print(number)
#     number += 1
# else:
#     print('Loop Ended')


# while True:
#     for i in range(12):
#         print(i)


number = 0

# while number <= 10:
#     if number == 5:
#         break
#     number += 1
#     print(number)

for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    if n < 5:
        continue
    print(n)

while number <= 10:
    number += 1
    if number < 5:
        continue
    print(number)


def greet():
    print('Greetings!')


greet()
