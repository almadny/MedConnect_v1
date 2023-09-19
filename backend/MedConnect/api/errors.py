from flask import Blueprint, jsonify

error = Blueprint('error', __name__)

@error.app_errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404


@error.app_errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 404


@error.app_errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Forbidden'}), 403

@error.app_errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500
