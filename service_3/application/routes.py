from application import app
from flask import request, Response
from random import randint

@app.route('/country/population', methods = ['POST'])
def topic():
    topics = ['population', 'continent', 'main language']
    topic = (topics[randint(0, len(topics)-1)], mimetype ='text/plain')
    return topic
    #country =  request.data.decode('utf-8')


