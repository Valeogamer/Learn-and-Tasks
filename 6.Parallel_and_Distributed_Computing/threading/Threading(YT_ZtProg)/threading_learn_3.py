"""
    Синхронизация потоков.
    Блокировка потоков:
        1) Lock (можем любым потоком заблокировать и разблокировать)
        2) Rlock (тот поток который заблокировал, только тот и может разблокировать)
"""
import time
import threading

value = 0
locker = threading.Lock()  # создаем объект нашего блокировщика

def inc_value():
    global value
    while True:
        locker.acquire()  # блокировка доступа потокам к данной области
        value += 1
        time.sleep(1)
        print(value)
        locker.release()  # освобождаем ранее заблоченную область под другой поток
        #  и поток который ранее вызовет данный метод, получит первым доступ к данной области

for _ in range(5):
    threading.Thread(target=inc_value).start()