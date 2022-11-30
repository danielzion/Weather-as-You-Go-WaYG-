from flask import Flask, abort, render_template, request 
from configparser import ConfigParser
# import requests
from os import path
from news_scrapper import scrapper

# import json to load JSON data to a python dictionary 
import json 

# urllib.request to make a request to api 
import urllib.request 

app = Flask(__name__) 

ICONS = path.join("static", "icons")


app.config['UPLOAD_FOLDER'] = ICONS



@app.route("/")
def index():
    return render_template("home.html")

@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form['city']
        city = city.replace(' ', '+')
    else:
        city = 'lagos'
    api = '48a09fb347f5f6bd562f1f58287eda4f'
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city + '&appid=' + api).read()
        forecast = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city + '&appid=' + api).read()
    except:
        city = 'lagos'
        
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city + '&appid=' + api).read() 
        list_of_data = json.loads(source)
        data = { 
		"country_code": str(list_of_data['sys']['country']), 
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']), 
		# "temp": str(list_of_data['main']['temp']) + 'k', 
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
        "cityname": city.replace('+', ' '),
        "temp_cel": str(round(list_of_data['main']['temp']-273.15,2)),
        "temp_max_cel": str(round(list_of_data['main']['temp_max']-273.15,2)),     
        "temp_min_cel": str(round(list_of_data['main']['temp_min']-273.15,2)),
        "desc": list_of_data['weather'][0]['description'],
        'icon': list_of_data['weather'][0]['icon'],
        'wind_speed': str(list_of_data['wind']['speed']),
	}
        # 5 days Forecast
        forecast = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city + '&appid=' + api).read()
        days_forecast = json.loads(forecast)
        forecast_data = days_forecast["list"][:4]

        return render_template('weather.html', msg='City name invalid!', data=data, forecast_data=forecast_data)
    list_of_data = json.loads(source)
    data = { 
		"country_code": str(list_of_data['sys']['country']), 
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']), 
		# "temp": str(list_of_data['main']['temp']) + 'k', 
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
        "cityname": city.replace('+', ' '),
        "temp_cel": str(round(list_of_data['main']['temp']-273.15,2)),
        "temp_max_cel": str(round(list_of_data['main']['temp_max']-273.15,2)),     
        "temp_min_cel": str(round(list_of_data['main']['temp_min']-273.15,2)),
        "desc": list_of_data['weather'][0]['description'],
        'icon': list_of_data['weather'][0]['icon'],
        'wind_speed': str(list_of_data['wind']['speed']),
	}
    # 5 days Forecast
    forecast = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city + '&appid=' + api).read()
    days_forecast = json.loads(forecast)
    forecast_data = days_forecast["list"][:4]

    print(forecast_data)

    return render_template('weather.html', data = data, forecast_data=forecast_data) 


# news route
@app.route('/wayg-news', methods=['GET'])
def news():
    titles,article_links,article_img_links=scrapper()

    return render_template('news.html',titles=titles,article_links=article_links,article_img_links=article_img_links)



# getting coordinated to be passed as args in the forecast api
def get_latitude_longitude(city):
    try:
        city_url = 'https://api.openweathermap.org/geo/1.0/direct'
        url_params = {
            'APPID': weather_api,
            'q': city
        }
        coordinates = requests.get(url=city_url, params=url_params)
        codJson = coordinates.json()

        result = [codJson[0]['lat'], codJson[0]['lon']]
    except:
        abort(400, "Error Handling Data")

    return result



if __name__ == '__main__':
    app.run(debug = True)