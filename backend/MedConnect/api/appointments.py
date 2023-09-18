from api import db

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


@appointments.route("/book_appointment", methods=["POST"])
def book_appointment():
    data = request.get_json()
    patient_id = data.get("patient_id")
    doctor_id = data.get("doctor_id")
    date_of_appointment = data.get("date_of_appointment")

    '''check if doctor has reached max limit'''
    doctor = Doctor.query.get(doctor_id)
    week_start = date_of_appointment - timedelta(days=date_of_appointment.weekday())
    week_end = week_start + timedelta(days=6)
    weekly_appointment = Appointment.query.filter_by(doctor_id=doctor_id).filter(
        Appointment.date_of_appointment >= week_start,
        Appointment.date_of_appointment <= week_end
    ).count()

    if weekly_appointment >= 21:
        return jsonify({'message': 'Doctor has reached the maximum number of patients for this week'}), 400
    daily_appointments = Appointment.query.filter_by(doctor_id=doctor_id, date_of_appointment=date_of_appointment).count()

    if daily_appointments >= 3:
        return jsonify({'message': 'Doctor has reached the max number of patients for today'}), 400

    appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, date_of_appointment=date_of_appointment, status='Scheduled')
    db.session.add(appointment)
    db.session.commit()

    return jsonify({'message': 'Appointment booked successfully'}), 201


@appointments.route("/appointment/<int>: id", methods=["PUT"])
def update_appointment(appointment_id):
    appointment = Appointments.query.get(id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}, 404
    data = request.get_son()
    appointment.time = data.get('time', appointment.time)
    appointment.doctor = data.get('doctor', appointment.doctor)


@appointments.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(post_id):
    appointment = Appointments.query.get(id)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
