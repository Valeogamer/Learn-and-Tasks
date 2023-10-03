"""
    +++ Link +++
1. http://python-3.ru/page/multiprocessing
2. https://docs.python.org/3.10/library/multiprocessing.html
"""
from multiprocessing import Process, Queue, Pool
import random
import threading
from time import perf_counter
import time
import matplotlib.pyplot as plt
import numpy


def create_data(n: int, left=-5, right=5) -> list[int]:
    """
    Генерация списка из целых чисел, длиной N
    """
    return [random.randint(left, right) for i in range(n)]


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
    lock = threading.Lock()
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size + 2 if i < num_threads - 1 else len(data)  # последний поток
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
        end = (i + 1) * chunk_size + 2 if i < num_process - 1 else len(data)  # последний поток
        process = Process(target=find_bitonic_count, args=(data, start, end, q))
        list_process.append(process)
        process.start()

    for proc in list_process:
        proc.join()
    total_count = sum([q.get() for i in range(num_process)])
    print(f"Количество битонических подпоследовательностей: {total_count}")


def find_bitonic_count_for_pool(data_indices):
    """
    Подсчет количества битонических подпоследовательностей в части массива по индексам
    Сложность O(n)
    """
    data, start, end = data_indices[0], data_indices[1], data_indices[2]
    up = down = False
    cnt = 0
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
    return cnt


def multiprocess_find_bitonic_pool(data: list[int], num_process: int) -> int:
    """
    Параллельный подсчет количества всех битонических подпоследовательностей в массиве, используя Pool
    """
    chunk_size = len(data) // num_process
    pool = Pool(processes=num_process)
    results = pool.map(find_bitonic_count,
                       [(data, i * chunk_size, (i + 1) * chunk_size + 2 if i < num_process - 1 else len(data),) for i in
                        range(num_process)])
    pool.close()
    pool.join()
    total_count = sum(results)
    print(f"Количество битонических подпоследовательностей: {total_count}")


def count_bitonic_in_subarray(data: list[int], start: int = 0, end=None, result=None) -> int:
    """
    Сложность O(n)
    """
    if end is None:
        end = len(data)

    if len(data) < 3:
        return
    trend = "none"
    trend_changes = 0
    current_trend_length = 1
    for i in range(start + 1, end):
        if data[i] > data[i - 1]:
            if trend == "decreasing":
                if current_trend_length > 2:
                    trend_changes += 1
                current_trend_length = 1
            trend = "increasing"
            current_trend_length += 1
        elif data[i] < data[i - 1]:
            if trend == "increasing":
                if current_trend_length > 2:
                    trend_changes += 1
                current_trend_length = 1
            trend = "decreasing"
            current_trend_length += 1
    if result is None:
        return print(f'Количество битонических подпоследовательностей: {trend_changes}')
    result.append(trend_changes)


def threading_count_all_bitonic(data: int, num_threads: int) -> int:
    """
    Сложность O(n)
    """
    chunk_size = len(data) // num_threads
    threads = []
    result = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size + 2 if i < num_threads - 1 else len(data)
        thread = threading.Thread(target=count_bitonic_in_subarray, args=(data, start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_changes = sum(result)
    print(f"Количество битонических переключений: {total_changes}")


if __name__ == '__main__':
    # генерация данных
    data = create_data(10)

    # визуализация
    # vizulation(data)

    # подсчет битонических без потоков
    start = perf_counter()
    find_bitonic_count(data)
    end = perf_counter()
    print(f"Затрачено времени: {end - start:.5f},  на список длиной: {len(data)}\n")

    # подсчет битонических с потоками
    start = perf_counter()
    num_threads = 4  # Укажите желаемое количество потоков
    threading_find_all_bitonic(data, num_threads)
    end = perf_counter()
    print(f"Затрачено времени (threading): {end - start:.5f}, на список длиной: {len(data)}\n")

    # подсчет битонических multiprocessing
    start = perf_counter()
    num_process = 16
    multiprocess_find_bitonic(data, num_process)
    end = perf_counter()
    print(f"Затрачено времени (multiprocessing): {end - start:.5f}, на список длиной: {len(data)}\n")

    # подсчет битонических multiprocessing Pool
    start = perf_counter()
    num_process = 16
    multiprocess_find_bitonic_pool(data, num_process)
    end = perf_counter()
    print(f"Затрачено времени (multiprocessing.Pool): {end - start:.5f}, на список длиной: {len(data)}\n")

    # подсчет битонических с некоторым правилом (см. рис)
    start = perf_counter()
    count_bitonic_in_subarray(data)
    end = perf_counter()
    print(f"Затрачено времени: {end - start:.5f},  на список длиной: {len(data)}\n")

    # подсчет битонических с некоторым правилом (см. рис) потоки
    start = perf_counter()
    num_threads = 4  # Укажите желаемое количество потоков
    threading_count_all_bitonic(data, num_threads)
    end = perf_counter()
    print(f"Затрачено времени (threading): {end - start:.5f},  на список длиной: {len(data)}\n")
