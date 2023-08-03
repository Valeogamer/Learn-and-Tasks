import itertools
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def calculate_total_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += euclidean_distance(points[order[i]], points[order[i + 1]])
    return total_distance


def find_shortest_path(points):
    shortest_distance = float('inf')
    shortest_path = []

    for order in itertools.permutations(range(len(points))):
        distance = calculate_total_distance(points, order)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = order

    return shortest_path, shortest_distance


if __name__ == '__main__':
    points = [(np.random.rand(), np.random.rand() + np.random.randint(1, 3), np.random.rand()),
              (np.random.rand(), np.random.rand() + np.random.randint(1, 3), np.random.rand()),
              (np.random.rand(), np.random.rand() + np.random.randint(1, 3), np.random.rand()),
              (np.random.rand(), np.random.rand() + np.random.randint(1, 3), np.random.rand())]

    shortest_path, shortest_distance = find_shortest_path(points)

    print("Самый короткий путь:", shortest_path)
    print("Весь кратчайший путь:", shortest_distance)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for point in points:
        ax.scatter(point[0], point[1], point[2], c='r', marker='*')

    for i in range(len(shortest_path) - 1):
        p1 = points[shortest_path[i]]
        p2 = points[shortest_path[i + 1]]
        distance = euclidean_distance(p1, p2)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], c='b')
        ax.text((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2, (p1[2] + p2[2]) / 2, f'{distance:.2f}', color='g')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
