import sqlite3 as sql


def dbconnection():
    conn = sql.connect("products.db")
    # conn.execute('''Create  table product
    # (id int unique,
    # name text not null,
    # category text not null,
    # price int not null,
    # image text not null,
    # description text not null,
    # instock int not null)''')

    #     conn.execute('''Create  table cart
        # (id int unique,
        # quantity int not null)
        #     ''')

    return conn
