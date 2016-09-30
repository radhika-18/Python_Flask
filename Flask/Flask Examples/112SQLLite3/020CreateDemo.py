import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully"




conn.execute('''CREATE TABLE COMPANY
       (ID INT NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE              INT,
       ADDRESS            TEXT     NOT NULL,
       SALARY        INT);''')
print "Table created successfully"

conn.close()

