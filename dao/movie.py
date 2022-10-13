from dao.model.movie import Movie


class MovieDAO:
	"""
	This DAO class is needed to coordinate with database
	and return all necessary information
	"""
	def __init__(self, session: db.session):
		self.session = session

	# Get one movie
	def get_one(self, pk):
		return self.session.query(Movie).get(pk)

	# Get all movies
	def get_all(self):
		return self.session.query(Movie).all()

	# Create new movie
	def create(self, data):
		movie = Movie(**data)
		self.session.add(movie)
		self.session.commit()
		return movie

	# Update some movie
	def update(self, data, pk):
		self.session.query(Movie).filter(Movie.id == pk).update(data)
		self.session.commit()
		return self.get_one(pk)

	# Delete a movie
	def delete(self, pk):
		movie = self.get_one(pk)
		self.session.delete(movie)
		self.session.commit()

	# Get all movies with defined director
	def get_by_director(self, pk):
		result = self.session.query(Movie).filter(Movie.director_id == pk).all()
		return result

	# Get all movies with defined genre
	def get_by_genre(self, pk):
		result = self.session.query(Movie).filter(Movie.genre_id == pk).all()
		return result

	# Get all movies with defined year
	def get_by_year(self, year):
		result = self.session.query(Movie).filter(Movie.year == year).all()
		return result