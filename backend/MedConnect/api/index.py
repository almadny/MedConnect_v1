from flask import Blueprint, jsonify, abort, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ First JSON file """
    return jsonify({'Status': 'Ok'}), 200
