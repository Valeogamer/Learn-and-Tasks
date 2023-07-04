def factorial(n):
    if n == 0:  # базовый случай
        return 1
    else:  # рекурсивный случай
        return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(995))  # максимальная глубина рекурсии
