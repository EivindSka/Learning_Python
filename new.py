

import random
t = (1, 2, 3, 4)

for x in t:
    print(x)


class Lotto:
    def __init__(self):
        self._max = 5

    def __iter__(self):
        for _ in range(self._max):
            yield random.randrange(0, 100)

    def setMax(self, value):
        self._max = value


print('-'*20)
lotto = Lotto()
lotto.setMax(20)  # how many numbers

for x in lotto:
    print(x)

print('-'*20)
