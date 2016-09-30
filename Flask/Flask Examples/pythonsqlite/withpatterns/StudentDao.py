import sqlite3
class StudentDao:
    def __init__(self, connection):
        self.connection = connection

    def addrecord(self, studentdata):
        try:
            with self.connection as con:
                cursor = con.cursor()
                cursor.execute('INSERT INTO students (name,addr,city,pin) VALUES (?, ?, ?, ?)',(studentdata.name, studentdata.address, studentdata.city,studentdata.pincode))
                con.commit()
                msg = "Record added successfully to the database"
        except Exception as e:
            con.rollback()
            msg = "Error in insertion",e
        return msg

    def showrecords(self):
        with self.connection as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            cursor.execute('SELECT * FROM students')
            rows = cursor.fetchall();
        return rows
