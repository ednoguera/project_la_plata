from flask import Flask
from app.views.register_user import bp_newuser
from app.views.home import bp_home

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_newuser)
    app.register_blueprint(bp_home)    

    return app