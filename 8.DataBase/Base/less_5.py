""" Хранение изображения - BLOB """
import sqlite3 as sq

def readAva(n):
    try:
        with open(f"avas/{n}.png", "rb") as f:  # считываем как бинарный
            return f.read()
    except IOError as e:
        print(e)
        return False

def writeAva(name, data):
    try:
        with open(name, "wb") as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False
    return True

with sq.connect("cars.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        ava BLOB,
        score INTEGER)   
    """)
    # запись изображения в БД
    # img = readAva(1)
    # if img:
    #     binary = sq.Binary(img)  # преобразовывваем бинарные данные в спец бинарный объект sqlite
    #     cur.execute("INSERT INTO users VALUES('Ник', ?, 1000)", (binary, ))

    # чтение изображения из БД
    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']
    writeAva("out.png", img)