import sqlite3 as sq
cars = [
    ('Audi', 52642),
    ('Mers', 57172),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bently', 350000)
]

with sq.connect("cars.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("""CREATE TABLE IF NOT EXISTS cars(
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER
    )""")
    '''Добавление данных'''

    # Способ №1
    # cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Mers', 57172)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Skoda', 9000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Bently', 350000)")

    # Способ №2
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # Способ №3
    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    '''Выполнение команд и скриптов'''
    # В шаблонах можно использовать именованные параметры
    # Все атомобили которые начинаются на A будут стоить 0.
    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price':0}

    # Если нужно выполнить несколько команд (но только в данном методе нелься использовать шаблоны запросов)
    cur.executescript("""DELETE FROM cars WHERE model LIKE 'S_od%';
        UPDATE cars SET price = price + 1000
    """)

# ручная обработка
# в чем удобство?
# Комитятся только успешные операции, а ошибки и исключения откатят базы данных в исходное состояние
con = None
try:
    con = sq.connect("cars.db")
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
        );
        BEGIN;
        INSERT INTO cars VALUES(NULL, 'Audi', 52642);
        INSERT INTO cars VALUES(NULL, 'Mers', 57172);
        INSERT INTO cars VALUES(NULL, 'Skoda', 9000);
        INSERT INTO cars VALUES(NULL, 'Volvo', 29000);
        INSERT INTO cars VALUES(NULL, 'Bently', 350000);
        UPDATE cars SET price = price + 10000
        """)
    con.commit()
except sq.Error as e:
    # В случае возникновения ошибки откатимся до метки BEGIN
    if con: con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con: con.close()