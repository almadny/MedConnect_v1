from flask import Blueprint, jsonify
from api.patients import Patients
from api.doctors import Doctors

main = Blueprint('main', __name__)

all_users = {'Patients': Patients, 'Doctors': Doctors}

def is_user(email):
    for user in all_users.values():
        real = user.query.filter_by(email=email).first()
        if real:
            return True, user
        return False


@main.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ First JSON file """
    return jsonify({'Status': 'Ok'}), 200
