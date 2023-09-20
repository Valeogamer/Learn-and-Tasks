import time
import threading


def get_data(data):
    while True:
        print(f'[{threading.currentThread().name}] - {data}')
        time.sleep(5)


thr = threading.Thread(target=get_data, args=(str(time.time()), ), name="thr-1")
thr.start()

for i in range(100):
    print(f"cur i: {i}")
    time.sleep(1)

    if i % 10 == 0:
        print("active thread: ", threading.activeCount())
        print("enumerate: ", threading.enumerate())
        print("thr-1 is alive: ", thr.is_alive())
