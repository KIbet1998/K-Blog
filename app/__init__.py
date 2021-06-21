from flask import Flask, app
from config import config_options,DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
def create_app(config_name):
    app=Flask(__name__)
     #Creating the main configurations
    app.config.from_object(config_options[config_name])
    #Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
   # setting config
    from .request import configure_request
    configure_request(app)
  # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app