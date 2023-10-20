class Major:
    def __init__(self, txt: str):
        self.txt = txt
        self._new_txt = None
        self._replace_txt = 'Hi, there!'

    def __repr__(self):
        return f'Основной класс: {id(self)}'

    @property
    def replace_text(self):
        return f'Replace_txt: {self._replace_txt}'

    @replace_text.setter
    def replace_text(self, rep_txt: str):
        if type(rep_txt) is str:
            self._replace_txt = rep_txt
        else:
            raise TypeError('Неверный тип данных. Ожидался тип \'str\' ')

    @property
    def add_text(self):
        return f'New_text: {self._new_txt}'

    @add_text.setter
    def add_text(self, new_text: str):
        if type(new_text) is str:
            self._new_txt = new_text
        else:
            raise TypeError('Неверный тип данных. Ожидался тип \'str\' ')


class Descendant(Major):
    def __init__(self, txt, num: float, uni_text: str):
        super().__init__(txt)
        self.num = num
        self.uni_text = uni_text

    def __repr__(self):
        return f'Класс потомка: {id(self)}'

    def __str__(self):
        return f'Все атрибуты:\n{self.txt}\n{self.num}\n{self.uni_text}'


if __name__ == '__main__':
    maj = Major("Hi!")
    print(maj.replace_text)
    print(maj.add_text)
    maj.replace_text = "HI, world!"
    maj.add_text = "Привет!"
    print(maj.replace_text)
    print(maj.add_text)

    des = Descendant('Hi there! I am descendants.', 10, 'Uni text!')
    print(des)
