from flask import request
from flask_restx import Namespace, Resource

from container import movie_service
from dao.model.movie import MovieSchema, Movie


movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):
	def get(self):

		director_request = request.args.get('director_id')
		genre_request = request.args.get('genre_id')
		year_request = request.args.get('year')

		if director_request:
			movies = movie_service.get_by_director(director_request)
			return movies_schema.dump(movies), 200
		if genre_request:
			movies = movie_service.get_by_genre(genre_request)
			return movies_schema.dump(movies), 200
		if year_request:
			movies = movie_service.get_by_year(year_request)
			return movies_schema.dump(movies), 200

		movies = movie_service.get_all()
		return movies_schema.dump(movies), 200

	def post(self):
		data = request.json
		movie_service.create(data)
		return 'ok', 201


@movie_ns.route('/<int:pk>')
class MovieViews(Resource):
	def get(self, pk: int):
		movie = movie_service.get_one(pk)
		return movie_schema.dump(movie), 200

	def put(self, pk: int):
		data = request.json
		movie_service.update(data, pk)
		return 'ok', 202

	def patch(self, pk: int):
		data = request.json
		movie_service.update(data, pk)
		return 'ok', 202

	def delete(self, pk: int):
		movie_service.delete(pk)
		return 'Ok', 200
