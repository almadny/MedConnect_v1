"""
This file contains routes for the main application
"""
from flask import Blueprint, jsonify
from api.models import Patients, Doctors

main = Blueprint('main', __name__)

all_users = {'Patients': Patients, 'Doctors': Doctors}

def is_user(email: str) -> bool:
    for user in all_users.values():
        real = user.query.filter_by(email_address=email).first()
        if real:
            return real
        return False
    


@main.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ First JSON file """
    return jsonify({'Status': 'Ok'}), 200
