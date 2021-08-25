from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import    SQLAlchemy
from flask_mail import Mail

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



    return app