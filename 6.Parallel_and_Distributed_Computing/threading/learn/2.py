"""
Модуль threading для мультипоточных программ

-thread = Thread(target, args)
    target:= func(args)
    args:= args

thread.start() -  запуск потока

-thread.join() - дождаться исполнения всех потоков
иначе отработает основной поток, и завершиться программы, а остальные после завершения доработают

-
"""
from time import sleep, perf_counter
from threading import Thread


def task():
    print('Начинаем выполнение задачи...')
    sleep(1)
    print('Выполнено')


if __name__ == '__main__':
    # начало отчета времени
    start_time = perf_counter()

    # создаем потоки
    new_thread_1 = Thread(target=task)
    new_thread_2 = Thread(target=task)

    # запуск потоков
    new_thread_1.start()
    new_thread_2.start()

    # дожидаемся исполнения всех потоков
    new_thread_1.join()
    new_thread_2.join()

    # окончание отчетат времени
    end_time = perf_counter()

    # вывод затраченного времени
    print(f'Выполнение заняло: {end_time - start_time: 0.2f} секунд.')
