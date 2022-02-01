from wtforms import Form, StringField, validators, EmailField, PasswordField, ValidationError
from app.models.User import User


class RegistrationForm(Form):
   username = StringField('Username', validators=[validators.Length(min=4, max=30)])
   email = EmailField('Email', validators=[validators.Length(min=5), validators.Email(message='Invalid email address.')])
   password = PasswordField('Password', validators=[validators.InputRequired(message='Password field cannot be empty.'), validators.EqualTo('confirm_password', message='Passwords do not match!')])
   confirm_password = PasswordField('Confirm password', validators=[validators.InputRequired()])

   def validate_email(self, field):
      if User.query.filter_by(email=field.data).first():
         raise ValidationError('Email already registered.')