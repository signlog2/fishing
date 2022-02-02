from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .. import login
from .. import db


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
   id = db.Column(db.Integer(), primary_key=True, nullable=False)
   username = db.Column(db.String(128), nullable=False, unique=True)
   email = db.Column(db.String(128), nullable=False, unique=True)
   password_hash = db.Column(db.String(128), nullable=False)
   created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
   updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)


   @property
   def password(self):
      raise AttributeError('`password` is not a readable attribute')

   @password.setter
   def password(self, password):
      self.password_hash = generate_password_hash(password)

   def verify_password(self, password):
      return check_password_hash(self.password_hash, password)
