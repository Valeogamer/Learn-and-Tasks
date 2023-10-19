"""
    Технология синхронизации:
    Condition - используя его мы можем
    Event
    Позволяют использовать сигналы и передавать их между разными процессами.
    Общение между процессами.
    Передавать между процессами состояния.
"""
# Condition - позволяет использовать состояние, используя его можем остановить нудный нам процесс
# в определенном месте, его выполнение не продолжиться, пока любой из процессов не сообщит ему об этом
# в отличие от Event, Condition можем отправлять уведомления всем процессам сразу и по какому то
# определенному процессу.

# Event - работают по похожему принципу Condition, но есть одно базовое состояние, либо значение по умолчанию
# то есть False (который позволяет процесс ждать), либо состояние True, которое говорит что необходимо
# начать выполнение.

# __ EVENT __
from multiprocessing import Process, Event
import time
event = Event()  # Подключаем event


def test():
    """
    Функция для проверки состояния Event
    и в зависимотси от этого выводит нужный нам результат.
    """
    print("функция test запущена!")
    while True:
        event.wait()  # останавливает выполнение event, так как по умолчанию False, код ниже не отработает,
        # пока не пердадим event у True
        # event.set() разблокировка event (вводить в консоль)
        # event.clear() сброс разблокировки (вводить в консоль)
        print("test")
        time.sleep(1)


def test_event():
    """
    Сам разблокирует и сам заблокирует
    """
    while True:
        time.sleep(5)
        event.set()  # Ставит event на True
        print("Event True")
        time.sleep(5)
        event.clear()
        print("Event False")  # сброс значений Event


if __name__ == '__main__':
    Process(target=test).start()
    Process(target=test_event).start()

# __ Condition __
# позволяет более строго контролировать процесс
# from multiprocessing import Process, Condition
#
# cond = Condition()  # подключаем condition
#
#
# def f1():
#     while True:
#         with cond:  # блокировку и разблокировку делает контекстный менеджер with (см.про Lock Rlock)
#             cond.wait()  # если в Event сброс был явный, тут сразу после исполнения кода, который за wait
#             print("Получили событие")
#             print("Получили событие")
#             print("Получили событие")
#
#
# def f2():
#     """
#     Разблокирует wait  у condition
#     """
# for i in range(100):
#     if i % 10 == 0:
#         with cond:
#             cond.notify()  # перевод condition в статус True при выполнении условия
#             print("Получили событие")
#     else:
#         print(f"f2: {i}")
#     time.sleep(1)
#
# if __name__ == '__main__':
#     Process(target=f1).start()
#     Process(target=f2).start()
