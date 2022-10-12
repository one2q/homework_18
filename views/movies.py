from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema, Movie
from setup_db import db

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):
	def get(self):
		data = db.session.query(Movie).all()
		return movies_schema.dump(data)
