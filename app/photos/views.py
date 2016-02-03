from flask import Blueprint, render_template
from app.core.db import db
from models import *
from app.home.models import PersonalInformation

photos_views = Blueprint('photos', __name__,
						template_folder='../templates',
						static_folder='../static')

@photos_views.route('/photos')
def photos():
	foto = Photos.query.all()
	personal_information = PersonalInformation.query.filter_by(id=1).first()
	return render_template('photos.html', **locals())
