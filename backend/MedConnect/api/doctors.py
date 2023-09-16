from app import db
from schedules import TimeSlots
from Appointments import Posts

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
