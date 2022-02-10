from flask import request
from flask_restx import Resource, Namespace
from dao.model.genres import Genre, GenreSchema
from setup_db import db
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/<id>')
class GenreView(Resource):
    def get(self, gid):
        req = genre_service.get_one(gid)
        return genre_schema.dump(req), 200


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        req = genre_service.get_all()
        return genres_schema.dump(req), 200

