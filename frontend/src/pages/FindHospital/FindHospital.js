import React, { useState, useEffect } from 'react';

const FindHospital = () => {
  const [userLocation, setUserLocation] = useState(null);
  const [nearestHospital, setNearestHospital] = useState(null);
  const [locationEnabled, setLocationEnabled] = useState(true);

  useEffect(() => {
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          setUserLocation({ latitude, longitude });
        },
        () => {
          setLocationEnabled(false);
        }
      );
    } else {
      setLocationEnabled(false);
    }
  }, []);

  useEffect(() => {
    if (userLocation) {
      const apiKey = 'YOUR_API_KEY';
      const googleMapsUrl = `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${userLocation.latitude},${userLocation.longitude}&radius=5000&type=hospital&key=${apiKey}`;

      fetch(googleMapsUrl)
        .then((response) => response.json())
        .then((data) => {
          if (data.results.length > 0) {
            setNearestHospital(data.results[0]);
          }
        });
    }
  }, [userLocation]);

  useEffect(() => {
    if (nearestHospital) {
      const map = new window.google.maps.Map(document.getElementById('map'), {
        center: {
          lat: nearestHospital.geometry.location.lat,
          lng: nearestHospital.geometry.location.lng,
        },
        zoom: 15,
      });

      new window.google.maps.Marker({
        position: {
          lat: nearestHospital.geometry.location.lat,
          lng: nearestHospital.geometry.location.lng,
        },
        map: map,
        title: nearestHospital.name,
      });
    }
  }, [nearestHospital]);

  return (
    <div>
      {locationEnabled ? (
        <div>
          <div id="map" style={{ height: '400px', width: '100%' }}></div>
          {nearestHospital ? (
            <p>Nearest Hospital: {nearestHospital.name}</p>
          ) : (
            <p>Finding nearest hospital...</p>
          )}
        </div>
      ) : (
        <p>Please enable location services to find the nearest hospital.</p>
      )}
    </div>
  );
};

export default FindHospital;




// import React, { useState, useEffect } from 'react';
// import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
// import axios from 'axios';

// const FindHospital = () => {
//   const [userLocation, setUserLocation] = useState(null);
//   const [nearestHospital, setNearestHospital] = useState(null);
//   const [locationEnabled, setLocationEnabled] = useState(true);

//   useEffect(() => {
//     if ('geolocation' in navigator) {
//       navigator.geolocation.getCurrentPosition(
//         (position) => {
//           const { latitude, longitude } = position.coords;
//           setUserLocation({ lat: latitude, lon: longitude });
//         },
//         () => {
//           setLocationEnabled(false);
//         }
//       );
//     } else {
//       setLocationEnabled(false);
//     }
//   }, []);

//   useEffect(() => {
//     if (userLocation) {
//       const apiUrl = `https://data.medicare.gov/resource/rbry-mqwu.json?$select=name,location&$where=location is not null&$order=location%20asc&$limit=1&$offset=0&$select=name,location&$where=within_circle(location,${userLocation.lat},${userLocation.lon},16093.4)`;

//       axios
//         .get(apiUrl)
//         .then((response) => {
//           if (response.data.length > 0) {
//             const { name, location } = response.data[0];
//             setNearestHospital({ name, location: location.coordinates });
//           }
//         })
//         .catch((error) => {
//           console.error('Error fetching hospital data:', error);
//         });
//     }
//   }, [userLocation]);

//   return (
//     <div>
//       {locationEnabled ? (
//         <div>
//           {userLocation && (
//             <MapContainer center={userLocation} zoom={15} style={{ height: '400px', width: '100%' }}>
//               <TileLayer
//                 url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//                 attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
//               />
//               {nearestHospital && (
//                 <Marker position={nearestHospital.location}>
//                   <Popup>{nearestHospital.name}</Popup>
//                 </Marker>
//               )}
//             </MapContainer>
//           )}
//           {nearestHospital ? (
//             <p>Nearest Hospital: {nearestHospital.name}</p>
//           ) : (
//             <p>Finding nearest hospital...</p>
//           )}
//         </div>
//       ) : (
//         <p>Please enable location services to find the nearest hospital.</p>
//       )}
//     </div>
//   );
// };

// export default FindHospital;
