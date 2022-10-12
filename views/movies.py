from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema, Movie


movie_ns = Namespace('films')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):
	def get(self):
		data = []
		return data
