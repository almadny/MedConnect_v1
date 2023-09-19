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
    jwt.init_app(app)

    from api.errors import error
    app.register_blueprint(error, url_prefix='/api/error')

    from api.main import main
    app.register_blueprint(main, url_prefix='/api/main')

    from api.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/api/users')

    from api.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    from api.appointments import appt_bp
    app.register_blueprint(appt_bp, url_prefix='/api/appt')

    from api.blog import blog
    app.register_blueprint(blog, url_prefix='/api/blog')

    from api.medical_records import records_bp
    app.register_blueprint(records_bp, url_prefix='/api/records')

    return app
