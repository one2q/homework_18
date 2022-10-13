from flask_restx import Namespace, Resource

from container import genre_service
from dao.model.genre import GenreSchema, Genre


genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)



@genre_ns.route('/')
class GenresViews(Resource):
	def get(self):
		genres = genre_service.get_all()
		return genres_schema.dump(genres), 200


@genre_ns.route('/<int:pk>')
class GenreViews(Resource):
	def get(self, pk):
		genre = genre_service.get_one(pk)
		return genre_schema.dump(genre), 200