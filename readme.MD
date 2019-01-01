# simple flask sacfold with pipenv

## If no installed pipenv - install - other solution docker (another scafold)
```
pip install pipenv
```
## Activate pipenv
```
pipenv shell
```
## Install a flask package
```
pipenv install Flask
```
## for environment variables
```
pipenv install python-dotenv
```
## create folder for all modules ie flask_scafold
```
mkdir flask_scafold
```
## create class for configuration ie:
```python
from dotenv import load_dotenv #to use .env
import os #read from os


class Config:    
    ''' config class for environment dependencies '''
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path=env_path) #this cause .env is a part of os system variables
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PORT=os.environ.get("PORT")
    HOST=os.environ.get("HOST")
```
## create __init__.py file (heart) of configuration:
```python
from flask_scafold.config import Config
from flask import Flask
from flask_mail import Mail

#any app configurarion place here - email as an example
mail = Mail()

def create_app(config_class=Config):
    """A create app method from config file (class).
    
    Attributes:
        :Config: Class whitch contains configuration from .env and all other
    """
    #set configuration to the app
    app = Flask(__name__)
    #simpler way - create Config class
    app.config.from_object(Config)

    #any utils can be easily initialise in here
    mail.init_app(app)

    #at the end return app
    return app

```
## For the SQL DB remember that Flask-SQLAlchemy doesn't come with Flask so:
```
$ pipenv install flask-sqlalchemy

```

## Ignore pipfile
```
pipenv install --ignore-pipfile
```
## Run app with pipenv
```
pipenv run app.py
```