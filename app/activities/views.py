from flask import Blueprint, render_template
from app.core.db import db
from models import Activities
from app.home.models import PersonalInformation

activities_views = Blueprint ('activities', __name__,
							template_folder='../templates',
							static_folder='../static')

@activities_views.route('/activities')
def activities():
	activity = db.session.query(Activities).all()
	personal_information = PersonalInformation.query.filter_by(id=1).first()
	return render_template('activities.html', **locals())
