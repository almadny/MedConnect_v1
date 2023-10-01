import React, { useState, useEffect } from 'react';

const Schedule = () => {
  const [selectedDay, setSelectedDay] = useState('');
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');

  const [selectedRanges, setSelectedRanges] = useState([]);

  const handleDayClick = (day) => {
    setSelectedDay(day);
  };

  const handleStartTimeChange = (e) => {
    setStartTime(e.target.value);
  };

  const handleEndTimeChange = (e) => {
    setEndTime(e.target.value);
  };

  const addTimeRange = () => {
    if (selectedDay && startTime && endTime) {
      const newRange = {
        day: selectedDay,
        timeRange: `${startTime} - ${endTime}`,
      };
      setSelectedRanges([...selectedRanges, newRange]);
      setSelectedDay('');
      setStartTime('');
      setEndTime('');
    }
  };

  const removeTimeRange = (index) => {
    const updatedRanges = [...selectedRanges];
    updatedRanges.splice(index, 1);
    setSelectedRanges(updatedRanges);
  };

  const apiUrl = '/api/appt/addTimeSlot'
  const doctorId = localStorage.getItem('user_id')

  const [appointmentData, setAppointmentData] = useState({
    doctor_id: '',
    start_time_str: '',
    end_time_str: '',
    day_of_the_week: '',
  });

  useEffect(() => {
    if (doctorId && startTime && endTime && selectedDay) {
      setAppointmentData({
        doctor_id: doctorId,
        start_time_str: startTime,
        end_time_str: endTime,
        day_of_the_week: selectedDay,
      });
    }
  }, [doctorId, startTime, endTime, selectedDay]);
  
  const handleAppointmentSave = () => {
    console.log(JSON.stringify(appointmentData))
    fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(appointmentData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log('Appointments saved:', data);
        
        alert('Available time successfully saved')
        setSelectedRanges([]);
      })
      .catch((error) => {
        console.error('Error saving appointments:', error);
      });
  };

  return (
    <div>
      <h1 className='flex justify-center py-10 text-3xl font-bold'>Schedule Your Appointments</h1>
      <div className="max-w-6xl mx-auto">
        <div className="justify-center">
          <h2>Select a Day:</h2>
          <div className="flex space-x-2">
            {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].map((day) => (
              <div
                key={day}
                className={`cursor-pointer p-2 border border-gray-300 rounded ${selectedDay === day ? 'bg-blue-200' : ''}`}
                onClick={() => handleDayClick(day)}
              >
                {day}
              </div>
            ))}
          </div>
          {selectedDay && (
            <>
              <h2>Select Time Range:</h2>
              <div className="flex space-x-2">
                <input
                  type="time"
                  value={startTime}
                  onChange={handleStartTimeChange}
                  className="p-2 border border-gray-300 rounded"
                />
                <div className="p-2">-</div>
                <input
                  type="time"
                  value={endTime}
                  onChange={handleEndTimeChange}
                  className="p-2 border border-gray-300 rounded"
                />
                <button className="p-2 bg-blue-500 text-white rounded" onClick={addTimeRange}>Add Time Range</button>
              </div>
              <ul>
                {selectedRanges.map((range, index) => (
                  <li className='p-4' key={index}>
                    {range.day} - {range.timeRange}
                    <button className='ps-4' onClick={() => removeTimeRange(index)}>Remove</button>
                  </li>
                ))}
              </ul>
            </>
          )}
          <button className="p-2 bg-blue-500 text-white rounded" onClick={handleAppointmentSave}>Save Appointments</button>
        </div>
      </div>
    </div>
  );
};

export default Schedule;
