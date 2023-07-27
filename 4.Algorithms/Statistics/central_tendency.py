import numpy as np


def measure_cent_tendecy(values: list[int]):
    values.sort()

    # Среднее значение (арифметическое среднее)
    sum = 0.
    for i in values:
        sum += i  # np.sum()
    mean_values = sum / len(values)
    print(f'Среднее значение: {mean_values:.3f}')

    # Медиана
    if len(values) % 2:  # если количество элементов нечетное
        mediana = values[int(len(values) // 2)]
    else:  # если количество элементов четное
        mediana = (values[int(len(values) / 2)] + values[int(len(values) / 2 - 1)]) / 2
    print(f'Медиана: {mediana:.3f}')

    # Мода
    uni_v = set(values)
    dict_uni_v = {}
    for key in uni_v:
        dict_uni_v[key] = []
    for j in values:
        for key_v in dict_uni_v.keys():
            if j == key_v:
                dict_uni_v[key_v].append(j)
    # Нахождение максимальной длины
    max_length = max(len(v) for v in dict_uni_v.values())
    # Нахождение всех ключей, соответствующих спискам максимальной длины
    max_keys = [k for k, v in dict_uni_v.items() if len(v) == max_length]
    if len(max_keys) > 1:
        print(f"Мода: {max(max_keys):.2f}")
    else:
        print(f"Мода: {max_keys:.2f}")

    # Геометрическая средняя
    # np.prod()
    op = 1.
    for i in values:
        op *= i
    geom_mean = op ** ((1 / len(values)))
    print(f'Геометрическая средняя: {geom_mean:.2f}')


if __name__ == '__main__':
    np.random.seed(12)
    values = np.random.randint(1, 20, 20)
    values = [1, 2, 3, 4, 5, 1, 2]
    measure_cent_tendecy(values)
