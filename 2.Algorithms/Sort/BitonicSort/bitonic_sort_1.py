"""
    Битоническая сортировка.
    1) Последовательное выполнение программы.
    2) С использованием multiprocessing и queue(очереди)
    3) С использованием MPI (mpi4py)

    Алгоритм:
    1) Формируем 4х элементные битонические последовательности. В котором 2 элемента возрастают, а 2 убывают.
    2) Затем берем две 4х элементные последовательности и формируем одну битоническую последовательность, и так далее
    пока не получим одну битоническую последовательность из всего массива.
    3) Затем сравниваем первый элемент возрастающей последовательность, с первым элементом убывающей и так далее
    второй со вторым, 3 с 3 и т.д..
    4) После в возрастающей части сравниваем через одного, т. е. четные с четным, нечетные с нечетным. Аналогично в убывающей части.
    5) После сравниваем 1 со 2, 3 с 4, n c n+1 и т.д..
    6) Должны получить отсортированный список

    Сложность алгоритма:
    O(log^2N)

    Входные данные:
    Количество элементов в массиве степень 2
    Желаетельно чтобы массив состоял из 0 и 1
    Выходные данные: отсортированный массив

"""

import random
import numpy as np
from numba import njit
import time


@njit
def create_data(n: int, left: int = 0, right: int = 10) -> list[int]:
    """
    Генерация списка из целых чисел, длиной N
    """
    return [random.randint(left, right) for i in range(n)]


@njit
def create_data_n(n: int, left: int = 0, right: int = 1) -> list[int]:
    """
    Генерация массива из целых чисел, длиной N
    """
    return np.random.randint(left, right, n)


def compAndSwap(a: list[int], i: int, j: int, dire: int):
    """
    Сравнение и замена двух элементов. Сравнение как на возрастание, так и на уменьшение.
    a: массив для сравнения
    i: индекс элемента массива a, который нужно сравнить
    j: индекс элемента массива a, который нужно сравнить
    dire: тип сортировки
    """
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]


def bitonicMerge(a: list[int], low: int, cnt: int, dire: int):
    """
    Функция слияния
    a: массив слияния
    low: индекс начала текущей последоваетельности в массиве
    cnt: кол-во элементов в текущей последовательности
    dire: тип сортировки
    """
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            # print(a[i:i+k], '\t', a[i])
            compAndSwap(a, i, i + k, dire)
        # print(a[low:k], '\t', a[low])
        bitonicMerge(a, low, k, dire)
        # print(a[low+k:k], '\t', a[low])
        bitonicMerge(a, low + k, k, dire)


def bitonicSort(a: list[int], low: int, cnt: int, dire: int):
    """
    Рекурсивная функцияя битонной сортировки
    a: массив
    low: индекс начала текущей последоваетельности в массиве
    cnt: кол-во элементов в текущей последовательности
    dire: тип сортировки
    """
    if cnt > 1:
        k = cnt // 2
        # print(a[low:k], '\t', a[low])  # отладочное
        bitonicSort(a, low, k, 1)
        # print(a[low+k:k], '\t', a[low])  # отладочное
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)


def sort(a: list[int], N: int, up: int):
    '''
    a: массив
    N: длина массива
    up: 1 - тип сортировки (возрастание, убывание)
    '''
    bitonicSort(a, 0, N, up)


if __name__ == '__main__':
    # arr_b = create_data_n(16_777_216)
    # arr_b = create_data_n(4_194_304)
    # arr_b = create_data_n(262_144)
    # arr_b = create_data(16_777_216)
    # arr_b = create_data(4_194_304)
    arr_b = create_data(262_144)
    # arr_b = create_data(32)
    n = len(arr_b)
    up = 1  # возрастание

    start = time.perf_counter()
    sort(arr_b, n, up)
    end = time.perf_counter()
    print(
        f"\t-Последовательная-\nСтруктура данных: {type(arr_b)}\nКоличество элементов: {n}\nЗатрачено времени: {(end - start):0.03f}")

    # print("\n\nОтсортированные элементы")
    # for i in range(n):
    #     print("%d" % arr_b[i], end=" ")
