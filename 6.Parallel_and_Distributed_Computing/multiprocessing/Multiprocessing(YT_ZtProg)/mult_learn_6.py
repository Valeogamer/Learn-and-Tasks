"""
    Технология передачи данных между разными процессами
    и реализовывать таким образом общение.
    Pipe (каналы, трубы)
"""
import multiprocessing
import time
from multiprocessing import Pipe

# функция для обработки каналов в отдельном процессе
def send_data(conn):
    conn.send("Hi world!")  # отправка сообщения через канал входа
    # conn.close()  # закрытие канала

if __name__ == '__main__':
    output_c, input_c = Pipe()  # передача, приём данных
    p = multiprocessing.Process(target=send_data, args=(input_c,))
    p.start()
    p.join()
    print('data: ', output_c.recv())  # вывод сообщения через канал выхода