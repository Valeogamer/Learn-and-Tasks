"""
Передача аргументов в потоки
"""
from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'Начинаем выполнение задачи: {id}')
    sleep(1)
    print(f'Задача {id} выполнена')


if __name__ == '__main__':
    # начало отчета времени
    start_time = perf_counter()

    # создаем и запускаем 10 потоков
    # threads = []
    # for n in range(1, 11):
    #     t = Thread(target=task, args=(n,))
    #     threads.append(t)
    #     t.start()
    threads = [Thread(target=task, args=(n,)).start() for n in range(1, 11)]
    _ = [t.join() for t in threads]
    # окончание отчетат времени
    end_time = perf_counter()

    # вывод затраченного времени
    print(f'Выполнение заняло: {end_time - start_time: 0.2f} секунд.')
