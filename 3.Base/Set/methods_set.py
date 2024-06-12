a = {0,}
c = {3, 4, 10, 9, 8, 7}
def set_add():
    """
    Добавить число к множеству.
    """
    print("---Добавить число к множеству--")
    print("@start->")
    global a
    [a.add(i) for i in range(5)]
    print(a)
    print("<-end@")

def set_clear():
    """
    Очистка множества.
    """
    global a
    print("---Очистка множества---")
    print("@start->")
    a.clear()
    print('Множество очищено')
    print(a)
    print("<-end@")

def set_copy():
    """
    Копирование  множества.
    """
    print("---Копировать множество---")
    print("@start->")
    global a
    b = a.copy()
    print("копия множества 'a':=", b)
    print("<-end@")

def set_union():
    """
    Объединение множества.
    """
    print("---Объединение множества---")
    print("@start->")
    global a, c
    print(f"a: {a} union c: {c} = ac: {a.union(c)}")
    print("<-end@")

def set_intersection():
    """
    Поиск пересечения.
    """
    print("---Поиск пересечения---")
    print("@start->")
    global a, c
    print(f"Пересекающиеся числа между a и b: {a.intersection(c)}")
    print("<-end@")

def set_discard(elem: int):
    print("---Удаление выбранного элемента---")
    print("@start->")
    global c
    print(f"Удаление элемента: {elem}")
    c.discard(elem)
    print("<-end@")

def set_difference():
    print("---Поиск уникальных в А по сравнению с B---")
    print("@start->")
    print(a.difference(c))
    print("<-end@")

def set_issubset():
    print("---А содержит B Вывод True/False---")
    print("@start->")
    print(a.issubset(c))
    print("<-end@")
    


if __name__ == "__main__":
    set_add()
    set_copy()
    set_union()
    set_intersection()
    set_discard(10)
    set_difference()
    set_issubset()
    set_clear()
