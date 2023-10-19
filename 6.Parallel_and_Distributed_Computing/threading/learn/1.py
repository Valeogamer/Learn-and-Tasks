"""
Однопоточные программы
"""
from time import sleep, perf_counter


def task():
    print('Начали выполнение задачи... ')
    sleep(1)
    print('Выполнено')


if __name__ == '__main__':
    start_time = perf_counter()
    task()
    task()
    end_time = perf_counter()
    print(f'Выполнение заняло {end_time - start_time: 0.2f}')
