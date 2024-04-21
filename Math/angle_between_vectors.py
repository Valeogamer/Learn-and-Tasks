import math

'''
    Угол между векторами.
'''


def calc_vector(a_cords: tuple[float, float], b_cords: tuple[float, float]) -> tuple[float, float]:
    """
    Вычисление вектора
    :param: a_coords, b_coords = А(x, y); B(x, y)
    :return: a(x, y)
    """
    a: tuple[float, float] = (b_cords[0] - a_cords[0], b_cords[1] - a_cords[1])
    return a


def dot_product_of_vectors(a: tuple[float, float], b: tuple[float, float]) -> float:
    """
    Скалярное произведение векторов
    :param: a, b - координы векторов.
    """
    scalar: float = a[0] * b[0] + a[1] * b[1]
    return scalar


def vector_lengths(a: tuple[float, float]) -> float:
    """
    Вычисление длины вектора
    :param: a(x, y); b(x, y)
    :return: c
    """
    c: float = math.sqrt(a[0] ** 2 + a[1] ** 2)
    return c


def cos_angle_between_vectors(a: tuple[float, float], b: tuple[float, float]) -> float:
    """
    Косинус угла между векторами
    :param: a(x, y); b(x, y)
    :return: cos
    """
    cos = dot_product_of_vectors(a, b) / (vector_lengths(a) * vector_lengths(b))
    return cos


def angle_vectors(a_cords: tuple[float, float], b_cords: tuple[float, float], c_cords: tuple[float, float]) -> float:
    """
    Определение угла между векторами
    :param: a_coords, b_coords, c_coords = А(x, y); B(x, y); C(x, y);
    :return: угол между вектором a и b.
    """
    a = calc_vector(a_cords, b_cords)
    b = calc_vector(b_cords, c_cords)
    cos = cos_angle_between_vectors(a, b)
    result_angle = math.acos(cos) * (180 / math.pi)
    return result_angle


if __name__ == '__main__':
    A, B, C = (5, 3), (-7, -4), (10, -5)
    result = angle_vectors(A, B, C)
    print(result)
