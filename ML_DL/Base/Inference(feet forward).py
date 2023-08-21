"""
Данная реализация только для прямого распространения.
Прямое распространения, функция активации(sigmoid), функция активации выходного слоя(softmax)

Без функции ошибок (Loss)
Без обратного распространения (backpropagation)
"""
import numpy as np


def create_input(num: int) -> list[float]:
    """
    Формирование списка со входными значениями X_i
    Генерация чисел в диапазоне от 0 до 10
    """
    return np.array([np.random.randint(10) for _ in range(num)])


def creat_weight(x: list[float], layer: int) -> list[list[float]]:
    """
    Формирование весов
    """
    return np.array([np.random.rand(len(x)) for _ in range(layer)])


def create_bias(w: list[list[float]]) -> list[float]:
    """
    Вектор столбец со значением смещения
    """
    # FIXME: 1) Можно заменить np.ones()
    return np.array([1 for _ in range(len(w))])


def sigmoid(h: list[float]) -> list[float]:
    """
    Функция активации Сигмоида
    (нормализация)
    """
    return 1 / (1 + np.exp(-h))


def softmax(h_i: list[float]) -> list[float]:
    """
    Функция выходного слоя получения вероятности
    """
    return [np.exp(h) / np.sum([np.exp(h) for h in h_i]) for h in h_i]


def inference(x: int, p_layer: int, y: int) -> list[float]:
    """
    Прямое распространение
    x: Кол-во на входе
    p_layer: Кол-во точек на скрытом слое (если передать в виде списка то еще можно кол во скрытых слоев)
    y: Кол-во на выходе
    """
    # FIXME: 1) Можно улучшить рекурсией 2) len(p_layer) - кол-во скрытых слоев, значения списка кол-во нейронов
    x_i = create_input(x)
    w_i = creat_weight(x_i, p_layer)
    b_i = create_bias(w_i)
    w_i = w_i.transpose()
    h_i = [sigmoid(h) for h in x_i @ w_i + b_i]
    w_i = creat_weight(h_i, y)
    b_i = create_bias(w_i)
    w_i = w_i.transpose()
    output = softmax(h_i @ w_i + b_i)
    return output


def check_output_p(output: list[float]) -> float:
    """
    Проверка вероятностей выходного слоя
    """
    return np.sum(output)


if __name__ == '__main__':
    # на входе 3 скртый слой 5 на выходе 3
    # гиперпараметры
    output = inference(3, 5, 3)
    print(output)
