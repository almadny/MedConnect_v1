import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

const Schedule = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [selectedTime, setSelectedTime] = useState('');
  const [selectedRanges, setSelectedRanges] = useState([]);

  const handleDateClick = (date) => {
    setSelectedDate(date);
  };

  const handleTimeChange = (e) => {
    setSelectedTime(e.target.value);
  };

  const addTimeRange = () => {
    if (selectedDate && selectedTime) {
      const newRange = {
        date: selectedDate,
        time: selectedTime,
      };
      setSelectedRanges([...selectedRanges, newRange]);
      setSelectedTime(''); // Clear the selected time after adding it to the list
    }
  };

  const removeTimeRange = (index) => {
    const updatedRanges = [...selectedRanges];
    updatedRanges.splice(index, 1);
    setSelectedRanges(updatedRanges);
  };

  // Function to save selected time ranges to the database
  const handleAppointmentSave = () => {
    // Send the data to your backend API using fetch
    fetch('/api/appointments', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(selectedRanges),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log('Appointments saved:', data);
        // Handle success, maybe show a confirmation message to the user
        // Clear selectedRanges after successful save if needed
        setSelectedRanges([]);
      })
      .catch((error) => {
        console.error('Error saving appointments:', error);
        // Handle errors, display an error message to the user
      });
  };

  return (
    <div>
      <h1 className='flex justify-center py-10 text-3xl font-bold'>Schedule Your Appointments</h1>
      <div className="max-w-6xl mx-auto">
        <div className="w-full">
          <Calendar className="mx-auto" onClickDay={handleDateClick} value={selectedDate} />
        </div>
        <div className="justify-center">
          <h2>Select Time:</h2>
          <input
            type="time"
            value={selectedTime}
            onChange={handleTimeChange}
          />
          <button onClick={addTimeRange}>Add Time Range</button>
          <ul>
            {selectedRanges.map((range, index) => (
              <li key={index}>
                {range.date.toDateString()} - {range.time}
                <button onClick={() => removeTimeRange(index)}>Remove</button>
              </li>
            ))}
          </ul>
          <button onClick={handleAppointmentSave}>Save Appointments</button>
        </div>
      </div>
    </div>
  );
};

export default Schedule;
