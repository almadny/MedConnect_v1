"""
Module that contains all appointments route like

getAppointment (single and multiple appointments)
bookAppointment
cancelAppointment
rescheduleAppointment

Routes for doctors schedule like
addSchedule
editSchedule
deleteSchedule
getSchedules (single and multiple schedules)

and routes for exceptions like
addException
getExceptions(single and multiple exceptions)
deleteExceptions
updateExceptions
"""

from api import db
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required
from api.models import Appointments, Doctors, Patients, TimeSlots, Exceptions

appt_bp = Blueprint('appt_bp', __name__)

@appt_bp.route('/timeSlots', methods=['GET'], strict_slashes=False)
@jwt_required()
def getTimeSlots():
    time_slots = TimeSlots.query.all()
    time_slots_data = [{
        'id': slot.id,
        'doctor_id': slot.doctor_id,
        'start_time': slot.start_time.strftime('%H:%M'),
        'end_time': slot.end_time.strftime('%H:%M'),
        'day_of_the_week': slot.day_of_the_week,
    } 
    for slot in time_slots
    ]
    return jsonify(time_slots_data), 200


@appt_bp.route("/timeSlots", methods=["POST"])
@jwt_required()
def createTimeSlot():
    data = request.get_json()
    
    # Parse start_time and end_time into datetime objects
    start_time_str = data.get("start_time")
    end_time_str = data.get("end_time")
    
    try:
        start_time = datetime.strptime(start_time_str, '%H:%M')
        end_time = datetime.strptime(end_time_str, '%H:%M')
    except ValueError as e:
        return jsonify({"error": "Invalid datetime format"}), 400
    
    # Validate day_of_the_week
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_the_week = data.get("day_of_the_week")
    
    if day_of_the_week not in valid_days:
        return jsonify({"error": "Invalid day_of_the_week"}), 400
    
    doctor_id = data.get("doctor_id")
    
    try:
        time_slot = TimeSlots(
                doctor_id=doctor_id,
                start_time=start_time,
                end_time=end_time,
                day_of_the_week=day_of_the_week)

        db.session.add(time_slot)
        db.session.commit()
        return jsonify({"message": "Time slot created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create time slot"}), 500


@appt_bp.route('/time-slots/<int:id>', methods=['PUT'])
@jwt_required()
def updateTimeSlot(id):
    data = request.get_json()
    
    # Parse start_time and end_time into datetime objects
    start_time_str = data.get("start_time")
    end_time_str = data.get("end_time")
    
    try:
        start_time = datetime.strptime(start_time_str, '%H:%M')
        end_time = datetime.strptime(end_time_str, '%H:%M')
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


@appt_bp.route('/timeSlot/<int:id>', methods=['DELETE'])
@jwt_required()
def deleteTimeSlot(id):
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


@appt_bp.route('/availTimeSlots/', methods=['GET'], strict_slashes=False)
def availTimeSlots():
    """
    Determine the available appointments timeslots for the choosen date

    Args:
        date - patient preferred date

    Return:
        List - list of dictionaries containing the available timeslots
    
    """
    # Extract date from request object
    data = request.get_json()
    date = data.get('dateChoosen')

    if not date:
        return jsonify({'error':'No date choosen'}), 401

    # Date is not less than today
    if datetime.fromisoformat(date).date() < datetime.today().date():
        return jsonify({'error' : 'invalid date'}), 401

    # Find the day corresponding to the booked date
    day = datetime.fromisoformat(date).strftime('%A')

    # Find all schedule corresponding to the said day
    matchedTimeSlots = TimeSlots.query.filter(
            or_(
                day=day,
                day='Everyday',
                )
            ).all()

    if not matchedTimeSlots:
        return jsonify({'error': 'No available for the selected date'}), 404
    
    # Define list of all schedules
    allTimeSlots = []

    # Create available timeslot list for date selected
    for timeSlot in matchedTimeSlots:
        doctorAppts = Appointments.query.filter_by(
                and_(
                    doctor_id=timeSlot.doctor_id,
                    time_id=timeSlot.id,
                    date=datetime.fromisoformat(date).date()
                    status='Scheduled'
                    )
                ).all()
    
        # Get doctor with schedule information
        doctor = Doctors.query.get(timeSlot.doctor_id)
        
        # Get doctors with exception on the choosen date
        exception = Exceptions.query.filter(
                and_(
                    doctor_id=timeSlot.doctor_id,
                    date=datetime.fromisoformat(date).date()
                    )
                ).first()
       
        # Exclude doctors with exceptions
        if exception:
            continue
        
        # Create a dictionary with doctor schedule
        timeslot_item = {
                'time slot id' : timeSlot.id,
                'time slot day' : timeSlot.day,
                'time slot start time' : timeSlot.start_time,
                'time slot end time' : timeSlot.end_time,
                'doctor id' : timeSlot.doctor_id,
                'doctor name' : f"{doctor.first_name} {doctor.last_name} {doctor.other_name}",
                'Patients on queue' : len(doctorAppts)
                }
        # Append schedule to all schedules
        allTimeSlots.append(timeslot_item)
    
    return jsonify({'availSchedules' : allTimeSlots }), 200


