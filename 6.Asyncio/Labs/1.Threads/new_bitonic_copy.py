"""
    +++ Link +++
1. http://python-3.ru/page/multiprocessing
2. https://docs.python.org/3.10/library/multiprocessing.html
# добавить функцию подсчет экстремумами
"""
from multiprocessing import Process, Queue, Pool, cpu_count
import multiprocessing
import random
import threading
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
from numba import njit


def create_data(n: int, left=-5, right=10) -> list[int]:
    """
    Генерация списка из целых чисел, длиной N
    """
    return [random.randint(left, right) for i in range(n)]


@njit
def create_data_n(n: int, left=-5, right=10) -> list[int]:
    """
    Генерация списка из целых чисел, длиной N, numpy
    """
    return np.random.randint(left, right, n)


def vizulation(data: int):
    """
    Визуализация данных
    """
    x = list(range(len(data)))
    plt.plot(x, data, marker='o', linestyle='-', markersize=2)
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.title('График данных')
    plt.xlim(0, len(data))
    plt.grid(True)
    plt.show()


def checker_peak(data: list[int], start: int, end: int, chunk: int) -> int:
    """
    Проверка разделенного списка, то есть не разделили ли там где происходят переключения
    """
    if len(data) == end:
        return
    # Пик максимум
    if data[end - 1] < data[end] > data[end + 1]:
        # print("Пик максимум")
        for i in range(1, chunk - 1):
            if data[end + 1] > data[end + i + 1]:
                return 1
            if data[end + 1] < data[end + i + 1]:
                return 2
    # Пик минимум
    if data[end - 1] > data[end] < data[end + 1]:
        # print("Пик минимум")
        for i in range(1, chunk - 1):
            if data[end + 1] < data[end + i + 1]:
                return 1
            if data[end + 1] > data[end + i + 1]:
                return 2
    # разделение в промежутке возрастания
    if data[end - 1] < data[end] < data[end + 1]:
        # print("разделение в промежутке возрастания")
        for i in range(1, chunk - 1):
            if data[end + 1] < data[end + i + 1]:
                return
            if data[end + 1] > data[end + i + 1]:
                return 1
    # разделение в промежутке убывания
    if data[end - 1] > data[end] > data[end + 1]:
        # print("разделение в промежутке убывания")
        for i in range(1, chunk - 1):
            if data[end + 1] < data[end + i + 1]:
                return 1
            if data[end + 1] > data[end + i + 1]:
                return
    # равные
    if data[end - 1] == data[end] == data[end + 1]:
        # print("равные")
        for i in range(1, chunk - 1):
            if data[end] < data[end - i]:
                for i in range(1, chunk - 1):
                    if data[end] > data[end + 1]:
                        return
                    if data[end] < data[end + 1]:
                        return 1
            if data[end] > data[end - i]:
                for i in range(1, chunk - 1):
                    if data[end] > data[end + 1]:
                        return 1
                    if data[end] < data[end + 1]:
                        return
            return 1
    # правый край равенство, левый неравество (максимум -> не факт)
    if data[end - 1] < data[end] == data[end + 1]:
        # print("правый край равенство, левый неравество (максимум -> не факт)")
        for i in range(1, chunk - 1):
            if data[end] > data[end + i]:
                return 1
            if data[end] < data[end + i]:
                return
    # левый равенство, правый неравенство (максимум -> не факт)
    if data[end - 1] == data[end] > data[end + 1]:
        # print("левый равенство, правый неравенство (максимум -> не факт)")
        for i in range(1, chunk - 1):
            if data[end - i] < data[end]:
                for i in range(1, chunk - 1):
                    if data[end + 1] < data[end + i + 1]:
                        return 2
                    if data[end + 1] > data[end + i + 1]:
                        return 1
            if data[end - i] > data[end]:
                for i in range(1, chunk - 1):
                    if data[end + 1] < data[end + i + 1]:
                        return 1
                    if data[end + 1] > data[end + i + 1]:
                        return
    # правый край равенство, левый неравество (минимум  -> не факт)
    if data[end - 1] > data[end] == data[end + 1]:
        # print("правый край равенство, левый неравество (минимум  -> не факт)")
        for i in range(1, chunk - 1):
            if data[end] > data[end + i]:
                return
            if data[end] < data[end + i]:
                return 1
        return

    # левый равенство, правый неравенство (минимум  -> не факт)
    if data[end - 1] == data[end] < data[end + 1]:
        # print("левый равенство, правый неравенство (минимум  -> не факт)")
        for i in range(1, chunk - 1):
            if data[end] < data[end - i]:
                for i in range(1, chunk - 1):
                    if data[end + 1] > data[end + i + 1]:
                        return 2
                    if data[end + 1] < data[end + i + 1]:
                        return 1
                return 1
            if data[end] > data[end - i]:
                for i in range(1, chunk - 1):
                    if data[end + 1] > data[end + i + 1]:
                        return 1
                    if data[end + 1] < data[end + i + 1]:
                        return
        return


