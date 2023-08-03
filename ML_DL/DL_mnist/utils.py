import numpy as np
import matplotlib.pyplot as plt


def load_dataset():
    """
    Загрузка датасета
    """
    with np.load("mnist.npz") as f:
        #  convert from RGB to Unit RGB (перебрасываем в значения от 0 до 1)
        x_train = f['x_train'].astype("float32") / 255
        # reshape from (60_000, 28, 28) into (60_000, 784) 28*28 =784
        # переводи в вектор строку, массив строку (входные слой, данные)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]* x_train.shape[2]))
        # метки
        y_train = f['y_train']
        # convert to output layer format
        # приводит классы датасета к удобному дял нас формату
        # Так как 10 классов, 10 вариантов ответа
        # то есть пример 1 это = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # то есть пример 2 это = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] и так далее
        y_train = np.eye(10)[y_train]
        return x_train, y_train