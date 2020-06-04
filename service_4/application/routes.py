from application import app
import requests


@app.route('/get/country', methods = ['GET'])
def city_location():
    city =  requests.get('http://service2:5001/city')
    country = requests.get('http://service3:5002/country')
    statement = city.text + 'is in ' + country.text

    #db.session.add(city.text)
    #db.session.add(country.text)
    #db.session.commit()
    return statement