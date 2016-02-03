from app.core.db import db

class PersonalInformation(db.Model):
    __tablename__ = 'personal_information'

    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String())
    avatar = db.Column(db.String())
    description = db.Column(db.String())
    address = db.Column(db.String())
    github = db.Column(db.String())
    facebook = db.Column(db.String())

    def __repr__(self):
        return '<PersonalInformation: {}>'.format(self.id)
