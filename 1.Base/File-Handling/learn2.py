"""
Работа с файлами с использованием контекстного менеджера
with
В данном случае файл уже автоматически закроется после выполнения блока with
"""
if __name__ == '__main__':
    # открываем файл для чтения в контексте
    # with open('work_file/openread.txt', 'r') as file:
    #     data = file.read()
    #     # Работа с данными
    #     print(data)
    # Файл автоматически закроется после заверщения блока with

    # Октрываем файл для записи в контексте
    # write - персоздаст файл и запишет
    # with open('work_file/openread.txt', 'w') as file:
    #     file.write('New_line')
        # Работа с данными
    # Файл автоматически закроется после заверщения блока with

    # Открытие файла для чтения и добавления данных в конец
    with open('work_file/openread.txt', 'a+') as file:
        # Чтение данных из файла
        file.seek(0) # чтобы чтение было с начала
        data = file.read()
        print("Содержимое файла:")
        print(data)
        # Добавление новых данных в конец файла
        file.write('New line add to file')
    # Файл автоматически закроется после завершения блока "with"
