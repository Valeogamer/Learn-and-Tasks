from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = np.array([1, 2, 3, 4, 5])
local_sum = np.array(0)

# Распределение данных по процессам
comm.Scatter(data, local_sum, root=0)
local_sum = np.sum(local_sum)

# Сбор локальных сумм на процессе 0 и вычисление общей суммы
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print("Total sum:", total_sum)
