# multithreading - многопоточность, подходит для IO-bound задач, использует ОС,страдает от GIL
# полезно для ускорения выполнения задач или для того, чтобы текущий поток занялся другой задачей
# любая программа это минимум один процесс и один поток
import os
import threading
import time
from threading import Thread
from tkinter import ttk
from tkinter import *
from queue import Queue


def waiting(timeout):
    """
    Ждет указанное количество времени.
    """
    while timeout > 0:
        timeout -= 1
        time.sleep(1)
    print("OK")


def thread_wait(timeout):
    thread = Thread(target=waiting, args=(timeout,), daemon=True)
    thread.start()
    return thread


def info():
    pid = os.getpid()
    name = threading.current_thread().name
    print(f"Process {pid}, name {name}")


counter = [0]
lock = threading.Lock()


def inc():
    lock.acquire()
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1
    lock.release()


queue = Queue()
queue.put(0)

def inc_q():
    c = queue.get()
    time.sleep(0.1)
    queue.put(c + 1)


if __name__ == '__main__':
    # tk = Tk()
    # button1 = ttk.Button(tk, text="WAIT", command=lambda: waiting(3))
    # button1.pack(side=LEFT)
    # button2 = ttk.Button(tk, text="THREAD", command=lambda: thread_wait(3))
    # button2.pack(side=LEFT)
    # tk.mainloop()

    # threads = [Thread(target=info, daemon=True) for _ in range(10)]
    # for th in threads:
    #     # После создания потоков их нужно обязательно запускать
    #     th.start()
    # for th in threads:
    #     # Дождаться их выполнения
    #     th.join()
    # info()

    # threads = [Thread(target=lambda: waiting(5), daemon=True) for _ in range(3)]
    # for th in threads:
    #     # После создания потоков их нужно обязательно запускать
    #     th.start()
    # for th in threads:
    #     # Дождаться их выполнения
    #     th.join()

    # threads = [Thread(target=inc, daemon=True) for _ in range(10)]
    # for th in threads:
    #     # После создания потоков их нужно обязательно запускать
    #     th.start()
    # for th in threads:
    #     # Дождаться их выполнения
    #     th.join()
    # print(counter)

    threads = [Thread(target=inc_q, daemon=True) for _ in range(10)]
    for th in threads:
        # После создания потоков их нужно обязательно запускать
        th.start()
    for th in threads:
        # Дождаться их выполнения
        th.join()
    print(queue.qsize()) # длина очереди
    print(queue.get_nowait()) # результат
