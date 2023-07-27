import numpy as np
import matplotlib.pyplot as plt


def linear_approximate(x: list[float], y: list[float]) -> tuple[float, float, float]:
    """
    Функция апроксимации методом НМК
    Линейная апроксимация
    """
    # ax + b = y
    # a = (len(x) * sum_xi_yi - sum_xi * sum_yi) / (len(x) * sum_xi_xi - np.power(sum_xi, 2))
    # b = (sum_yi - a * sum_xi) / len(x)
    _, _ = x, y
    sum_xi_yi = np.sum(np.multiply(x, y))
    sum_xi = np.sum(x)
    sum_yi = np.sum(y)
    sum_xi_xi = np.sum(np.multiply(x, x))
    a = (len(x) * sum_xi_yi - sum_xi * sum_yi) / (len(x) * sum_xi_xi - np.power(sum_xi, 2))
    b = (sum_yi - a * sum_xi) / len(x)

    def linear_function(x):
        return a * x + b

    return a, b, linear_function


def quadratic_approximate(x: list[float], y: list[float]) -> tuple[float, float, float, float]:
    """
    Функция апроксимации методом НМК
    Квадратичная апроксимация
    """
    a = None
    b = None
    c = None
    # ax^2 + bx + c = y^2
    # S(a,b,c) = sum(ax^2+bx+c - y)^2
    # Найдем производную и преобразуем
    # Sa' = sum_xi_4 * a + sum_xi_3 * b + sum_xi_2 * c  = sum_xixi_yi
    # Sb' = sum_xi_3 * a + sum_xi_2 * b + sum_xi_1 * c =  sum_xi_yi
    # Sc' = sum_xi_2 * a + sum_xi_1 * b + c = sum_yi
    # Получаем все необходимые значения
    sum_xi_1 = np.sum(x)
    sum_xi_2 = np.sum(np.power(x, 2))
    sum_xi_3 = np.sum(np.power(x, 3))
    sum_xi_4 = np.sum(np.power(x, 4))
    sum_xi_yi = np.sum(np.multiply(x, y))
    sum_xixi_yi = np.sum(np.multiply(np.power(x, 2), y))
    sum_yi = np.sum(y)

    # Решим СЛАУ (Sa, Sb, Sc) методом крамера
    A = np.array([[sum_xi_4, sum_xi_3, sum_xi_2],  # значения с каждой строчки
                  [sum_xi_3, sum_xi_2, sum_xi_1],  # значения с каждой строчки
                  [sum_xi_2, sum_xi_1, 1]])  # значения с каждой строчки

    B = np.array([sum_xixi_yi, sum_xi_yi, sum_yi])  # значения после равно

    X = np.linalg.solve(A, B)  # Решение слау, получаем коэфициенты

    a = X[0]
    b = X[1]
    c = X[2]

    # print(f'Коэффициенты: a={a:.3f}, b={b:.3f}, c={c:.3f}')

    def quadric_function(x):
        return a * x * x + b * x + c

    return a, b, c, quadric_function


def loss_function(x, y, extra_fn):
    y_pred = np.array([extra_fn(i) for i in x])
    loss = np.subtract(y_pred, y)
    loss = np.sum(np.power(loss, 2))
    print(f"Loss: {loss:.3f}")
    return y_pred


def plot_xy(x: list[float], y: list[float], y_pred=None):
    plt.figure(figsize=(10, 5))
    if any(y_pred):
        plt.plot(x, y_pred, '-ro', label='y_pred')
    plt.plot(x, y, '-go', label='y')
    plt.legend(loc='best', fontsize=12)
    plt.show()


def windows_size(return_size: bool = None) -> list[float, float]:
    """
    Информация о размере окна
    retrun: list[x:float, y:float]
    """
    fig = plt.gcf()
    window_size_inches = fig.get_size_inches()
    print("Размер окна:", window_size_inches)
    if return_size:
        return window_size_inches


if __name__ == '__main__':
    x: list[float] = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    y: list[float] = np.array([3, 5, 7, 9, 11, 14, 17, 21, 25, 30, 35, 40, 46, 52, 59, 67, 75, 84, 94, 105])
    # a, b, linear_fn = linear_approximate(x, y)
    # y_pred = loss_function(x, y, linear_fn)
    a, b, c, quadratic_fn = quadratic_approximate(x, y)
    y_pred = loss_function(x, y, quadratic_fn)
    plot_xy(x, y, y_pred)
