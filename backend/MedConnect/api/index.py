from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ First JSON file """
    return jsonify({'status': 'Ok'}), 200
