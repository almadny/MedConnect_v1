#!/usr/bin/python3
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request, jsonify
from model import Appointment, db, User, Doctor

from flask_jwt_extended import (create_access_token,
                            get_jwt_identity,
                            jwt_required,
                            JWTManager)
app = Flask(__name__)

db.init_app(app)

#setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)



@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    """ Check if the user already exists in the database"""
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 409  # 409 Conflict

    """ If the user doesn't exist, create a new user and add them to the database"""
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception:
        db.session.rollback()
        return jsonify({"message": "Registration failed"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    """ Check if the user exists in the database"""
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.hashed_password, password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
        # 401 Unauthorized
    return jsonify({"message": "Invalid username or password"}), 401
