from flask import Flask
from flask_sqlalchemy import SQLAlchemy

cartApp = Flask("mycart")
cartApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/products.db'
cartApp.config['SECRET_KEY'] = "xoriant123"
cartApp.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(cartApp)
