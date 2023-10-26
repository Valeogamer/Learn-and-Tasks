"""
    С использование MPI
    mpiexec -n 8 python bitonic_sort_3.py

"""

from mpi4py import MPI
import random
import numpy as np
from numba import njit
import time

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

def main(arr_b, n):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    arr_b = comm.bcast(arr_b, root=0)
    n = comm.bcast(n, root=0)
    up = 1

    butch_size = n // size
    scatter_data = []

    for i in range(size):
        start_index = i * butch_size
        end_index = start_index + butch_size if i < size - 1 else n
        sub_array = arr_b[start_index:end_index]
        bitonicSort(sub_array, 0, len(sub_array), up)
        scatter_data.append(sub_array)

    sorted_data = comm.gather(scatter_data, root=0)

    if rank == 0:
        # Сортировка собранных данных на корневом процессе
        merged_data = [elem for sublist in sorted_data for elem in sublist]
        bitonicSort(merged_data, 0, len(merged_data), up)
        # print(merged_data)

if __name__ == '__main__':
    arr_b = create_data(262_144)
    # arr_b = create_data(4_194_304)
    # arr_b = create_data_n(16_777_216)
    n = len(arr_b)
    start = time.perf_counter()
    main(arr_b, n)
    end = time.perf_counter()
    print(f"\t-Mpi-\nCount Kernel: 4\nData structure: {type(arr_b)}\nCount element: {n}\nTime: {(end - start):0.03f}")
