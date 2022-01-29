from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.Blueprints.index_bp import index_bp

app.register_blueprint(index_bp)