def find_bitonic_count(data: list[int], start: int = 0, end=None, result=None) -> int:
    """
    Подсчет количества битонических подпоследовательностей в части массива
    Сложность O(n)
    """
    check = False
    if end is None:
        end = len(data)
    if type(data) is tuple:
        check = True
        data, start, end = data[0], data[1], data[2]
    up = down = False
    cnt = 0
    if result != None:  # type(result) is list
        if end != len(data):
            end += 1
    for i in range(start, end - 1):
        if data[i + 1] > data[i]:
            up = True
            if down:
                cnt += 1
                down = False
        elif data[i + 1] < data[i]:
            down = True
            if up:
                cnt += 1
                up = False
    if check:
        return cnt
    elif result is None:
        return print(f'Количество битонических подпоследовательностей: {cnt}')
    elif type(result) != list:
        result.put(cnt)
    else:
        result.append(cnt)


def threading_find_all_bitonic(data: list[int], num_threads: int) -> int:
    """
    Параллельный подсчет количества всех битонических подпоследовательностей в массиве, Потоками
    Сложность O(n)
    """
    result = []
    chunk_size = len(data) // num_threads
    threads = []
    # lock = threading.Lock()
    for i in range(num_threads):
        start = i * chunk_size
        if i > 0:
            start += 1
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(data)  # последний поток
        # проверка
        add_cnt = checker_peak(data, start, end, chunk_size)
        if add_cnt:
            result.append(add_cnt)
        thread = threading.Thread(target=find_bitonic_count, args=(data, start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_count = sum(result)
    print(f"Количество битонических подпоследовательностей: {total_count}")


def multiprocess_find_bitonic(data: list[int], num_process: int) -> int:
    """
    Параллельный подсчет количества всех битонических подпоследовательностей в массиве, Процессами
    """
    q = Queue()
    chunk_size = len(data) // num_process
    list_process = []
    for i in range(num_process):
        start = i * chunk_size
        if i > 0:
            start += 1
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(data)
        # проверка
        add_cnt = checker_peak(data, start, end, chunk_size)
        if add_cnt:
            q.put(add_cnt)
        process = Process(target=find_bitonic_count, args=(data, start, end, q))
        list_process.append(process)
        process.start()

    for proc in list_process:
        proc.join()
    total_count = 0
    while not q.empty():
        item = q.get()
        if isinstance(item, int):
            total_count += item
        else:
            break

    print(f"Количество битонических подпоследовательностей: {total_count}")


if __name__ == '__main__':
    # генерация данных
    # data = create_data(1_000_000_00)
    data = create_data_n(100_000)
    # print(data)

    # визуализация
    # vizulation(data)

    # подсчет битонических без потоков
    start = perf_counter()
    find_bitonic_count(data)
    end = perf_counter()
    print(
        f"---Последовательный---\n\tЗатрачено времени: {end - start:.5f} \n\tДлина списка: {len(data)} \n\tСтруктура данных: numpy array\n")

    # подсчет битонических с потоками
    start = perf_counter()
    num_threads = 4  # Укажите желаемое количество потоков
    threading_find_all_bitonic(data, num_threads)
    end = perf_counter()
    print(
        f"---Потоки {num_threads}---\n\tЗатрачено времени: {end - start:.5f} \n\tДлина списка: {len(data)} \n\tСтруктура данных: numpy array\n")

    # подсчет битонических multiprocessing
    start = perf_counter()
    num_process = 4
    multiprocess_find_bitonic(data, num_process)
    end = perf_counter()
    print(
        f"---Мультипроцессинг {num_process}---\n\tЗатрачено времени: {end - start:.5f} \n\tДлина списка: {len(data)} \n\tСтруктура данных: numpy array\n")
