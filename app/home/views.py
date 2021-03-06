from flask import Blueprint, render_template
from app.core.db import db
from models import *

home_views = Blueprint('home', __name__,
                        template_folder='../templates',
                        static_folder='../static')

@home_views.route('/')
def home():
	personal_information = PersonalInformation.query.filter_by(id=1).first()
	return render_template('index.html', **locals())
