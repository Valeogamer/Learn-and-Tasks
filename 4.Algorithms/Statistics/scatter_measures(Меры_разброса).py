import numpy as np
from typing import Any

from numpy import ndarray


def mean_v(values: list[float]) -> tuple[Any, ndarray]:
    """
    Математическое ожидание
    Среднее значение
    """
    # np.mean()  # среднее значение
    return (np.sum(values) / len(values), np.mean(values))


def dispersion_v(values: list[float]) -> tuple[Any, ndarray]:
    """
    Дисперсия
    """
    # np.var(values)  # вычисление дисперсии numpy
    return (np.sum([(i - mean_v(values)[1]) ** 2 for i in values])) / len(values), np.var(values)


def standard_deviation_v(values: list[float]) -> tuple[Any, ndarray]:
    """
    Стандартное отклонение
    """
    # np.std(values)  # Стандартное отклонение
    return np.sqrt(np.sum([(i - mean_v(values)[1]) ** 2 for i in values]) / len(values)), np.std(values)


def root_mean_SD(values: list[float]) -> tuple[Any, ndarray]:
    """
    Среднеквадратичное отклонение
    """
    # np.std(values, ddof=1)  # Среднеквадратичное отклонение
    return (np.sum([(i - mean_v(values)[1]) ** 2 for i in values]) / len(values) - 1) ** (1 / 2), np.std(values, ddof=1)


def range_v(values: list[float]) -> tuple[ndarray]:
    """
    Диапазон
    """
    return np.amax(values) - np.amin(values)


if __name__ == '__main__':
    values: list[float] = [1, 2, 3, 4, 5]
    print("Среднее значени (мат ожидание):", mean_v(values))
    print("Дисперсия:", dispersion_v(values))
    print("Стандартное отклонение:", standard_deviation_v(values))
    print("Среднеквадратичное отклонение:", root_mean_SD(values))
    print("Диапазон:", range_v(values))

