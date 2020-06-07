from flask import render_template
from application import app
import requests

@app.route('/')
@app.route('/home', methods = ['GET'])
def home():
    response = requests.get('http://service4:5003/country_fact')
    statement = response.text

    
    db.session.add(statement)
    db.session.commit()
    return render_template('home.html', statement = statement, title='Home Page')
