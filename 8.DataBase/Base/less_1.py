import sqlite3 as sq

if __name__ == '__main__':
    # подключение каталога, если его нет то он будет создан
    with sq.connect("saper.db") as con:  # .db, .db3, .sqlite, .sqlite3
        # cur = con.cursor() для непосредственного взаимодействия с базами данных
        # должны использовать эккзепляр cursor класса Cursosr
        #
        # cur.execute("""ЗАПРОС""") -  Непосредственно запрос к базе данных с помощью метода execute
        #
        # в конце программы базу данных обязательно нужно закрыть
        # если работать с помощью контекстного менеджера то это уже не нужно
        # con.close()

        cur = con.cursor()  # Cursor
        # создаем таблицу TABLE с именем users
        # далее прописываем структуру таблицы имя - тип (набор полей)
        # cur.execute("""DROP TABLE IF EXISTS users""")
        # cur.execute("""CREATE TABLE IF NOT EXISTS users (
        # user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        # name TEXT NOT NULL,
        # sex INTEGER DEFAULT 1,
        # old INTEGER,
        # score INTEGER
        # )""")
        # cur.execute("""DROP TABLE users""")  # удаление таблицы
        cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 3")
        # result = cur.fetchall()
        result_1 = cur.fetchone()
        result_2 = cur.fetchmany(2)
        # print(result)
        print(result_1)
        print(result_2)

