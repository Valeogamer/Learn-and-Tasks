# Механизм перегрузки (overloading) - это возможность определения функций и методов с одинаковым именем,
# но разными параметрами.
# В зависимости от типов и количества аргументов, вызывается соответствующая функция.

# В Python механизм перегрузки методов основан на использовании аргументов по умолчанию и переменного числа аргументов.
# Например, можно определить метод print_info, который может принимать различное количество аргументов разных типов:

from functools import singledispatch


@singledispatch
def print_info(arg):
    print("Unsupported type!")


@print_info.register
def _(arg_1: int, arg_2: int):
    print("Two integers provided!", f'This is {arg_1} and {arg_2}')


@print_info.register
def _(arg_1: str):
    print("One string provided!", f'This is {arg_1}')


if __name__ == '__main__':
    # если писать значения типа инт то будет вызывать вторую реализацию при str третью, иначе выводит первую
    print_info('df')
    print_info([1, 2, 3])
    print_info(1, 2)
    print_info((1, 2))
    print_info({1: 'a'})
