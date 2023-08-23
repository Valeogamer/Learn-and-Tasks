import numpy as np

# Параметры
LEARNING_RATE: float = 0.5


def f(x: float) -> float:
    """
    Функция активации
    """
    return 2 / (1 + np.exp(-x)) - 1


def df(x: float) -> float:
    """
    Производная функции активации
    """
    return LEARNING_RATE * (1 + x) * (1 - x)


if __name__ == '__main__':
    pass