@appt_bp.route("/bookAppt", methods=["POST"], strict_slashes=False)
def bookAppointment():
    """
    Book an appointment

    Args:
        Json - containing all appointment details

    Return:
        dict - JSON dictionary with status of book
    """
    # Get data from request
    data = request.get_json()
    
    doctor_id = data.get('doctor_id')
    patient_id = data.get('patient_id')
    timeslot_id = data.get('timeslot_id')
   # date_booked = datetime.today().date()
    date_of_appointment = data.get('date')
    notes = data.get('notes')

    newAppt = Appointments(
            doctor_id=doctor_id,
            patient_id=patient_id,
            timeslot_id=timeslot_id,
            date_of_appointment= date_of_appointment,
            notes=notes
            )
    
    db.session.add(newAppt)
    db.session.commit()

    return jsonify({
                    'status' : 'appointment booked successfully',
                    'appointment id' : newAppt.id
                }), 200


@appt_bp.route("/updateAppt/<int:id>", methods=["PUT"], strict_slashes=False)
def rescheduleAppointment(id):
    """
    Reschedules an appointment
    """
    appointment = Appointments.query.get(id)
    
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404
    
    data = request.get_json()
    timeslot_id = data.get('timeslot_id')
    
    if timeslot_id == appointment.timeslot_id:
        return jsonify({'status' : 'same data as before'}), 200
    
    appointment.schedule_id = data.get('schedule_id', appointment.schedule_id)
    appointment.date_booked = datetime.today().date()
    db.session.commit()
    
    return jsonify({'status' : 'successfully rescheduled'}), 200

@appt_bp.route('/cancelAppt/<int:id>', methods=['PUTS'], strict_slashes=False)
def cancelAppt(id):
    """
    Cancel an appointment

    Args:
        id - Appointment id

    Return:
        JSON - Status of operation

    """
    appointment = Appointments.query.get(id)

    if appointment.status == 'Cancelled':
        return ({'status': 'appointment already canceled'}), 401

    appointment.status = 'Cancelled'

    db.session.commit()
    return jsonify({'status' : 'successfully canceled'}), 200

@appt_bp.route('/completeAppt/<int:id>', methods=['PUTS'], strict_slashes=False)
def completeAppt(id):
    """
    Complete an appointment

    Args:
        id - Appointment id

    Return:
        JSON - Status of operation

    """
    appointment = Appointments.query.get(id)

    if appointment.status == 'cancelled' or appointment.status == 'completed':
        return ({'status': 'Appointment canceled or completed'}), 404

    appointment.status = 'Completed'

    db.session.commit()
    return jsonify({'status' : 'appointment completed'}), 200

@appt_bp.route('/getAppt/<int:id>', methods=['GET'], strict_slashes=False)
def getAppointment(id):
    """
    Return an appointment data

    Args:
        id - id of the requested appointment

    Return:
        Dict - dictionary of appointment data

    """
    # Get appointment from database
    appointment = Appointments.query.get(id)

    if not appointment:
        return ({'error':'appointment not found'}), 404

    return jsonify({
        'appointment id' : appointment.id,
        'patient id' : appointment.patient_id,
        'doctor id' : appointment.doctor_id,
        'date' : datetime.isoformat(appointment.date_of_appointment.date()),
        'time' : dateime.isoformat(appointment.time.time())
        }), 200


