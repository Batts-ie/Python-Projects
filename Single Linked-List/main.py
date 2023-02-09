import os
import time
import LinkedList

import concurrent.futures as multiproc


def create_random_values(rlenght=100):
    import random
    values = []
    for i in range(rlenght):
        values.append(random.randint(0, 10000))
        return values


def l_output(time, text, olist):
    print(" ")
    print(text + str(time))
    olist.output()


def maintesting(unn=1):
    pass
    messungen = {}
    llist = LinkedList.LinkedList
    perf_time = time.perf_counter()
    val = create_random_values(100000)
    perf_time = time.perf_counter() - perf_time
    print("Basic Values have been created! Performance-Time: " + str(perf_time))
    # add ll
    perf_time = time.perf_counter()
    llist.append(val)
    perf_time = time.perf_counter() - perf_time


if __name__ == "__main__":
    print(maintesting())
