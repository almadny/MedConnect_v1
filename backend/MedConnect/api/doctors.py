from api import db
from flask import Blueprint, jsonify, abort

doctors_bp = Blueprint('doctors', __name__)

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
    hashed_password = db.Column(db.String(64), nullable=False, default='all_password')
    # confirm_password = db.Column(db.String(64), nullable=False, default='all_password')
    healthcare_id = db.Column(db.Integer, db.ForeignKey('healthcares.id'), nullable=False)
    timeslots = db.relationship('TimeSlots', backref='doctors', lazy=True)
    dr_appointments = db.relationship('Appointments', backref='doctors', lazy=True)
    diagnosis = db.relationship('Diagnosis', backref='doctors', lazy=True)
    posts = db.relationship('Posts', backref='doctors', lazy=True)


    def __repr__(self):
        """ Defines the doctor object string representation """
        return f"Doctor('{self.id}': '{self.first_name}' '{self.last_name}' '{self.email_address}')"

@doctors_bp.route('/doctors', methods=['GET'])
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
