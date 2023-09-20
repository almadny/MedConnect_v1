from api import db
from flask import Blueprint
from flask_jwt_extended import jwt_required

appt_bp = Blueprint('appt_bp', __name__)

# To Book an Appointment, The following must be done
# get the timeshedule of the doctors endpoint
# post a appointment

@appt_bp.route("/book_appointment", methods=["POST"])
def bookAppointment():
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


@appt_bp.route("/appointment/<int>: id", methods=["PUT"])
def update_appointment(appointment_id):
    appointment = Appointments.query.get(id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404
    data = request.get_json()
    appointment.time = data.get('time', appointment.time)
    appointment.doctor = data.get('doctor', appointment.doctor)


@appt_bp.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(post_id):
    appointment = Appointments.query.get(id)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()

