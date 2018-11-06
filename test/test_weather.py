import unittest
import requests
from datetime import datetime, timedelta
from project import app
import pytz

class TestWeather(unittest.TestCase):
    def setUp(self):
        pass

    def test_weather_by_city(self):
        city = 'kowloon'
        r = requests.get('http://127.0.0.1/api/v1/weather?city='+city)
        self.assertEqual(r.status_code,200)
        response = r.json()
        self.assertIsNone(response['error'])
        self.assertIn(city,response['data']['city'])

    def test_weather_by_range(self):
        hk = pytz.timezone('Asia/Hong_Kong')
        city = 'kowloon'
        last_hour_date_time = datetime.now(hk) - timedelta(hours = 1)
        start = last_hour_date_time.strftime(app.dateformat)
        end = datetime.now(hk).strftime(app.dateformat)
        r = requests.get('http://127.0.0.1/api/v1/weather?city='+city+'&start='+start+'&end='+end)
        self.assertEqual(r.status_code,200)
        response = r.json()
        self.assertIsNone(response['error'])

if __name__ == '__main__':
    unittest.main()
