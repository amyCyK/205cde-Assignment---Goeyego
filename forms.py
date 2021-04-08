from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, textAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
	name = TextField('Name of viewer', [validators.Required('Please enter your name.')])
	Gender = RadioField('Gender', choices=[('M','Male'),('F','Female')])
	Address = textAreaField('Email',[validators.Required('Please enter your email address.')])
	Age = IntegerField('Age')
	Region = SelectField('Languages', choices=[('HK','Hong Kong'),('UK','United Kingdom')])
	Submit = SubmitField('Send')
		