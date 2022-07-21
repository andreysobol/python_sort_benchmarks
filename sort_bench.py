import random
import time

def get_random_list(size):
    return [random.randint(0, 2**32) for i in range(size)]

def calc_time(size):
    lst = get_random_list(size)
    start = time.time()
    try_sort(lst)
    end = time.time()
    return end - start

def try_sort(lst):
    lst.sort()

def print_time():
    sized = range(28)
    for i in sized:
        print("{} ({}): {}".format(i, 2**i, calc_time(2**i)))

print_time()
