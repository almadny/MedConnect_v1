import React, { useState, useEffect } from 'react';
import Video from 'react-twilio-video';

const PRoom = () => {
  const [roomName, setRoomName] = useState(''); // Initialize with the room name received from the backend
  const [token, setToken] = useState(''); // Initialize with the access token received from the backend
  const [isAudioEnabled, setIsAudioEnabled] = useState(true);
  const [isCameraEnabled, setIsCameraEnabled] = useState(true);

  const toggleAudio = () => {
    // Implement logic to toggle audio
    setIsAudioEnabled(!isAudioEnabled);
  };

  const toggleCamera = () => {
    // Implement logic to toggle camera
    setIsCameraEnabled(!isCameraEnabled);
  };

  const endCall = () => {
    // Implement logic to end the call
  };

  useEffect(() => {
    // Initialize Twilio Video with the token and roomName
    // Make sure to use your Twilio Account SID and API Key/Secret from your backend to generate the token
    // You should use the 'Video.connect' method to join the room
    if (token && roomName) {
      // Example usage
      // Video.connect(token, {
      //   name: roomName,
      //   audio: isAudioEnabled,
      //   video: { enabled: isCameraEnabled },
      // }).then((room) => {
      //   // Handle room events and UI updates here
      // });
    }
  }, [token, roomName, isAudioEnabled, isCameraEnabled]);

  return (
    <div>
      <div className="flex justify-center mt-4">
        <Video />
      </div>
      <div className="flex justify-center mt-4">
        <button
          className={`mr-4 ${
            isAudioEnabled ? 'bg-green-500' : 'bg-red-500'
          } text-white px-4 py-2 rounded-lg`}
          onClick={toggleAudio}
        >
          {isAudioEnabled ? 'Mute' : 'Unmute'}
        </button>
        <button
          className={`mr-4 ${
            isCameraEnabled ? 'bg-green-500' : 'bg-red-500'
          } text-white px-4 py-2 rounded-lg`}
          onClick={toggleCamera}
        >
          {isCameraEnabled ? 'Turn Off Camera' : 'Turn On Camera'}
        </button>
        <button
          className="bg-red-500 text-white px-4 py-2 rounded-lg"
          onClick={endCall}
        >
          End Call
        </button>
      </div>
    </div>
  );
};


export default PRoom
