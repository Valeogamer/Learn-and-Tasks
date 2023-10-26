from multiprocessing.managers import BaseManager

BaseManager.register("get_t")
manager = BaseManager(address=('127.0.0.1', 4444), authkey=b'abc')
print("client connected!")
manager.connect()

res = manager.get_t()
print("result: ", res)