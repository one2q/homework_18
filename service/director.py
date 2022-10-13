from dao.director import DirectorDAO


class DirectorService:
	def __init__(self, dao: DirectorDAO):
		self.dao = dao

	def get_one(self, pk: int):
		return self.dao.get_one(pk)

	def get_all(self):
		return self.dao.get_all()