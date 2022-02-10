from flask import request
from flask_restx import Resource, Namespace
from dao.model.directors import Director, DirectorSchema
from setup_db import db
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/<did>')
class DirectorView(Resource):
    def get(self, did):
        req = director_service.get_one(did)
        return director_schema.dump(req), 200

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        req = director_service.get_all()
        return directors_schema.dump(req), 200
