from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema, Genre
from setup_db import db

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresViews(Resource):
	def get(self):
		try:
			directors = db.session.query(Genre).all()
			return genres_schema.dump(directors), 200
		except Exception as e:
			print(e)
			return e, 200


@genre_ns.route('/<int:pk>')
class GenreViews(Resource):
	def get(self, pk):
		try:
			director = db.session.query(Genre).get(pk)
			return genre_schema.dump(director), 200
		except Exception as e:
			print(e)
			return e, 200