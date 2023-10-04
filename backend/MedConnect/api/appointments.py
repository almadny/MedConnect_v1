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
from sqlalchemy import or_, and_
from api.models import Appointments, Doctors, Patients, TimeSlots, Exceptions

appt_bp = Blueprint('appt_bp', __name__)


@appt_bp.route('/getTimeSlot/<int:id>', methods=['GET'], strict_slashes=False)
# @jwt_required()
def getTimeSlot(id):
    try:
        time_slot = TimeSlots.query.get(id)
        
        if time_slot is None:
            return jsonify({'error' : 'time slot not found'}), 400
        return jsonify({
            'id': time_slot.id,
            'doctor_id': time_slot.doctor_id,
            'start_time': time_slot.start_time.strftime('%H:%M %p'),
            'end_time': time_slot.end_time.strftime('%H:%M %p'),
            'day_of_the_week': time_slot.day_of_the_week,
            }), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error' : 'server error'}), 500


@appt_bp.route('/getTimeSlots', methods=['GET'], strict_slashes=False)
# @jwt_required()
def getTimeSlots():
    time_slots = TimeSlots.query.all()
    time_slots_data = [{
        'id': slot.id,
        'doctor_id': slot.doctor_id,
        'start_time': slot.start_time.strftime('%H:%M %p'),
        'end_time': slot.end_time.strftime('%H:%M %p'),
        'day_of_the_week': slot.day_of_the_week,
    } 
    for slot in time_slots
    ]
    return jsonify({"Time Slots" : time_slots_data}), 200


@appt_bp.route("/addTimeSlot", methods=["POST"], strict_slashes=False)
# @jwt_required()
def createTimeSlot():
    try:
        data = request.get_json()
    
        # Parse start_time and end_time into datetime objects
        doctor_id = data.get("doctor_id")
        start_time_str = data.get("start_time")
        end_time_str = data.get("end_time")
        day_of_the_week = data.get("day_of_the_week")
        

        if doctor_id is None:
            return jsonify({"error" : "doctor id is required"}), 400

        doctor = Doctors.query.get(doctor_id)
        if doctor is None:
            return jsonify({"error" : f"doctor with id of {doctor_id} does not exist"}), 400

        if day_of_the_week is None:
            return jsonify({"error" : "Day of the week is required"}), 400

        # Validate day_of_the_week
        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Everyday']
    
        if day_of_the_week not in valid_days:
            return jsonify({"error": "Invalid day_of_the_week"}), 400
    
        if start_time_str is None or end_time_str is None:
            return jsonify({"error" : "start and end time is required"}), 400
            
        try:
            start_time = datetime.strptime(start_time_str, "%I:%M %p").time() 
            end_time = datetime.strptime(end_time_str, "%I:%M %p").time()
        
        except ValueError as e:
            return jsonify({"error": "invalid time format"}), 400
    
        
        timeSlot = TimeSlots.query.filter(
                TimeSlots.doctor_id==doctor_id,
                TimeSlots.start_time>=start_time,
                TimeSlots.end_time<=end_time,
                TimeSlots.day_of_the_week==day_of_the_week
                ).all()

        if timeSlot:
            return jsonify({'error' : 'Time Slot already exists'}), 409

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
        print(str(e))
        return jsonify({"error": "Failed to create time slot"}), 500


