# deamon thread runs in backgroun, program will not wait for thuis
# non-deamon threads will not be killed an dstays alive untill program is complete

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f'logged in for: {count} seconds')


x = threading.Thread(target=timer)      # can use ',deamon=True'
x.setDaemon(True)
# if 'deamon=True' does not exist the counter will not stop and program keeps on running
x.start()


answer = input('Do you wish to EXIT?')
