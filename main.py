from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
from werkzeug.wrappers import response
import db_config as database

#resources
from res.badge import Badge
from res.badges import Badges

app=Flask(__name__)
api=Api(app)

@app.route('/all/adults/')
def get_adults():
    response = list(database.db.Badges.find({'age': {"$gte": 21}}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/projection/')
def get_name_and_age():
    response = list(database.db.Badges.find({'age': {"$gte": 21}}, {'name':1, 'age':1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/kids/')
def get_kids():
    response = list(database.db.Badges.find({'age': {"$lte": 21}}, {'name':1, 'age':1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

"""

database.db.Badges.

.database is the config file
.db is the database name
.NameCollection The next part is the collection

"""





api. add_resource(Badge,'/new/','/<string:by>=<string:data>/')
api. add_resource(Badges, '/all/', '/delete/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True)