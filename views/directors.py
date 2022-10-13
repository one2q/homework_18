from flask_restx import Namespace, Resource

from container import director_service
from dao.model.director import DirectorSchema


director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsViews(Resource):
	def get(self):
		genres = director_service.get_all()
		return directors_schema.dump(genres), 200


@director_ns.route('/<int:pk>')
class DirectorViews(Resource):
	def get(self, pk):
		genre = director_service.get_one(pk)
		return director_schema.dump(genre), 200