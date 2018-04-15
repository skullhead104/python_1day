#config: euc-kr
import sqlite3
import sys
import datetime

conn = sqlite3.connect("korea.db")
cur = conn.cursor()

num = 0
rows = cur.execute("SELECT * FROM sample")
for row in rows.fetchall():
    print(row)

print("end")
conn.close()

