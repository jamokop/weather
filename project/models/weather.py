from project import app,db
from time import time
import json

class Weather(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.DECIMAL(5,2), nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False,index=True)

    def __init__(self, city, temp,humidity):
        self.city = city
        self.temp = temp
        self.humidity = humidity
        self.addtime = int(time())

    def __str__(self):
        return '<City %s> temp:%s' % (self.city, self.temp)

    def toJSON(self):
        return {
            'id'      : self.id,
            'city'    : self.city,
            'temp'    : float(self.temp),
            'humidity': self.humidity,
            'addtime' : self.addtime
        }


