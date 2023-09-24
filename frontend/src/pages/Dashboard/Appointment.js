import React, { useEffect, useState } from 'react';

const Appointment = () => {
  // const [appointments, setAppointments] = useState([]);

  // useEffect(() => {
  //   const apiUrl = 'api/appointments/book_appointment';

  //   fetch(apiUrl)
  //     .then((response) => response.json())
  //     .then((data) => {
  //       setAppointments(data);
  //     })
  //     .catch((error) => {
  //       console.error('Error fetching appointment data:', error);
  //     });
  // }, []);

  const joinRoom = (doctorId) => {
    
  };

  const [doctors] = useState([
    {
      id: 1,
      name: "Dr. John Doe",
      hospital: "City Hospital",
      specialty: "Cardiology",
    }])
  return (
    <div className='mt-10 max-w-5xl mx-auto'>
      <ul>
        {doctors?.map((doctor) => (
          <li key={doctor.id} className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
            <div>
              <p> {doctor.name} - {doctor.hospital} ({doctor.specialty})</p>
              <p>2pm - 4pm</p>
            </div>
            <button
              onClick={() => joinRoom(doctor.id)}
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
