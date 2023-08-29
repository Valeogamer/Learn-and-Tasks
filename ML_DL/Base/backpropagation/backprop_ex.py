"""
Если забыл пересмотри видео у SelfEdu
"""

import numpy as np

# Параметры
LEARNING_RATE: float = 0.5

# Веса для нашей НС
W1 = np.array([[-0.2, 0.3, -0.4], [0.1, -0.3, -0.4]])
W2 = np.array([0.2, 0.3])

# обучающая выборка (она же полная выборка)
# x[0:3] - на входе что
# x[-1] - какой должен быть результат
EPOCH = [(-1, -1, -1, -1),
         (-1, -1, 1, 1),
         (-1, 1, -1, -1),
         (-1, 1, 1, 1),
         (1, -1, -1, -1),
         (1, -1, 1, 1),
         (1, 1, -1, -1),
         (1, 1, 1, -1), ]


def f(x: float) -> float:
    """
    Функция активации
    Гиперболический тангенс
    """
    return 2 / (1 + np.exp(-x)) - 1


def df(x: float) -> float:
    """
    Производная функции активации
    """
    global LEARNING_RATE
    return LEARNING_RATE * (1 + x) * (1 - x)


def go_forward(inp: list) -> tuple[float, float]:
    """
    Прямое распространение
    notes:  np.dot([1, 2], [1, 4]) = 9
    """
    summ = np.dot(W1, inp)
    out = np.array([f(x) for x in summ])  # выход первого слоя

    summ = np.dot(W2, out)
    y = f(summ)  # Выход последнего слоя
    return (y, out)


def train(epoch):
    """
    Обучение НС
    """
    global W2, W1, EPOCH
    lmd = 0.01  # шаг обучения
    N = 10_000  # число итераций при обучении
    count = len(EPOCH)
    for k in range(N):
        x = EPOCH[np.random.randint(0, count)]  # случайный выбор входного сигнала из обучающей выборки
        y, out = go_forward(x[0:3])  # прямой проход по НС и вычисление выходных значений НС
        e = y - x[-1]  # ошибка
        delta = e * df(y)  # локальный градиент
        W2[0] = W2[0] - lmd * delta * out[0]  # корректировка веса первой связи
        W2[1] = W2[1] - lmd * delta * out[1]  # корректировка веса второй связи

        delta2 = W2 * delta * df(out)

        # корректировка связей первого слоя
        W1[0, :] = W1[0, :] - np.array(x[0:3]) * delta2[0] * lmd
        W1[1, :] = W1[1, :] - np.array(x[0:3]) * delta2[1] * lmd


if __name__ == '__main__':
    train(EPOCH)

    # Проверка полученных результатов
    for x in EPOCH:
        y, out = go_forward(x[0:3])
        print(f"Выходное значение НС: {y} => {x[-1]}")
