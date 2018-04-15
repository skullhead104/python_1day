#config: euc-kr
import sqlite3
import sys
import datetime


conn = sqlite3.connect('korea.db')
# conn = sqlite3.connect(':memory.')
cur = conn.cursor()
# query = "DELETE TABLE sample_""" + testType +";"
# conn.execute(query)
# conn.commit()

query = """CREATE TABLE sample
             (commodity VARCHAR(10),
             product VARCHAR(20),
             amount INTEGER(5),
             date DATE);"""
conn.execute(query)


datas = [
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d")),
    ('JAVA',datetime.datetime.today().strftime("%H:%M:%S"), 123, datetime.datetime.today().strftime("%Y-%m-%d"))
]

statement = "INSERT INTO sample VALUES(?,?,?,?)"
conn.executemany(statement,  datas)
conn.commit()



num = 0
rows = conn.execute("SELECT * FROM sample")

print("many=======================")
for row in rows.fetchmany(3):
    print(row)

print("all=======================")
for row in rows.fetchall():
    print(row)

print("one=======================")
for row in rows.fetchone():
    print(row)


conn.close()