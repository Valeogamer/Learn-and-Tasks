"""
    Потоки Демоны
    с завершением исполнения основного потока, автоматически завершаются все потоки.
"""
import time
import threading


def get_data(data):
    for _ in range(5):
        name_curr_thr = threading.current_thread().name  # имя текущего потока
        print(f"[{name_curr_thr}] - {data}")
        time.sleep(1)

thr = threading.Thread(target=get_data, args=(str(time.time()), ), daemon=True)
thr.start()
print('Finish')