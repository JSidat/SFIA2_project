from application import app
from flask import request, Response
from random import randint

@app.route('/city/name', methods = ['GET'])
def country():
    countries = ['Italy', 'Japan', 'Brazil']
    Country = (cities[randint(0, len(list)-1)], mimetype= 'text/plain')
    return Country