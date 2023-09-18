from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    """ Check if the user exists in the database"""
    user = is_user(email)
    if user and check_password_hash(user.hashed_password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200
        # 401 Unauthorized
    return jsonify({"message": "Invalid username or password"}), 401
