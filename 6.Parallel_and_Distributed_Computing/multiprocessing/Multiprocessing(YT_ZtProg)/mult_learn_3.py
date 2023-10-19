"""
 Пул прцессов (Pool)
"""

# __ Применение Pool __
# работает только в режиме отладки
# import random
# import multiprocessing
#
#
# def print_value(value):
#     name_curr_p = multiprocessing.current_process().name
#     print(f"[{name_curr_p}] value: {value}")
#
#
# if __name__ == '__main__':
#     print_value(5)
#     cpu_cnt = int(multiprocessing.cpu_count() / 2)
#     # p = multiprocessing.Pool(processes=cpu_cnt)
#     with multiprocessing.Pool(processes=cpu_cnt) as p:
#         p.map(func=print_value, iterable=list(range(10)))

# __ map_async, callback __
# map_async - после завершения всех процессов, позволяет нам заупустить нужный callback
# callback по умолчанию возвращает результат выполнения (response)

# import random
# import multiprocessing
#
#
# def end_func(response):
#     print("Задание завершено!")
#     print("Callback возвращает результаты всех процессов: ", response)
#     # вернет в виде списка все что вернут процессы исполнив функцию print_value
#
#
# def print_value(value):
#     name_curr_p = multiprocessing.current_process().name
#     print(f"[{name_curr_p}] value: {value}")
#     return value
#
#
# if __name__ == '__main__':
#     print_value(5)
#     cpu_cnt = int(multiprocessing.cpu_count() / 2)
#     # p = multiprocessing.Pool(processes=cpu_cnt)
#     with multiprocessing.Pool(processes=cpu_cnt) as p:
#         p.map_async(func=print_value, iterable=list(range(10)), callback=end_func)
#         p.close()  # после того как вызвали map_async, нам нужно закрыть наш Pool
#         p.join()  # и также вызвать join() который позволяет дождаться выполнения всех процессов

# __ apply_as __
# - позволяет вызывать функцию отдельно, и после того хоть одна функция выполнена мы запускаем callback
# import random
# import multiprocessing
#
#
# def end_func(response):
#     print("Задание завершено!")
#     print("Callback возвращает результат одного из процессов: ", response)
#     # вернет в виде списка все что вернут процессы исполнив функцию print_value
#
#
# def print_value(value):
#     name_curr_p = multiprocessing.current_process().name
#     print(f"[{name_curr_p}] value: {value}")
#     return value
#
#
# if __name__ == '__main__':
#     print_value(5)
#     cpu_cnt = int(multiprocessing.cpu_count() / 2)
#     # p = multiprocessing.Pool(processes=cpu_cnt)
#     with multiprocessing.Pool(processes=cpu_cnt) as p:
#         for i in range(10):
#             p.apply_async(print_value, args=(i,), callback=end_func)
#         p.close()  # после того как вызвали map_async, нам нужно закрыть наш Pool
#         p.join()  # и также вызвать join() который позволяет дождаться выполнения всех процессов

# __ starmap __
# дает возможность передавать сразу несколько аргументов, вместой одной как в map
# import random
# import multiprocessing
#
#
# def print_value(x, y, z):
#     name_curr_p = multiprocessing.current_process().name
#     print(f"[{name_curr_p}] x: {x}, y: {y}, z: {z}")
#     # return value
#
#
# if __name__ == '__main__':
#     cpu_cnt = int(multiprocessing.cpu_count() / 2)
#     # p = multiprocessing.Pool(processes=cpu_cnt)
#     with multiprocessing.Pool(processes=cpu_cnt) as p:
#         # Каждый последующий Pool возьмет по одному кортежу, то есть
#         # у каждого процесса свой кортеж из списка
#         p.starmap(print_value, [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
#         p.close()  # после того как вызвали map_async, нам нужно закрыть наш Pool
#         p.join()  # и также вызвать join() который позволяет дождаться выполнения всех процессов

# __ starmap async __
# после выполнения каждого Pool возвращает результат
import random
import multiprocessing

def end_func(response):
    print(f"Выполнен: {multiprocessing.current_process().name}, вернул: {response}")
    return response


def print_value(x, y, z):
    name_curr_p = multiprocessing.current_process().name
    print(f"[{name_curr_p}] x: {x}, y: {y}, z: {z}")
    return x, y, z


if __name__ == '__main__':
    cpu_cnt = int(multiprocessing.cpu_count() / 2)
    # p = multiprocessing.Pool(processes=cpu_cnt)
    with multiprocessing.Pool(processes=cpu_cnt) as p:
        # Каждый последующий Pool возьмет по одному кортежу, то есть
        # у каждого процесса свой кортеж из списка
        p.starmap_async(print_value, [(1, 2, 3), (4, 5, 6), (7, 8, 9)], callback=end_func)
        p.close()  # после того как вызвали map_async, нам нужно закрыть наш Pool
        p.join()  # и также вызвать join() который позволяет дождаться выполнения всех процессов
