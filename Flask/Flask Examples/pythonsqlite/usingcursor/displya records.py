import sqlite3

conn =sqlite3.connect('../mydb.db')

c=conn.cursor()

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
#c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
conn.commit()
print("All records")
for row in c.execute(" SELECT * FROM stocks "):
    print row

print "Searchig one"
t = ('IBM',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print c.fetchall()
