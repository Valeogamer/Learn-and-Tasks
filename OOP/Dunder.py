# repr для программистов, возвращает строку, по которой видно (и можно воссоздать) состояние объекта
# str - для людей, возвращает строку
# после создания класса и определения инита, лучше всего сразу определить repr
# если не реализован repr и str, то будет возвращен адрес памяти
# eq - по умполчанию сравниваем адресс в памяти, в реализации лучше сразу проверить тип
# если методы сравнения не реализованы то падает ошибка
# contains - для реализации проверки содержит ли
# проверка на bool in, bool для самодельных объектов всегда вернет True, для изменения поведения нужно писать __bool__
# len - вернет ошибку если не переопределить метод
# чтобы объект стал вызываемым (callable) нужно реализовать __call__
# iter - возвращает объект итератор, тот кто реализует iter = Итерабл
# __next__ - должен вернуть следующий объект из контейнера, кто его реализует = Итератор, for работает до stopIterrartion
# __getitem__ - нужен для функционала [] (аналог списка и словаря)
# __Setitem__ - для присвоения через [], если не реализовать = ошибка
# если в объекте не реализован итер то для цикла for будет использован  __getitem__ там ожидается падение индексЕrror
#

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


class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        while 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


class Wallet:

    def __init__(self, *banknotes: Banknote):  # РАЗОБРАТЬСЯ С *
        self.index = 0
        self.container = []
        self.container.extend(banknotes)

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):  # содержит
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):  # количество купюр, то есть количество экземпляров
        return len(self.container)

    def __call__(self):  # позволяет вызывать объекты нашего класса
        # перебираем наш контейнер, получем оттуда наши объекты и складываем целые числа
        return f'{sum(e.value for e in self.container)} рублей'

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item: int):
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key: int, value: Banknote):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


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
    wallet = Wallet(fifty, hundred, hundred)
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
    print(len(wallet))  # количество купюр
    print(wallet())
    for money in wallet:  # next и iter
        print(money)
    for money in wallet:  # больше не подсчитает, потому что исчерпался итератор
        # теперь создали отдельный класс и теперь все работает так как у нового класса индекс обнуляется при вызове
        print(money)
    print(wallet[0])  # setitem
    print(wallet[2])
    wallet[0] = Banknote(500)  # getitem
