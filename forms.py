from flask_wtf import Form
from wtforms import StringField, fields
from wtforms.validators import DataRequired

class CityForm(Form):
    city = StringField('city', validators=[DataRequired()])
