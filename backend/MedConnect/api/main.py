"""
This file contains routes for the main application
"""
from flask import Blueprint, jsonify
from api.models import Patients, Doctors

main = Blueprint('main', __name__)

all_users = {'patients': Patients, 'doctors': Doctors}

def is_user(email: str) -> bool:
    for user_type, user_value in all_users.items():
        real = user_value.query.filter_by(email_address=email).first()
        if real:
<<<<<<< HEAD
            return real
        return False
    
=======
            return [real, user_type]
    return None
>>>>>>> b05707b39010306ebb54e10264a2ae9a0b0175bc


@main.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ First JSON file """
    return jsonify({'Status': 'Ok'}), 200
