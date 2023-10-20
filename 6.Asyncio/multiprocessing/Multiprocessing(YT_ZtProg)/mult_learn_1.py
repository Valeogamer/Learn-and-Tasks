"""
    Процессы
"""
import multiprocessing
import time


def test():
    for _ in range(3):
        curr_pr = multiprocessing.current_process().name  # вывод текущего процесса
        print(f"Текущий процесс: {curr_pr}", time.time())
        time.sleep(1)


# процессы вне конструкции if name нельзя запускать.
if __name__ == '__main__':

    process_list = []
    for i in range(1, 6):
        process = multiprocessing.Process(target=test,
                                          name=f"МойПроцесс_{i}")  # создание процесса, target= задача, name=имя процесса
        process_list.append(process)
        process.start()  # запуск процесса

    for prc in process_list:
        prc.join()  # дождаться исполнения процесса
    # print(process.is_alive())  # Работает ли процесс, живо ли оно. Возвращает True False
    # print(process.pid)  # ID процесса, можем обращаться и что либо с ним сделать через GREP
    # process.terminate()  # убить процесс

    print('Все процессы завершены!')
