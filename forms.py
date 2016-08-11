from flask_wtf import Form
from wtforms import StringField, fields

class CityForm(Form):
    city = StringField('city')
