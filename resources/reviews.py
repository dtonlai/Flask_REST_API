from flask import jsonify

from flask_restful import Resource

import models


class Reviewist(Resource):
    def get(self):
        return jsonify({"review": [{"course": 1, "rating": 5}]})

class Review(Resource):
    def get(self, id):
        return jsonify({"course": 1, "rating": 5})

    def put(self, id):
        return jsonify({"course": 1, "rating": 5})
