from application import app
from flask import request, Response
from random import randint

@app.route('/country', methods = ['GET', 'POST'])
def country():
    countries = ['Italy', 'Japan', 'Brazil']
    
    return Response(countries[randint(0, len(countries)-1)], mimetype='text/plain')

