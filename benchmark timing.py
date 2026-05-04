import time
import random

sizes = [1000, 5000, 10000]

for size in sizes:
    arr = [random.randint(1, 100000) for _ in range(size)]

    start = time.time()

    sorted(arr)   # sorting benchmark

    end = time.time()

    print("Dataset Size:", size)
    print("Execution Time:", end - start, "seconds")
    print()