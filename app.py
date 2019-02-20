from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum.insert({
    'num_of_users': 0 
})

@app.route('/')
def running():
    return "I am fully operational and all my systems are functioning perfectly"

api.add_resource(Visit, "/hello")

if __name__ == "__main__":
    app.run(host="0.0.0.0")