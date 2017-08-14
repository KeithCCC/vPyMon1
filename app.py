from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def store_list():
    client = MongoClient('localhost',27017)
    db = client.csdb
    col = db.storelist2
    mylist = list(col.find())

    return render_template('storelist.html', col=mylist)
