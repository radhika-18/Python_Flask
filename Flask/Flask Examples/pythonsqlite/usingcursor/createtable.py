import sqlite3

conn =sqlite3.connect('../mydb.db')

cursor=conn.cursor()

cursor.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

conn.close()