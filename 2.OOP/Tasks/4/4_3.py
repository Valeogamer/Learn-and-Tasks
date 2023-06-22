class Country:
    pass


class Russia(Country):
    _country = 'RUSSIA'

    def __init__(self, population: str, language: str):
        self.population = population
        self.language = language

    def __repr__(self):
        return f'Страна {self._country}'

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, replace_name: str):
        if replace_name == 'Russia':
            self._country = replace_name
        elif replace_name == 'RUSSIA':
            self._country = replace_name
        elif replace_name == 'russia':
            self._country = replace_name
        else:
            raise AttributeError("Ошибка!")

class Canada(Country):
    _country = 'CANADA'

    def __init__(self, population: str, language: str):
        self.population = population
        self.language = language

    def __repr__(self):
        return f'Страна {self._country}'

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, replace_name: str):
        if replace_name == 'Canada':
            self._country = replace_name
        elif replace_name == 'CANADA':
            self._country = replace_name
        elif replace_name == 'canada':
            self._country = replace_name
        else:
            raise AttributeError("Ошибка!")

class Germany(Country):
    _country = 'GERMANY'

    def __init__(self, population: str, language: str):
        self.population = population
        self.language = language

    def __repr__(self):
        return f'Страна {self._country}'

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, replace_name: str):
        if replace_name == 'Germany':
            self._country = replace_name
        elif replace_name == 'GERMANY':
            self._country = replace_name
        elif replace_name == 'germany':
            self._country = replace_name
        else:
            raise AttributeError("Ошибка!")


if __name__ == '__main__':
    rus = Russia('Russian', 'ru')
    print(rus.country)
    rus.country = 'Russia'
    print(rus.country)
    ca = Canada('Canad', 'ca')
    print(ca.country)
    ca.country = 'Canada'
    print(ca.country)
    ger = Germany('German', 'ge')
    print(ger.country)
    ger.country = 'Germany'
    print(ger.country)