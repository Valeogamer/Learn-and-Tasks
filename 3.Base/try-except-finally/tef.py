try:
    # попытка выполнить код, который может вызвать исключение
    x = 10 / 0  # попытка деления на ноль
    # Если возникнет ошибка, то принт не сработает, 
    # сразу перенесемся в except
    print(x)
except ZeroDivisionError:
    # Обработка конкретного типа исключения (деления на ноль)
    print("Ошибка деления на ноль!")
finally:
    # код который выполнить в любом случае, даже если возникла ошибка
    print("Финальный блок: завершение работы")