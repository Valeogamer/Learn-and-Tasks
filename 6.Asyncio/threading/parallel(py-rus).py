# Конкурентность (concurrrency) - запуск на выполнение нескольких задач (не обязательно в 1 момент времени
# выполняется несколько). Зависит от ПО

# Параллельность (parallel) - конкурентность, когда 2+ задачи выполняются одновременно. Зависит от железа.
import threading
import time
import requests


def activity():
    # for e in range(1000_0000):
    #     abs(round(e ** 2 / 122) + e * 3.14)
    # или
    requests.get("https://ya.ru/")  #  использует IO и будет рабоать быстрее на уровне OS уже потоки не блокируются

def run(threaded=False):
    start = time.time()
    if not threaded:
        for e in range(10):
            activity()
    else:
        threades = [threading.Thread(target=activity, daemon=True) for _ in range(10)]
        for e in threades:
            e.start()
        for e in threades:
            e.join()
    end = time.time()
    print("Время работы: ", end - start)


if __name__ == '__main__':
    # True работа с потоками
    # False отключаем
    # Смысла никакого, GIL блокирует, просто теперь потоки в очереди
    # Хоть и исполнителей 10, они друг за другом выполняют свою часть работы
    # Как если бы и один исполнитель выполнял один
    # Но при IO оно будет работать быстрее
    run(threaded=True)
