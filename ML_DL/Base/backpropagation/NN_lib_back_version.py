import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Ваш набор данных
dataset = [(-1, -1, -1, -1),
           (-1, -1, 1, 1),
           (-1, 1, -1, -1),
           (-1, 1, 1, 1),
           (1, -1, -1, -1),
           (1, -1, 1, 1),
           (1, 1, -1, -1),
           (1, 1, 1, -1)]

# Разделяем данные на входные признаки и целевые значения
data = np.array(dataset)
X = data[:, :-1]  # Входные признаки (первые три столбца)
y = data[:, -1]   # Целевые значения (последний столбец)

# Создаем модель
model = keras.Sequential([
    layers.Input(shape=(3,)),        # Входной слой с 3 нейронами
    layers.Dense(2, activation='relu'),  # Первый скрытый слой с 2 нейронами
    layers.Dense(2, activation='relu'),  # Второй скрытый слой с 2 нейронами
    layers.Dense(1, activation='linear')  # Выходной слой с линейной активацией (для регрессии)
])

# Компилируем модель с использованием MSE в качестве функции потерь
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

# Обучаем модель
model.fit(X, y, epochs=100, batch_size=2)

# Оцениваем модель
loss, mse = model.evaluate(X, y)
print(f"Потери: {loss:.4f}, MSE: {mse:.4f}")

# Предсказываем значения
predictions = model.predict(X)
print("Предсказания:")
for i in range(len(X)):
    print(f"Входные данные: {X[i]}, Предсказание: {predictions[i][0]:.2f}")
