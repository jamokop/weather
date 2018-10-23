from flask import request
from project import create_app
import flask_nicely
from werkzeug.exceptions import ServiceUnavailable
import requests
import configparser
from pprint import pprint

app = create_app()

@app.route("/", methods=['GET'])
@flask_nicely.nice_json
def spider():
    config = configparser.ConfigParser()
    config.read('cfg.ini')
    city = request.args.get("city")
    if not city:
        raise flask_nicely.errors.Forbidden('city is missing')

    try:
        url = config['Openweather']['ApiUrl'] +'?q='+city+'&appid='+ config['Openweather']['AppId']
        weather = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise  flask_nicely.errors.GatewayTimeout("Openweather service is unavailable.")

    response = weather.json()
    if weather.status_code != 200:
        return response
    payload = {
        'city':city,
        'temp':response['main']['temp'],
        'humidity':response['main']['humidity']
    }
    result = requests.post('http://127.0.0.1:5001/weather',  json = payload )
    if result.status_code != 200:
        raise  flask_nicely.errors.GatewayTimeout("database service is unavailable.")
    return result.json()['data']

if __name__ == "__main__":
    app.run(port=5000, debug=True)



