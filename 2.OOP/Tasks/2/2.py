from pympler import asizeof
from typing import Union
import sys


class Math:
    def __init__(self, a: float, b: float) -> Union[int, float]:
        self.a = a
        self.b = b

    def __repr__(self):
        return f'a:= {self.a} b:= {self.b}'

    def addition(self) -> float:
        return self.a + self.b

    def multiplication(self) -> float:
        return self.a * self.b

    def subtraction(self) -> float:
        return self.a - self.b

    def division(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError
        return self.a / self.b


if __name__ == '__main__':
    res = Math(1, 1)
    print(asizeof.asizeof(res), "байт")  # смотрит все
    print(sys.getsizeof(res), "байт")
    print(res.multiplication())
    print(res.division())
