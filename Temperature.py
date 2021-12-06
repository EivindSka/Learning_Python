
import time
from typing import ValuesView

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


# # Lists
# #          0          1           2          3
# food = ["Pizza", "Hamburger", "Hot Dawg", "Pasta"]

# food.append("Sushi")
# food.remove("Pasta")
# # Will remove the last index of the list
# food.pop()
# # Replaces index 1 with Tikkamasala
# food.insert(1, "Tikkamasala")
# food.sort()
# # Will remove every value in the list
# food.clear()

# print(food[1:3])

# for x in food:
#     print(x)


# utensils = {"fork", "spoon", "knife"}   # set, unordered, and unindex
# dishes = {"bowl", "plate", "cup": 20}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.update(dishes)

# dinnertable = utensils.union(dishes)

# for x in dinnertable:
#     print(x)


#           Key         Value
# capitals = {"USA": "Washington DC",
#             "India": "New Dehli",
#             "China": "Beijing",
#             "Russia": "Moscow"}

# capitals.update({"Germany": "Berlin"})

# capitals.pop("China")                 Vil fjerne paret
# print(capitals["Germany"])
# print(capitals.get("Germany"))        Check if the key is in the dictionary
# print(capitals.keys())                Countries
# print(capitals.values())              Capitals
# print(capitals.items())               Vil printe parene

# for key, value in capitals.items():
#     print(key, value)


# def say_hi(first_name, last_name, age):
#     # F-string gjør det lettere å legge inn parmetre
#     print(f"Hello, {first_name} {last_name}")
#     # print("Hello, " + first_name + " " + last_name)     # "Alternativ måte" med samme utfall
#     print(f"You are {age} years old ")


# say_hi("Eivind", "Skårnes", 22)


# def multiply(number1, number2):
#     return number1 * number2


# x = multiply(6, 8)
# print(x)
