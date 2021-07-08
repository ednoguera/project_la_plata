from flask import Flask
from app.register_blueprint import register_new_user_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(register_new_user_blueprint)

    @app.route('/')
    def home():
        return "Getting started in La Plata"

    

    return app