from datetime import date
from app.core.db import db

class Activities (db.Model):
	__tablename__ = 'activities'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	content = db.Column(db.String())
	created = db.Column(db.String())

	def __init__(self, title, content):
		self.title = title
		self.content = content
		create = date.today()
		self.created = '%d/%d/%d' %(create.day, create.month, create.year)

	def __repr__(self):
		return '<Activities{}>'.format(self.title)
