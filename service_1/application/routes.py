from flask import render_template
from application import app
import requests

@app.route('/')
@app.route('/home', methods = ['GET'])
def home():
    response = requests.get('http://service4:5003/city_location')
    statement = response.text

    #possibly in service 4
    db.session.add(statement)
    db.session.commit()
    return render_template('home.html', statement = statement, title='Home Page')
