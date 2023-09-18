from api import db
from datetime import datetime

class Patients(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    other_name = db.Column(db.String(32), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False, index=True, unique=True)
    email_address = db.Column(db.String(30), nullable=False, unique=True, index=True)
    password = db.Column(db.String(64), nullable=False)
    confirm_password = db.Column(db.String(64), nullable=False)
    pat_appointments = db.relationship('Appointments', backref='patients')
    diagnosis = db.relationship('Diagnosis', backref='patients')

    def __repr__(self):
        """ Defines the patient object string representation """
        return f"Patient('{self.id}': '{self.first_name}' '{self.last_name}' '{self.email_address}')"
