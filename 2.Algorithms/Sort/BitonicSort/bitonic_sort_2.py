import random
import numpy as np
from numba import njit
import time
import concurrent.futures


@njit
def create_data(n: int, left: int = 0, right: int = 10) -> list[int]:
    return [random.randint(left, right) for i in range(n)]


@njit
def create_data_n(n: int, left: int = 0, right: int = 10) -> list[int]:
    return np.random.randint(left, right, n)


def compAndSwap(a: list[int], i: int, j: int, dire: int):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]


def bitonicMerge(a: list[int], low: int, cnt: int, dire: int):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)


def bitonicSort(a: list[int], low: int, cnt: int, dire: int):
    if cnt > 1:
        k = cnt // 2
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)


def sort(a: list[int], N: int, up: int):
    bitonicSort(a, 0, N, up)
    return a

def parallel_sort(arr_b, up=1, num_threads=2):
    n = len(arr_b)
    chunk_size = n // num_threads
    results = []
    #  Создание пула потоков с заданным количеством потоков (num_threads).
    #  Данный контекстный менеджер автоматически управляет потоками и их выполнением.
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        #  Создание пустого списка futures, который будет содержать объекты Future для отслеживания выполнения каждого потока.
        futures = []
        for i in range(num_threads):
            start = i * chunk_size
            end = start + chunk_size
            # Запуск потока с функцией sort, которая выполняет битонную сортировку на указанном подмассиве данных.
            # Результат этой задачи (подмассив, отсортированный текущим потоком) будет доступен через объект Future.
            futures.append(executor.submit(sort, arr_b[start:end], len(arr_b[start:end]), up))

        # Этот цикл ожидает, пока каждый поток завершит выполнение.
        for future in concurrent.futures.as_completed(futures):
            #  Получение результата выполнения каждого потока (отсортированного подмассива)
            #  с использованием метода result() объекта Future.
            result = future.result()
            results.append(result)

    # объединение отсортированных подмассивов
    #  Инициализация sorted_array первым отсортированным подмассивом из results.
    sorted_array = results[0]
    #  Цикл для объединения отсортированных подмассивов в sorted_array.
    for result in results[1:]:
        sorted_array = merge(sorted_array, result, up)  # Функция merge определена ниже

    return sorted_array

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

if __name__ == '__main__':
    # arr_b = create_data_n(16_777_216)
    # arr_b = create_data_n(4_194_304)
    # arr_b = create_data_n(262_144)
    # arr_b = create_data(16_777_216)
    # arr_b = create_data(4_194_304)
    arr_b = create_data(262_144)
    # print("Исходный массив:", arr_b)
    n = len(arr_b)
    up = 1  # возрастание

    start = time.perf_counter()
    sorted_array = parallel_sort(arr_b, up=up, num_threads=8)  # Указать желаемое количество потоков
    end = time.perf_counter()
    print(
        f"\t-Параллельная 8 -\nСтруктура данных: {type(arr_b)}\nКоличество элементов: {n}\nЗатрачено времени: {(end - start):0.03f}")

    # print("\n\nОтсортированный массив:", sorted_array)
