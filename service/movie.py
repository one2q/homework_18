from dao.movie import MovieDAO


class MovieService:
	def __init__(self, dao: MovieDAO):
		self.dao = dao

	def get_one(self, pk: int):
		return self.dao.get_one(pk)

	def get_all(self):
		return self.dao.get_all()

	def create(self, data):
		return self.dao.create(data)

	def update(self, data, pk: int):
		return self.dao.update(data, pk)

	def delete(self, pk):
		self.dao.delete(pk)

	def get_by_director(self, pk: int):
		return self.dao.get_by_director(pk)

	def get_by_genre(self, pk: int):
		return self.dao.get_by_genre(pk)

	def get_by_year(self, year: int):
		return self.dao.get_by_year(year)