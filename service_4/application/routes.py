from application import app
import requests


@app.route('/get/country', methods = ['GET'])
def country_fact():
    country =  requests.get('http://service2:5001/country')
    topic = requests.get('http://service3:5002/topic')
    if country == 'Italy' and topic == 'population':
        statement = 'The population of Italy is 60.36 million'
    elif country == 'Italy' and topic == 'continent':
        statement = 'Italy is in Europe'
    elif country == 'Italy' and topic == 'main language':
        statement = 'The main language in Italy is Italian'
    elif country == 'Brazil' and topic == 'population':
        statement = ' The population of Brazil is 209.5 million'
    elif country == 'Brazil' and topic == 'continent':
        statement = 'Brazil is in South America'
    elif country == 'Brazil' and topic == 'main language':
        statement = 'The main language of Brazil is Portuguese'
    elif country == 'Japan' and topic == 'population':
        statement = 'The population of Japan is 126.5 million'
    elif country == 'Japan' and topic == 'continent':
        statement = 'Japan is in Asia'
    elif country == 'Japan' and topic == 'main Language':
        statement = 'The main language of Japan is Japanese'
    statement = (statement, mimetype='plain/text')
    return statement
    
    