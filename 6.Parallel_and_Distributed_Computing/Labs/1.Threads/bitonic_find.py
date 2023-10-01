"""
Поиск битонической подпоследовательности
В массиве из целых чисел длины N подсчитать число битонических подпоследовательностей.
Битоническая последовательность - монотонно возрастает и монотонно убывает (и наоборот)
Битоническая последовательность
Последовательность чисел называется битонической тогда и только тогда, когда
1. Монотонно увеличивается, а затем монотонно уменьшается
или монотонно уменьшается, а затем монотонно увеличивается
2. Может быть разделен на две части, которые можно поменять местами, чтобы получить
любой из первых двух случаев.
"""
import threading


def count_trend_changes(arr):
    if len(arr) < 3:
        return 0  # Если массив слишком короткий, то нет переключений

    trend = "none"  # Начинаем без тренда
    trend_changes = 0  # Инициализируем счетчик переключений
    current_trend_length = 1  # Текущая длина текущего тренда

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            if trend == "decreasing":
                if current_trend_length > 2:
                    trend_changes += 1
                current_trend_length = 1
            trend = "increasing"
            current_trend_length += 1
        elif arr[i] < arr[i - 1]:
            if trend == "increasing":
                if current_trend_length > 2:
                    trend_changes += 1
                current_trend_length = 1
            trend = "decreasing"
            current_trend_length += 1

    return trend_changes


def count_trend_changes(arr, start, end, result_lock):
    trend_changes_local = 0  # Локальный счетчик переключений для потока

    if len(arr) < 3:
        return 0  # Если массив слишком короткий, то нет переключений

    trend = "none"  # Начинаем без тренда
    current_trend_length = 1  # Текущая длина текущего тренда

    for i in range(start + 1, end):
        if arr[i] > arr[i - 1]:
            if trend == "decreasing":
                if current_trend_length > 2:
                    trend_changes_local += 1
                current_trend_length = 1
            trend = "increasing"
            current_trend_length += 1
        elif arr[i] < arr[i - 1]:
            if trend == "increasing":
                if current_trend_length > 2:
                    trend_changes_local += 1
                current_trend_length = 1
            trend = "decreasing"
            current_trend_length += 1

    # Захватываем блокировку, чтобы избежать гонки данных
    with result_lock:
        trend_changes_total.value += trend_changes_local


# Пример использования:
arr = [1, 2, 3, 2, 1, 4, 3, 2, 1, 2, 3, 4]
result = count_trend_changes(arr)
print(result)


def find_all_bitonic(n):
    """
    Подсчет количества всех битонических подпоследовательностей в массиве
    Сложность O(n) линейно
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
    nn = [6, 7, 1, 5, 3, 2, 4, 9, 3, 2, 8, 7]
    nnn = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]
    nnnn = [-1, -1, -1, -2, -3, 3, 4, 5, 6, 6, 7, 6, 6, 8, 10, -100]
    find_all_bitonic(n)

    # data = [-1, -1, -1, -2, -3, 3, 4, 5, 6, 6, 7, 6, 6, 8, 10, -100]
    # num_threads = 4  # Количество потоков
    #
    # # Разделим массив на равные части для каждого потока
    # chunk_size = len(data) // num_threads
    # threads = []
    #
    # global_results = []  # Глобальный список для хранения результатов из каждого потока
    #
    # for i in range(num_threads):
    #     start = i * chunk_size
    #     end = (i + 1) * chunk_size if i < num_threads - 1 else len(data)
    #     thread = threading.Thread(target=lambda: global_results.append(count_bitonic_subsequences(data, start, end)))
    #     threads.append(thread)
    #
    # for thread in threads:
    #     thread.start()
    #
    # for thread in threads:
    #     thread.join()
    #
    # # Объединяем результаты из каждого потока и суммируем их
    # total_count = sum(global_results)
    # print(f"Количество битонических подпоследовательностей: {total_count}")

    import threading

    # для count_trend_change
    # Пример использования многопоточности:
    arr = [1, 2, 3, 2, 1, 4, 3, 2, 1, 2, 3, 4]
    num_threads = 4  # Количество потоков, которые вы хотите использовать
    result_lock = threading.Lock()  # Блокировка для синхронизации результатов

    # Создаем список потоков и разбиваем массив на сегменты для каждого потока
    threads = []
    segment_length = len(arr) // num_threads
    trend_changes_total = threading.Value('i', 0)  # Общий счетчик переключений

    for i in range(num_threads):
        start = i * segment_length
        end = (i + 1) * segment_length if i < num_threads - 1 else len(arr)
        thread = threading.Thread(target=count_trend_changes, args=(arr, start, end, result_lock))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    print(
        trend_changes_total.value)  # Вывод: 2 (переключения с возрастания на убывание после 3 и с убывания на возрастание после 1)
