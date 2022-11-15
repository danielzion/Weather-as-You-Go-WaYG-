from flask import Flask, render_template, request, abort, Response, json
import urllib

app = Flask(__name__)

@app.route('/<city>', methods=["GET"])
def index(city):

    city = request.args.get('city')
    if city is None:
        abort(400, "Missing Argument")

    data = {}
    data['q'] = request.args.get('city')
    data['appid'] = 'XXXXXXX'
    data['units'] = 'metric'
    url_values = urllib.parse.urlencode(data)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)

    resp = Response(data)
    resp.status_code = 200
    return render_template('index.html', title="Weather App", data=json.loads(data.read().decode("utf8")))


app.run(debug=True)
    