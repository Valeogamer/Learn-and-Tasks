from time import perf_counter  # измеряет время более точно
from functools import wraps
import typing as tp
import os
import shelve


# Кэширование в локальный диск.


def memory(func):
    cache_filename = "cache"
    if not os.path.exists(cache_filename):
        with shelve.open(cache_filename, "c") as db:
            pass

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(*args)
        with shelve.open(cache_filename) as db:
            try:
                return db[key]
                print("Return from cache.")
            except KeyError:
                db[key] = func(*args, **kwargs)
                print("Was not in the cache.")
            finally:
                return db[key]

    return wrapper


@memory
def stress_test(iter_num: tp.Union[int, float]) -> tp.Union[int, float]:
    result = 2
    for n in range(iter_num):
        result **= 2
    return result


def main():
    for _ in range(2):
        start = perf_counter()
        stress_test(30)
        end = perf_counter()
        print(f"stress_test: {(end - start):0.7f}\n")


if __name__ == '__main__':
    main()
