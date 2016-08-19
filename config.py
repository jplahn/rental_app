import os

SECRET_KEY = os.environ.get('SECRET_KEY')
# Mongo DB Configuration
MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')

# App Config
FLASK_DEBUG = bool(os.environ.get('FLASK_DEBUG'))
ASSETS_DEBUG = bool(os.environ.get('ASSETS_DEBUG'))
