from app.core.db import db

class Photos(db.Model):
	__tablename__ = 'photos'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String())

	def __repr__(self):
		return '<Photos{}>'.format(self.name)
