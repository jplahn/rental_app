# -*- coding: utf-8 -*- 
import json
import logging
import os
import requests

from dotenv import Dotenv
from flask import Flask, flash, request, render_template, redirect, url_for, jsonify
from flask import _request_ctx_stack
from flask_assets import Environment
from flask.ext.cors import cross_origin
from flask_pymongo import PyMongo
from forms import CityForm
from functools import wraps
from werkzeug.local import LocalProxy

app = Flask(__name__)
app.config.from_object('config')
assets = Environment(app)

# define logfile name 
logfile = app.config['APP_LOG_FILENAME']

# configure MongoDB values
mongo = PyMongo(app, config_prefix='MONGO')

# authentication annotation
current_user = LocalProxy(lambda: _request_ctx_stack.top.current_user)

# Load Env variables
env = None

try:
    env = Dotenv('/.env')
except IOError:
    env = os.environ

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      return redirect('/')
    return f(*args, **kwargs)

  return decorated

@app.route('/', methods=['POST', 'GET'])
def get_index():
    form = CityForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            city = form.city.data
            return redirect(url_for('get_data', city=city, env=env))
        else:
            flash('Please fill in the required details', 'danger')

    return render_template('index.html', form=form, env=env)

@app.route('/<city>')
def get_data(city):
    result = mongo.db.monthly_rent_average.find_one({'city': city})
    if result:
        flash('Alright alright alright, city ' + city + ' found!', 'success')
        return render_template('city.html', city=city, env=env)
    else:
        flash('Oops! City ' + city + ' doesn\'t exist in our DB yet!', 'danger')
        return render_template('index.html', env=env)

@app.route('/callback')
def callback_handling():
  code = request.args.get('code')

  json_header = {'content-type': 'application/json'}

  token_url = "https://{domain}/oauth/token".format(domain=env["AUTH0_DOMAIN"])
  token_payload = {
    'client_id' : env['AUTH0_CLIENT_ID'], \
    'client_secret' : env['AUTH0_CLIENT_SECRET'], \
    'redirect_uri' : env['AUTH0_CALLBACK_URL'], \
    'code' : code, \
    'grant_type': 'authorization_code' \
  }

  token_info = requests.post(token_url, data=json.dumps(token_payload), headers = json_header).json()

  user_url = "https://{domain}/userinfo?access_token={access_token}"  \
    .format(domain=env["AUTH0_DOMAIN"], access_token=token_info['access_token'])

  user_info = requests.get(user_url).json()

  session['profile'] = user_info

  return redirect('/account')

@app.route('/account')
@requires_auth
def get_account(f):
    return "You're authenticated!"

@app.errorhandler(404)
def page_not_found(e):
    app.logger.error('Page not found: {page}'.format(page=request.path))
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error('Internal Server Error when accessing: {page}'.format(page=request.path))
    return render_template('500.html'), 500

if __name__ == "__main__":
    # Create log files up to 10MB (with backup of prior logs) then rotate the file
    handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=10240, backupCount=10)
    handler.setLevel(logging.WARNING)
    # File logging timestamp from Flask documentation
    handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'))

    app.logger.addHandler(handler)
    app.logger.warning('WARNING test')
    app.logger.error('ERROR test')

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
