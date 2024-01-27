""" Созание базы данных непосредственно в памяти"""
import sqlite3 as sq
data = [("car", "машина"),
        ("cat", "кот"),
        ("tree", "дерево"),
        ("color", "цвет"),
        ("house", "дом")]
con = sq.connect(':memory:')
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dict(
    eng TEXT, rus TEXT
    )""")
    cur.executemany("INSERT INTO dict VALUES(?, ?)", data)
    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())