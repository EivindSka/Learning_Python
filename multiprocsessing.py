
# running multiple tasks in paralell on different cpu cores, better for cpu bound tasks

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count)

    a = Process(target=counter, args=(50000000,))
    b = Process(target=counter, args=(50000000,))

    a.start()
    b.start()

    a.join()
    b.join()

    print(f'Finished in {time.perf_counter()} seconds')


if __name__ == '__main__':
    main()
