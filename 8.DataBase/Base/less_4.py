import sqlite3 as sq

with sq.connect("cars.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.executescript("""CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER)   
    """)
    cur.execute("SELECT model, price FROM cars")

    for result in cur:
        # print(result)
        print(result['model'], result['price'])