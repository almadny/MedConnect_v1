from api import db
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required
from api.models import Appointments, Doctors, Patients, TimeSlots
appt_bp = Blueprint('appt_bp', __name__)

# To Book an Appointment, The following must be done
# get the timeshedule of the doctors endpoint
# post a appointment
# Get convenient date and time for patients
# Determine the day and time
# Determine doctor that matches the day and time
# Filter to remove doctors with exception coinciding with the date
# Determine the number of appointment for a selected doctor
# Assign appointment to doctor with smallest appointment
    # If doctors have the same appointment
        # Assign appointments to doctors with highest duration
#Exception route with : id, doctors id, date


@appt_bp.route('/time-slots', methods=['GET'])
#@jwt_required()
def get_time_slots():
    time_slots = TimeSlots.query.all()
    time_slots_data = [{
        'id': slot.id,
        'doctor_id': slot.doctor_id,
        'start_time': slot.start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'end_time': slot.end_time.strftime('%Y-%m-%d %H:%M:%S'),
        'day_of_the_week': slot.day_of_the_week,
    } for slot in time_slots]
    return jsonify(time_slots_data), 200


@appt_bp.route("/time-slots", methods=["POST"])
@jwt_required()
def create_time_slot():
    data = request.get_json()
    
    # Parse start_time and end_time into datetime objects
    start_time_str = data.get("start_time")
    end_time_str = data.get("end_time")
    
    try:
        start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return jsonify({"error": "Invalid datetime format"}), 400
    
    # Validate day_of_the_week
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_the_week = data.get("day_of_the_week")
    
    if day_of_the_week not in valid_days:
        return jsonify({"error": "Invalid day_of_the_week"}), 400
    
    doctor_id = data.get("doctor_id")
    
    try:
        time_slot = TimeSlots(doctor_id=doctor_id, start_time=start_time, end_time=end_time, day_of_the_week=day_of_the_week)
        db.session.add(time_slot)
        db.session.commit()
        return jsonify({"message": "Time slot created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create time slot"}), 500


@appt_bp.route('/time-slots/<int:id>', methods=['PUT'])
@jwt_required()
def update_time_slot(id):
    data = request.get_json()
    
    # Parse start_time and end_time into datetime objects
    start_time_str = data.get("start_time")
    end_time_str = data.get("end_time")
    
    try:
        start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return jsonify({"error": "Invalid datetime format"}), 400
    
    # Validate day_of_the_week
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_the_week = data.get("day_of_the_week")
    
    if day_of_the_week not in valid_days:
        return jsonify({"error": "Invalid day_of_the_week"}), 400
    
    doctor_id = data.get("doctor_id")
    
    try:
        time_slot = TimeSlots.query.get(id)
        if not time_slot:
            return jsonify({"error": "Time slot not found"}), 404
        
        time_slot.doctor_id = doctor_id
        time_slot.start_time = start_time
        time_slot.end_time = end_time
        time_slot.day_of_the_week = day_of_the_week
        
        db.session.commit()
        
        return jsonify({"message": "Time slot updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update time slot"}), 500


@appt_bp.route('/time-slots/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_time_slot(id):
    time_slot = TimeSlots.query.get(id)
    if not time_slot:
        return jsonify({'message': 'Time slot not found'}), 404

    try:
        db.session.delete(time_slot)
        db.session.commit()
        return jsonify({'message': 'Time slot deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete time slot'}), 500

@appt_bp.route("/appointments", methods=['GET'], strict_slashes=False)
#@jwt_required()
def all_healthcares():
    appointments = Appointments.query.all()
    all_appointments = []
    if appointments:
        for appointment in appointments:
            appointment = {
            'doctor_id' : appointments.get('doctor_id'),
            'time_slot' : appointments.time_slots,
            'day_of_the_week' : appointments.day_of_the_week,
            }
            all_appointments.append(appointment)
    return jsonify({'healthcare': all_appointments}), 200


@appt_bp.route("/book-appointment", methods=["POST"])
# @jwt_required()
def book_appointment():
    data = request.get_json()

    # Validate input data
    patient_id = data.get("patient_id")
    date_of_appointment_str = data.get("date_of_appointment")

    if not patient_id or not date_of_appointment_str:
        return jsonify({"message": "Invalid input data"}), 400

    try:
        date_of_appointment = datetime.strptime(
            date_of_appointment_str, "%Y-%m-%d"
        ).date()
    except ValueError:
        return (
            jsonify({"message": "Invalid date format. Expected format: YYYY-MM-DD"}),
            400,
        )

    # Check if the patient exists
    patient = Patients.query.get(patient_id)
    if not patient:
        return jsonify({"message": "Patient not found"}), 404

    # Determine the day of the week for the appointment
    day_of_the_week = date_of_appointment.strftime("%A")

    # Check if the patient already has an appointment on this day
    appt = Appointments.query.filter_by(
        patient_id=patient_id, date_of_appointment=date_of_appointment
    ).first()
    if appt:
        return jsonify({"message": "Patient has an appointment on this day"}), 400

    # Query available time slots for the specified day of the week
    time_slots = TimeSlots.query.filter_by(day_of_the_week=day_of_the_week).all()

    if not time_slots:
        return jsonify({"message": "No time slots available for this date"}), 400

    doctor_appointment_counts = {}

    # Iterate through available time slots to calculate the number of appointments each doctor has on the specified date
    for time_slot in time_slots:
        appointment_count = Appointments.query.filter_by(
            doctor_id=time_slot.doctor_id, date_of_appointment=date_of_appointment
        ).count()
        # Store the doctor's ID as the key and their appointment count as the value in a dictionary
        doctor_appointment_counts[time_slot.doctor_id] = appointment_count

    # Sort the doctors based on their appointment counts in ascending order
    sorted_doctors = sorted(doctor_appointment_counts.items(), key=lambda x: x[1])

    # Get the appointment count of the doctor with the fewest appointments (the first item in the sorted list)
    smallest_appointment_count = sorted_doctors[0][1]

    # Filter doctors with the same (smallest) appointment count and create a list of available doctors
    available_doctors = [
        doctor
        for doctor, count in sorted_doctors
        if count == smallest_appointment_count
    ]

    # If there are no available doctors with the smallest appointment count, return an error message
    if not available_doctors:
        return jsonify({"message": "No available doctors for this date"}), 400

    chosen_doctor = available_doctors[0]

    # Find the time slot for the chosen doctor and day of the week
    time_slot = TimeSlots.query.filter_by(
        doctor_id=chosen_doctor, day_of_the_week=day_of_the_week
    ).first()

    # Create a new appointment
    appointment = Appointments(
        patient_id=patient_id,
        doctor_id=chosen_doctor,
        date_of_appointment=date_of_appointment,
        time=time_slot.id,
    )

    db.session.add(appointment)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Appointment booked successfully",
                "doctor_id": chosen_doctor,
                "time_slot_id": time_slot.id,
            }
        ),
        200,
    )




@appt_bp.route("/appointment/<int>: id", methods=["PUT"])
def update_appointment(appointment):
    appointment = Appointments.query.get(id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404
    data = request.get_json()
    appointment.time = data.get('time', appointment.time)
    appointment.doctor = data.get('doctor', appointment.doctor)


@appt_bp.route("/posts/<int:id>", methods=["DELETE"])
def delete_post():
    appointment = Appointments.query.get(id)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()

