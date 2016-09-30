import sqlite3

conn =sqlite3.connect('../mydb.db')

c=conn.cursor()

#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#assigning python variables
search=('IBM',)

#using them in query
#
# c.execute(' Select * from stocks where symbol=? ',search)
# print c.fetchone()

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

for i in c.execute("select * from stocks order by price"):
    print i

conn.close()