"""
Работа с файлами open -mode
"""
if __name__ == '__main__':
    # Открытие файла для чтения
    fileR = open('work_file/openread.txt', 'r')
    # Вы можете читать файл построчно, используя метод readline(), или в список строк с помощью метода readlines().
    print(fileR.read())
    # print(fileR.readline())
    # print(fileR.readlines())


    # Открытие файла для записи (создание файла, если он не существует)
    # mode 'w' обнуляет все содержимое лучше воспользоваться 'a'
    fileW = open('work_file/openread.txt', 'w')
    fileW.write('Hi!')

    # Открытие файла для добавления данных в конец
    fileA = open('work_file/openread.txt', 'a')
    fileA.write('HiHHI')

    # После завершения работы с файлом рекомендуется закрывать его
    fileR.close()
    fileW.close()
    fileA.close()