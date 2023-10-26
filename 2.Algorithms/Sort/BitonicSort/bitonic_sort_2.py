"""
    Реализовано с помощью:
    https://docs.python.org/3/library/concurrent.futures.html
    Потому что возникли проблемы с сериализацией функций в многозадачности
"""

import multiprocessing
import random
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor
from numba import njit

@njit
def create_data(n: int, left: int = 0, right: int = 10) -> list[int]:
    return [random.randint(left, right) for i in range(n)]

@njit
def create_data_n(n: int, left: int = 0, right: int = 10) -> list[int]:
    return np.random.randint(left, right, n)

def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)

def parallel_bitonic_sort(sub_array, low, cnt, dire):
    bitonicSort(sub_array, low, cnt, dire)
    return sub_array

def main(arr_b, n):
    arr_b = arr_b
    n = n
    up = 1

    # num_threads = int(multiprocessing.cpu_count() / 4)
    num_threads = 6
    butch_size = n // num_threads

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []

        for i in range(num_threads):
            start_index = i * butch_size
            end_index = start_index + butch_size if i < num_threads - 1 else n
            sub_array = arr_b[start_index:end_index]
            futures.append(executor.submit(parallel_bitonic_sort, sub_array, 0, len(sub_array), up))

        sorted_subarrays = [future.result() for future in futures]
        sorted_subarrays.sort(key=lambda x: x[0])

        sorted_array = [elem for subarray in sorted_subarrays for elem in subarray]
    return sorted_array

if __name__ == '__main__':
    arr_b = create_data(262_144)
    # arr_b = create_data_n(4_194_304)
    # arr_b = create_data_n(16_777_216)
    # arr_b = [3, 4, 7, 8, 6, 5, 2, 1]
    n = len(arr_b)
    start = time.perf_counter()
    arr_b = main(arr_b, n)
    end = time.perf_counter()
    print(f"\t-Многопроцессорная-\nСтруктура данных: {type(arr_b)}\nКоличество элементов: {n}\nЗатрачено времени: {(end - start):0.03f}")
