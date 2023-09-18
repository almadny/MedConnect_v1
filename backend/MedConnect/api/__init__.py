from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_name=Config):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)
    jwt.init_app(jwt)

    from api.errors import error
    app.register_blueprint(error, url_prefix='/api')

    from api.index import main
    app.register_blueprint(main, url_prefix='/api')

    from api.doctors import doctors_bp
    app.register_blueprint(doctors_bp, prefix='/api')

    from api.auth import auth_bp
    app.register_blueprint(auth_bp, prefix='/api/auth')

    return app
