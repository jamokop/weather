from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .helper.config import Config
import os
db = SQLAlchemy()

def create_app(cfg):
    app = Flask(__name__)
    config = Config(cfg)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['Mysql']['Uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.dateformat = "%Y-%m-%d %H:%M:%S"
    db.init_app(app)
    return app,config

env = os.environ.get("ENVIRONMENT", "production")
if env == 'development':
    app,config = create_app('cfg_test.ini')
else:
    app,config = create_app('cfg.ini')
db.create_all(app=app)
