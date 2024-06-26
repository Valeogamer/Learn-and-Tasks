"""
Простое сообщение между процессами
Процесс 0 отправляет сообщение процессу 1, который его принимает и выводит.
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD  # объект коммуникатор, который представляет группу всех процессов
rank = comm.Get_rank()  # Ранг текущего процесса
# Ранг - это уникальный идентификатор процесса в рамках данного коммуникатора.
# Он может быть использован для определения поведения каждого процесса в программе
print('Привет')

if rank == 0:  # проверяем ранг текущего процесса
    data = "Привет от процесса 0, для процесса 1"  # заготавливаем письмо
    comm.send(data, dest=1)  # отправляем письмо процессу с рангом 1
elif rank == 1:  # проверяем ранг текушего процесса
    data = comm.recv(source=0)  # принимаем письма от процесса 0
    print("Вывод полученного письма: ", data)  # выводим
