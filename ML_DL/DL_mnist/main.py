# Урок от Haudi Ho (https://youtu.be/tihq_bLfk08)
import numpy as np
import matplotlib.pyplot as plt
import utils

# загрузка обработанного датасета
images, labels = utils.load_dataset()
#  инициализируем матрицу вессов 784 на 20 с входного на скрытый слой
#  инициализируем матрицу вессов 10 на 20 с скрытого на выходной слой
weights_input_to_hidden = np.random.uniform(-0.5, 0.5, (20, 784))
weights_hidden_to_output = np.random.uniform(-0.5, 0.5, (10, 20))

# матрица нейрона смещения (bias)
bias_input_to_hidden = np.zeros((20, 1))
bias_hidden_to_output = np.zeros((10, 1))

#  Переходим к обучению нейросети (процессу корекции весов)
epochs = 3
e_loss = 0
e_correct = 0
loss = 0
learning_rate = 0.01  # Скорость обучения
for epoch in range(epochs):  # итерируем все наши изображения столько раз, сколько у нас эпох обучения
    print(f"Epoch №{epoch}")
    #  Также сразу перебрасываем изображение и его класс в форму двумерного массива, так как дальше
    #  они будут использованы для перемножения матриц, ну а эпохи обучения нужны нам для того чтобы некоторое количество раз
    #  корректировать веса на всем датасете
    for image, label in zip(images, labels):
        image = np.reshape(image, (-1, 1))
        label = np.reshape(label, (-1, 1))

        # Дальше первый этап обучения (Forward Propagation)
        # Он нужен для того чтобы скормить нейросети входные данные, прогнать их через скрытые слои
        # И наконец получить выходные данные
        # Forward propagation
        hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
        # однако значения нейронов могут получиться гораздо больше или меньше ожидаемого диапазона
        # поэтому их нужно еще нормализовать для этого пользуются функцией активации (sigmoid)
        hidden = 1 / (1 + np.exp(-hidden_raw))  # Функция активации (sigmoid)

        # Аналогичные действия и для выходного слоя
        output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
        output = 1 / (1 + np.exp(-output_raw))  # Функция активации (sigmoid)

        #  получим массив из 10 элементов которая отражает процент совпадения
        #  с тем или иным классом

        # после того как получили значения после первого обучения
        # надо проверить насколько наш выхлоп отличается от фактического значения храниться в label
        # и нейросеть максимальна должна к нему приблизиться
        # Также как и для функции активации, для функции потерь существует много разных функции
        # Мы возьмем самую простую и популярную MSE (Mean Squared Error)

        # Loss / Error calculation
        e_loss += 1 / len(output) * np.sum((output - label) ** 2, axis=0)
        e_correct += int(np.argmax(output) == np.argmax(label))

        # Backpropagation - именно этот алгоритм отвечает за обучение нейросети
        # Производим корректировку весов в обратном направлении
        # До тех пор пока либо функции ошибки не уменьшиться или эпохи не пройдут
        # Backpropagation(outputlayer)
        delta_output = output - label
        weights_hidden_to_output += -learning_rate * delta_output @ np.transpose(hidden)
        bias_hidden_to_output += -learning_rate * delta_output

        # Backpropagation(hidden layer)
        delta_hidden = np.transpose(weights_hidden_to_output) @ delta_output * (hidden * (1 - hidden))
        weights_input_to_hidden += -learning_rate * delta_hidden @ np.transpose(image)
        bias_input_to_hidden += -learning_rate * delta_hidden

        # DONE


    # print info
    print(f"Loss: {round((e_loss[0] / images.shape[0]) * 100, 3)}%")
    print(f"Accuracy: {round((e_correct / images.shape[0]) * 100, 3)}%")
    e_loss = 0
    e_correct = 0

# для проверки что на самом деле и что предсказал
while True:
    index = int(input("Enter a number (0 - 59999): "))
    img = images[index]
    plt.imshow(img.reshape(28, 28), cmap="Greys")
    img.shape += (1,)
    # Forward propagation input -> hidden
    h_pre = bias_input_to_hidden + weights_input_to_hidden @ img.reshape(784, 1)
    h = 1 / (1 + np.exp(-h_pre))
    # Forward propagation hidden -> output
    o_pre = bias_hidden_to_output + weights_hidden_to_output @ h
    o = 1 / (1 + np.exp(-o_pre))

    plt.title(f"Subscribe if its a {o.argmax()} :)")
    plt.show()