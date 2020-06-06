#possibly in service 4
from application import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

