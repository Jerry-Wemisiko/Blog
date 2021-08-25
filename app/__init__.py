from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import    SQLAlchemy
from flask_mail import Mail
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy ()
mail = Mail()

def create_app(config_name):

    app = Flask (__name__)
    # create app configurations
    app.config.from_object(config_options[config_name])
    

    #initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    #Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    return app