import sqlite3

conn =sqlite3.connect('../mydb.db')

c=conn.cursor()

c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

c.execute("Select * from stocks")

print c.fetchone()

conn.close()