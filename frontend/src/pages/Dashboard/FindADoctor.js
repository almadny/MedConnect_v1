import React, { useState, useEffect } from "react";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";

const FindADoctor = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [availableDoctors, setAvailableDoctors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (selectedDate) {
      setIsLoading(true);
      const apiUrl = `/api/appt/availTimeSlots?dateChosen=${selectedDate.toISOString()}`

      fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => {
          setAvailableDoctors(data.availTimeSlots);
          console.log(availableDoctors)
          setIsLoading(false);
        })
        .catch((error) =>
          console.error("Error fetching available doctors: ", error)
        );
    }
  }, [selectedDate]);

  const handleDateChange = (date) => {
    setSelectedDate(date);
    console.log(selectedDate.toISOString())
  };

  const patientId = Number(localStorage.getItem('user_id'))

  const bookAppointment = (doctorId, timeSlotId) => {
    fetch(`/api/appt/bookAppt`, {
      method: "POST",
      body: JSON.stringify({
        date: selectedDate.toISOString(),
        doctor_id: doctorId,
        patient_id: patientId,
        timeslot_id: timeSlotId,
        notes: ""
      }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Appointment booked:", data);
        console.log([selectedDate.toISOString(), doctorId, patientId, timeSlotId])
        alert('Appointment booked')
        localStorage.setItem('appt_id', data.appointment_id)
      })
      .catch((error) => {
        console.error("Error booking appointment: ", error);
      });
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Find a Doctor</h2>

      <div className="mb-4">
        <label htmlFor="date" className="block text-gray-600">
          Select a Date:
        </label>
        <Calendar onChange={handleDateChange} value={selectedDate} />
      </div>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <div>
          {availableDoctors ? (
            <div>
              <h3 className="text-lg font-semibold mb-2">Available Doctors:</h3>
              <ul>
                {availableDoctors?.map((doctor) => (
                  <li key={doctor.doctor_id} className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
                    <div>
                      <p> {doctor.doctor_name} </p>
                      <p>{doctor.start_time} - {doctor.end_time}</p>
                      <p>Patients on queue: {doctor.Patients_on_queue}</p>
                    </div>
                    <button
                      onClick={() => bookAppointment(doctor.doctor_id, doctor.time_slot_id )}
                     className="ml-2 bg-blue-500 text-white px-2 py-1 rounded"
                    >
                      Book Appointment
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          ) : (
            <p>No available doctors for the selected date and time.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default FindADoctor;
