from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
csrf = CSRFProtect()
admin = Admin()

def create_app():
   # Initialize the app and the config
   app = Flask(__name__)
   app.config.from_object('config')

   # Initialize plugins
   db.init_app(app)
   login.init_app(app)
   migrate.init_app(app, db)
   csrf.init_app(app)
   admin.init_app(app)

   with app.app_context():
      
      from app.models.User import User

      admin.add_view(ModelView(User, db.session))
      # Register Blueprints
      from app.Blueprints.index_bp import index_bp
      from app.Blueprints.auth_bp import auth_bp
        
      app.register_blueprint(index_bp)
      app.register_blueprint(auth_bp)

      return app