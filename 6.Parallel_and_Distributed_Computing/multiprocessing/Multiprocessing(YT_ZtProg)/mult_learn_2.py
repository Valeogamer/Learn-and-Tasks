"""
    Синхронизация процессов.
    Lock - позволяют создавать блокировщики и
    RLock - ограничивать доступ к определенным блокам кода
    Array массивы - с помощью которой можем давать доступ к одной переменной сразу ко многим процессам
    и изменять его сразу же из многих других процессов. Тем самым это можем использовать для общения между процессами
    и обмена информацией.
    Queue - очередь.
"""
import random
# __Lock и RLock__
# import time
# import multiprocessing
#
# lock = multiprocessing.Lock()  # экземпляр блокировщика Lock (Можно разблокировать с любого процесса)
# rlock = multiprocessing.RLock()  # экземпляр блокировщика RLock (Может разблокировать только тот, кто заблокировал)
#
#
# def get_value(l):
#     l.acquire()  # блокируем все последующие процессы, пока данный процесс не дойдет до разблокировки
#     #  НО стоит учесть что данную блокировку легко снять с любого места
#     # LOCK - можно сравнить с замком, ключ к которому есть у каждого, то есть получиться разлочить
#     # даже с заблоченного процесса.
#     # А вот RLock напротив, его может разблокировать только тот, кто его заблокировал.
#     proc_name = multiprocessing.current_process().name
#     print(f"Процесс [{proc_name}] запущен!")
#     l.release()  # разблокировка процессов
#
#
# if __name__ == '__main__':
#     lock = multiprocessing.Lock()  # экземпляр блокировщика
#     # Чтобы воспользоваться блокировщиком нужно его явно передать внурь нашего процесса
#     process = multiprocessing.Process(target=get_value, args=(lock,), name='MyProc-1').start()
#     process = multiprocessing.Process(target=get_value, args=(lock,), name='MyProc-2').start()

# __Array - общая структура для всех запущенных потоков__
# import time
# import multiprocessing
#
#
# def add_value(locker, array, index):
#     # для того чтобы каждый раз не писать acquire(заблокировать) и release(разблокировать)
#     # вызовем контекстный менеджер with, который сам все проделает, и также исключения обработает
#     # и не допусит взаимоблокировок
#     with locker:
#         num = random.randint(0, 5)
#         vtime = time.ctime()  # текущее время
#         array[index] = num
#         print(f"array [{index}] = {num}, sleep = {vtime}")
#         time.sleep(num)
#
#
# if __name__ == '__main__':
#     lock = multiprocessing.Lock()  # экземпляр блокировщика
#     arr = multiprocessing.Array("i", range(10))  # создаем массив, укажем тип используемых данных
#     process_list = []
#
#     for i in range(10):
#         proc = multiprocessing.Process(target=add_value, args=(lock, arr, i), name=f"MyProc-{i}")
#         process_list.append(proc)
#         proc.start()
#
#     for proc in process_list:
#         proc.join()
#
#     print(list(arr))

# __Queue - Очередь__

import time
import multiprocessing
import random


def get_text(q):
    val = random.randint(0, 5)
    q.put(str(val))  # добавляем в очередь значение Test, из процесса "Другой процесс"


if __name__ == '__main__':
    queue = multiprocessing.Queue()  # инициализация очереди
    process_list = []
    for i in range(1, 6):
        proc = multiprocessing.Process(target=get_text, args=(queue,), name=f"Другой_процесс_{i}")
        process_list.append(proc)
        proc.start()

    for proc in process_list:
        proc.join()

    for elem in iter(queue.get, None):
        print(elem)

    # попробуем из другого процесса получить наше значение из очереди
    # print(queue.get())  # получаем значение другого процесса из основного процесса
    # Основной процесс и другой процесс, между собой никак не связаны, но мы все же можем
    # получить значение. Это говорит о том, что мы можем общаться между процессами.
