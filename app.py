from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import bcrypt
import spacy
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SimilarDB
users = db["Users"]

def UserExist(username):
    if user.find({"Username": username }).count() == 0:
        return False
    else:
        return True

def verifyPW(username, password):
    return true

class Register(Resource):
    def post(self)
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData['password']

        if (UserExist(username)): 
            retJson = {
                "status": "301",
                "msg": "Invalid Username"
            }
            return jsonify(retJson)
        
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            "Username": username,
            "Password": hashed_pw
        })

        retJson = {
            'status': 200,
            'msg': 'registration successful'
        }



class Detect(Resource):
    def post(self)
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]
        text1 = postedData["text1"]
        text2 = postedData["text2"]

        if not UserExist(username):
            retJson = {
                "status": "301",
                "msg": "Invalid Username"
            }
            return jsonify(retJson)
        

@app.route('/')
def running():
    return "I am fully operational and all my systems are functioning perfectly"


api.add_resource(Visit, "/hello")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
