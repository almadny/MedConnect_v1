from flask import Flask
from api.index import main
from api.errors import error

def create_app():
    app = Flask(__name__)

    app.register_blueprint(error, url_prefix='/api')
    app.register_blueprint(main, url_prefix='/api')

    return app
