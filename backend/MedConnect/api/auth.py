from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, jwt_required
from functools import wraps

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/login", methods=["POST"], strict_slashes=False)
def login():
    try:
        data = request.get_json()
        email = data.get("email_address")
        password = data.get("password")

        """ Check if the user exists in the database"""
        from api.main import is_user
        user = is_user(email)
        if user is None:
            return jsonify({"message": "Invalid username or password"}), 401
        user_object = user[0]
        if user_object and check_password_hash(user_object.hashed_password, password):
            additional_claims = {'type': user[1]}
            access_token = create_access_token(identity=user_object.id, additional_claims=additional_claims)

            return jsonify({"access_token": access_token, 
            "user_type": user[1],
            "id": user_object.id}), 200
            # 401 Unauthorized
        return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        print(e)


@jwt_required()
def access_required(access_level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = get_jwt_claims()
            from api.main import all_users
            if not isinstance(user, all_users[access_level]):
                return jsonify ({'status' : 'Unauthorized'}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
