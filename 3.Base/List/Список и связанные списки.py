# Определение класса для узла связанного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    print("_______Создание связанного списка_______")
    head = Node(111)
    node2 = Node(232)
    node3 = Node(4533)

    head.next = node2
    node2.next = node3

    # Перебор элементов связанного списка
    current = head
    while current is not None:
        print(current.data)
        current = current.next

    print("_______Создание списка_______")
    arr = [1, 2, 3, 4, 5]

    # Доступ к элементам по индексу
    print(arr[0])  # Вывод: 1
    print(arr[2])  # Вывод: 3

    # Изменение элемента
    arr[3] = 10
    print(arr)  # Вывод: [1, 2, 3, 10, 5]

    # Длина списка
    print(len(arr))  # Вывод: 5
