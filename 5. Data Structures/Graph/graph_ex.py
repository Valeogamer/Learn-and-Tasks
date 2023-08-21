import networkx as nx
import matplotlib.pyplot as plt

# Создаем направленный взвешенный граф
G = nx.DiGraph()
G.add_edge(1, 2, weight=7)
G.add_edge(1, 3, weight=9)
G.add_edge(1, 6, weight=14)
G.add_edge(2, 3, weight=10)
G.add_edge(2, 4, weight=15)
G.add_edge(3, 4, weight=11)
G.add_edge(3, 6, weight=2)
G.add_edge(4, 5, weight=6)
G.add_edge(5, 6, weight=9)

# Рисуем граф (опционально)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Находим кратчайший путь от вершины 1 до вершины 5
shortest_path = nx.shortest_path(G, source=1, target=5, weight='weight')
shortest_distance = nx.shortest_path_length(G, source=1, target=5, weight='weight')

print("Кратчайший путь:", shortest_path)
print("Длина кратчайшего пути:", shortest_distance)
