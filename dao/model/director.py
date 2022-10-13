from marshmallow import Schema, fields
from setup_db import db

# Describe director table for db
class Director(db.Model):
	__tablename__ = 'director'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))

# Describe director table for serialization
class DirectorSchema(Schema):
	id = fields.Int()
	name = fields.Str()

