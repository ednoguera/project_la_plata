from flask import Blueprint

bp_home = Blueprint("bp_home", __name__, url_prefix='/')

@bp_home.route('/')
def home():
        return {
            "app_message":"Getting started in La Plata",
            "server_status": "Running"
        }
