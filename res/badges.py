from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
from pymongo import results
from werkzeug.wrappers import response
import db_config as database


class Badges(Resource):
    """ Get all badges """
    def get(self):
        response = list(database.db.Badges.find())

        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)

    def post(self):
        _ids = list(database.db.Badges.insert_many([
            {
                'header_img_url':request.json[0]['header_img_url'],
                'profile_picture_url':request.json[0]['profile_picture_url'],
                'name':request.json[0]['name'],
                'age':request.json[0]['age'],
                'city':request.json[0]['city'],
                'bets':request.json[0]['bets'],
                'state':request.json[0]['state'],

            },
            {
                'header_img_url':request.json[1]['header_img_url'],
                'profile_picture_url':request.json[1]['profile_picture_url'],
                'name':request.json[1]['name'],
                'age':request.json[1]['age'],
                'city':request.json[1]['city'],
                'bets':request.json[1]['bets'],
                'state':request.json[1]['state'],

            }

        ]).inserted_ids)

        results = []

        for _id in _ids:
            results.append(str(_id))

        return jsonify({'inserted_ids': results})
    
    def delete(self):
        return database.db.Badges.delete_many({}).deleted_count