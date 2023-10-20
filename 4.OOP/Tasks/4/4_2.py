class Games:
    year = None

    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year
        Games.__dashes()

    def __repr__(self):
        return f'Game: {self.name}'

    def getName(self) -> str:
        return f'Имя игры: {self.name}'

    @classmethod
    def __dashes(cls) -> str:
        print('-' * 15)


class PCGames(Games):
    def __init__(self, name, year, platforms: str):
        super().__init__(name, year)
        self.platforms = platforms

    def getName(self) -> str:
        return f'Имя игры: {self.name} \nПлатформа: {self.platforms}'


class PS4Games(Games):
    def __init__(self, name, year, platforms: str):
        super().__init__(name, year)
        self.platforms = platforms

    def getName(self) -> str:
        return f'Имя игры: {self.name} \nПлатформа: {self.platforms}'


class XBOXGames(Games):
    def __init__(self, name, year, platforms: str):
        super().__init__(name, year)
        self.platforms = platforms

    def getName(self) -> str:
        return f'Имя игры: {self.name} \nПлатформа: {self.platforms}'


class MobileGames(Games):
    def __init__(self, name, year, platforms: str):
        super().__init__(name, year)
        self.platforms = platforms

    def getName(self) -> str:
        return f'Имя игры: {self.name} \nПлатформа: {self.platforms}'


if __name__ == '__main__':
    pc = PCGames('GTA', 2003, 'PC')
    print(pc.getName())
    pc = PS4Games('MK 11', 2021, 'PS4')
    print(pc.getName())
    pc = XBOXGames('Forza Horizon 5', 2018, 'XBox')
    print(pc.getName())
    pc = MobileGames('Pubg Lite', 2015, 'Android')
    print(pc.getName())
