# Вызовем просто модуль который умеет делать все то же самое что и модули 01 и 02
from time import perf_counter  # измеряет время более точно
from functools import cache
import typing as tp


# Кэширование готовым модулем py

@cache
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
