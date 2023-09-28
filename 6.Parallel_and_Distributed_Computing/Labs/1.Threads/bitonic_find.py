"""
Поиск битонической подпоследовательности
В массиве из целых чисел длины N подсчитать число битонических подпоследовательностей.
Битоническая последовательность - монотонно возрастает и монотонно убывает (и наоборот)

"""
import threading

def find_all_bitonic(n):
    """
    Подсчет количества всех битонических подпоследовательностей в массиве
    """
    up = down = False
    cnt = 0
    for i in range(len(n) - 1):
        if n[i + 1] > n[i]:
            up = True
            if down:
                cnt += 1
                down = False
        elif n[i + 1] < n[i]:
            down = True
            if up:
                cnt += 1
                up = False
    return print(cnt)

def count_bitonic_subsequences(arr, start, end):
    """
    Подсчет битонических подпоследовательностей в части массива arr[start:end]
    """
    up = down = False
    cnt = 0

    for i in range(start, end - 1):
        if arr[i + 1] > arr[i]:
            up = True
            if down:
                cnt += 1
                down = False
        elif arr[i + 1] < arr[i]:
            down = True
            if up:
                cnt += 1
                up = False

    return cnt

if __name__ == '__main__':
    n = [1, 1, 2, 3, 4, 3, 2, 1, 1, 8, 9, 10, -95, -96, -97, -97, 100, 101, 102]
    # n = [-1, -1, -1, -2, -3, 3, 4, 5, 6, 6, 7, 6, 6, 8, 10, -100]
    find_all_bitonic(n)

    data = [-1, -1, -1, -2, -3, 3, 4, 5, 6, 6, 7, 6, 6, 8, 10, -100]
    num_threads = 4  # Количество потоков

    # Разделим массив на равные части для каждого потока
    chunk_size = len(data) // num_threads
    threads = []

    global_results = []  # Глобальный список для хранения результатов из каждого потока

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(data)
        thread = threading.Thread(target=lambda: global_results.append(count_bitonic_subsequences(data, start, end)))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Объединяем результаты из каждого потока и суммируем их
    total_count = sum(global_results)
    print(f"Количество битонических подпоследовательностей: {total_count}")
