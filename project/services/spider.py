import requests
import configparser
import sys
import os


def spider():
    cfg_file = os.path.dirname(os.path.abspath(__file__))+'/../cfg.ini'
    config = configparser.ConfigParser()
    config.read(cfg_file)
    if len(sys.argv) < 2:
        sys.exit('city is missing')
    city = sys.argv[1]
    try:
        url = config['Openweather']['ApiUrl'] +'?q='+city+'&appid='+ config['Openweather']['AppId']
        weather = requests.get(url)
    except requests.exceptions.ConnectionError:
        sys.exit("Openweather service is unavailable.")

    response = weather.json()
    if weather.status_code != 200:
        sys.exit(response)

    try:
        payload = {
            'city':city,
            'temp':response['main']['temp'],
            'humidity':response['main']['humidity']
        }
        result = requests.post('http://127.0.0.1:5001/weather',  json = payload )
    except requests.exceptions.ConnectionError:
        sys.exit("database service is unavailable.")

    if result.status_code != 200:
        raise  sys.exit("weather data inserts failed")

    print(result.json()['data'])

if __name__ == "__main__":
    spider()



