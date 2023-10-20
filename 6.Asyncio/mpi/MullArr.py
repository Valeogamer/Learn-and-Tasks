from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])
local_result = np.zeros((2, 2))

# Распределение матрицы A по процессам
comm.Scatter(matrix_A, local_result, root=0)
local_result = np.dot(local_result, matrix_B)

global_result = np.zeros((2, 2))

# Сбор локальных результатов на процессе 0 и вычисление глобального результата
comm.Reduce(local_result, global_result, op=MPI.SUM, root=0)

if rank == 0:
    print("Global result:")
    print(global_result)
