import sqlite3 as sql


def setdbconnection():
    conn = sql.connect("studentdb1.db")
    
    return conn

