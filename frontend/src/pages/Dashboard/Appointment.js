import React, { useEffect, useState } from 'react';

const Appointment = () => {
  const [appointment, setAppointment] = useState([]);
  const [doctor, setDoctor] = useState([])
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

  const docId = appointment.doctor_id
  useEffect(() => {
    fetch(`/api/users/getDoctors/${docId}`)
      .then((response) => response.json())
      .then((data) => {
        setDoctor(data)
        console.log(data)
      })
      .catch((error) => {
        console.error('Error fetching appointment data:', error);
      });
  }, []);

  const apiUrl = `/api/videoChat/generateAccessToken/${apptId}`
  const generateToken = () => {
    fetch(apiUrl, {
      method: 'GET',
    })
      .then((response) => response.json())
      .then((data) => {
        const { token, room } = data;
        
        console.log('Token:', token);
        console.log('Room:', room);

        localStorage.setItem('video_token', data.token)
        localStorage.setItem('room_number', data.room)
      })
      .catch((error) => {
        console.error('Error generating token:', error);
      });
  };

  return (
    <div className='mt-10 max-w-5xl mx-auto'>
      <ul>
          <li className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
            <div>
              <p> Dr. {doctor.first_name} {doctor.last_name}  {doctor.hospital}</p>
              <p>{appointment.time}</p>
            </div>
            <button
              onClick={() => generateToken()}
              className="ml-2 bg-blue-500 text-white px-2 py-1 rounded"
            >
              Join Room
            </button>
          </li>
      </ul>
    </div>
  );
};

export default Appointment;
