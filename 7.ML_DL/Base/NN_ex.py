import numpy as np

# Гиперпараметры
input_size = 2
hidden_size = 3
output_size = 1
learning_rate = 0.1

# Веса и смещения для первого и второго слоев
weights_input_hidden = np.random.rand(input_size, hidden_size)
bias_hidden = np.random.rand(1, hidden_size)
weights_hidden_output = np.random.rand(hidden_size, output_size)
bias_output = np.random.rand(1, output_size)

# Входные данные (пример)
input_data = np.array([[0.5, 0.8]])
target_output = np.array([[1.0]])  # Фактический результат

# Прямое и обратное распространение
for epoch in range(10):
    # Прямое распространение
    hidden_layer_input = np.dot(input_data, weights_input_hidden) + bias_hidden
    hidden_layer_output = 1 / (1 + np.exp(-hidden_layer_input))
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = 1 / (1 + np.exp(-output_layer_input))

    # Вычисление ошибки
    error = target_output - predicted_output

    # Обратное распространение
    d_output = error * predicted_output * (1 - predicted_output)
    error_hidden_layer = np.dot(d_output, weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * hidden_layer_output * (1 - hidden_layer_output)

    # Обновление весов и смещений
    weights_hidden_output += np.dot(hidden_layer_output.T, d_output) * learning_rate
    bias_output += np.sum(d_output) * learning_rate
    weights_input_hidden += np.dot(input_data.T, d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer) * learning_rate

print("Predicted Output after Training:", predicted_output)