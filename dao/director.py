from dao.model.director import Director


class DirectorDAO:
	"""
		This DAO class is needed to coordinate with database
		and return all necessary information
	"""
	def __init__(self, session):
		self.session = session

	# Get one director
	def get_one(self, pk: int):
		return self.session.query(Director).get(pk)

	# Get all directors
	def get_all(self):
		return self.session.query(Director).all()