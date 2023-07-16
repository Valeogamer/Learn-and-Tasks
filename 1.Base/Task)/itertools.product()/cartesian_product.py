from itertools import product


def cartesian_prod_legacy(a, b) -> str:
    cartesian_product = list(product(a, b))
    res = ''
    for i in cartesian_product:
        res += str(i)
    return res


def cartesian_prod(a, b):
    return product(a, b)

if __name__ == '__main__':
    # legacy
    # a = [int(i) for i in str(input()) if i != ' ']
    # b = [int(i) for i in str(input()) if i != ' ']
    # result = cartesian_prod(a, b)
    a = map(int, input().split())
    b = map(int, input().split())
    print(*cartesian_prod(a, b))
