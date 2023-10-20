import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance(point1, point2):
    return math.sqrt(np.sum((point2 - point1) ** 2))

def sort_and_calculate_distances(points):
    sorted_points = points[points[:, 0].argsort()]
    distances = []
    for i in range(len(sorted_points) - 1):
        distances.append(distance(sorted_points[i], sorted_points[i+1]))
    return sorted_points, distances

# Генерация рандомных точек
num_points = 5
points = np.random.rand(num_points, 3)

print("Сгенерированные точки:")
print(points)

sorted_points, distances = sort_and_calculate_distances(points)
print("Расстояния между точками:")
print(distances)

# Отображение точек
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')

# Отображение отсортированных точек и соединение линиями
for i in range(num_points - 1):
    ax.plot(sorted_points[i:i+2, 0], sorted_points[i:i+2, 1], sorted_points[i:i+2, 2], c='r')

# Настройки графика
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
