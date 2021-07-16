from flask import Blueprint, request
from http import HTTPStatus
from app.models.models import User
from app.models.models import db

bp_user = Blueprint("bp_user", __name__, url_prefix='/register')

#DATA SERIALIZER
def serialize_list(gen_list) -> list:
    return [{'id': gen.id, 'name': gen.username, 'email': gen.email} for gen in gen_list]

# ROUTE TO CREATE A NEW USER
@bp_user.route("/", methods=["POST"])
def register() -> dict:
    username = request.json["username"]
    email = request.json["email"]
    
    user = User(username=username, email=email)
    
    db.session.add(user)
    db.session.commit()
    
    return {
        "request_status": HTTPStatus.CREATED
    }
    

# ROUTE TO GET A USER LIST
@bp_user.route('/', methods=["GET"])
def get_users():
    user_list = User.query.all()
    user_dict = serialize_list(user_list)
    return {'users': user_dict}