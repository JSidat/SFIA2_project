from flask import render_template, request, redirect, Response
from application import app, db
import requests
from application.models import Facts

@app.route('/', methods = ['GET'])
def home():
    factsData = Facts.query.all()
    response = requests.get('http://service_4:5003/fact')
    result = response.text
    print(result)
    return render_template('home.html', countryfact=factsData, result=result, title='Home Page')
