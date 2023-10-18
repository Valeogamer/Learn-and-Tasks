"""
    Класс Timer в потоках.
    Данная технология позволяет запускать потоки спустя заданное количество времени.

"""
#
# import time
# import threading
#
# def test():
#     while True:
#         print("test")
#         time.sleep(1)
#
# thr = threading.Timer(10, test)
# thr.start()
#
#
# for _ in range(6):
#     print("111")
#     time.sleep(2)
#
# thr.cancel()  # Позволяет отменить поток, до того как он запущен
# print('Finish')

"""
    .local() - позволяет хранить данные  в наших потоках и задавать нужные атрибуты 
    и задавать нужные значения этим атрибутам.
"""

import time
import threading

data = threading.local()


def get():
    print(data.value)


def t1():
    data.value = 111
    get()


def t2():
    data.value = 222
    get()

threading.Thread(target=t1).start()
threading.Thread(target=t2).start()