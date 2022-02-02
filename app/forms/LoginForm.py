from wtforms import Form, validators, EmailField, PasswordField, BooleanField, ValidationError
from app.models.User import User


class LoginForm(Form):
   email = EmailField('Email', validators=[validators.Length(min=5), validators.Email(message='Invalid email address.')])
   password = PasswordField('Password', validators=[validators.InputRequired(message='Password field cannot be empty.')])
   remember_me = BooleanField('Remember me')
   