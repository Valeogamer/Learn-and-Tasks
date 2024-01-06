from time import perf_counter  # измеряет время более точно
from functools import wraps
import typing as tp

# кэширование, в одном цикле работы, после отключения все стирается.


def memory(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(*args)
        if key not in cache:
            print("Was not in the cache.")
            cache[key] = func(*args, **kwargs)
        else:
            print("Return from cache.")
        return cache[key]

    return wrapper


@memory
def stress_test(iter_num: tp.Union[int, float]) -> tp.Union[int, float]:
    result = 2
    for n in range(iter_num):
        result **= 2
    return result


def main():
    for _ in range(1):
        start = perf_counter()
        stress_test(30)
        end = perf_counter()
        print(f"stress_test: {(end - start):0.7f}\n")


if __name__ == '__main__':
    main()
