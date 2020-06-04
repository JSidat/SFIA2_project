from flask import render_template
from application import app
import requests

@app.route('/')
@app.route('/home', methods = ['GET'])
def home():
    response = requests.get('http://service4:5003/city_location')
    print(response)
    statement = response.text
    return render_template('home.html', statement = statement, title='Home')
