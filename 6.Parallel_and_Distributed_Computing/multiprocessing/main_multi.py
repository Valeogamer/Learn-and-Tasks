import os
from multiprocessing import Process, current_process, Pool, Queue
import multiprocessing

sentinel = -1


def f(x: int) -> int:
    return x * x


def doubler(number: int):
    """
    Функция умножитель на 2
    """
    result = number * 2
    # proc = os.getpid()  # id текущего процесса
    proc = current_process().name  # имя текущего процесса
    print(f'{number} doubled to {result} by process id: {proc}')


def doubler_exe():
    """
    Пуск doubler
    """
    numbers = [5, 10, 15, 20, 25]
    procs = []
    # Количесво данных в списке, количество процессов
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))  # name = свое имя процесса
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


def doubler_poll_exe():
    """
    Пуск doubler
    С использованием Pool
    """
    numbers = [5, 10, 20]
    # создали экземпляр Pool, указали ему создать 3 раб процесса
    pool = Pool(processes=3)
    # далее используем метод map для отображения функции для каждого процесса
    print(pool.map(doubler, numbers))


def creator(data, q):
    """
    Создание и Добавление данных в очередь
    """
    print('Создание данных и помещение их в очередь')
    for item in data:
        q.put(item)


def my_consumer(q):
    """
    Использование данных и их обработка из очереди
    """
    while True:
        data = q.get()
        print(f'Данные в обработке: {data}')
        processed = data * 2
        print(processed)
        if data is sentinel:
            break


def creator_consumer_exe():
    q = Queue()
    data = [5, 10, 13, -1]
    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q, ))

    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()

if __name__ == '__main__':
    doubler_exe()
    doubler_poll_exe()
    creator_consumer_exe()
