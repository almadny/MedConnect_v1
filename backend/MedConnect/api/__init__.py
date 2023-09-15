from flask import Flask
from app.index import main

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main, url_prefix='api/')

    return app
