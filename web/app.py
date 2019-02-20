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
    if users.find({"Username": username }).count() == 0:
        return False
    else:
        return True

def verifyPW(username, password):
    if not UserExist(username):
        return False

    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


class Register(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["Username"]
        password = postedData['Password']

        if (UserExist(username)): 
            retJson = {
                "status": 301,
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

        return jsonify(retJson)


class Detect(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["Username"]
        password = postedData["Password"]
        text1 = postedData["Text1"]
        text2 = postedData["Text2"]

        if not UserExist(username):
            retJson = {
                "status": 301,
                "msg": "Invalid Username"
            }

            return jsonify(retJson)
        
        if not verifyPW(username, password):
            retJson = {
                "status": 302,
                "msg": "Invalid Password"
            }
        
        #calculate 
        nlp = spacy.load('en_core_web_sm')
        
        text1 = nlp(text1)

        text2 = nlp(text2)
        # as ratio approaches 1 the more similar the texts are
        ratio = text1.similarity(text2)

        retJson = {
            "status": 200,
            "msg": "Similarity ratio calculated as ratio approaches 1 the more similar the texts are.",
            "ratio": ratio
        }

        return jsonify(retJson)

# @app.route('/')
# def running():
#     return "I am fully operational and all my systems are functioning perfectly"


# api.add_resource(Visit, "/hello")
api.add_resource(Detect, "/detect")
api.add_resource(Register, "/register")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
