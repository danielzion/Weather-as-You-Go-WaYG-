from flask import Flask, abort, render_template
from configparser import ConfigParser
import requests
from os import path
from news_scrapper import scrapper


# the app
app = Flask(
    __name__,
    instance_relative_config=True,
    template_folder='../Frontend/', # relative path to template folder
    static_folder='../Frontend/static/' # relative path to static folder
)

ICONS = path.join("static", "icons")

app.config['SECRET_KEY'] = "ThisIsASecretDonTel"
app.config['SESSION_TYPE'] = "filesystem"
app.config['UPLOAD_FOLDER'] = ICONS


# getting the weather API key
config_file = 'key.ini'
config = ConfigParser()
config.read(config_file)
weather_api = config['api_key']['key']


# homepage route
@app.route('/home-page')
def homepage():
    return render_template('home.html')

# main weather route
@app.route("/show-forecast/<city>", methods=['GET'])
def getForecast(city):
    
    # city = request.args.get('city')

    if city:
        try:
            # latitude and longitude coordinates to be passed to the forecast api
            coordinates = get_latitude_longitude(city)

            weather_url = 'https://api.openweathermap.org/data/2.5/forecast'
            url_params = {
                'APPID': weather_api,
                'units': 'metric',
                'lat': str(coordinates[0]),
                'lon': str(coordinates[0])
            }

            forecast_response = requests.get(weather_url, params=url_params).json()

        except Exception as error:
            return error
    else:
        abort(400, "City Argument Not Found")

    return render_template('weather.html', title="Weather As You Go (WAY-G) - Index", weatherJson=forecast_response)


# news route
@app.route('/wayg-news', methods=['GET'])
def checkNews():
    scrap_news = scrapper()
    return render_template('news.html', news=scrap_news)



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
    app.run(debug=True)