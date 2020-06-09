from application import app
from flask import request, Response
from random import randint

@app.route('/country/name', methods = ['GET'])
def country():
    countries = ['Italy', 'Japan', 'Brazil']
    
    return Response(cities[randint(0, len(countries)-1)], mimetype='text/plain')

