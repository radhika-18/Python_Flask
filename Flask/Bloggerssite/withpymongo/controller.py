from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import bson

app = Flask(__name__)
mongo = PyMongo(app)

app.config['MONGO_DBNAME'] = 'bloggerdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/bloggerdb'


@app.route('/insertblog/<title>/<postedby>/<postedon>', methods=['POST', 'GET'])
def addtoblog(title, postedby, postedon):
    if request.method == 'POST':
        blog = mongo.db.blogger
        result = str(blog.insert({'title': title, 'postedby': postedby, 'postedon': postedon, 'comments':[]}))
        return jsonify({"message": "Blog added successfully", "blog id": result})


@app.route('/showallblogs')
def showblogs():
    ap = mongo.db.blogger.find()
    allPosts, temp = [], {}
    for a in ap:
        for i in a:
            if i == "_id":
                temp[i] = str(a[i])
            else:
                temp[i] = a[i]
        allPosts.append(temp)
        temp = {}
    del temp
    return jsonify(allPosts)


@app.route('/addcomment/<id>/<commenttext>/<commentedby>', methods=['POST', 'GET'])
def showablog(id,commenttext,commentedby):
    if request.method == "POST":
        print(id)
        result = mongo.db.blogger.update(
             {'_id': bson.objectid.ObjectId(id) },
            {'$push':
                 {'comments':
                      {
                          'commenttext':commenttext,
                        'commentedby': commentedby
                        }
                  }
             })
        return jsonify({"message":"Successfully added"})

if __name__ == '__main__':
    app.run(debug=True)
