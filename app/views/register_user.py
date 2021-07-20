from flask import Blueprint, request
from http import HTTPStatus
from app.models.models import User
from app.models.models import db


# SERIALIZERS
from app.services.user_services import (
    serialize_user, 
    serialize_user_list
)

# IMPORTING INTEGRITY ERROR IF USER IS ALREADY CREATED ON DATABASE
from sqlalchemy.exc import IntegrityError


bp_user = Blueprint("bp_user", __name__, url_prefix='/users')


# ROUTE TO CREATE A NEW USER
@bp_user.route("/register", methods=["POST"])
def register() -> dict:
    username = request.json["username"]
    email = request.json["email"]
    
    user = User(username=username, email=email)
        
    try:
        db.session.add(user)
        db.session.commit()
        
        return {
            'status': HTTPStatus.CREATED,
            'user': {'name': username, 'email': email}
        }
    except IntegrityError:
        return {
            'msg': 'Email already exists', 
            'status': HTTPStatus.BAD_REQUEST
            }

# ROUTE TO GET A USER LIST
@bp_user.route('/', methods=["GET"])
def get_users():
    user_list = User.query.all()
    user_dict = serialize_user_list(user_list)
    return {'users': user_dict}

@bp_user.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id: int ):
    user_map = User.query.get(user_id)
    user_by_id = serialize_user(user_map)
    
    if not user_by_id:
        return "User not exists"
    print(user_by_id)
    
    return {'user': user_by_id}