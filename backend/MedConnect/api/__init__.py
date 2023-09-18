from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_name=Config):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)

    from api.errors import error
    app.register_blueprint(error, url_prefix='/api')

    from api.index import main
    app.register_blueprint(main, url_prefix='/api')

    from api.doctors import doctors_bp
    app.register_blueprint(doctors_bp, prefix='/api')

    return app
