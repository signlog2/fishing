from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
# login = LoginManager()

def create_app():
   # Initialize the app and the config
   app = Flask(__name__)
   app.config.from_object('config')

   # Initialize plugins
   db.init_app(app)
   # login.init_app(app)
   migrate.init_app(app, db)

   with app.app_context():
      
      from app.models.User import User

      # Register Blueprints
      from app.Blueprints.index_bp import index_bp
      from app.Blueprints.auth_bp import auth_bp
        
      app.register_blueprint(index_bp)
      app.register_blueprint(auth_bp)

      return app