import numpy as np

input_layer = [(-1, -1, -1, -1)]  # X
target = input_layer[0][-1]  # Y

W1 = np.array([[-0.2, 0.3, -0.4], [0.1, -0.3, -0.4]])
B1 = np.array([0.1, 0.2])
W2 = np.array([[0.4, 0.1], [-0.1, 0.6]])
B2 = np.array([0.3, 0.1])
W3 = np.array([0.3, 0.2])
B3 = np.array([0.4])


def mse(y_pred, target):
    return 0.5 * (y_pred - target) ** 2


def d_mse(y_pred, target):
    return y_pred - target


def sigmoida(x):
    return 1 / 1 + np.exp(-x)


def d_sigmoida(x):
    return sigmoida(x) * (1 - sigmoida(x))


# Прямое распространение
out_h1 = [sigmoida(out) for out in np.dot(W1, input_layer[0][:3]) + B1]
out_h2 = [sigmoida(out) for out in np.dot(W2, out_h1) + B2]
y_pred = sigmoida(np.dot(W3, out_h2) + B3)

# Ошибки
error = mse(y_pred, target)  # MSE ниже производная от MSE

# Обратное распространение
# Обратное распространение
l_r = 0.001  # скорость обучения
e = d_mse(y_pred, target)  # ошибка

delta = e * d_sigmoida(np.dot(W3, out_h2) + B3)  # локальный градиент для выходного слоя

# Корректировка весов для W3 и B3
W3[0] = W3[0] - l_r * delta * out_h2[0]
W3[1] = W3[1] - l_r * delta * out_h2[1]
B3 = B3 - l_r * delta

# Расчет локального градиента для скрытого слоя 2 (out_h2)
delta2 = np.multiply(delta, W3) * d_sigmoida(np.dot(W2, out_h1) + B2)

# Корректировка весов для W2 и B2
W2[0][0] = W2[0][0] - l_r * delta2[0] * out_h1[0]
W2[0][1] = W2[0][1] - l_r * delta2[0] * out_h1[1]
W2[1][0] = W2[1][0] - l_r * delta2[1] * out_h1[0]
W2[1][1] = W2[1][1] - l_r * delta2[1] * out_h1[1]
B2[0] = B2[0] - l_r * delta2[0]
B2[1] = B2[1] - l_r * delta2[1]

# Расчет локального градиента для скрытого слоя 1 (out_h1)
delta1 = np.multiply(np.dot(W2.T, delta2), d_sigmoida(np.dot(W1, input_layer[0][:3]) + B1))

# Корректировка весов для W1 и B1
W1[0][0] = W1[0][0] - l_r * delta1[0] * input_layer[0][0]
W1[0][1] = W1[0][1] - l_r * delta1[0] * input_layer[0][1]
W1[0][2] = W1[0][2] - l_r * delta1[0] * input_layer[0][2]
W1[1][0] = W1[1][0] - l_r * delta1[1] * input_layer[0][0]
W1[1][1] = W1[1][1] - l_r * delta1[1] * input_layer[0][1]
W1[1][2] = W1[1][2] - l_r * delta1[1] * input_layer[0][2]
B1[0] = B1[0] - l_r * delta1[0]
B1[1] = B1[1] - l_r * delta1[1]
