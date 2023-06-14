from singleton import Singleton
from model_two import two


def one():
    return Singleton().data * 100


if __name__ == '__main__':
    result = one() + two()
    print(result)
