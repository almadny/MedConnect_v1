from app import db

class Diagnosis(db.Model):
    __tablename__ = 'diagnosis'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    appointment_id = db.Column(db.ForeignKey('appointments.id'), nullable=False, unique=True)
    diagnosis = db.Column(db.Text, nullable=False)
    doctor_notes = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """ Defines the Diagnosis object string representation """
        return f"Diagnosis('{self.id}': '{self.appointment_id}')"
