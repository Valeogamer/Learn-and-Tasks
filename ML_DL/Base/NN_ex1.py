import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        self.weights = []
        self.biases = []

        sizes = [input_size] + hidden_sizes + [output_size]
        for i in range(len(sizes) - 1):
            self.weights.append(np.random.rand(sizes[i], sizes[i+1]))
            self.biases.append(np.random.rand(1, sizes[i+1]))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, x):
        layer_output = x
        layer_outputs = [layer_output]

        for i in range(len(self.weights)):
            layer_input = np.dot(layer_output, self.weights[i]) + self.biases[i]
            layer_output = self.sigmoid(layer_input)
            layer_outputs.append(layer_output)

        return layer_outputs

    def train(self, input_data, target_output, learning_rate, num_epochs):
        for epoch in range(num_epochs):
            for x, target in zip(input_data, target_output):
                layer_outputs = self.forward(x)

                # Обратное распространение
                error = target - layer_outputs[-1]
                d_output = error * self.sigmoid_derivative(layer_outputs[-1])

                d_hidden = d_output
                for i in range(len(self.hidden_sizes) - 1, 0, -1):
                    d_hidden = np.dot(d_hidden, self.weights[i+1].T) * self.sigmoid_derivative(layer_outputs[i])
                    self.weights[i] += np.dot(layer_outputs[i-1].reshape(-1, 1), d_hidden) * learning_rate
                    self.biases[i] += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

                d_hidden = np.dot(d_hidden, self.weights[1].T) * self.sigmoid_derivative(layer_outputs[0])
                self.weights[0] += np.dot(x.reshape(-1, 1), d_hidden) * learning_rate
                self.biases[0] += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# Пример использования
input_size = 5
hidden_sizes = [4, 3]  # Минимум два скрытых слоя
output_size = 1
learning_rate = 0.1
num_epochs = 1000

nn = NeuralNetwork(input_size, hidden_sizes, output_size)

input_data = np.random.rand(10, input_size)
target_output = np.random.rand(10, output_size)

nn.train(input_data, target_output, learning_rate, num_epochs)

new_input = np.random.rand(1, input_size)
predicted_output = nn.forward(new_input)[-1]
print("Predicted Output:", predicted_output)
