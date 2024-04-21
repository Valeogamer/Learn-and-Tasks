import time
import multiprocessing

square_list = []
cubic_list = []

def calc_square(num):
    global square_list
    for n in num:
        # time.sleep(5)  # чтобы была возможность увидеть данные процессы в Диспетчере задач(win)
        # print('square ' + str(n * n))
        square_list.append(n*n)
    print(square_list)  # внутри процесса будет результат, то бишь здесь, за пределами не будет то в main.


def calc_cubic(num):
    for n in num:
        # time.sleep(5)
        # print('cubic ' + str(n * n * n))
        cubic_list.append(n*n*n)


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    # формируем процессы p1, p2
    # target - функция для обработки
    # args(кортеж) - что через функцию прогнать
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cubic, args=(arr,))

    # запуск процессов
    p1.start()
    p2.start()

    # ожидаем завершения исполнения процессов
    p1.join()
    p2.join()
    print(square_list) #  даст пустой список
