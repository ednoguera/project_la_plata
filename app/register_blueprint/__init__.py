from flask import Blueprint, request

register_new_user_blueprint = Blueprint("register", __name__)

@register_new_user_blueprint.route("/register", methods=["POST"])
def register() -> dict:
    username = request.json["username"]
    email = request.json["email"]
    return {
        "username": username,
        "email": email
    }