from datetime import datetime
from werkzeug.security import generate_password_hash
from .. import db


class User(db.Model):
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
