from application import app
from flask import request, Response
from random import randint

@app.route('/country/name', methods = ['GET'])
def country():
    countries = ['Italy', 'Japan', 'Brazil']
    Country = (cities[randint(0, len(countries)-1)], mimetype= 'text/plain')
    return Country

@app.route('country/coordinates', methods = ['GET'])
def coordinates():
    coordinates = ['36.2048° N 138.2529° E', '41.8719° N 12.5674° E', '14.2350° S 51.9253° W']
    coordinate = (coordinates[randint(0, len(coordinates)-1)], mimetype='text/plain')
    if coordinate == coordinates[0]:
        country = 'Japan'
    elif coordinate == coordinates[1]:
        country = 'Italy'
    elif coordinate == coordinates[2]:
        country = 'Brazil'
    return country