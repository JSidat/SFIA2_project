#possibly in service 4
from application import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_fact = db.Column(db.String(100), nullable=False)

    

