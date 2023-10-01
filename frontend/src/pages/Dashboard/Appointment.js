import React, { useEffect, useState } from 'react';

const Appointment = () => {
  const [appointment, setAppointment] = useState([]);
  const apptId = localStorage.getItem('appt_id')

  useEffect(() => {
    fetch(`/api/appt/getAppt/${apptId}`)
      .then((response) => response.json())
      .then((data) => {
        setAppointment(data);
        console.log(data)
      })
      .catch((error) => {
        console.error('Error fetching appointment data:', error);
      });
  }, []);

  const generateToken = () => {
    fetch(`/generateAccessToken/${apptId}`, {
      method: 'POST',
    })
      .then((response) => response.json())
      .then((data) => {
        const { token, room } = data;
        
        console.log('Token:', token);
        console.log('Room:', room);
      })
      .catch((error) => {
        console.error('Error generating token:', error);
      });
  };

  return (
    <div className='mt-10 max-w-5xl mx-auto'>
      <ul>
          <li key={appointment.appointment_id} className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
            <div>
              <p> {appointment.doctorName} - {appointment.hospital} ({appointment.specialty})</p>
              <p>{appointment.time}</p>
            </div>
            <button
              onClick={() => generateToken()}
              className="ml-2 bg-blue-500 text-white px-2 py-1 rounded"
            >
              Join Room
            </button>
          </li>
        ))
      </ul>
    </div>
  );
};

export default Appointment;
