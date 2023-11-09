"""
    Как обмениваться данными между 2 процессами.
    Общая разделяемая память.

"""
import time
import multiprocessing


def calc_square(nums, shared_memory, val):
    val.value = 5.67
    for idx, n in enumerate(nums):
        shared_memory[idx] = n * n


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    # создадим общую память, структура массив, типа данных int, размер массива
    shared_memory_arr = multiprocessing.Array('i', 4)
    # также можно создать Value тоже общая разделяемая память, хранит только одно значение
    shared_memory_val = multiprocessing.Value('d', 0.0)
    # всякий раз когда создаешь новый процесс он получает свое собственное адресное пространство
    p1 = multiprocessing.Process(target=calc_square, args=(arr, shared_memory_arr, shared_memory_val))

    # запуск процессов
    p1.start()

    # ожидаем завершения исполнения процессов
    p1.join()

    # вывод результата из общей памяти
    print(shared_memory_arr[:])
    print(shared_memory_val.value)
