from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = np.array([7, 12, 5, 9, 22])
local_max = np.array(0)

# Распределение данных по процессам
comm.Scatter(data, local_max, root=0)
local_max = np.max(local_max)

# Сбор локальных максимумов на процессе 0 и поиск глобального максимума
max_global = comm.reduce(local_max, op=MPI.MAX, root=0)

if rank == 0:
    print("Max global:", max_global)
