import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def euclidean_distance(point_0, point_1):
    return np.sqrt((point_0[0] - point_1[0]) ** 2 + (point_0[1] - point_1[1]) ** 2 + (point_0[2] - point_1[2]) ** 2)


def all_dist(coords):
    mat_coords_dist = []
    for coord_0 in coords:
        c_1 = []
        for coord_1 in coords:
            c_1.append(euclidean_distance(coord_0, coord_1))
        mat_coords_dist.append(c_1)
    return mat_coords_dist


if __name__ == '__main__':
    coords_mat = []
    for i in range(5):
        coords_mat.append([np.random.rand(), np.random.rand(), np.random.rand()])
    mat_coords_dist = all_dist(coords_mat)
    print(np.round(mat_coords_dist, 2))  # Вывод матрицы смежности

    # Преобразуем матрицу смежности в граф для использования в NetworkX
    G = nx.Graph()
    num_points = len(mat_coords_dist)

    for i in range(num_points):
        for j in range(i + 1, num_points):
            G.add_edge(i, j, weight=mat_coords_dist[i][j])

    # Найдите индексы точек с минимальной и максимальной координатой (по x, y и z)
    min_index = np.argmin(coords_mat, axis=0)
    max_index = np.argmax(coords_mat, axis=0)

    # Выведите информацию о точке с минимальным значением координаты
    print("Точка с минимальным значением координаты:", coords_mat[min_index[0]])
    graph_0 = min_index[0]

    # Выведите информацию о точке с максимальным значением координаты
    print("Точка с максимальным значением координаты:", coords_mat[max_index[0]])
    graph_exit = max_index[0]

    # Найдите кратчайший путь с помощью алгоритма Дейкстры от точки 0 к выходу
    shortest_path_to_exit = nx.shortest_path(G, source=graph_0, target=graph_exit, weight='weight')
    shortest_path_to_exit = np.round(shortest_path_to_exit, 2)
    # Выведите кратчайший путь к выходу и его длину
    print("Кратчайший путь к выходу:", shortest_path_to_exit)
    print("Длина кратчайшего пути к выходу:",
          nx.shortest_path_length(G, source=graph_0, target=graph_exit, weight='weight'))

    # Добавим промежуточные точки пути
    intermediate_points = [shortest_path_to_exit[0]]
    for i in range(1, len(shortest_path_to_exit) - 1):
        curr_node = shortest_path_to_exit[i]
        next_node = shortest_path_to_exit[i + 1]

        # Найдем ближайшую точку к следующему узлу
        nearest_node = min(G.neighbors(curr_node), key=lambda node: G[node][next_node]['weight'])

        intermediate_points.append(nearest_node)

    # Добавим граф выхода в промежуточные точки
    intermediate_points.append(graph_exit)

    # Выведем промежуточные точки пути
    print("Промежуточные точки пути:", intermediate_points)

    # Визуализируйте граф и кратчайший путь (требуется matplotlib)
    pos = {i: coords_mat[i][:2] for i in range(num_points)}  # Используйте только первые две координаты для визуализации
    nx.draw(G, pos, with_labels=True, node_size=3000, font_size=10)
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path_to_exit, node_color='r', node_size=5000)
    nx.draw_networkx_edges(G, pos,
                           edgelist=[(shortest_path_to_exit[i], shortest_path_to_exit[i + 1]) for i in
                                     range(len(shortest_path_to_exit) - 1)],
                           edge_color='r', width=2)

    # Выведем значения длин ребер на ребрах графа
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()
