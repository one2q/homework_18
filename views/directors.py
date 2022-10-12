from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema, Director
from setup_db import db

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsViews(Resource):
	def get(self):
		try:
			directors = db.session.query(Director).all()
			return directors_schema.dump(directors), 200
		except Exception as e:
			print(e)
			return e, 200


@director_ns.route('/<int:pk>')
class DirectorViews(Resource):
	def get(self, pk):
		try:
			director = db.session.query(Director).get(pk)
			return director_schema.dump(director), 200
		except Exception as e:
			print(e)
			return e, 200