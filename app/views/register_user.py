from flask import Blueprint, request

bp_newuser = Blueprint("bp_newuser", __name__)

@bp_newuser.route("/register", methods=["POST"])
def register() -> dict:
    username = request.json["username"]
    email = request.json["email"]
    return {
        "username": username,
        "email": email
    }