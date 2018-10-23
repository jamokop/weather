from project import db,create_app
from project.models.weather import Weather
import flask_nicely
import configparser
from flask import request
from pprint import pprint


app = create_app()
db.create_all(app=app)

@app.route("/weather", methods=['GET'])
@flask_nicely.nice_json
def get():
    return 'hello world'

@app.route("/weather", methods=['POST'])
@flask_nicely.nice_json
def post():
    pprint(request.get_json())
    data = request.get_json()
    if not data:
        raise flask_nicely.errors.Forbidden('Content-Type should be application/json')

    record = Weather(data['city'],data['temp'],data['humidity'])
    db.session.add(record)
    db.session.commit()
    return {'insert_id':record.id}

if __name__ == "__main__":
    app.run(port=5001, debug=True)



