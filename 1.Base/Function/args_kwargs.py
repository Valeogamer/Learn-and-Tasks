def test(a, b):
    """
    Количество аргументов строго фиксировано
    """
    pass


def test_one(*args):
    """
    Количество аргументов нефиксировано (неопределенное количество)
    return tuple(*args)
    """
    print(args)


def test_two(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


if __name__ == '__main__':
    test_one(1, 2, 3, 4, 5)
    a = [1, 2, 3]
    test_one(a)
    print("Распаковка списка *a")
    test_one(*a)
    print('*args **kwargs')
    b = {'1': 'c', '2': 'a', '3': 'b'}
    bb = [11, 22, 33, 44]
    test_two(5, 10, 7, 9, **{'1': '2', '2': '1'})
    print('*args **kwargs')
    test_two(*bb, **b)