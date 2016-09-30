from flask import Flask, jsonify, request,json
from ProductData import Product
from ProductCrud import Productdao
from Dbconnecton import dbconnection

products = {
    1: {
        'name': 'Samsung Galaxy S7 Edge (Black Onyx)',
        'category': 'Electronics',
        'price': 88999,
        'image': 'static/mobile1.jpg',
        'description': 'Redefine what a phone can do. Samsung is completely changing how you"ll share experiences and memories. They are doing that by shattering the boundaries of what a phone can do. And it"s the biggest thing to happen to phones. Ever.',
        'instock': 5
    },
    2: {
        'name': 'Huawei P8 Lite Gold',
        'category': 'Electronics',
        'price': 21999,
        'image': 'static/electronics2.jpg',
        'description': 'Redefine what a phone can do. Samsung is completely changing how you"ll share experiences and memories. They are doing that by shattering the boundaries of what a phone can do. And it"s the biggest thing to happen to phones. Ever.',
        'instock': 5
    },
    3: {
        'name': 'Dany HDTV-1000 (LCD TV Media Player)',
        'category': 'Electronics',
        'price': 3100,
        'image': 'static/electronics3.jpg',
        'description': 'High Resolution Support.High Resolution 1920x1200 output, which feasts your eyes withextra-ordinary picture quality.It is fully compatible with both CRT & LCD Monitor.',
        'instock': 5
    },
    4: {
        'name': 'NESTLE NIDO 1+ 1kg (Box)',
        'category': 'Baby Products',
        'price': 975,
        'image': 'static/babyproducts.jpg',
        'description': 'When your child turns 1, his curious mind wants to explore, touch and feel everything, and in the process, puts things in his mouth.',
        'instock': 5
    },
    5: {
        'name': 'NESTLE NIDO 1+ 1kg (Box)',
        'category': 'Baby Products',
        'price': 975,
        'image': 'static/babyproducts.jpg',
        'description': 'When your child turns 1, his curious mind wants to explore, touch and feel everything, and in the process, puts things in his mouth.',
        'instock': 5
    },
    6: {
        'name': 'NESTLE NIDO 1+ 1kg (Box)',
        'category': 'Baby Products',
        'price': 975,
        'image': 'static/babyproducts.jpg',
        'description': 'When your child turns 1, his curious mind wants to explore, touch and feel everything, and in the process, puts things in his mouth.',
        'instock': 5
    },
    7: {
        'name': 'Dollar Marker Allmark Permanent 2.0 Black',
        'category': 'Stationery',
        'price': 25,
        'image': 'static/stationery.jpg',
        'description': 'My pen',
        'instock': 5
    },
    8: {
        'name': 'Dollar Marker Allmark Permanent 2.0 Black',
        'category': 'Stationery',
        'price': 25,
        'image': 'static/stationery.jpg',
        'description': 'My pen',
        'instock': 5
    },
    9: {
        'name': 'Dollar Marker Allmark Permanent 2.0 Black',
        'category': 'Stationery',
        'price': 25,
        'image': 'static/stationery.jpg',
        'description': 'My pen',
        'instock': 5
    }

}
categories = ['Electronics', 'Stationery', 'Baby Products']

myProductList = []
cartApp = Flask(__name__)
cartApp.secret_key = "xoriant123#"


@cartApp.route('/getCategories')
def getCategory():
    productdao = Productdao(dbconnection())
    return jsonify(productdao.getCategory())


@cartApp.route('/getProducts')
def getAllProducts():
    productdao = Productdao(dbconnection())
    return jsonify(productdao.showallproducts())


@cartApp.route('/getProduct/<category>')
def getProducts(category):
    productdao = Productdao(dbconnection())
    return jsonify(productdao.showaproductbycategory(category))


@cartApp.route('/getProduct/<int:id>')
def getProduct(id):
    productdao = Productdao(dbconnection())
    return jsonify(productdao.showaproductbyid(id))


@cartApp.route('/addToCart/productid/<int:id>/quantity/<int:quantity>', methods=['POST'])
def addProduct(id, quantity):
    if request.method == 'POST':
        productdao = Productdao(dbconnection())
        return jsonify(productdao.addproducttocart(id,quantity))


@cartApp.route('/showMyCart')
def showMyCart():
    productdao = Productdao(dbconnection())
    return jsonify(productdao.showMyCart())


@cartApp.route('/addproduct/<name>/<category>/<int:price>/<description>/<image>/<int:instock>',methods=['POST', 'GET'])
def addproduct(name, category, price, description, image, instock):
    if request.method == 'POST':
        product = {'name': name, 'category': category, 'price': price, 'description': description, 'image': image,
                   'instock': instock}
        productdata = Product(product)
        productdao = Productdao(dbconnection())
        return jsonify(productdao.addproduct(productdata))


if __name__ == '__main__':
    cartApp.run(debug=True)
