#possibly in service 4
from application import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_location = db.Column(db.String(100), nullable=False)

