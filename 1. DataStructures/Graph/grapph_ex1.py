import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # расстояние вершина

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)  # извлечение наимаеньшего элемента из кучи

        # если текущее расстояние больше расстояния следующей вершины то продолжить
        if current_distance > distances[current_vertex]:
            continue

        # перебираем соседей текущей вершины ключ значения словаря внутри словаря
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight  # вычисляем расстояние от текущей вершины до соседей
            # если получившееся расстояние меньше ребра соседа, то расстояние вершины 2 будет расстояние d = c_d + w и
            # добавляем в кучу значение для вершины 2 и саму вершину
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == '__main__':
    # Создаем граф (словарь) с вершинами и весами ребер
    graph = {
        1: {2: 7, 3: 9, 6: 14},
        2: {3: 10, 4: 15},
        3: {4: 11, 6: 2},
        4: {5: 6},
        5: {6: 9},
        6: {}
    }

    start_vertex = 1
    shortest_distances = dijkstra(graph, start_vertex)

    # Выводим результат
    for vertex, distance in shortest_distances.items():
        print(f"Кратчайшее расстояние от вершины {start_vertex} до вершины {vertex}: {distance}")
