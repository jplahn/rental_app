import os

from flask import Flask, flash, request, render_template, redirect, url_for
from forms import CityForm
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config')

# configure MongoDB values
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/', methods=['POST', 'GET'])
def get_index():
    form = CityForm(csrf_enabled=False)
    if form.validate_on_submit():
        city = form.city.data
        return redirect(url_for('get_data', city=city))
    else:
        return render_template('index.html')


@app.route('/<city>')
def get_data(city):
    result = mongo.db.monthly_rent_average.find_one({'city': city})
    if result:
        return render_template('city.html', city=city)
    else:
        flash('Oops! City doesn\'t exist in the DB yet!')
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
