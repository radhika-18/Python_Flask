from flask import Flask
from flask_pymongo import PyMongo


blogapp=Flask(__name__)

blogapp.config['MONGO_DBNAME']='blogdb'
blogapp.config['MONGO_URI']='mongodb://localhost:27017/blogdb'

mongo=PyMongo(blogapp)