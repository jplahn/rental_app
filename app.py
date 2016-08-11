from flask import Flask, request, render_template, redirect, url_for
from forms import CityForm
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

# configure MongoDB values
app.config['MONGO_HOST'] = 'ds153715.mlab.com'
app.config['MONGO_PORT'] = '53715'
app.config['MONGO_DBNAME'] = 'rental_app'
app.config['MONGO_USERNAME'] = 'test'
app.config['MONGO_PASSWORD'] = 'test'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/', methods=['POST', 'GET'])
def get_index():
    form = CityForm(csrf_enabled=False)
    if form.validate_on_submit():
        city = form['city']
        return render_template('city.html', city=city)
    else:
        return render_template('index.html')


@app.route('/db')
def get_data():
    result = mongo.db.monthly_rent_average.find_one_or_404({'city': 'Seattle'})
    print result
