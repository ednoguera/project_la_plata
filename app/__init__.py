#IMPORT SESSION: FLASK APP AND BLUEPRINTS FROM VIEW
from flask import Flask
from app.views.register_user import bp_user
from app.views.home import bp_home
from app.views.transaction import bp_transactions

#IMPORT DB FROM MODEL
from app.models.models import (
    db, 
    mg
)

#IMPORT ENVIRONS
from environs import Env


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)

    #CONFIG TO NOT TRACK WARNING MESSAGES
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
    
    #CONFIG TO TRACK THE CONNECTION STRING WITH THE POSTGRES
    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI") 


    app.register_blueprint(bp_user)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_transactions)
    db.init_app(app)
    mg.init_app(app, db) 
    
    #CREATE AN APP CONTEXT
    # app = create_app()
    # app.app_context().push()

    return app