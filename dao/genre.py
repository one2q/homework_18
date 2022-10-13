from dao.model.genre import Genre


class GenreDAO:
	"""
		This DAO class is needed to coordinate with database
		and return all necessary information
	"""
	def __init__(self, session):
		self.session = session

	# Get one genre
	def get_one(self, pk: int):
		return self.session.query(Genre).get(pk)

	# Get all genres
	def get_all(self):
		return self.session.query(Genre).all()