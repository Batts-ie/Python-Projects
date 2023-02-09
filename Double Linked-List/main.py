import os
import time

import DLinkedList as LL

import concurrent.futures as multiproc


def create_random_values(rlength=100):
    import random
    values = []
    for i in range(rlength):
        values.append(random.randint(0, 10000))
    return values


def main():
    llist = LL.LinkedList()
    val = create_random_values()
    llist.adding_random(val)
    print("Linked-List: ")
    llist.output()
    print("Menu Linked-List: ")
    llist.menu()


def l_output(time, text, olist):
    print(" ")
    print(text + str(time))
    olist.output()


def maintesting(unn=1):
    messungen = {}
    llist = LL.LinkedList()
    perf_time = time.perf_counter()
    val = create_random_values(10000)
    perf_time = time.perf_counter() - perf_time
    print("Basic Values has been created! Performance Time:" + str(perf_time))
    # Llist add
    perf_time = time.perf_counter()
    llist.adding_random(val)
    perf_time = time.perf_counter() - perf_time
    l_output(perf_time, "Linked-list [Element ADD] with Performance Time: ", llist)
    messungen["llistadd"] = perf_time
    # Llist sort
    perf_time = time.perf_counter()
    llist.insertionSortAsc()
    perf_time = time.perf_counter() - perf_time
    l_output(perf_time, "Linked-list [Sort] with Performance Time: ", llist)
    messungen["llistsort"] = perf_time
    return messungen

def testing():
    max_work = os.cpu_count()
    tester = []
    arr_size = []
    for i in range(10):
       arr_size.append(1)
    max_work = 7 if max_work > 7 else max_work
    perftime= time.perf_counter()
    with multiproc.ProcessPoolExecutor(max_workers=max_work) as executor:
        for messung in executor.map(maintesting, arr_size):
           tester.append(messung)
    perftime = time.perf_counter()-perftime
    print(tester)
    print("performance time:"+str(perftime))\
   #  tester = []
   #  for i in range(1000):
   #      tester.append(rubnertest_foo())



if __name__ == '__main__':
    print(maintesting())
