import  sqlite3

conn = sqlite3.connect('../mydb.db')

conn.execute(''' CREATE TABLE EMPLOYEE
                 (  ID INT NOT NULL ,
                    NAME  TEXT NOT NULL ,
                    AGE  INT  NOT NULL ,
                    ADDRESS CHAR(50) ,
                    SALARY REAL ) ; ''')

print "Table added successfully"

conn.close()

