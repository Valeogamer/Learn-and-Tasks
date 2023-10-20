import multiprocessing
import random

def end_func(response):
    print("Задание завершено!")
    print(response)

def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}] value: {value}")
    return value

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.map_async(get_value, list(range(100)), callback=end_func)  # смотри еще apply_async
        p.close()
        p.join()
