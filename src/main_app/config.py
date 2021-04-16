import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'EFFE50097ED8F3804B847626CCFDA43EB68629B226797377AD1F958964BBDEF7'
	DEBUG = False
	

class DevelomentConfig(Config):
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/tierritas.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	DEBUG = False
	# uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base

config_by_name = dict(
	dev = DevelomentConfig,
	prod = ProductionConfig
)

SECRET_KEY = Config.SECRET_KEY
FRONTEND_URL = 'https://www.tierritas.com.sv'
EMAIL_FROM = "tierritasmotoclub@gmail.com"
EMAIL_PASSWORD = ('CrmzG#01')


ALLOWED_EXTENSIONS = {'text', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'upload/')



