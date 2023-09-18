from app import db
from schedules import TimeSlots
from Appointments import Posts
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request, jsonify




class Doctors(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    other_name = db.Column(db.String(32), nullable=True)
    gender = db.Column(db.String(6), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False, index=True, unique=True)
    email_address = db.Column(db.String(30), nullable=False, unique=True, index=True)
    specialty = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(64), nullable=False, default='all_password')
    confirm_password = db.Column(db.String(64), nullable=False, default='all_password')
    healthcare_id = db.Column(db.Integer, db.ForeignKey('healthcares.id'), nullable=False)
    timeslots = db.relationship('TimeSlots', backref='doctors', lazy=True)
    dr_appointments = db.relationship('Appointments', backref='doctors', lazy=True)
    diagnosis = db.relationship('Diagnosis', backref='doctors', lazy=True)
    posts = db.relationship('Posts', backref='doctors', lazy=True)
    def __repr__(self):
        """ Defines the doctor object string representation """
        return f"Doctor('{self.id}': '{self.first_name}' '{self.last_name}' '{self.email_address}')"



@app.route("/doctors/<int:id>", methods=["GET"])
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


@app.route("/doctors", methods=["POST"])
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


@app.route("/doctors/<int:id>", methods=["PUT"])
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


@app.route("/doctors/<int:id>", methods=["DELETE"])
def delete_doctor(id):
    doctor = Doctor.query.get(id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return jsonify({"message": "Doctor removed successfully"}), 200
    else:
        return jsonify({"message": "Doctor not found"}), 404

