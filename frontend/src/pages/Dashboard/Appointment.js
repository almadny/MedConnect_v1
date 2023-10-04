import React, { useEffect, useState } from 'react';
import {useNavigate} from 'react-router-dom'

const Appointment = () => {
  const [appointment, setAppointment] = useState([]);
  const [doctor, setDoctor] = useState([])
  const apptId = localStorage.getItem('appt_id')
  const navigate = useNavigate()
  const JWT = localStorage.getItem('jwt-token')
  const headers = new Headers({
    'Authorization': `Bearer ${JWT}`
  });
  

  useEffect(() => {
    fetch(`/api/appt/getAppt/${apptId}`, {
      method: "GET",
      headers: headers
    })
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
    fetch(`/api/users/getDoctors/${docId}`, {
      method: 'GET',
      headers: headers
    })
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
      headers: headers
    })
      .then((response) => response.json())
      .then((data) => {
        const { token, room } = data;
        
        console.log('Token:', token);
        console.log('Room:', room);

        localStorage.setItem('video_token', data.token)
        localStorage.setItem('room_name', data.room)
      })
      .catch((error) => {
        console.error('Error generating token:', error);
      });
    navigate('/video_chat/')
  };

  return (
    <div className='mt-10 max-w-5xl mx-auto'>
      <ul>
          <li className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
            <div>
              <p> Dr. John Smith</p>
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
