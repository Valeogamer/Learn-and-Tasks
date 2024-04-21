"""
    Обмен данными между процессами с помощью Очередей.
"""
import time
import multiprocessing


def calc_square(nums, q):
    for n in nums:
        q.put(n * n)  # добавляем данные в конец очереди


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    # организуем очередь
    queue = multiprocessing.Queue()  # FIFO (первым положил, первым взял)
    p1 = multiprocessing.Process(target=calc_square, args=(arr, queue))

    # запуск процессов
    p1.start()

    # ожидаем завершения исполнения процессов
    p1.join()

    # вывод результата из очереди
    # выводить до тех пор, пока очередь не окажется пустым
    while queue.empty() is False:
        print(queue.get())  # выводим элементы с очереди начиная с первого
