# repr для программистов, возвращает строку, по которой видно (и можно воссоздать) состояние объекта
# str - для людей, возвращает строку
# после создания класса и определения инита, лучше всего сразу определить repr
# если не реализован repr и str, то будет возвращен адрес памяти
# eq - по умполчанию сравниваем адресс в памяти, в реализации лучше сразу проверить тип
# если методы сравнения не реализованы то падает ошибка
# contains - для реализации проверки содержит ли
# проверка на bool in, bool для самодельных объектов всегда вернет True, для изменения поведения нужно писать __bool__
class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):  # для программистов
        return f'Banknote({self.value})'  # должна возвращать такой объект, который аналогичен созданию объекта
        # repr должен возвращать такую строку чтобы она позволяла восстановить объект, воссоздать

    def __str__(self):  # для людей
        return f'Банкнота номиналом в {self.value} рублей'

    def __eq__(self, other):  # сравнение eq ==
        if other is None or not isinstance(other, Banknote):  # проверка принадлежности классу
            return False
        return self.value == other.value

    def __lt__(self, other):  # меньше чем
        if other is None or not isinstance(other, Banknote):  # проверка принадлежности классу, проверка типа
            return False
        return self.value < other.value

    def __gt__(self, other):  # больше чем
        if other is None or not isinstance(other, Banknote):  # проверка принадлежности классу, проверка типа
            return False
        return self.value > other.value

    def __le__(self, other):  # меньше или равно
        if other is None or not isinstance(other, Banknote):  # проверка принадлежности классу, проверка типа
            return False
        return self.value <= other.value

    def __ge__(self, other):  # больше или равно
        if other is None or not isinstance(other, Banknote):  # проверка принадлежности классу, проверка типа
            return False
        return self.value >= other.value


class Wallet:

    def __init__(self, *banknotes: Banknote):  # РАЗОБРАТЬСЯ С *
        self.container = []
        self.container.extend(banknotes)

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):  # содержит
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0


if __name__ == '__main__':
    banknote = Banknote(50)
    other = eval(repr(banknote))  # через eval восстановили состояние объекта
    print(f'{banknote!r}')  # вывод repr
    print(banknote)
    print(other)
    fifty = Banknote(50)
    hundred = Banknote(100)
    print(fifty == banknote)
    print(fifty == hundred)
    print(fifty < hundred)
    print(fifty > hundred)
    print(fifty <= hundred)
    print(fifty >= hundred)
    wallet = Wallet(fifty, hundred)
    print(wallet)
    print(fifty in wallet)
    print(Banknote(500) in wallet)
    wallet_new = Wallet()
    if wallet:
        print('есть')
    if wallet_new:
        print('есть')
    else:
        print('Пусто')
