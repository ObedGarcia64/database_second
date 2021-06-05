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