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
    hashed_password = db.Column(db.String(128), nullable=False)
    pat_appointments = db.relationship('Appointments', backref='patients')
    diagnosis = db.relationship('Diagnosis', backref='patients')

    def __repr__(self):
        """ Defines the patient object string representation """
        return f"Patient('{self.id}': '{self.first_name}' '{self.last_name}' '{self.email_address}')"

class Healthcares(db.Model):
    __tablename__ = 'healthcares'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    address = db.Column(db.String(32), nullable=False, unique=True)
    contact_number = db.Column(db.String(32), nullable=False, unique=True)
    doctor = db.relationship('Doctors', backref='healthcares')

    def __repr__(self):
        """ Defines the Healthcare object string representation """
        return f"Healthcare('{self.id}': '{self.name}')"


class TimeSlots(db.Model):
    __tablename__ = 'timeslots'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    day_of_the_week = db.Column(db.String(10), nullable=False, default='Everyday')
    timeslots_appointment = db.relationship('Appointments', backref='timeslots')

    def __repr__(self):
        """ Defines the available_time object string representation """
        return f"TimeSlot('{self.id}': '{self.doctor_id}' '{self.day_of_the_week}' '{self.start_time}' '{self.end_time}')"

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
    password = db.Column(db.String(128), nullable=False)
    healthcare_id = db.Column(db.Integer, db.ForeignKey('healthcares.id'), nullable=False)
    timeslots = db.relationship('TimeSlots', backref='doctors', lazy=True)
    dr_appointments = db.relationship('Appointments', backref='doctors', lazy=True)
    diagnosis = db.relationship('Diagnosis', backref='doctors', lazy=True)
    posts = db.relationship('Posts', backref='doctors', lazy=True)

    def __repr__(self):
        """ Defines the doctor object string representation """
        return f"Doctor('{self.id}': '{self.first_name}' '{self.last_name}' '{self.email_address}')"

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


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(15), nullable=True, index=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """ Defines the appointment object string representation """
        return f"Post('{self.id}': '{self.title}' '{self.category}' '{self.date_posted}')"
