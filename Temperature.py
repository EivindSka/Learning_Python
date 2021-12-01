
import time

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello " + name)


# for i in range(10):
#     print(i+1)


# for i in range(50, 100+1, 5):
#     print(i)


# for i in "Eivind":
#     print(i)


# # Timer from 10

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("HAPPY NEW YEAR!!")


# # Nested Loops

# rows = int(input("How many rows?: "))
# colums = int(input("How many columns?: "))
# symbol = input("Enter a sybol to use: ")

# for i in range(rows):
#     for j in range(colums):
#         print(symbol, end="")
#     print()


# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break


# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")


# # Does not print 13 since it's passing it

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)


# Lists
#          0          1           2          3
food = ["Pizza", "Hamburger", "Hot Dawg", "Pasta"]

food.append("Sushi")
food.remove("Pasta")
# Will remove the last index of the list
food.pop()
# Replaces index 1 with Tikkamasala
food.insert(1, "Tikkamasala")
food.sort()

print(food[1:3])

for x in food:
    print(x)
