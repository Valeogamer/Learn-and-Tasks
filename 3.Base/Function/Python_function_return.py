# None используется для обычных функций которые ничего не возвращают или явно возвращают значение None

# NoRetrun используется только для тех функции которые выходят только по исключению
# и точно также можно использовать Never
import enum
from typing import Never, NoReturn


def always_raise() -> NoReturn:  # NoReturn для типизации функции которая выходит только по исключению
    raise RuntimeError("Ох Ох")


def main() -> None:
    always_raise()
    print("Мы сюда не дойдем так как вызвали исключение!")


########################################################################
def assert_never(_: Never) -> NoReturn:
    raise AssertionError("Expected to be unreachable")


class Gender:
    MALE = "male"
    FEMALE = "female"
    TRACTOR = "tractor"


def handle_incorrect_password(user_gender: Gender) -> None:
    message = "Вы {} неправильный пароль!"
    match user_gender:
        case Gender.MALE:
            entered = "ввел"
        case Gender.FEMALE:
            entered = "ввела"
        case _ as unreachable:
            assert_never(unreachable)  # В Runtime мы сюда никогда не должны дойти
        # также если добавим новый гендер данная функция предупредит что есть не обработанные сценарии
    print(message.format(entered))
