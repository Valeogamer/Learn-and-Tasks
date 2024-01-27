""" iterdump - Создание бэкапа БД """

import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    # получаем спсиок запросов sql для воссоздания БД
    # for sql in con.iterdump():
    #     # получим список sql запросов для формирования прочитанной таблицы
    #     print(sql)

    # создаем dump базы данных
    # with open("sql_dump.sql", "w") as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    # восстановление БД
    with open("sql_dump.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)