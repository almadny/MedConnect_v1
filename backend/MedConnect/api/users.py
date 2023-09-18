"""
This file contains routes that concerns Users as listed below
1. Doctors
2. Patients
3. Healthcares
4. Admins
"""
from api import db
from flask import Blueprint, jsonify, abort

users_bp = Blueprint('users', __name__)

@users_bp.route("/doctors/<int:id>", methods=["GET"])
def get_doctor(id):
    doctor = Doctor.query.get(id)
    if doctor:
        return (
            jsonify(
                {"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty}
            ),
            200,
        )
    return jsonify({"message": "Doctor not found"}), 404


@users_bp.route("/doctors", methods=["POST"])
def add_doctor():
    data = request.get_json()
    print(data)
    name = data.get("name")
    specialty = data.get("specialty")

    new_doctor = Doctor(name=name, specialty=specialty)

    try:
        db.session.add(new_doctor)
        db.session.commit()
        return jsonify({"message": "Doctor successfully added"}), 200
    except Exception as err:
        print(str(err))
        return jsonify({"message": "Failed to create doctor"}), 400


@users_bp.route("/doctors/<int:id>", methods=["PUT"])
def update_doctors(id):
    doctor = Doctor.query.get(id)
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
    doctor = Doctor.query.get(id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return jsonify({"message": "Doctor removed successfully"}), 200
    else:
        return jsonify({"message": "Doctor not found"}), 404


@users_bp.route('/doctors', methods=['GET'])
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
    except Exception(e):
        print(e)
        abort(500)
