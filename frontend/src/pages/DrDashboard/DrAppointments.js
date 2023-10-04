import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const DrAppointments = () => {
  const [appointments, setAppointments] = useState([]);
  const navigate = useNavigate()

  const JWT = localStorage.getItem('jwt-token');
  const headers = new Headers({
    'Authorization': `Bearer ${JWT}`
  });
  const docId = localStorage.getItem('user_id');

  useEffect(() => {
    fetch(`/api/appt/getDocAppts/${docId}`, {
      method: 'GET',
      headers: headers
    })
      .then((response) => response.json())
      .then((data) => {
        setAppointments(data.appointments);
      })
      .catch((error) => {
        console.error('Error fetching appointment data:', error);
      });
  }, [docId]);

  const generateToken = (apptId) => {
    const apiUrl = `/api/videoChat/generateAccessToken/${apptId}`;
    fetch(apiUrl, {
      method: 'GET',
      headers: headers
    })
      .then((response) => response.json())
      .then((data) => {
        const { token, room } = data;
        
        console.log('Token:', token);
        console.log('Room:', room);

        localStorage.setItem('video_token', data.token);
        localStorage.setItem('room_name', data.room);
        navigate('/video_chat/')
        })
      .catch((error) => {
        console.error('Error generating token:', error);
      });
  };

  useEffect(() => {
    appointments.forEach((appointment, index) => {
      fetch(`/api/users/getPatient/${appointment.patient_id}`, {
        method: 'GET',
        headers: headers
      })
        .then((response) => response.json())
        .then((data) => {
          const updatedAppointments = [...appointments];
          updatedAppointments[index].patient = data;
          setAppointments(updatedAppointments);
        })
        .catch((error) => {
          console.error('Error fetching patient data:', error);
        });
    });
  }, [appointments]);

  return (
    <div className="mt-10 max-w-5xl mx-auto">
      <ul>
        {appointments.map((appointment) => (
          <li key={appointment.appointment_id} className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
            <div>
              {/* Display patient first name and last name */}
              <p>{`Patient: ${appointment.patient ? appointment.patient.first_name + ' ' + appointment.patient.last_name : 'Loading...'}`}</p>
		{/*<p>{`Appointment Time: ${appointment.time}`}</p>*/}
              <button
                onClick={() => generateToken(appointment.appointment_id)}
                className="ml-2 bg-blue-500 text-white px-2 py-1 rounded"
              >
                Join Room
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DrAppointments;
