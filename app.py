from flask import Flask
from flask_restx import Api
from config import Config
from dao.model.movies import Movie
from dao.model.directors import Director
from dao.model.genres import Genre
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns

# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    # create_data(app, db)


# функция создать несколько сущностей чтобы добавить их в БД (здесь список созданных объектов)
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#         with db.session.begin():
#             db.session.add_all


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
