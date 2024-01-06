# Передача функции в другую функцию в качестве аргумента,
# именно это свойств функций позволяет их декорировать.
# Декоратор позволяет расширить возможности одной функции
# за счет другой функции.

def i_am_top(func):
    def wrapper(*args, **kwargs):
        print("Я наверху!")
        func(*args, **kwargs)

    return wrapper


def py_decorator(hi_msg, bye_msg):
    # wrapper - функция обертка, в ней мы добавляем нужные действия
    # и вызываем функцию func
    def inner_dec(func):
        def wrapper(*args, **kwargs):
            print(hi_msg)
            func(*args, **kwargs)
            print(bye_msg)

        # возвращаем функцию обертку, чтобы не вызывать ее сразу
        # а сделать это в потом в коду
        return wrapper

    return inner_dec


@i_am_top
@py_decorator("Привет!", "Пока!")
def py_get(x, y, z):
    print("Как дела?")
    print(x)
    print(y)
    print(z)


if __name__ == '__main__':
    py_get(1, 2, 3)
