# Атрибуты класса

class MightiesWeapon:
    first_name = "Default name"  # статический атрибут

    # статический и динамический атрибут могут иметь одинаковое имя
    def __init__(self, first_name: str, second_name: str):
        self.first_name = first_name
        self.second_name = second_name  # динамический атрибут


# Класс метод и методы

class SpaceShip:
    def __init__(self):
        SpaceShip.__atack()

    def atack_new(self) -> None:  # метод
        print('Пиу - Пиу!')

    @classmethod
    def __atack(cls) -> None:  # класс метод
        print('Пиу!')


# Создание объекта класса

class AirConditioner:
    def __init__(self, model: str, capacity: int):
        self.model = model
        self.capacity = capacity

    def turn_on(self):
        print(f"Кондей {self.model, self.capacity} включен!")


#  Наследование

class Animal:
    def __init__(self):
        Animal.__make_a_sound()

    @classmethod
    def __make_a_sound(cls) -> None:
        print("Животное издает звук:")

    def kar(self):
        print("Kar - Kar")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        Cat.__meow()

    @classmethod
    def __meow(cls):
        print("meow - meow")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        Dog.__gav()

    @classmethod
    def __gav(cls):
        print("gav - gav")


# Перегрузка (переопределение)

class Pituh(Animal):
    def __init__(self):
        super().__init__()

    def kar(self):  # если закоментить то будет отрабатывать метод родительского класса
        print("Ku - ka - re - ku")


if __name__ == '__main__':
    star_ship = SpaceShip()
    star_ship.atack_new()

    cond = AirConditioner('Iphone', 34)
    cond.turn_on()

    Tom = Cat()
    Spike = Dog()
    Petya = Pituh()
    Petya.kar()
