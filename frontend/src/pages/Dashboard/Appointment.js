import React, { useEffect, useState } from 'react';

const Appointment = () => {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    // Fetch appointments from your backend
    fetch('/api/appointments/book_appointment')
      .then((response) => response.json())
      .then((data) => {
        setAppointments(data);
      })
      .catch((error) => {
        console.error('Error fetching appointment data:', error);
      });
  }, []);

  const generateToken = (appointmentId) => {
    // Make a request to your Flask backend to generate a video token for the selected appointment
    fetch(`/generateAccessToken/${appointmentId}`, {
      method: 'POST',
    })
      .then((response) => response.json())
      .then((data) => {
        const { token, room } = data;
        // Use the generated token and room for video calls
        console.log('Token:', token);
        console.log('Room:', room);
        // You can navigate to the room component or perform other actions here
      })
      .catch((error) => {
        console.error('Error generating token:', error);
      });
  };

  return (
    <div className='mt-10 max-w-5xl mx-auto'>
      <ul>
        {appointments.map((appointment) => (
          <li key={appointment.id} className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
            <div>
              <p> {appointment.doctorName} - {appointment.hospital} ({appointment.specialty})</p>
              <p>{appointment.time}</p>
            </div>
            <button
              onClick={() => generateToken(appointment.id)}
              className="ml-2 bg-blue-500 text-white px-2 py-1 rounded"
            >
              Join Room
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Appointment;
