import numpy as np
from numba import njit
from time import perf_counter
import math


def f(x, y):
    a = np.dot(x, y)
    return a


@njit
def f_njit(x, y):
    a = np.dot(x, y)
    return a


@njit(fastmath=True)
def f_math(x, y):
    a = np.dot(x, y)
    return a


if __name__ == '__main__':
    x = np.arange(1_000_000)
    y = np.arange(1_000_000)
    start = perf_counter()
    a = f(x, y)
    end = perf_counter()
    print(f'@time: [{end - start:.08f}]')
    start = perf_counter()
    b = f_njit(x, y)
    end = perf_counter()
    print(f'@time: [{end - start:.05f}]')
    start = perf_counter()
    c = f_math(x, y)
    end = perf_counter()
    print(f'@time: [{end - start:.05f}]')
