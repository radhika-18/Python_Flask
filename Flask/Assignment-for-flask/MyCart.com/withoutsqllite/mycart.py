from flask import Flask,render_template,jsonify,request

products={
    1:{
        'name':'Samsung Galaxy S7 Edge (Black Onyx)',
        'category':'Electronics',
        'price':88999,
        'image':'static/mobile1.jpg',
        'description':'Redefine what a phone can do. Samsung is completely changing how you"ll share experiences and memories. They are doing that by shattering the boundaries of what a phone can do. And it"s the biggest thing to happen to phones. Ever.',
        'instock':5
    },
    2:{
        'name':'Huawei P8 Lite Gold',
        'category':'Electronics',
        'price':21999,
        'image':'static/electronics2.jpg',
        'description':'Redefine what a phone can do. Samsung is completely changing how you"ll share experiences and memories. They are doing that by shattering the boundaries of what a phone can do. And it"s the biggest thing to happen to phones. Ever.',
        'instock':5
        },
    3:{
        'name':'Dany HDTV-1000 (LCD TV Media Player)',
        'category':'Electronics',
        'price':3100,
        'image':'static/electronics3.jpg',
        'description':'High Resolution Support.High Resolution 1920x1200 output, which feasts your eyes withextra-ordinary picture quality.It is fully compatible with both CRT & LCD Monitor.',
        'instock':5
    },
    4:{
        'name':'NESTLE NIDO 1+ 1kg (Box)',
        'category':'Baby Products',
        'price':975,
        'image':'static/babyproducts.jpg',
        'description':'When your child turns 1, his curious mind wants to explore, touch and feel everything, and in the process, puts things in his mouth.',
        'instock':5
        },
    5:{
        'name': 'NESTLE NIDO 1+ 1kg (Box)',
        'category': 'Baby Products',
        'price': 975,
        'image': 'static/babyproducts.jpg',
        'description': 'When your child turns 1, his curious mind wants to explore, touch and feel everything, and in the process, puts things in his mouth.',
        'instock': 5
        },
    6:{
        'name':'NESTLE NIDO 1+ 1kg (Box)',
        'category':'Baby Products',
        'price':975,
        'image':'static/babyproducts.jpg',
         'description': 'When your child turns 1, his curious mind wants to explore, touch and feel everything, and in the process, puts things in his mouth.',
        'instock':5
    },
    7:{
        'name':'Dollar Marker Allmark Permanent 2.0 Black',
        'category':'Stationery',
        'price':25,
        'image':'static/stationery.jpg',
        'description':'My pen',
        'instock':5
    },
    8:{
        'name':'Dollar Marker Allmark Permanent 2.0 Black',
        'category':'Stationery',
        'price':25,
        'image':'static/stationery.jpg',
        'description':'My pen',
        'instock':5
    },
    9:{
        'name':'Dollar Marker Allmark Permanent 2.0 Black',
        'category':'Stationery',
        'price':25,
        'image':'static/stationery.jpg',
        'description':'My pen',
        'instock':5
    }

}
categories= [ 'Electronics', 'Stationery', 'Baby Products']

myProductList=[]
cartApp=Flask(__name__)
cartApp.secret_key="xoriant123#"

@cartApp.route('/getCategories')
def getCategory():
    global categories
    return jsonify(categories)

@cartApp.route('/getProducts')
def getAllProducts():
    global products
    productList = products
    return jsonify(productList)

@cartApp.route('/getProducts/<category>')
def getProducts(category):
    global products
    productList = {}
    for key,value in products.items():
        if value['category']==category:
            productList[key]=value
    return jsonify(productList)

@cartApp.route('/getProduct/<int:id>')
def getProduct(id):
    global products
    flag=0
    productList = {}
    for key,value in products.items():
        if int(key)==id:
            flag=1
            productList[key]=value
            break
    if flag==1:
        return jsonify(productList)
    else:
        error={}
        error['errormsg']="ID does not exist"
        return jsonify(error)


@cartApp.route('/addToCart/productid/<int:id>/quantity/<int:quantity>',methods=['POST'])
def addProduct(id,quantity):
    global products, successmsg
    global myProductList
    if request.method=='POST':
        if int(id) in  myProductList:
            msg="Element already exists"
        else:
            if quantity>products[id]['instock']:
                msg="Items not in stock"
            else:
                myProductList.append((id,quantity))
                msg="Successfull added to cart"
            print myProductList
    return jsonify(msg)


@cartApp.route('/showMyCart')
def showMyCart():
    global products,myProductList,quantity
    productList={}
    total=0
    for firstvalue in myProductList:
        productList[firstvalue[0]]=products[firstvalue[0]]
        quantity = firstvalue[1]
        total+=(products[firstvalue[0]]['price']*quantity)
    mycart={
        'productList':productList,
        'quantity':quantity,
        'total':total
    }
    return jsonify(mycart)

if __name__=='__main__':
    cartApp.run(debug=True)