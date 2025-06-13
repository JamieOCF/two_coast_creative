from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SearchField, IntegerField, DecimalField, FloatField, PasswordField
from wtforms import RadioField, BooleanField, SubmitField, DateField
from wtforms.validators import InputRequired, NumberRange, EqualTo

class Form(FlaskForm):
    submit = SubmitField("Submit")
