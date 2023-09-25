import React, { useState } from "react";

const FindADoctor = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  // const [selectedTime, setSelectedTime] = useState("09:00");
  const [doctors] = useState([
    {
      id: 1,
      name: "Dr. John Doe",
      hospital: "City Hospital",
      specialty: "Cardiology",
    },
    {
      id: 2,
      name: "Dr. Jane Smith",
      hospital: "General Hospital",
      specialty: "Pediatrics",
    },
    {
      id: 3,
      name: "Dr. Alice Johnson",
      hospital: "Community Clinic",
      specialty: "Dermatology",
    },
  ]);
  // const [availableDoctors, setAvailableDoctors] = useState([]);
  // const [isLoading, setIsLoading] = useState(false);

  const handleDateChange = (date) => {
    setSelectedDate(date);
    console.log(date)
  };

  // const handleTimeChange = (time) => {
  //   setSelectedTime(time);
  //   console.log(time)
  // };

  const bookAppointment = (doctorId) => {
    // You can implement the booking logic here (e.g., display a confirmation message).
    console.log(`Booked an appointment with doctor ID: ${doctorId}`);
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Find a Doctor</h2>

      <div className="mb-4">
        <label htmlFor="date" className="block text-gray-600">
          Select Prefered Appointment Date:
        </label>
        <input
          type="date"
          value={selectedDate.toISOString().split("T")[0]}
          onChange={(e) => handleDateChange(new Date(e.target.value))}
          className="border border-gray-300 px-2 py-1 rounded"
        />
      </div>

      {/* <div className="mb-4">
        <label htmlFor="time" className="block text-gray-600">
          Select a Time:
        </label>
        <input
          type="time"
          value={selectedTime}
          onChange={(e) => handleTimeChange(e.target.value)}
          className="border border-gray-300 px-2 py-1 rounded"
        />
      </div> */}

      <div>
        <h3 className="text-lg font-semibold mb-2">Available Doctors:</h3>
        <ul>
          {doctors.map((doctor) => (
            <li key={doctor.id} className="flex justify-between mb-4 max-w-6xl mx-auto bg-white rounded shadow p-4">
              <div>
                <p> {doctor.name} - {doctor.hospital} ({doctor.specialty})</p>
                <p>2pm - 4pm</p>
              </div>
              <button
                onClick={() => bookAppointment(doctor.id)}
                className="ml-2 bg-blue-500 text-white px-2 py-1 rounded"
              >
                Book Appointment
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default FindADoctor;





// import React, { useState, useEffect } from "react";
// import Calendar from "react-calendar";
// import "react-calendar/dist/Calendar.css";

// const FindADoctor = () => {
//   const [selectedDate, setSelectedDate] = useState(new Date());
//   const [selectedTime, setSelectedTime] = useState("09:00");
//   const [doctors, setDoctors] = useState([]);
//   const [availableDoctors, setAvailableDoctors] = useState([]);
//   const [isLoading, setIsLoading] = useState(false);

//   useEffect(() => {
//     fetch("/api/doctors")
//       .then((response) => response.json())
//       .then((data) => setDoctors(data))
//       .catch((error) => console.error("Error fetching doctors: ", error));
//   }, []);

//   useEffect(() => {
//     if (selectedDate && selectedTime) {
//       setIsLoading(true);
//       const apiUrl = `/api/available-doctors?date=${selectedDate.toISOString()}&time=${selectedTime}`;

//       fetch(apiUrl)
//         .then((response) => response.json())
//         .then((data) => {
//           setAvailableDoctors(data);
//           setIsLoading(false);
//         })
//         .catch((error) =>
//           console.error("Error fetching available doctors: ", error)
//         );
//     }
//   }, [selectedDate, selectedTime]);

//   const handleDateChange = (date) => {
//     setSelectedDate(date);
//   };

//   const handleTimeChange = (time) => {
//     setSelectedTime(time);
//   };

//   const bookAppointment = (doctorId) => {
//     // Send a booking request to the backend
//     fetch(`/api/book-appointment/${doctorId}`, {
//       method: "POST",
//       body: JSON.stringify({
//         date: selectedDate.toISOString(),
//         time: selectedTime,
//       }),
//       headers: {
//         "Content-Type": "application/json",
//       },
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         // Handle success or display an error message
//         console.log("Appointment booked:", data);
//       })
//       .catch((error) => {
//         console.error("Error booking appointment: ", error);
//       });
//   };

//   return (
//     <div className="p-4">
//       <h2 className="text-2xl font-bold mb-4">Find a Doctor</h2>

//       <div className="mb-4">
//         <label htmlFor="date" className="block text-gray-600">
//           Select a Date:
//         </label>
//         <Calendar onChange={handleDateChange} value={selectedDate} />
//       </div>

//       <div className="mb-4">
//         <label htmlFor="time" className="block text-gray-600">
//           Select a Time:
//         </label>
//         <input
//           type="time"
//           value={selectedTime}
//           onChange={(e) => handleTimeChange(e.target.value)}
//           className="border border-gray-300 px-2 py-1 rounded"
//         />
//       </div>

//       {isLoading ? (
//         <p>Loading...</p>
//       ) : (
//         <div>
//           {availableDoctors.length > 0 ? (
//             <div>
//               <h3 className="text-lg font-semibold mb-2">Available Doctors:</h3>
//               <ul>
//                 {availableDoctors.map((doctor) => (
//                   <li key={doctor.id}>
//                     {doctor.name}
//                     <button
//                       onClick={() => bookAppointment(doctor.id)}
//                       className="ml-2 bg-blue-500 text-white px-2 py-1 rounded"
//                     >
//                       Book Appointment
//                     </button>
//                   </li>
//                 ))}
//               </ul>
//             </div>
//           ) : (
//             <p>No available doctors for the selected date and time.</p>
//           )}
//         </div>
//       )}
//     </div>
//   );
// };

// export default FindADoctor;
