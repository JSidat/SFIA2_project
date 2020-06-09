from application import app, db
from flask import render_template, request, redirect, Response
from application.models import Facts
from random import randint
import requests


@app.route('/fact', methods = ['GET', 'POST'])
def country_fact():
    country =  requests.get('http://service_2:5001/country').text
    topic = requests.get('http://service_3:5002/topic').text    
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
    

    addstatement=Facts(country_fact=statement)
    db.session.add(addstatement)
    db.session.commit() 

    return statement.text
    


      
    
    
    
    
    
    