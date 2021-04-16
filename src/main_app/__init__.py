from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import *

DB = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config_by_name[config_name])
	app.config.from_pyfile('config.py')
	DB.init_app(app)
	flask_bcrypt.init_app(app)

	return app