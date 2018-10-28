from project import db,create_app
from project.models.weather import Weather
import flask_nicely
import configparser
from flask import request,jsonify
from pprint import pprint
import datetime
import pytz


app = create_app()
db.create_all(app=app)

@app.route("/weather", methods=['GET'])
@flask_nicely.nice_json
def get():
    hk = pytz.timezone('Asia/Hong_Kong')
    city = request.args.get('city')
    start = request.args.get('start')
    end = request.args.get('end')
    query = Weather.query.filter_by(city=city)
    if start and end:
        date1 = datetime.datetime.strptime(start, app.dateformat).replace(tzinfo=hk).timestamp()
        date2 = datetime.datetime.strptime(end, app.dateformat).replace(tzinfo=hk).timestamp()
        query = query.filter(Weather.addtime.between(date1,date2))
        return [ record.toJSON() for record in query.all()]
    else:
        return query.order_by(Weather.addtime.desc()).first().toJSON()

@app.route("/weather", methods=['POST'])
@flask_nicely.nice_json
def post():
    data = request.get_json()
    if not data:
        raise flask_nicely.errors.Forbidden('Content-Type should be application/json')

    record = Weather(data['city'],data['temp'],data['humidity'])
    db.session.add(record)
    db.session.commit()
    return {'insert_id':record.id}

if __name__ == "__main__":
    app.run(port=5001, debug=True)



