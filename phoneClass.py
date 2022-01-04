
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f'{self.brand} is calling {phoneNumber}')

    def __str__(self) -> str:
        return f'Brand = {self.brand} Price = {self.price}'


iphone = Phone('IPhone 13 Pro', 1500)
samsung = Phone('Samsung S20', 1400)

print(iphone.brand)                 # Properties
print(f'{iphone.price} Dollar')     # Properties
print(samsung.brand)                # Properties
print(f'{samsung.price} Dollar')    # Properties

iphone.call('978-846-236')            # Behavior
samsung.call('898-453-178')           # Behavior

print(iphone)
