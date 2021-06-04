from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
import db_config as database

app=Flask(__name__)
api=Api(app)

class Badge(Resource):
    def post(self):
        database.db.Badges.insert_one(
            {
                'header_img_url':request.json['header_img_url'],
                'profile_picture_url':reques.json['profile_picture_url'],
                'name':reques.json['name'],
                'age':reques.json['age'],
                'city':reques.json['city'],
                'followers':reques.json['followers'],
                'likes':reques.json['likes'],
                'post':reques.json['post'],
            }
        )

class AllBadge(Resource):
    """ Get all badges """
    def get(self):
        pass

api. add_resource(Badge,'/new')

if __name__ == '__main__':
    app.run(load_dotenv=True)