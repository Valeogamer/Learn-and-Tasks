"""
Входной слой (input layer): 3 нейрона (монитор, системный блок, клава+мышь)
Скрытый слой (hidden layer): 2 слоя по 2 нейрона
Выходной слой (output layer): 1 нейрон
"""
from typing import List

import numpy as np

# датасет
data = [(-1, -1, -1, -1),
        (1, 1, 1, 1),
        (-1, 1, 1, 1),
        (1, -1, 1, -1),
        (1, 1, -1, 1),
        (-1, -1, 1, -1),
        (1, -1, -1, -1)]

# Входной вектор
X = data[0][:3]

# Ожидаемый отклик
TARGET = data[0][-1]

# Веса и смещения
W1 = np.array(np.random.uniform(-1, 1, size=(2, 3)))
B1 = np.array(np.random.uniform(-1, 1, size=(2,)))
W2 = np.array(np.random.uniform(-1, 1, size=(2, 2)))
B2 = np.array(np.random.uniform(-1, 1, size=(2,)))
W3 = np.array(np.random.uniform(-1, 1, size=(2,)))
B3 = np.array(np.random.uniform(-1, 1, size=(1,)))

# Скорость обучения
LR = 0.001  # LEARNING RATE

def sigmoida(x: float) -> float:
    """
    Функция активации: Сигмоида
    """
    return 1 / (1 + np.exp(-x))


def tanh(x: float) -> float:
    """
    Функция активации: Гиперболический тангенс
    """
    return 2 / (1 + np.exp(-x)) - 1


def feedforward() -> set[float]:
    """
    Прямое распространение f(W*x + b), f() - функция активации (сигмоида)
    """
    out_h1: list[float] = [sigmoida(out) for out in np.dot(W1, X) + B1]
    out_h2: list[float] = [sigmoida(out) for out in np.dot(W2, out_h1) + B2]
    y: list[float] = [sigmoida(out) for out in np.dot(W3, out_h2) + B3]
    return (y, out_h2, out_h1)


def MSE(y_pred, y_true):
    """
    Функция потерь: MSE
    """
    return 0.5 * (y_pred - y_true) ** 2

def d_MSE(y_pred, y_true):
    """
    Производная MSE
    """
    return y_pred - y_true

def backprop():
    """
    Обратное распространение
    """
    # Прямое распространение для получения выхода
    global W1, B1, W2, B2, W3, B3




if __name__ == '__main__':
    backprop()
