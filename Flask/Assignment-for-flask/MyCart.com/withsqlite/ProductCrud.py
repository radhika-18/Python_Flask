import sqlite3 as sql

productid = 101


class Productdao:
    def __init__(self, connection):
        self.connection = connection

    def addproduct(self, productdata):
        global productid
        try:
            with self.connection as con:
                cursor = con.cursor()
                cursor.execute(
                    "INSERT INTO product(id,name,category,price,image,description,instock) VALUES (?,?,?,?,?,?,?) ", (
                    productid, productdata.name, productdata.category, productdata.price, productdata.image,
                    productdata.description, productdata.instock))
                productid += 1
                con.commit()
                msg = "record added successfully"
        except Exception as e:
            con.rollback()
            msg = "Could not add", e
        return msg

    def showallproducts(self):
        products = {}
        productlist = []
        with self.connection as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM product')
            rows = cursor.fetchall()
            for row in rows:
                products = {
                    'id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3],
                    'image': row[4],
                    'description': row[5],
                    'instock': row[5],
                }
                productlist.append(products)
        return productlist

    def getCategory(self):
        productlist=[]
        with self.connection as con:
            cursor = con.cursor()
            for rows in  cursor.execute('SELECT distinct(category) FROM product'):
                productlist.append(rows)
        return productlist

    def showaproductbyid(self,id):
        products={}
        productlist=[]
        with self.connection as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM product WHERE id=:id',{"id": id})
            rows=cursor.fetchall()
            for row in rows:
                products={
                    'id':row[0],
                    'name':row[1],
                    'category':row[2],
                    'price':row[3],
                    'image':row[4],
                    'description':row[5],
                    'instock':row[5],
                }
                productlist.append(products)
        return  productlist

    def showaproductbycategory(self,category):
        products={}
        productlist=[]
        with self.connection as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM product WHERE category=:category',{"category": category})
            rows=cursor.fetchall()
            for row in rows:
                products={
                    'id':row[0],
                    'name':row[1],
                    'category':row[2],
                    'price':row[3],
                    'image':row[4],
                    'description':row[5],
                    'instock':row[5],
                }
                productlist.append(products)
        return  productlist

    def addproducttocart(self,id,quantity):
        try:
            with self.connection as con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO cart(id,quantity) VALUES (?,?) ",(id,quantity))
                con.commit()
                msg = "added to cart"
        except Exception as e:
            con.rollback()
            msg = "Could not add", e
        return msg

    def showMyCart(self):
        productlist = []
        with self.connection as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM cart')
            rows = cursor.fetchall()
            for row in rows:
                productlist.append(self.showaproductbyid(row[0]))
            return productlist

