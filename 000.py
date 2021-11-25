from datetime import datetime

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

print(now.year)
print(now.month)
print(now.day)
print(now)

print("%02d/%02d/%04d" % (now.month, now.day, now.year))
print("%02d:%02d:%04d" % (now.hour, now.minute, now.second))

from time import sleep


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am a {self.name} and I am a {self.age} years old")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Super tar den overnevnte Pet class'en
        self.color = color

    def speak(self):
        print("meow")

    def show(self):
        print(
            f"I am a {self.name} and I am a {self.age} years old and i am {self.color}"
        )


class Dog(Pet):
    def speak(self):
        print("bark")

    def show(self):
        print(f"I am a {self.name} and I am a {self.age} years old")


class Fish(Pet):
    def speak(self):
        print("Blub Blub")

    def show(self):
        print(f"I am a {self.name} and I am a {self.age} years old")


p = Pet("Tim", 12)
p.show()
sleep(2)
c = Cat("Snupi", 19, "Red")
c.speak()
sleep(1)
c.show()
sleep(2)
d = Dog("Enzo", 4)
d.speak()
sleep(1)
d.show()
sleep(2)
f = Fish("Bubbles", 2)
f.speak()
sleep(1)
f.show()
