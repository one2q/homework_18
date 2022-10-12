from flask import request
from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema, Movie
from setup_db import db

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):
	def get(self):
		movies = db.session.query(Movie).all()
		return movies_schema.dump(movies), 200

	def post(self):
		data = request.json
		try:
			db.session.add(Movie(**data))
			return 'Ok', 200
		except Exception as e:
			print(e)
			db.session.rollback()
			return e, 200


@movie_ns.route('/<int:pk>')
class MoviesViews(Resource):
	def get(self, pk):
		movie = db.session.query(Movie).get(pk)
		return movie_schema.dump(movie), 200

	# def post(self, pk):
	# 	data = request.json
	# 	try:
	# 		movie = db.session.query(Movie).get(pk)
	# 		movie = Movie(**data)
	# 		db.session.add(movie)
	# 		return 'Ok', 200
	# 	except Exception as e:
	# 		print(e)
	# 		db.session.rollback()
	# 		return e, 200

	def put(self, pk):
		data = request.json
		try:
			db.session.execute(db.update(Movie).where(Movie.id == pk).values(**data))
			db.session.commit()
			return 'ok', 200
		except Exception as e:
			print(e)
			db.session.rollback()
			return e, 200

	def delete(self, pk):
		try:
			movie = db.session.query(Movie).get(pk)
			db.session.delete(movie)
			db.session.commit()
			return 'Ok', 200
		except Exception as e:
			print(e)
			db.session.rollback()
			return e, 200