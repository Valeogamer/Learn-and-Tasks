"""
    MPI
    mpiexec -n 8 python bitonic_sort_3.py
    MPI4PY DOC (https://mpi4py.readthedocs.io/en/stable/reference/mpi4py.MPI.Comm.html#mpi4py.MPI.Comm)
    MPI.Comm.COMM_WORLD - инициализация MPI
    MPI.Get_size - количество процессов в коммуникаторе
    MPI.Get_rank - ранг текущего процесса (родительский или по умолчанию 0, <- сбор результатов с процессов иного ранга)
    MPI.Comm.Bcast - широковещательный обмен
    MPI.Comm.Gather - собрать результат со всех процессов

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


def merge(left, right, up):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if (up == 1 and left[i] < right[j]) or (up == 0 and left[i] > right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main(arr_b, n):
    #  Создание объекта MPI-коммуникатора для взаимодействия между процессами.
    comm = MPI.COMM_WORLD
    # Получение номера текущего процесса в коммуникаторе. rank будет представлять номер текущего процесса.
    rank = comm.Get_rank()
    # Получение общего числа процессов в коммуникаторе. size будет представлять общее количество процессов.
    size = comm.Get_size()

    # Распространение данных из процесса с номером 0 (корневой процесс) на все остальные процессы.
    # Это гарантирует, что у всех процессов будет доступ к исходному массиву arr_b. (Широковещательный обмен)
    # Широковещательная передача сообщения от одного процесса всем остальным процессам в группе (doc mpi4py)
    arr_b = comm.bcast(arr_b, root=0)
    # Аналогично распространение значения n (количества элементов) на все процессы.
    n = comm.bcast(n, root=0)
    # 1 - возрастание 0 - убывание
    up = 1

    butch_size = n // size
    sub_array = arr_b[rank * butch_size:(rank + 1) * butch_size]
    bitonicSort(sub_array, 0, len(sub_array), up)
    # Собираем сортированные подмассивы от всех процессов и сохраняем их в sorted_data.
    # Все собранные подмассивы будут находиться в корневом процессе (процесс с номером 0).
    # (Собирает воедино значения из группы  (doc mpi4py)
    sorted_data = comm.gather(sub_array, root=0)

    #  Проверяем, является ли текущий процесс корневым процессом (с номером 0).
    if rank == 0:
        # Объединение сортированных данных
        merged_data = [elem for sublist in sorted_data for elem in sublist]
        bitonicSort(merged_data, 0, len(merged_data), up)
        sorted_array = merged_data
        # print(sorted_array)


if __name__ == '__main__':
    # arr_b = create_data_n(16_777_216)
    # arr_b = create_data_n(4_194_304)
    # arr_b = create_data_n(262_144)
    # arr_b = create_data(16_777_216)
    # arr_b = create_data(4_194_304)
    # arr_b = create_data(262_144)
    arr_b = create_data(32)
    n = len(arr_b)
    start = time.perf_counter()
    main(arr_b, n)
    end = time.perf_counter()
    print(f"\t-MPI 8 kernel-\nData structure: {type(arr_b)}\nCount element: {n}\nTime: {(end - start):0.03f}")