@appt_bp.route('/updateTimeSlot/<int:id>', methods=['PUT'], strict_slashes=False)
# @jwt_required()
def updateTimeSlot(id):
    try:
        data = request.get_json()
        timeSlot = TimeSlots.query.get(id)

        if timeSlot is None:
            return jsonify({"error" : "Time Slot does not exist"}), 400
    
        # Parse start_time and end_time into datetime objects
        start_time_str = data.get("start_time")
        end_time_str = data.get("end_time")
        day_of_the_week = data.get("day_of_the_week")
    
        if start_time_str:
            try:
                start_time = datetime.strptime(start_time_str, '%I:%M %p').time()
            except ValueError as sve:
                return jsonify({"error" : "time format is incorrect"}), 400
            timeSlot.start_time = start_time

        
        if end_time_str:
            try:
                end_time = datetime.strptime(end_time_str, '%H:%M %p').time()
            except ValueError as e:
                return jsonify({"error": "invalid time format"}), 400
            timeSlot.end_time = end_time
        
        # Validate day_of_the_week
        if day_of_the_week:
            valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Everyday']
            
            if day_of_the_week not in valid_days:
                return jsonify({"error": "Invalid day of the week"}), 400
            timeSlot.day_of_the_week = day_of_the_week
    
        doctor_id = data.get("doctor_id")

        if doctor_id:
            doctor = Doctors.query.get(doctor_id)
            if doctor is None:
                return jsonify({"error" : f"doctor with the id {doctor_id} does not exist"}), 400
    
        db.session.commit()
        
        return jsonify({"message": "Time slot updated successfully"}), 200
    
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({"error": "Failed to update time slot"}), 500


@appt_bp.route('/delTimeSlot/<int:id>', methods=['DELETE'], strict_slashes=False)
# @jwt_required()
def delTimeSlot(id):
    time_slot = TimeSlots.query.get(id)
    
    if time_slot is None:
        return jsonify({'message': 'Time slot not found'}), 404

    try:
        db.session.delete(time_slot)
        db.session.commit()

        return jsonify({'message': 'Time slot deleted successfully'}), 200
   
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'error': 'your request failed while processing'}), 500


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
    try:
        # data = request.get_json()
        # date_str = data.get('dateChoosen')

        date_str = request.args.get('dateChosen')
        #date_string = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

        if date_str is None:
            return jsonify({'error':'No date choosen'}), 400

        try:
            # Date is not less than today
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            #date = date_string.strftime("%Y-%m-%d")

            if date.date() < datetime.today().date():
                return jsonify({'error' : 'date must be later than now'}), 400
        
        except ValueError as ve:
            return jsonify({'error' : str(ve)}), 400

        # Find the day corresponding to the booked date
        day = date.strftime('%A')

        # Find all schedule corresponding to the said day
        matchedTimeSlots = TimeSlots.query.filter(
                or_(
                    TimeSlots.day_of_the_week==day,
                    TimeSlots.day_of_the_week=='Everyday'
                    )
                ).all()

        if not matchedTimeSlots:
            return jsonify({'error': 'No available slot for the selected date'}), 404

        print(f"{matchedTimeSlots}")
    
        # Define list of all schedules
        allTimeSlots = []

        # Create available timeslot list for date selected
        for timeSlot in matchedTimeSlots:
    
            doctorAppts = Appointments.query.filter(
                        Appointments.doctor_id==timeSlot.doctor_id,
                        Appointments.timeslot_id==timeSlot.id,
                        Appointments.date_of_appointment==date.date(),
                        Appointments.status=='Scheduled'
                    ).all()

            # print(f"{doctorAppts}")
            # print(f"{date}")

            # Get doctor with schedule information
            doctor = Doctors.query.get(timeSlot.doctor_id)
        
            # Get doctors with exception on the choosen date
            exception = Exceptions.query.filter_by(
                        doctor_id=timeSlot.doctor_id,
                        date_of_exception=date
                    ).first()
       
            # Exclude doctors with exceptions
            if exception:
                continue
        
            # Create a dictionary with doctor schedule
            timeslot_item = {
                'time_slot_id' : timeSlot.id,
                'slot_day' : timeSlot.day_of_the_week,
                'start_time' : timeSlot.start_time.strftime('%H:%M %p'),
                'end_time' : timeSlot.end_time.strftime('%H:%M %p'),
                'doctor_id' : timeSlot.doctor_id,
                'doctor_name' : f"{doctor.first_name} {doctor.last_name} {doctor.other_name}",
                'Patients_on_queue' : len(doctorAppts)
                }

            # Append schedule to all schedules
            allTimeSlots.append(timeslot_item)
    
        return jsonify({'availTimeSlots' : allTimeSlots }), 200

    except Exception as ex:
        print(str(ex))
        return jsonify({'error' : 'An error occurred while proccessing the request'}), 500


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
    try:
        data = request.get_json()
    
        doctor_id = data.get('doctor_id')
        patient_id = data.get('patient_id')
        timeslot_id = data.get('timeslot_id')
        date_of_appointment = data.get('date')
        notes = data.get('notes')

        if doctor_id is None or patient_id is None or timeslot_id is None or date_of_appointment is None:
            return jsonify({'error' : 'doctor id, patient id, timeslot id and date of appointment are required'}), 400
        
        try:
            apptDate = datetime.strptime(date_of_appointment, "%Y-%m-%dT%H:%M:%S.%fZ").date()

        except ValueError as date_conversion_error:
            return jsonify({"error" : f"Invalid date format {date_conversion_error}"}), 400


        newAppt = Appointments(
            doctor_id=doctor_id,
            patient_id=patient_id,
            timeslot_id=timeslot_id,
            date_of_appointment=apptDate,
            notes=notes
            )
    
        db.session.add(newAppt)
        db.session.commit()

        return jsonify({
                    'status' : 'appointment booked successfully',
                    'appointment_id' : newAppt.id
                }), 200

    except Exception as ex:
        db.session.rollback()
        print(str(ex))
        return jsonify({'error' : 'An error occurred while processing the request'}), 500


