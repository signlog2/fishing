from datetime import datetime
from .. import db


class Product(db.Model):
   id = db.Column(db.Integer(), primary_key=True, nullable=False)
   prod_name = db.Column(db.String(256), nullable=False)
   created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
   updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
