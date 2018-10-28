from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .helper.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    config = Config()
    app.config['SQLALCHEMY_DATABASE_URI'] = config['Mysql']['Uri']
    app.dateformat = "%Y-%m-%d %H:%M:%S"
    db.init_app(app)
    return app
