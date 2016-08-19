import os

from flask import Flask, flash, request, render_template, redirect, url_for
from flask_assets import Environment
from forms import CityForm
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config')
assets = Environment(app)

# configure MongoDB values
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/', methods=['POST', 'GET'])
def get_index():
    form = CityForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            city = form.city.data
            return redirect(url_for('get_data', city=city))
        else:
            flash('Please fill in the required details', 'danger')

    return render_template('index.html', form=form)


@app.route('/<city>')
def get_data(city):
    result = mongo.db.monthly_rent_average.find_one({'city': city})
    if result:
        flash('Alright alright alright, city ' + city + ' found!', 'success')
        return render_template('city.html', city=city)
    else:
        flash('Oops! City ' + city + ' doesn\'t exist in our DB yet!', 'danger')
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
