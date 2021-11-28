phonebook = ["Ahmed", "Davis", "Damian", "Joe", "Joffery", "John", "Dickens", "David"]
target = "David"

for element in phonebook:
    if element == target:
        print("I found him!")
        break

else:
    print("David is not in the phonebook")

phonebook.append("Julian")
phonebook.remove("David")

for element in phonebook:
    if element == target:
        print("I found him")
        break
else:
    print("David is not in the phonebook")

print(phonebook)
phonebook.remove("Davis")
print(phonebook)
