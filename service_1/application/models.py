from application import db

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String(100), nullable=False)

    