@appt_bp.route('/cancelAppt/<int:id>', methods=['PUT'], strict_slashes=False)
def cancelAppt(id):
    """
    Cancel an appointment

    Args:
        id - Appointment id

    Return:
        JSON - Status of operation

    """
    try:
        appointment = Appointments.query.get(id)

        if not appointment:
            return jsonify({'error': 'appointment not found'}), 400

        if appointment.status == 'Cancelled':
            return jsonify({'status': 'appointment already canceled'}), 401

        if appointment.status == 'Completed':
            return jsonify({'status' : 'appointment already completed'}), 401

        appointment.status = 'Cancelled'

        db.session.commit()
        return jsonify({'status' : 'successfully canceled'}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error':'server error'}), 500


@appt_bp.route('/completeAppt/<int:id>', methods=['PUT'], strict_slashes=False)
def completeAppt(id):
    """
    Complete an appointment

    Args:
        id - Appointment id

    Return:
        JSON - Status of operation

    """
    appointment = Appointments.query.get(id)

    if not appointment:
        return jsonify({'error': 'appointment not found'}), 400
    
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
    try:
    # Get appointment from database
        appointment = Appointments.query.get(id)

        if appointment is None:
            raise ValueError('No data found')

        timeSlot = TimeSlots.query.get(appointment.timeslot_id)

        return jsonify({
            'appointment_id' : appointment.id,
            'patient_id' : appointment.patient_id,
            'doctor_id' : appointment.doctor_id,
            'date' : datetime.strftime(appointment.date_of_appointment, '%Y-%m-%d'),
            'time_id' : appointment.timeslot_id, # dateime.isoformat(timeSlot.time.time())
            'status' : appointment.status
            }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@appt_bp.route('/getDocAppts/<int:doctor_id>', methods=['GET'], strict_slashes=False)
def getDocAppt(doctor_id):
    """
    Get a doctors appointments

    Args:
        doctor_id - Doctor's id

    Return:
        List - list of dictionaries of a doctor's appointments
    """
    try:
        # data = request.get_json()

        # if data is None:
            # raise ValueError('No JSON data provided')

        # doctor_id = data.get('doctor_id')
        doctor = Doctors.query.get(doctor_id)
        if not doctor:
            raise ValueError("Doctor does not exist")

        appointments = Appointments.query.filter_by(doctor_id=doctor_id).all()

        docAppts = [{
                        'appointment_id' : appointment.id,
                        'appointment_date' : datetime.strftime(appointment.date_of_appointment, '%Y-%m-%d'),
                        'doctor_id' : appointment.doctor_id,
                        'patient_id' : appointment.patient_id,
                        'time_id' : appointment.timeslot_id,
                        'status' : appointment.status,
                        'notes' : appointment.notes,
                    } 
                    for appointment in appointments
                ]
        return jsonify({'appointments' : docAppts}), 200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as ex:
        print(str(ex))
        return jsonify({'error' : 'server error'}), 500


@appt_bp.route('/getAllAppts/', methods=['GET'], strict_slashes=False)
def getAllAppt():
    """
    Get all appointments

    Args:
        None

    Return:
        List - list of dictionaries of a doctor's appointments
    """
    try:
        appointments = Appointments.query.all()

        appts = [
                {'appointment_id' : appointment.id,
                'appointment date' : datetime.strftime(appointment.date_of_appointment, '%Y-%m-%d'),
                'doctor id' : appointment.doctor_id,
                'patient id' : appointment.patient_id,
                'time slot id' : appointment.timeslot_id,
                'status' : appointment.status,
                'notes' : appointment.notes
                } 
                for appointment in appointments
                ]
    
        if not appts:
            return jsonify({'status' : 'no appointments'}), 200
        
        return jsonify({'appointments' : appts}), 200
    
    except ValueError as e:
        return jsonify({'error' : str(e)}), 400


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
    try:
        data = request.get_json()

        if data is None:
            raise ValueError('No valid JSON data provided')

        doctor_id = data.get('doctor_id')
        date_of_exception_str = data.get('date_of_exception')

        if doctor_id is None or date_of_exception_str is None:
            raise ValueError('doctor id and date of exception are required')

        date_of_exception = datetime.strptime(date_of_exception_str, '%Y-%m-%d')

        exception = Exceptions(doctor_id=doctor_id,  date_of_exception=date_of_exception)

        db.session.add(exception)
        db.session.commit()

        return jsonify({'status' : 'successfully created an exception'}), 200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as ex:
        print(str(ex))
        return jsonify({'error' : 'server error'}), 500
    
    except Exception as ex:
        db.session.rollback()
        return jsonify({'error': 'An error ocurred while processing your request'}), 500



@appt_bp.route('/getException/<int:id>', methods=['GET'], strict_slashes=False)
def getException(id):
    """
    Retrieve an exception object

    Args:
        id - Exception id

    Return:
        Dict - A JSON dictionary of exception object
    """
    try:
        exception = Exceptions.query.get(id)

        if not exception:
            raise ValueError('exception id is incorrect')

        doctor = Doctors.query.get(exception.doctor_id)

        return jsonify({
            'exception id' : exception.id,
            'doctor id' : exception.doctor_id,
            'doctor name' : f'{doctor.first_name} {doctor.last_name} {doctor.other_name}',
            'exception date' : datetime.strftime(exception.date_of_exception, '%Y-%m-%d')
            }), 200

    except ValueError as e:
        return jsonify({'error' : str(e)}), 400

    except Exception as ex:
        return jsonify({'error' : 'An error occurred while processing your request'}), 500


@appt_bp.route('/getExceptions/', methods=['GET'], strict_slashes=False)
def getExceptions():
    """
    Retrieve all exceptions

    Args:
        none
    
    Return:
        List - JSON list with dictionaries of exceptions

    """
    try:
        exceptions = Exceptions.query.all()

        if not exceptions:
            return jsonify({'error': 'No exceptions available'}), 200

        allExceptions = [{
                            'exception id' : exception.id,
                            'doctor id' : exception.doctor_id,
                            'exception date' : datetime.strftime(exception.date_of_exception, '%Y-%m-%d')
                        }
                        for exception in exceptions
                        ]

        return jsonify({'Exceptions' : allExceptions}), 200

    except Exception as ex:
        return jsonify({'error' : 'An error occurred while processing the request'}), 500


@appt_bp.route('/deleteException/<int:id>', methods=['DELETE'], strict_slashes=False)
def deleteException(id):
    """
    Remove an exception

    Args:
        id - exception id

    Return:
        dict - JSON status dictionary

    """
    try:
        exception = Exceptions.query.get(id)

        if not exception:
            return jsonify({'status':'no exception found'}), 400
        
        db.session.delete(exception)
        db.session.commit()

        return jsonify({'status' : 'exception deleted'}), 200
    
    except Exception as ex:
        db.session.rollback()
        return jsonify({'error' : 'An error ocurred while processing the request'}), 500

