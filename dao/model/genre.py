from marshmallow import Schema, fields
from setup_db import db

# Describe genre table for db
class Genre(db.Model):
	__tablename__ = 'genre'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))

# Describe genre table for serialization
class GenreSchema(Schema):
	id = fields.Int()
	name = fields.Str()