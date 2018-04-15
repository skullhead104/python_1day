import sqlite3
import sys
import datetime

conn = sqlite3.connect("test.db")
cur = conn.cursor()
# cur.execute('CREATE TABLE stocks (data text, trans text, symbol text, qty real, price real)')
cur.execute("INSERT INTO stocks VALUES ('%s', 'BUY', 'RHAT', 150,35.2)" %datetime.datetime.today().strftime("%Y-%m-%d"))
cur.execute("INSERT INTO stocks VALUES ('%s', 'BUY', 'RHAT', 150,35.2)" %datetime.datetime.today().strftime("%Y-%m-%d"))
# cur.execute("INSERT INTO stocks VALUES ('2018-04-16', 'BUY', 'RHAT', 170,35.17)")
conn.commit()


rows = cur.execute("SELECT * FROM stocks")
for row in rows:
    print(row)

conn.close()

