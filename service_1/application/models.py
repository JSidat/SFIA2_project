from application import db

class Facts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_fact = db.Column(db.String(100), nullable=False)

    

