"""
Однопоточная vs Многопоточная (I/O bound)
1) Создание файлов
2) Чтение
"""
from time import perf_counter
import os
import threading
from threading import Thread

def create_and_write_file_threading(test_number):
    file_path = f'test_threading/test_{test_number}.txt'
    if not os.path.exists('test_threading'):
        os.makedirs('test_threading')
    with open(file_path, 'w') as file:
        file.write(f'Test_threading-{test_number}')


def create_and_write_file(test_number):
    file_path = f'test/test_{test_number}.txt'
    if not os.path.exists('test'):
        os.makedirs('test')
    with open(file_path, 'w') as file:
        file.write(f'Test-{test_number}')


def fileWrite():
    """
    Создание фалов
    1) Однопоточная
    2) Многопоточная
    """
    start = perf_counter()
    [create_and_write_file(i) for i in range(10)]
    end = perf_counter()

    start_t = perf_counter()
    # Создаем 10 потоков для выполнения задачи
    threads = []
    for i in range(1, 11):
        thread = threading.Thread(target=create_and_write_file_threading, args=(i,))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()
    end_t = perf_counter()
    print(f"Все файлы созданы и записаны с помощью потоков, времени затрачно: {end_t - start_t:.4f}")
    print(f"Все файлы созданы и записаны, времени затрачно: {end - start:.4f}")


def open_and_read_file_threading(i):
    with open(f'test_threading/test_{i}.txt', 'r') as f:
        f.seek(0)
        data_p = f.read()
        print(f'Содержимое_потоков: {data_p}')


def open_and_read_file(i):
    with open(f'test/test_{i}.txt', 'r') as f:
        f.seek(0)
        data = f.read()
        print(f'Содержимое: {data}')

def fileOpen():
    start_t = perf_counter()
    # threads = [Thread(target=open_and_read_file_threading, args=(i,)).start() for i in range(1, 11)]
    threads = []
    for i in range(1, 11):
        thread = Thread(target=open_and_read_file_threading, args=(i, ))
        thread.start()
        threads.append(thread)
    _ = [t.join() for t in threads]
    end_t = perf_counter()

    start = perf_counter()
    [open_and_read_file(i)
    for i in range(10)]
    end = perf_counter()

    print(f"Все файлы прочтены с помощью потоков, времени затрачно: {end_t - start_t:.4f}")
    print(f"Все файлы прочтены, времени затрачно: {end - start:.4f}")

if __name__ == '__main__':
    fileWrite()
    fileOpen()