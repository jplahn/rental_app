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

# Auth0 Config
AUTH0_CLIENT_SECRET = bool(os.environ.get('AUTH0_CLIENT_SECRET'))
AUTH0_CLIENT_ID= bool(os.environ.get('AUTH0_CLIENT_ID'))
AUTH0_DOMAIN = bool(os.environ.get('AUTH0_DOMAIN'))
AUTH0_CALLBACK_URL = bool(os.environ.get('AUTH0_CALLBACK_URL'))
