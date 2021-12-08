
str = "Hello World, this is what we call a string!"

print(len(str))                         # Get the length of the string
print(str.replace("Hello", 'Hola'))     # Will replace "Hello" with "Hola"
# Will make the string in to two strings from the ","
print(str.split(","))                   # Check if the string start with "H"
print(str.startswith("H"))              # Check if the string ends with "!"
print(str.endswith("!"))
print(str.upper())                      # Will make the whole string uppercase
print(str.lower())                      # Will make the whole string lowercase
# Will make the first letter of the string uppercase
print(str.capitalize())

# // Slicing - or getting substring //

# Will print the first 5 letters of the string
print(str[0:5])
# Will print all the letters after index 6
print(str[6:])

# // Index - the position of //

l = ","
c = str.find(l)
print(f'Find returned {c}')             # Will tell what index the "," is

i = str.index(l)
print(f'Find returned {i}')             # Will tell what index the "," is


# Will print everything up till the "l" aka the "i"
x = str[:i]
print(x)


# // Lists []

z = ['Eivind', 'Ørjan', 22]             # Can mix datatypes
print(f'List: {z}')                     # Will print the list
print(f'Lenght: {len(z)}')              # Will print the lenght of the list


# // Index and positioning - Zero based //

print(f'Zero: {z[0]}')                  # First item is ZERO
print(f'Slice: {z[1:2]}')               # Slice the list

# // Adding Items - append, insert //
z.append('Years')                       # Will add at the end
z.append('Old')                         # Will add at the end
z.insert(1, 'Flamingos')                # The first number specifies where
print(f'List: {z}')


# // Remove Items - remove, pop, delete //
z.remove('Flamingos')                   # Will remove 'Flamingo'
print(f'List: {z}')

i = z.index('Ørjan')                    # Will raise error if not found
print(f'Brother: {z.pop(i)}')           # Will remove and return item
print(f'List: {z}')

i = z.index("Old")                      # Will raise error if not found
del z[i]                                # Delete item w.o return item
print(f'List: {z}')


# // Extending - Adds elements from another list //
y = ['Cats', 'Fish', 'Flamingo']
z.extend(y)                             # Will add y to z list
print(f'Extended: {z}')


# // Sort - sort , reverse //
z.remove(22)
z.sort()                                # Will raise error if mixed types
print(f'Sort: {z}')                     # Will sort alphabetically
z.reverse()
print(f'Reverse: {z}')                  # Will sort reverse alphabetically


# // Copy //
æ = z.copy()                            # Copies elements into new list
æ.reverse()
æ.append('Eggs')
print(f'Original: {z}')
print(f'New: {æ}')

# // Delete the whole thing //
del æ                                   # Simply deletes the whole variable / list
# print(æ)

# // Clear //
z.clear()                               # Clear the whole thing
print(f'Cleared: {z}')                  # Will show a cleared list of the
print(f'Lenght: {len(z)}')              # Will print how many idexes is filled


# // List can contain other lists //
a = []
b = [1, 2, 3]
c = ['Eivind', 'Ørjan']
a.append(b)
a.insert(0, c)                          # Will insert c to index 0

print(f'List: {a}')
print(f'Len: {len(a)}')
print(f'0: {a[0][0]}')                  # First value is the list index
print(f'1: {a[1][1]}')                  # Second value is index in the list


# // Change items - positioning //
x = [1, 2, 3, 4, 5]
x[2] = 'TEST'                           # Will assign different value to index 2
print(x)


# // Sets {} //
s = {1, 2, 2, 2, 3, 4, 5}               # Will not have duplicates
print(s)

l = ['Eivind', 'Ørjan', 22]
s = set(l)
print(s)

# // Adding items to sets //

s.add('Hello')                          # Will simply add to the set
s.update([1, 2, 3, 'Hello'])            # Will also add
print(s)                                # Removed duplicates

# // Removing items from sets //
s.discard('Hello')                      # Perfect way of doing it
s.remove(1)                             # Error if not present
v = s.pop()                             # Removes and gives it to you
print(s)

# // Can not change items - remove and add
# s[0] = 'A'     'Error'                # Does not support indexing
# print(s[0])    'Error'
# print(3 in s)                         # This will say True or False
s.remove(3)
s.add(12)
print(s)

x = set('abcd')
y = set('cdefg')

s = x.union(y)                          # All elements in either set
print(f'Union: {s}')


s = x.intersection(y)                   # All elements in both sets
print(f'Intersection: {s}')             # Common elements ^

s = x.difference(y)                     # All elements in x but not y
print(f'Difference: {s}')

s = x.symmetric_difference(y)           # All the elements in one of the sets
print(f'Symmetric: {s}')


# // Tuple - Can not be modified //
t = (1, 2, 3, 4)
print(t)

print(f'Index: {t[0]}')
print(f'Slice: {t[2:]}')
print(f'Bool: {3 in t}')

(x, y, z) = (1, 2, 3)
print(x)
print(y)
print(z)

(x, y, z) = range(1, 4)
print(x)
print(y)
print(z)


# // Dictionary {k:v, k:v} //
d = {'pet': 'dog', 'age': 5, 'name': 'Sport'}
print(d)

d = dict(pet='dog', age=5, name='Sport')
print(d)


print(f'Items: {d.items()}')
print(f'Keys: {d.keys()}')
print(f'Values: {d.values()}')


print(f'Name: {d["name"]}')

# Adding items
d['trick'] = 'sit'
print(d)
d['trick'] = 'roll over'
print(d)

# Remove items                         # When delete key
del d['trick']                         # Will remove k and v
print(d)


# Testing for existence
if 'name' in d:
    print(d['name'])

# Looping
for key in d.keys():
    print(f'{key} = {d[key]}')
