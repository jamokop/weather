import unittest
from project import app
from project.services.spider import spider
from project.models.weather import Weather
import time

class TestSpider(unittest.TestCase):
    def setUp(self):
        pass

    def test_spider(self):
        city = 'kowloon'
        response = spider(city)
        self.assertIn('insert_id',response)
        id = response['insert_id']
        with app.app_context():
            query = Weather.query.filter_by(id=id).first()
            self.assertIsInstance(query,Weather)

if __name__ == '__main__':
    unittest.main()
