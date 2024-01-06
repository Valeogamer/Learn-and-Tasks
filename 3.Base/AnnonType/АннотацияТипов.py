from typing import Union, Final, NoReturn

# Union - либо/либо int/float/str/...
# Final - констаната, больше нигде не должна назначаться
# NoReturn - ничего не возвращает

def car_speed() -> Union[int, float]:
    return 89.6
print(car_speed())

MAX_PRICE: Final = 9.99

def greeting() -> NoReturn:
    print("Hi")

greeting()