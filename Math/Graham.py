import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Генерация случайных точек
np.random.seed(0)
points = np.random.rand(20, 2)  # 10 случайных точек в диапазоне [0, 1) x [0, 1)

# Построение выпуклой оболочки
hull = ConvexHull(points)

# Визуализация точек и контура
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.title('Выпуклая оболочка')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Вычисление площади
area = hull.volume
print("Площадь фигуры:", area)
