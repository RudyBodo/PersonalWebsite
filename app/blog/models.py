from app.core.db import db
from datetime import date

class Category(db.Model):
	__tablename__  = 'category'
	id = db.Column(db.Integer, primary_key=True)
	category_name = db.Column(db.String())
	created  = db.Column(db.String())

	def __init__(self, category_name):
		self.category_name = category_name
		create  = date.today()
		self.created = '%d/%d/%d' %(create.day, create.month, create.year)

	def __repr__(self):
		return '{}'.format(self.category_name)

class Blog(db.Model):
	__tablename__ = 'blog'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String())
	content = db.Column(db.String())
	created = db.Column(db.String())
	id_category = db.Column(db.Integer, db.ForeignKey(Category.id))
	category = db.relationship('Category',backref = db.backref('blog', lazy = 'dynamic'))

	def __init__(self, title , content, id_category):
		self.title = title
		self.content  = content
		self.id_category = id_category
		create = date.today()
		self.created = '%d/%d/%d' %(create.day, create.month, create.year)

	def __repr__(self):
		return '<Blog{}'.format(self.title)
