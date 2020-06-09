from flask import render_template, request
from application import app, db
import requests
from application.models import Facts

@app.route('/')
@app.route('/home', methods = ['GET'])
def home():
    statement = requests.get('http://service_4:5003').text   
    facts = Facts.query.all()
    return render_template('home.html', statement=statement, posts=facts, title='Home Page')
