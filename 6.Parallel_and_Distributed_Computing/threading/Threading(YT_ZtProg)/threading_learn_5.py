"""
    Технологии синхронизации.
    Семафоры и Берьеры.
    Семафора - это технология, в основе которой лежит счетчик
    он позволяет заранее указать максимальное значение счетчика.
    Когда потоков, которые попытаются получить семафор, будет больше этого значения
    он заблокируется. Предположим максимальное значение которое задали для семафоры равно 5,
    но запускаем перед этим 10 потоков, в итоге только 5 потоков получат доступ к семафору.
    А остальным 5  потокам придется ждать свою очередь. В итоге если хоть один поток завершит
    выполнения действия, у нас сразу осводиться место под другой поток. И она попадает под семафору
    обновляя счетчик и опять все блокируя.
    Используя семафору можем четко граничить с количеством одновременно выполянемых потоков.
    Опять же аналогия с Lock и с его методами acquire(блокировка) и release(разблокировка)
    Но блокировка и разблокировка при определенных условиях.

    Барьеры - это противоположная семафору технология, заранее указываем количество одновременных активных потоков
    Они все дойдут до вызова метода wait и после чего эти 5 потоков не вызовут метод wait после того как все потоков вызвали этот метода
    то только тогда можем разблокироваться и продолжим выполнение. То есть тут нужно чтобы все потоки макс колво указанное
    исполнились, только после этого будет разблокировка.
"""
# Семафора
# import time
# import random
# from threading import Thread, BoundedSemaphore, current_thread
#
# max_thread = 5  # макс количество потоков, которые будут работать у нас одновременно
# pool = BoundedSemaphore(value=max_thread)  # блокировщик в виже BoundedSemaphore
#
#
# def test():
#     with pool:
#         slp = random.randint(1, 5)
#         print(current_thread().name)
#         time.sleep(slp)
#
#
# for i in range(10):
#     Thread(target=test, name=f'thr-{i}').start()

# Барьеры
import time
import random
import threading

def test(barrier):
    slp = random.randint(3, 7)
    time.sleep(slp)
    print(f"Поток [{threading.current_thread().name}] запущен в ({time.ctime()})")

    barrier.wait()
    print(f"Поток [{threading.current_thread().name}] преодолел барьер в ({time.ctime()})")

bar = threading.Barrier(5)
for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f'thr-{i}').start()