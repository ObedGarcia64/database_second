from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
import db_config as database

app=Flask(__name__)
api=Api(app)

class AllBadge(Resource):
    """ Get all badges """
    def get(self):
        all_badges = list(database)

if __name__ == '__main__':
    app.run(load_dotenv=True)