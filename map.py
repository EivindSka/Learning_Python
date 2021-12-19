# map() = applies a function to each item in an iterable (list, tuple, etc)

# map(functiom, iterable)

store = [('shirt', 20.00),
         ('pants', 30.00),
         ('jacket', 45.00),
         ('socks', 5.00)]


def to_euro(data): return (data[0], data[1]*0.82)
def to_dollar(data): return(data[0], data[1]/0.82)


store_dollar = list(map(to_dollar, store))

for i in store_dollar:
    print(i)
