from flask_scafold.config import Config
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


#class flask.Flask(import_name, static_url_path=None, static_folder='static', 
# static_host=None, host_matching=False, subdomain_matching=False, 
# template_folder='templates', instance_path=None, instance_relative_config=False, root_path=None)

#any app configurarion place here
#email as an example
# let create mail
mail = Mail()
db = SQLAlchemy() #for the SQL DB


def create_app(config_class=Config):
    """A create app method from config file (class).
    
    Attributes:
        :Config: Class whitch contains configuration from .env and all other
    """
    #set configuration to the app
    app = Flask(__name__)

    #simpler way - create Config class
    app.config.from_object(Config)

    #any tools can be easily initialised in here
    mail.init_app(app)

    #the same with database
    db.init_app(app)

    from flask_scafold.main.routes import main

    app.register_blueprint(main)

    #at the end return app
    return app

def app_config(app, var, default):
    return app.config.get(var) if app.config.get(var) else default
