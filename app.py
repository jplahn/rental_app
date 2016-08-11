from flask import Flask, request, render_template, redirect, url_for
from forms import CityForm

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def get_index():
    form = CityForm(csrf_enabled=False)
    if form.validate_on_submit():
        city = form['city']
        return render_template('city.html', city=city)
    else:
        return render_template('index.html')
