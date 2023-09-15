from app import db
from diagnosis import Diagnosis

class Appointments(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False, index=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False, index=True)
    diagnosis = db.relationship('Diagnosis', backref='appointments', uselist=False)
    date_of_appointment = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False, default='Scheduled')
    notes = db.Column(db.Text, nullable=True)
    time = db.Column(db.Integer, db.ForeignKey('timeslots.id'), nullable=False)


    def __repr__(self):
        """ Defines the appointment object string representation """
        return f"Appointment('{self.id}': '{self.doctor_id}' '{self.patient_id}' '{self.status}' '{self.notes}')"
