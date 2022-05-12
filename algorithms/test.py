import algorithms as alg
import random
import time
# import timeit

random.seed(20)
numbers = [random.randint(0, 10**9) for i in range(0, 10**5)]
start = time.time()
alg.merge_sort(numbers)
end = time.time()
print(end - start)
# time = timeit.timeit(lambda: "alg.insertion_sort(numbers)")
# print(time)