@appt_bp.route('/getDocAppts/', methods=['GET'], strict_slashes=False)
def getDocAppt():
    """
    Get a doctors appointments

    Args:
        id - Doctor's id

    Return:
        List - list of dictionaries of a doctor's appointments
    """
    data = request.get_json()
    doctor_id = data.get('doctor_id')
    appointments = Appointments.query.filter_by(doctor_id=doctor_id).all()

    docAppts = [
            {'appointment_id' : appointment.id,
            'appointment date' : datetime.isoformat(appointment.date.date()),
            'doctor id' : appointment.doctor_id,
            'patient id' : appointment.patient_id,
            'time' : dateime.isoformat(appointment.time.time())
            'status' : appointment.status
            'notes' : appointment.notes
            } for appointment in appointments
            ]
    if not docAppt:
        return jsonify({'status' : 'no appointments for this doctor'}), 200
    return jsonify({'appointments' : docAppts}), 200


@appt_bp.route('/getAllAppts/', methods=['GET'], strict_slashes=False)
def getAllAppt():
    """
    Get all appointments

    Args:
        None

    Return:
        List - list of dictionaries of a doctor's appointments
    """
    data = request.get_json()
    doctor_id = data.get('doctor_id')
    appointments = Appointments.query.all()

    appts = [
            {'appointment_id' : appointment.id,
            'appointment date' : datetime.isoformat(appointment.date.date()),
            'doctor id' : appointment.doctor_id,
            'patient id' : appointment.patient_id,
            'time' : dateime.isoformat(appointment.time.time())
            'status' : appointment.status
            'notes' : appointment.notes
            } 
            for appointment in appointments
            ]
    
    if not docAppt:
        return jsonify({'status' : 'no appointments'}), 200
    return jsonify({'appointments' : appts}), 200


@appt_bp.route('/addException', methods=['POST'], strict_slashes=False)
def addException():
    """
    Create a new exception object

    Args:
        Dict - JSON Dictionary containing
            doctor_id and exception date

    Return:
        Dict - JSON Dictionary containing status of object creation
    """
    data = request.get_json()

    doctor_id = date.get('doctor_id')
    date_of_exception = data.get('date_of_exception')

    exception = Exceptions(doctor_id=doctor_id,  date_of_exception=date_of_exception)

    db.session.add(exception)
    db.session.commit()

    return jsonify({'status' : 'successfully created an exception'}), 200


@appt_bp.route('/getException/<int:id>', methods=['GET'], strict_slashes=False)
def getException(id):
    """
    Retrieve an exception object

    Args:
        id - Exception id

    Return:
        Dict - A JSON dictionary of exception object
    """
    exception = Exceptions.query.get(id)

    if not exception:
        return jsonify({'error' : 'No exception found'}), 404

    doctor = Doctors.query.get(exception.doctor_id)

    return jsonify({
        'exception id' = exception.id,
        'doctor id' = exception.doctor_id
        'doctor name' = f'{doctor.first_name} {doctor.last_name} {doctor.other_name}',
        'exception date' = datetime.isoformat(exception.date_of_exception.date())
        }), 200


@appt_bp.route('/getExceptions/', methods=['GET'], strict_slashes=False)
def getExceptions():
    """
    Retrieve all exceptions

    Args:
        none
    
    Return:
        List - JSON list with dictionaries of exceptions

    """
    exceptions = Exceptions.query.all()

    if not exceptions:
        return jsonify({'error': 'No exceptions available'}), 404

    allExceptions = [
                {'exception id' = exception.id,
                 'doctor id' = exception.doctor_id,
                 'exception date' = exception.date_of_exception
                 }
                for exception in exceptions
                ]
    return jsonify({'Exceptions' : allExceptions}), 200


@appt_bp.route('/deleteException/<int:id>', methods=['DELETE'], strict_slashes=False)
def deleteException(id):
    """
    Remove an exception

    Args:
        id - exception id

    Return:
        dict - JSON status dictionary

    """
    exception = Exceptions.query.get(id)

    if not exception:
        return jsonify({'status':'no exception found'}), 404
    return jsonify({'status' : 'exception deleted'}), 200

    db.session.delete(exception)
    db.session.commit()

