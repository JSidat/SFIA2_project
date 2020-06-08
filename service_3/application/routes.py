from application import app
from flask import request, Response
from random import randint

@app.route('/country/population', methods = ['POST'])
def population():
    numbers = ['60.36 million', '209.5 million', '126.5 million']
    population = (numbers[randint(0, len(topics)-1)], mimetype='text/plain')
    return population
    #country =  request.data.decode('utf-8')

@app.route('/country/continent', methods = ['POST'])
def continent():
    continents = ['South America', 'Asia', 'Europe']
    continent = (continents[randint(0, len(continents)-1)], mimetype='plain/text')
    return continent
