from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresViews(Resource):
	def get(self):
		data = []
		return data