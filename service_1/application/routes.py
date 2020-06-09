from flask import render_template, request
from application import app, db
import requests
from application.models import Facts

@app.route('/')
@app.route('/home', methods = ['GET'])
def home():
    response = requests.get('http://service4:5003/country_fact')
    statement = response.text
    addstatement = Facts(
        country_fact = statement
    )

    
    db.session.add(addstatement)
    db.session.commit()
    facts = Facts.query.all()

    return render_template('home.html', statement = statement, posts = facts, title='Home Page')
