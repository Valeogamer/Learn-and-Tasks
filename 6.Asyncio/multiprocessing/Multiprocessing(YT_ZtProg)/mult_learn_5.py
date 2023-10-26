"""
    Принцип работы брьеров (Barrier) в процессах.
    Менеджеры - которые позволяют передавать доступ на определенные функции нужного на мпроцесса.
    То есть делиться с ним с областью памяти. В процессах используются менеджеры, и во  таким вот
    образом, может передавать целые объекты между процессами.

"""
# __ Barrier __
# import multiprocessing
# from multiprocessing import Process, Barrier
#
#
# # Функция для работы с барьером
# def f1(bar):
#     name = multiprocessing.current_process().name
#     bar.wait()
#     print(f"[{name}] - запущено!")
#
#
# if __name__ == '__main__':
#
#     b = Barrier(5)  # создаем экземпляр(объект) барьера и минимальное количество процессов
#     # которое используется в барьере.
#     for i in range(5):
#         Process(target=f1, args=(b,)).start()

# __ Manager __
import multiprocessing
from multiprocessing import Process, Manager
import time
import random


# Используя менеджеры можем передавать практически любой тип данных

def f(m_dict, m_array):
    m_dict["name"] = "test"
    m_dict["version"] = "1.0"
    m.array.append(1)
    m.array.append(2)


if __name__ == '__main__':
    m = Manager()
    with m:
        d = m.list()
        l = m.list()
        pr = Process(target=f, args=(d, l,))
        pr.start()
        pr.join()

        print("dict: ", d)
        print("dict: ", l)

# __ Base Manager __
# Позволяет передавать целые объекты между процессами
# То есть можно передавть классы, функции, методы между процессами

# import time
# from multiprocessing.managers import BaseManager
#
#
# def get_time():
#     return time.time()  # возвращаем текущее время Unix
#
#
# BaseManager.register("get_t", callable=get_time)  # регистрация объекта нашей функции
# # название с помощью которой будет вызываться функция
# # callable - адрес нашей функции
# # тем самым когда клиент получит след значение: "get_t", у нас будет вызываться след значение : get_time
# # и результаат выполнения функции передается самому клиенту
#
# # далее указываем:
# # address
# # port
# # которые будут использоваться в качестве сервера и также нужно передать пароль
# # который используется для авторизации в нащ менеджер
# manager = BaseManager(address=('', 4444), authkey=b'abc')
# server = manager.get_server()
# print("server start")
# server.serve_forever()