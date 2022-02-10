from flask import request
from flask_restx import Resource, Namespace
from dao.model.movies import Movie, MovieSchema
from setup_db import db
from implemented import movie_service


movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
                    "director_id": director_id,
                    "genre_id": genre_id,
                    "year": year,
        }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req = request.json
        new_movie = movie_service.create(req)
        return "", 201, {"location": f"/movies/{new_movie.id}"}


@movie_ns.route('/<id>')
class MovieView(Resource):
    def get(self, mid):
        req = movie_service.get_one(mid)
        return movie_schema.dump(req), 200

    def put(self, mid):
        req = request.json
        if "id" not in req:
            req["id"] = mid
        movie_service.update(req)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204