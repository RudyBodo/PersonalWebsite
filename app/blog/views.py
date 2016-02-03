from flask import Blueprint, render_template, abort
from app.core.db import db
from models import *
from app.home.models import PersonalInformation

blog_views = Blueprint ('blog', __name__,
                        template_folder='../templates',
                        static_folder='../static')


@blog_views.route('/blog')
def blog():
    personal_information = PersonalInformation.query.filter_by(id=1).first()
    blog = Blog.query.all()
    return render_template('blog.html', **locals())

@blog_views.route('/blog/<id>')
def show_post(id):
	personal_information = PersonalInformation.query.filter_by(id=1).first()
	blog = Blog.query.filter_by(id=id).first_or_404()
	return render_template('blog_post.html', **locals())


@blog_views.route('/blog/category')
def category_blog():
	personal_information = PersonalInformation.query.filter_by(id=id).first()
	category = Category.query.all()
	return render_template('category.html', **locals())

@blog_views.route('/blog/category/<id_category>')
def show_category(id_category):
	personal_information = PersonalInformation.query.filter_by(id=1).first()
	blog = Blog.query.filter(Blog.id_category.endswith(id_category)).all()
	return render_template('category_post.html', **locals())

@blog_views.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
