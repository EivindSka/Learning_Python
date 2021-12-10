
from functools import cache, lru_cache
import timeit
import datetime


@lru_cache(maxsize=3)
# @cache  # cache vil huske tall før og etter
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    for i in range(400):
        print(i, fib(i))
    print("Done!")


if __name__ == "__main__":
    main()


begin_time = datetime.datetime.now()

[4, 2, 3, 1, 5].sort()

print(datetime.datetime.now() - begin_time)
