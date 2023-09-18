"""
This file contains routes that concerns Users as listed below
1. Doctors
2. Patients
3. Healthcares
4. Admins
"""

from api import db
from flask import Blueprint, jsonify, abort, request
from api.main import is_user
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
from api.models import Patients, Doctors
from flask_jwt_extended import jwt_required

users_bp = Blueprint('users', __name__)

@users_bp.route("/addpatient", methods=["POST"], strict_slashes=False)
def register_patient():
    """
    Register a new patient
    """
    try:
        data = request.get_json()
        email_address = data['email_address']
        password = data['hashed_password']
        first_name = data['first_name']
        last_name = data['last_name']
        other_name = data['other_name']
        dob_str = data['date_of_birth']
        date_of_birth = date.fromisoformat(dob_str)
        gender = data['gender']
        phone_number = data['phone_number']

        hashed_password = generate_password_hash(password)
        if not is_user(email_address):
            patient = Patients(
                    first_name=first_name,
                    last_name=last_name,
                    other_name=other_name,
                    email_address=email_address,
                    date_of_birth=date_of_birth,
                    gender=gender,
                    phone_number=phone_number,
                    hashed_password=hashed_password
                    )
            from api import db
            db.session.add(patient)
            db.session.commit()
            return jsonify({'status' : 'Patient successfully added'}), 200

        return jsonify({'fail': 'User exists'})
    except Exception as e:
        print(e)


@users_bp.route("/patients/<int:id>", strict_slashes=False)
@jwt_required()
def get_patient(id):
    """
    Get a patient from the database
    """
    patient = Patients.query.get(id)
    if patient:
        return jsonify({
            'id': patient.id,
            'first_name' : patient.first_name,
            'last_name' : patient.last_name,
            'other_name' : patient.other_name,
            'email_address' : patient.email_address
            'phone_number' : patient.phone_number,
            'date_of_birth' : patient.date_of_birth,
            'gender' : patient.gender
            }), 200
    return jsonify({'error': 'User not found'})


@users_bp.route("/patients", strict_slashes=False)
@jwt_required()
def all_patients():
    patients = Patients.query.all()
    all_patients = []
    if patients:
        for patient in patients:
            pat = {
            'id': patient.id,
            'first_name' : patient.first_name,
            'last_name' : patient.last_name,
            'other_name' : patient.other_name,
            'email_address' : patient.email_address
            'phone_number' : patient.phone_number,
            'date_of_birth' : patient.date_of_birth,
            'gender' : patient.gender
            }
            all_patients.append(pat)
    return jsonify({'patients': all_patients}), 200

@users_bp.route("/update_patients/<int:id>", methods=["PUT"], strict_slashes=False)
@jwt_required()
def update_patient(id):
    patient = Patients.query.get(id)
    if not patient:
        return jsonify({'msg': 'User does not exist'})
    try:
        data = request.get_json()
        patient.email_address = data['email_address']
        patient.hashed_password = generate_password_hash(data['hashed_password'])
        patient.first_name = data['first_name']
        patient.last_name = data['last_name']
        patient.other_name = data['other_name']
        dob_str = data['date_of_birth']
        patient.date_of_birth = date.fromisoformat(dob_str)
        patient.gender = data['gender']
        patient.phone_number = data['phone_number']

        from api import db
        db.session.commit()
        return jsonify({'status' : 'Patient successfully added'}), 200
    except Exception as e:
        print(e)


@users_bp.route("/doctors/<int:id>", methods=["GET"])
def get_doctor(id):
    doctor = Doctors.query.get(id)
    if doctor:
        return (
            jsonify({
                "id": doctor.id,
                "first_name": doctor.name,
                "specialty": doctor.specialty
                }),
            200
        )
    return jsonify({"message": "Doctor not found"}), 404


@users_bp.route("/doctors", methods=["POST"])
def add_doctor():
    data = request.get_json()
    print(data)
    name = data.get("name")
    specialty = data.get("specialty")

    new_doctor = Doctors(name=name, specialty=specialty)

    try:
        db.session.add(new_doctor)
        db.session.commit()
        return jsonify({"message": "Doctor successfully added"}), 200
    except Exception as err:
        print(str(err))
        return jsonify({"message": "Failed to create doctor"}), 400


@users_bp.route("/doctors/<int:id>", methods=["PUT"])
def update_doctors(id):
    doctor = Doctors.query.get(id)
    if doctor:
        data = request.get_json()
        doctor.name = data.get("name", doctor.name)
        doctor.specialty = data.get("specialty", doctor.specialty)
        db.session.commit()
        return jsonify({"message": "Doctor updated successfully"}), 200
    else:
        return jsonify({"message": "Doctor not found"}), 404


@users_bp.route("/doctors/<int:id>", methods=["DELETE"])
def delete_doctor(id):
    doctor = Doctors.query.get(id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return jsonify({"message": "Doctor removed successfully"}), 200
    else:
        return jsonify({"message": "Doctor not found"}), 404


@users_bp.route('/doctors', strict_slashes=False)
def get_doctors():
    try:
        doctors = Doctors.query.all()
        all_doctors = []

        for doctor in doctors:
            doc = {
                    'first_name': doctor.first_name,
                    'last_name' : doctor.last_name,
                    'other_name': doctor.other_name,
                    'gender' : doctor.gender,
                    'phone_number' : doctor.phone_number,
                    'email_address' : doctor.email_address,
                    'specialty': doctor.specialty,
                    'healthcare_id' : doctor.healthcare_id
            }

            all_doctors.append(doc)

        return jsonify({'doctors' : all_doctors}), 200
    except Exception as e :
        print(e)
        abort(500)
