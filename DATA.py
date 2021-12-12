# Pakcing and Unpacking data


# Pakcing


def pack(*nums):
    print(f'Packed: {nums}')
    for x in nums:
        print(f'Packed {x}')


pack(1, 2, 3)


# Unpacking

def unpack(a, b, c):
    print(f'Unpack')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')


num = [1, 2, 3]
unpack(*num)            # * = Packing or Unpacking

# // Dictionary issue

d = dict(name='Eivind', age=22, car='Tesla')
print('Packing dictionary')
pack(*d)

print('Unpacking dictionary')
unpack(*d)

# Packing dictionary


def packdict(**nums):
    print(f'nums = {nums}')
    for k in nums:
        print(f'Packed: {k} = {nums[k]}')


packdict(name='Eivind', age=22, car='Tesla')


# Unpack Dic
def unpackdict(name, age, car):
    print('Unpacked dictionary')
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'car = {car}')


unpackdict(**d)
