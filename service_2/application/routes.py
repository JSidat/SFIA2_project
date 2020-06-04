from application import app
from flask import request, Response
from random import randint

@app.route('/city/name', methods = ['GET'])
def city():
    cities = ['London', 'Paris', 'Tokyo', 'New York', 'Vaduz', 'Luxembourg City', 'Sydney', 'Moscow', 'Geneva', 'Madrid',
    'Edinburgh', 'Beijing', 'Mumbai', 'Berlin' 'Cape Town', 'Rio de Janeiro', 'Toronto']
    return Response(cities[randint(0,16)], mimetype= 'text/plain')