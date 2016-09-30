from flask import jsonify, request
from db_config import cartApp,db
from withsqlalchemy.models.Product import Product
from withsqlalchemy.models.Cart import Cart


@cartApp.route('/getCategories')
def getCategory():
    pass


@cartApp.route('/getProducts')
def getAllProducts():
    productlist = []
    result = Product.query.all()
    for product in result:
        productlist.append(Product.getJSON(product))
    return jsonify(productlist)


@cartApp.route('/getProduct/<category>')
def getProducts(category):
    productlist = []
    result = Product.query.filter_by(category=category)
    for product in result:
        productlist.append(Product.getJSON(product))
    return jsonify(productlist)


@cartApp.route('/getProduct/<int:id>')
def getProduct(id):
    productlist = []
    result = Product.query.filter_by(id=id)
    for product in result:
        productlist.append(Product.getJSON(product))
    return jsonify(productlist)


@cartApp.route('/addToCart/productid/<int:id>/quantity/<int:quantity>', methods=['POST','GET'])
def addProduct(id, quantity):
    if request.method == 'POST':
        cart = Cart(id,quantity)
        try:
            db.session.add(cart)
            db.session.commit()
            return jsonify("Record successfully added")
        except Exception as e:
            print e
            return jsonify("Could not add")

#
# @cartApp.route('/showMyCart')
# def showMyCart():
#     pass


@cartApp.route('/addproduct/<name>/<category>/<int:price>/<description>/<image>/<int:instock>', methods=['POST', 'GET'])
def addproduct(name, category, price, description, image, instock):
    if request.method == 'POST':
        product = Product(name, category, price, description, image, instock)
        db.session.add(product)
        db.session.commit()
        return jsonify("Record successfully added")


if __name__ == '__main__':
    db.create_all()
    cartApp.run(debug=True)
