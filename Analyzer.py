import time
import random
from demo import mergesort, bubblesort, quicksort


def create_randm_list(size, max):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1, max))
    return ran_list


def analyze_func(name, arr):
    tic = time.time()
    name(arr)
    toc = time.time()
    seconds = toc - tic
    print(name, "Ellapsed Time ->", seconds.5)


size = int(input("Enter the size of list ypu want to create? "))
max = int(input("Enter the max value of the range : "))
runtime = int(input("Enter the no. of time the analyser should run : "))

for num in range(runtime):
    print("Run ", num + 1)
    l = create_randm_list(size, max)
    analyze_func(quicksort, l)
    analyze_func(mergesort, l)
    analyze_func(bubblesort, l)
    print("*" * 50)
