#IMPORT SESSION: FLASK APP AND BLUEPRINTS FROM VIEW
from flask import Flask
from app.views.register_user import bp_newuser
from app.views.home import bp_home

#IMPORT DB FROM MODEL
from models.register_model import db

#IMPORT ENVIRONS
from environs import Env

def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    #ENVIRONMENT CONFIGURATION
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI")


    app.register_blueprint(bp_newuser)
    app.register_blueprint(bp_home)
    db.init_app(app)    

    return app