from  withsqlalchemy.db_config import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.String(100))
    image = db.Column(db.String(300))
    instock = db.Column(db.Integer)
    products=db.relationship('Cart',backref='product',lazy='dynamic')

    def __init__(self, name, category, price, description, image, instock):
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.image = image
        self.instock = instock

    def getJSON(self):
        return {'id':self.id,'name':self.name,'category':self.category,'description':self.description,'image':self.image,'instock':self.instock,'price':self.price}
