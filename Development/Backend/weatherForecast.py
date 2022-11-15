from flask import Flask, abort, jsonify, render_template
from configparser import ConfigParser
import requests
from os import path


# the app
app = Flask(__name__, instance_relative_config=True)

# icons folder
ICONS = path.join("static", "icons")

app.config['SECRET_KEY'] = "ThisIsASecretDonTel"
app.config['SESSION_TYPE'] = "filesystem"
app.config['UPLOAD_FOLDER'] = ICONS

# getting the weather API key
config_file = 'key.ini'
config = ConfigParser()
config.read(config_file)
weather_api = config['api_key']['key']


# main route
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

            final_result = format_weather(forecast_response)

            return final_result

        except Exception as error:
            return error
    else:
        abort(400, "City Argument Not Found")



# formatting the weather json
def format_weather(weatherJson):
    try:
        city_name = weatherJson['city']['name']
        city_country = weatherJson['city']['country']
        for item in weatherJson['list']:
            weather_description = item['weather'][0]['description']
            weather_temperature = item['main']['temp']
            weather_humidity = item['main']['humidity']
            wind_speed = item['wind']['speed']
            weather_icon = item['weather'][0]['icon']
            forecast_date = item['dt_txt']

        data_result = {
            'City': city_name,
            'Country': city_country,
            'Description': weather_description,
            'Temperature': weather_temperature,
            'Humidity': weather_humidity,
            'Wind Speed': wind_speed,
            'Icon': weather_icon,
            'Date': forecast_date
        }

        data_response = jsonify(data_result)

    except Exception as error:
        abort(400, error)

    return data_response



#@app.route("/show-coordinates/<city>")
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