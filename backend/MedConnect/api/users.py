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

# Patient Endpoints
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
def getPatient(id):
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
def getAllPatients():
    """
    Get all Patients
    """
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

@users_bp.route("/patients/doctors_id", strict_slashes=False)
@jwt_required()
def getDoctorsPatients(doctors_id):
    """
    Get all Patients
    """
    # Incomplete, need a join operation
    patients = Patients.query.filter_by().all()
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
def updatePatient(id):
    """
    Update a patient record
    """
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


# Doctors Endpoints
@users_bp.route("/doctors/<int:id>", methods=["GET"])
def getDoctor(id):
    """
    Get a single doctor
    """
    doctor = Doctors.query.get(id)
    if doctor:
        return jsonify({
            'id': doctor.id,
            'first_name' : doctor.first_name,
            'last_name' : doctor.last_name,
            'other_name' : doctor.other_name,
            'email_address' : doctor.email_address
            'phone_number' : doctor.phone_number,
            'specialty' : doctor.specialty,
            'gender' : doctor.gender
            'healthcare_id' : doctor.healthcare_id
            }), 200

    return jsonify({'error': 'User not found'})


@users_bp.route("/doctors", methods=["POST"])
def addDoctor():
    """
    Add a Doctor
    """
    try:
        data = request.get_json()
        email_address = data['email_address']
        password = data['hashed_password']
        first_name = data['first_name']
        last_name = data['last_name']
        other_name = data['other_name']
        specialty = data['specialty']
        gender = data['gender']
        phone_number = data['phone_number']
        healthcare_id = date['healthcare_id']

        hashed_password = generate_password_hash(password)
        if not is_user(email_address):
            doctor = Doctors(
                    first_name=first_name,
                    last_name=last_name,
                    other_name=other_name,
                    email_address=email_address,
                    specialty=specialty,
                    gender=gender,
                    phone_number=phone_number,
                    healthcare_id=healthcare_id
                    hashed_password=hashed_password
                    )
            from api import db
            db.session.add(doctor)
            db.session.commit()
            return jsonify({'status' : 'Doctor added successfully'}), 200

        return jsonify({'fail': 'User exists'})
    except Exception as e:
        print(e)

@users_bp.route("/doctors/<int:id>", methods=["PUT"])
def editDoctor(id):
    """
    Update Doctors profile
    """
    doctor = Doctors.query.get(id)
    if not doctor:
        return jsonify({'msg': 'Doctor does not exist'})
    try:
        data = request.get_json()
        doctor.email_address = data['email_address']
        doctor.hashed_password = generate_password_hash(data['hashed_password'])
        doctor.first_name = data['first_name']
        doctor.last_name = data['last_name']
        doctor.other_name = data['other_name']
        doctor.specialty = data['specialty']
        doctor.gender = data['gender']
        doctor.phone_number = data['phone_number']

        from api import db
        db.session.commit()
        return jsonify({'status' : 'Patient successfully added'}), 200
    except Exception as e:
        print(e)

@users_bp.route("/doctors/<int:id>", methods=["DELETE"])
def removeDoctor(id):
    """
    Remove a doctor
    """
    # Consider creating a status column that will be marked inactive when a doctor is removed
    # Instead of removing his/her record completely from the database
    doctor = Doctors.query.get(id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return jsonify({"message": "Doctor removed successfully"}), 200
    else:
        return jsonify({"message": "Doctor not found"}), 404


@users_bp.route('/doctors', strict_slashes=False)
def getAllDoctors():
    """
    Get all Doctors
    """
    try:
        doctors = Doctors.query.all()
        all_doctors = [

            {
                    'first_name': doctor.first_name,
                    'last_name' : doctor.last_name,
                    'other_name': doctor.other_name,
                    'gender' : doctor.gender,
                    'phone_number' : doctor.phone_number,
                    'email_address' : doctor.email_address,
                    'specialty': doctor.specialty,
                    'healthcare_id' : doctor.healthcare_id
            }
            for doctor in doctors
                ]
        return jsonify({'doctors' : all_doctors}), 200
    except Exception as e :
        print(e)
        abort(500)

# Get doctors in a specific healthcare
@users_bp.route('/doctors/<int:healthcare_id>', strict_slashes=False)
def getHealthcareDoctors(healthcare_id):
    """
    Get all Healthcare Doctors
    """
    try:
        doctors = Doctors.query.filter_by(healthcare_id=healthcare_id).all()
        all_doctors = []

        for doctor in doctors:
            doc = {
                    'id' : doctor.id,
                    'first_name': doctor.first_name,
                    'last_name' : doctor.last_name,
                    'other_name': doctor.other_name,
                    'gender' : doctor.gender,
                    'phone_number' : doctor.phone_number,
                    'email_address' : doctor.email_address,
                    'specialty': doctor.specialty
            }

            all_doctors.append(doc)

        return jsonify({'doctors' : all_doctors}), 200
    except Exception as e:
        print(e)
        abort(500)

