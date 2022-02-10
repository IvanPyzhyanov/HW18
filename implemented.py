# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)

from setup_db import db
from service.movies import MovieService
from dao.movies import MovieDAO
from service.directors import DirectorService
from dao.directors import DirectorDAO
from service.genres import GenreService
from dao.genres import GenreDAO

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(movie_dao)
