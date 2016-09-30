from withsqlalchemy.db_config import db

class Cart(db.Model):
    cart_id=db.Column('cart_id',db.Integer,primary_key=True)
    product_id=db.Column(db.Integer,db.ForeignKey('product.id'))
    quantity=db.Column(db.Integer)


    def __init__(self,product_id,quantity):
        self.product_id=product_id
        self.quantity=quantity




