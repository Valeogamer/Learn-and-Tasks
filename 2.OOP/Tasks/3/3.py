import random


class Warrior:
    def __init__(self, name, health: int = 100, damage: int = 20):
        self.name = name
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f'Класс: "Воин", name: {self.name}'

    def attack(self, enemy):
        print(f'{self.name} атакует {enemy.name}')
        enemy.health -= self.damage
        print(f'У {enemy.name} осталось {enemy.health} здоровья')

    def is_alive(self):
        return self.health > 0


def win(n_1, n_2):
    if n_1.is_alive:
        print(f'Победил {n_1.name}')
    else:
        print(f'Победил {n_2.name}')


def ring(n_1, n_2):
    """
    Бойцовский клуб
    :param n_1: Боец_1
    :param n_2: Боец_2
    :return: Победитель
    """
    while n_1.is_alive() and n_2.is_alive():
        attacker, defender = random.sample([n_1, n_2], k=2)
        attacker.attack(defender)
    win(n_1, n_2)

if __name__ == '__main__':
    war_1 = Warrior("Воин 1")
    war_2 = Warrior("Воин 2")
    ring(war_1, war_2)
    print('breakpoint')
